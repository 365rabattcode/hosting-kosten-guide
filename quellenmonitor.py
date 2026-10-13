"""Read the publisher's source page without following affiliate destinations."""
import argparse
import html
import json
import os
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from urllib.request import Request, build_opener, HTTPRedirectHandler

SOURCE = "https://365rabattcode.de/shop/hostinger/"
ROOT = Path(__file__).resolve().parent
EXPECTED = {"57445": "Webhosting", "57454": "VPS", "57450": "Agency",
            "57451": "Cloud", "57456": "Website Builder", "57458": "E-Mail",
            "57460": "Reach", "57463": "Business Email"}


class SameHostRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlparse(newurl).scheme != "https" or urlparse(newurl).hostname != "365rabattcode.de":
            raise ValueError("Source redirected outside the publisher's HTTPS domain")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class CouponLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.records = {}

    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        link = fields.get("data-affiliate", "")
        parsed = urlparse(link)
        if parsed.scheme != "https" or parsed.hostname != "365rabattcode.de":
            return
        coupon_id = parse_qs(parsed.query).get("cout", [""])[0]
        if coupon_id not in EXPECTED:
            return
        title = html.unescape(fields.get("title", ""))
        if title or coupon_id not in self.records:
            self.records[coupon_id] = {"url": link, "source_title": title}


def md_text(value):
    return html.escape(str(value)).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--html-file", type=Path, help="Offline source fixture")
    parser.add_argument("--output", type=Path, default=ROOT / "monitor-output")
    args = parser.parse_args()
    if args.html_file:
        source_html = args.html_file.read_text(encoding="utf-8")
        mode = "Offline fixture, no live request"
    else:
        req = Request(SOURCE, headers={"User-Agent": "365Rabattcode-SourceMonitor/1.0 (+https://github.com/365rabattcode/hosting-kosten-guide)"})
        with build_opener(SameHostRedirect()).open(req, timeout=30) as response:
            if response.status != 200:
                raise ValueError(f"Unexpected source status: {response.status}")
            source_html = response.read(5_000_001)
            if len(source_html) > 5_000_000:
                raise ValueError("Source page exceeds size limit")
            source_html = source_html.decode("utf-8")
        mode = "Live source request"
    links = CouponLinks()
    links.feed(source_html)
    if not links.records:
        raise ValueError("No known coupon links found; inspect source markup before updating")
    baseline_path = ROOT / "source-baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8")) if baseline_path.exists() else {}
    changed = links.records != baseline
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    report = {"checked_at_utc": stamp, "source": SOURCE, "mode": mode,
              "changed_since_baseline": changed, "records": links.records,
              "not_found_in_source": sorted(set(EXPECTED) - links.records.keys()),
              "validity_checked": False, "affiliate_destinations_visited": False}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "source-status.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Quellenmonitor: 365Rabattcode", "", f"Prüfzeitpunkt (UTC): {stamp}",
             f"Modus: {mode}", "", f"Quelle: {SOURCE}", "",
             f"Änderung gegenüber dem gespeicherten Ausgangsstand: {'Ja' if changed else 'Nein'}", "",
             "| Bereich | Link auf der Quellseite |", "| --- | --- |"]
    for coupon_id, name in EXPECTED.items():
        record = links.records.get(coupon_id)
        status = "Gefunden" if record else "Nicht gefunden; kein Urteil zur Gültigkeit"
        lines.append(f"| {md_text(name)} | {status} |")
    lines += ["", "Der Monitor prüft die Quellseite und erfasst hinterlegte Links. Er öffnet keine Affiliate-Ziele, prüft keine Rabatte im Checkout und bestätigt keine Provisionen.",
              "", "Die manuell gepflegte Ablaufzeit auf der Website ist keine verifizierte Anbieterfrist. Änderungen an Links oder Quelltiteln müssen redaktionell geprüft werden."]
    text = "\n".join(lines) + "\n"
    (args.output / "source-status.md").write_text(text, encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
            summary.write(text)
    print(text)


if __name__ == "__main__":
    main()

"""Anbieterneutraler Hosting-Kostenvergleich ohne Netzwerkzugriff."""
import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def geld_eingabe(value):
    try:
        number = Decimal(value.replace(',', '.'))
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError('Bitte einen Betrag eingeben.') from exc
    if not number.is_finite() or number < 0:
        raise argparse.ArgumentTypeError('Beträge müssen endlich und nicht negativ sein.')
    return number


def ganze_zahl(value):
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError('Bitte eine ganze Zahl eingeben.') from exc
    if number < 0:
        raise argparse.ArgumentTypeError('Die Zahl darf nicht negativ sein.')
    return number


def betrag(value):
    return f'{value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP):.2f}'.replace('.', ',') + ' €'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--intro-monat', type=geld_eingabe, required=True, help='Einführungspreis pro Monat in EUR')
    parser.add_argument('--intro-monate', type=ganze_zahl, required=True, help='Monate zum Einführungspreis')
    parser.add_argument('--verlaengerung-monat', type=geld_eingabe, required=True, help='Verlängerungspreis pro Monat in EUR')
    parser.add_argument('--horizont-monate', type=ganze_zahl, required=True, help='Vergleichszeitraum, mindestens 1 Monat')
    parser.add_argument('--domain-jahr', type=geld_eingabe, default=Decimal(0), help='Domainpreis pro Jahr in EUR')
    parser.add_argument('--domain-gratis-jahre', type=ganze_zahl, default=0, help='Anzahl anfangs enthaltener Domainjahre')
    parser.add_argument('--extras-monat', type=geld_eingabe, default=Decimal(0), help='Zusatzkosten pro Monat in EUR')
    parser.add_argument('--einmalig', type=geld_eingabe, default=Decimal(0), help='Einmalige Kosten in EUR')
    args = parser.parse_args()
    if args.horizont_monate == 0:
        parser.error('Der Vergleichszeitraum muss mindestens 1 Monat betragen.')
    intro_monate = min(args.horizont_monate, args.intro_monate)
    renewal_monate = args.horizont_monate - intro_monate
    intro = args.intro_monat * intro_monate
    renewal = args.verlaengerung_monat * renewal_monate
    domain_jahre = max(0, (args.horizont_monate + 11) // 12 - args.domain_gratis_jahre)
    domain = args.domain_jahr * domain_jahre
    extras = args.extras_monat * args.horizont_monate
    total = intro + renewal + domain + extras + args.einmalig
    for label, amount in [('Einführungsphase', intro), ('Verlängerungsphase', renewal), ('Domain', domain), ('Zusatzleistungen', extras), ('Einmalig', args.einmalig), ('Gesamt', total), ('Durchschnitt pro Monat', total / args.horizont_monate)]:
        print(f'{label}: {betrag(amount)}')
    print('Vergleichswert, kein Zahlungsplan. Einheitliche Steuerbasis verwenden.')
    print('Angefangene Domainjahre werden vollständig berechnet.')
    if args.horizont_monate < args.intro_monate:
        print('Achtung: Die Erstlaufzeit ist länger als der Vergleichszeitraum; die tatsächliche Vorauszahlung kann höher sein.')


if __name__ == '__main__':
    main()

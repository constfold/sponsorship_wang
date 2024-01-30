import json
import re
from collections import defaultdict
from currency_converter import CurrencyConverter, SINGLE_DAY_ECB_URL
with open('王局给所有人道歉 ｜台湾｜民进党｜贺珑夜夜秀｜残障人士｜歧视｜道歉｜王局拍案20240126 [Jutrlp_6ww8].info.json', 'r') as f:
    chip = json.load(f)

print('comments(no replies) = ', len(chip['comments']))

chip = list(map(lambda c: c['chip'], filter(lambda c: 'chip' in c, chip["comments"])))

print('donate = ', len(chip))

currency_names = {
    'A$': 'AUD',
    'NZ$': 'NZD',
    '£': 'GBP',
    '€': 'EUR',
    'NT$': 'TWD',
    'SGD': 'SGD',
    '$': 'USD',
    'CA$': 'CAD',
    '¥': 'JPY',
    'HK$': 'HKD',
    'R$': 'BRL',
    '₩': 'KRW',
    'SEK': 'SEK',
    'THB': 'THB',
    'TRY': 'TRY',
    'AED': 'AED',
    'ZAR': 'ZAR',
    'NOK': 'NOK',
    'COP': 'COP',
    'CHF': 'CHF',
    'HUF': 'HUF',
    '₫': 'VND',
    'MYR': 'MYR',
    'IDR': 'IDR',
    'DKK': 'DKK',
    'MX$': 'MXN',
    'JOD': 'JOD',
    'ARS': 'ARS',
    '₱': 'PHP',
    'CZK': 'CZK',
    'EGP': 'EGP',
    'NGN': 'NGN',
    'PLN': 'PLN',
}
chip2 = defaultdict(float)
for c in chip:
    m = re.match(r'(.+?)([0-9,\.]+)', c)
    chip2[currency_names[m[1].replace("\xa0", '')]] += float(m[2].replace(',', ''))

chip = dict(chip2)
print('chip = ', json.dumps(chip, indent=2))

# from xe.com 2024-01-30
currency = {
    'TWD': 0.22911232,
    'AED': 1.942817,
    'COP': 0.0018146561,
    'VND': 0.00029213364,
    'JOD': 10.063463,
    'ARS': 0.0086405422,
    'EGP': 0.23089351,
    'NGN': 0.0079978511,
}

c = CurrencyConverter(SINGLE_DAY_ECB_URL)
chip_cny = chip.copy()
for k in chip:
    if k in currency:
        chip_cny[k] *= currency[k]
    else:
        chip_cny[k] = c.convert(chip[k], k, 'CNY')

print('chip(CNY) = ', json.dumps(chip_cny, indent=2))
print('chip total(CNY) = ', sum(chip_cny.values()))
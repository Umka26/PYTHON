import json
import requests

keys = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR'
}


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты "{base}".')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{base}"')

        try:
            quote_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{quote}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Количество валюты которую необходимо конертировать "{amount}" введено неверно!')
        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base*amount
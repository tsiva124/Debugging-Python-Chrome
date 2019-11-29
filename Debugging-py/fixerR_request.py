import requests


def main():
    API_KEY = '7ed0f4c49f64b239a037fa2f0d0d7247'
    base = 'INR'
    symbol = 'GBP,JPY,EUR'

    response = requests.get('http://data.fixer.io/api/latest?access_key={0}&base={1}&symbols={2}'
                            .format(API_KEY, base, symbol))
    print(response)


main()

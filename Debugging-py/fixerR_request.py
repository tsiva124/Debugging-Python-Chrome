import requests
import json


def main():
    API_KEY = '7ed0f4c49f64b239a037fa2f0d0d7247'
    base = 'INR'
    symbol = 'GBP,JPY,EUR'

    response = requests.get('http://127.0.0.1:8000/getSongs')
    data = json.loads(response.content)
    for d in data:
        print(d["filename"])
    print(response.content)


main()

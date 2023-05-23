import http.client
import json
import urllib.parse

def fetch_amazon_data(api_key):
    symbol = 'AMZN'
    api_endpoint = '/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'.format(symbol, api_key)
    host = 'www.alphavantage.co'
    connection = http.client.HTTPSConnection(host)
    connection.request('GET', api_endpoint)
    response = connection.getresponse()

    if response.status == 200:
        data = response.read().decode('utf-8')
        json_data = json.loads(data)

        if 'Global Quote' in json_data:
            quote_data = json_data['Global Quote']
            symbol = quote_data['01. symbol']
            price = quote_data['05. price']
            volume = quote_data['06. volume']
            print('Symbol:', symbol)
            print('Price:', price)
            print('Volume:', volume)
        else:
            print('Error: Global Quote not found in response.')
    else:
        print('Error occurred while making the API request.')

    connection.close()

api_key = '<your-api-key>'
fetch_amazon_data(api_key)

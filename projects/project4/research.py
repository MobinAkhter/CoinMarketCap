import math
import json
import locale
import requests
from prettytable import PrettyTable

local_currency = 'USD'
local_symbol = '$'

api_key = 'f04699ce-768b-41c3-8966-996380933287'
headers = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'
global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

# To call the API

request = requests.get(global_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

total_market_cap = int(data['quote'][local_currency]['total_market_cap'])
total_market_cap_string = '{:,}'.format(total_market_cap)

table = PrettyTable(['Name', 'Asset', '% of total global cap', 'Price', '10.9T (Gold)', '35.2T (Narrow Money)', '89'
                                                                                                                  '.5T (Stock Markets)'])

listing_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

request = requests.get(listing_url, headers=headers)
results = request.json()

data = results['data']

for currency in data:
    name = currency['name']
    symbol = currency['symbol']
    market_cap = currency['quote'][local_currency]['market_cap']

    percentage_of_global_cap = float(market_cap / total_market_cap)
    price = currency['quote'][local_currency]['price']

    available_supply = currency['total_supply']
    try:
        gold_price = 10900000000000 * percentage_of_global_cap / available_supply
    except ZeroDivisionError:
        print("Available supply is 0. Can't divide by zero")
    try:
        narrow_money_price = 35200000000000 * percentage_of_global_cap / available_supply
    except ZeroDivisionError:
        print("Available supply is 0. Can't divide by zero")
    try:
        stock_market_price = 89500000000000 * percentage_of_global_cap / available_supply
    except ZeroDivisionError:
        print("Available supply is 0. Can't divide by zero")

    percentage_of_global_cap_string = str(round(percentage_of_global_cap * 100, 2)) + '%'
    price_string = local_symbol + '{:,}'.format(round(price, 2))
    gold_price_string = local_symbol + '{:,}'.format(round(gold_price, 2))
    narrow_money_string = local_symbol + '{:,}'.format(round(narrow_money_price, 2))
    stock_market_price_string = local_symbol + '{:,}'.format(round(stock_market_price, 2))

    table.add_row([name, symbol, percentage_of_global_cap_string, price_string, gold_price_string, narrow_money_string, stock_market_price_string])

print()
print(table)
print()
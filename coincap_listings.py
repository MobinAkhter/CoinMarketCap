import requests  # this library lets us communicate with the API
import json

local_currency = 'USD'  # this is the currency we want to use
local_symbol = '$'  # this is the symbol for the currency we want to use

# API KEY taken from https://pro.coinmarketcap.com/account/
api_key = 'f04699ce-768b-41c3-8966-996380933287'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

# To call the API

request = requests.get(global_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

for currency in data:
    name = currency['name']
    symbol = currency['symbol']
    rank = currency['cmc_rank']
    circulating_supply = currency['circulating_supply']
    circulating_supply_string = '{:,}'.format(circulating_supply)
    total_supply = currency['total_supply']
    total_supply_string = '{:,}'.format(total_supply)
    quote = currency['quote'][local_currency]
    market_cap = quote['market_cap']
    market_cap = round(market_cap, 2)
    hour_change = quote['percent_change_1h']
    day_change = quote['percent_change_24h']
    week_change = quote['percent_change_7d']
    percent_change_24h = quote['percent_change_24h']
    price = quote['price']
    price = round(price, 2)
    volume = quote['volume_24h']
    volume = round(volume, 2)
    volume_string = '{:,}'.format(volume)

    price_string = local_symbol + '{:,}'.format(price)
    percent_change_24h_string = '{:,}'.format(percent_change_24h)
    market_cap_string = local_symbol + '{:,}'.format(market_cap)

    print(name + ' (' + symbol + ')')
    print('Rank: ' + str(rank))
    print('Price: ' + str(price_string))
    print('Market cap: ' + str(market_cap_string))
    print('Hour change: ' + str(hour_change) + '%')
    print('Day change: ' + str(day_change) + '%')
    print('Week change: ' + str(week_change) + '%')
    print('Percent change 24h: ' + str(percent_change_24h_string) + '%')
    print('Total supply: ' + str(total_supply_string))
    print('Circulating supply: ' + str(circulating_supply_string))
    print('Volume: ' + str(volume_string))
    print()

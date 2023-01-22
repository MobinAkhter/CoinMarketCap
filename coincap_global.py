import requests # this library lets us communicate with the API
import json

local_currency = 'USD' # this is the currency we want to use
local_symbol = '$' # this is the symbol for the currency we want to use

# API KEY taken from https://pro.coinmarketcap.com/account/
api_key = 'f04699ce-768b-41c3-8966-996380933287'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

# To call the API

request = requests.get(global_url, headers=headers)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

btc_dominance = data['btc_dominance']
eth_dominance = data['eth_dominance']
total_market_cap = data['quote'][local_currency]['total_market_cap']
total_volume_24h = data['quote'][local_currency]['total_volume_24h']

btc_dominance = round(btc_dominance, 2)
eth_dominance = round(eth_dominance, 2)
total_market_cap = round(total_market_cap, 2)
total_volume_24h = round(total_volume_24h, 2)


total_market_cap_string = local_symbol + '{:,}'.format(total_market_cap)
total_volume_24h_string = local_symbol + '{:,}'.format(total_volume_24h)

print()
print("Bitcoin dominance is", btc_dominance)
print("Ethereum dominance is", eth_dominance)
print("Total market cap is", total_market_cap_string)
print("Total volume 24h is", total_volume_24h_string)
print()



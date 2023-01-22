import os
import csv
import sys
import json
import requests
import time
from datetime import datetime

local_currency = 'USD'  # this is the currency we want to use
local_symbol = '$'  # this is the symbol for the currency we want to use

# API KEY taken from https://pro.coinmarketcap.com/account/
api_key = 'f04699ce-768b-41c3-8966-996380933287'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("Tracking Alerts...")
print()

already_hit_symbols = [] # this is to keep track of the symbols we have already alerted on

while True:
    with open("my_alerts.csv", "r", encoding ="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if '\ufeff' in line[0]:
                # line[0] = line[0].replace('\ufeff', '')
                line[0] = line[0][1:].upper()
            else:
                line[0] = line[0].upper()

            symbol = line[0]
            amount = line[1]
            quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol

            request = requests.get(quote_url, headers=headers)
            results = request.json()

            currency = results['data'][symbol]
            name = currency['name']
            price = currency['quote'][local_currency]['price']
            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                os.system('say ALERT ALERT ALERT')
                os.system('say ' + name + ' hit ' + amount + ' ' + local_currency)
                sys.stdout.flush()

                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(name + ' hit ' + amount + 'at ' + current_time + '!')
                already_hit_symbols.append(symbol)

    print()
    print("Sleeping for 5 minutes...")
    print()
    time.sleep(300)

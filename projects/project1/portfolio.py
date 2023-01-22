import os
import csv
import json
import requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style  # for colored text in terminal

local_currency = 'USD'  # this is the currency we want to use
local_symbol = '$'  # this is the symbol for the currency we want to use

# API KEY taken from https://pro.coinmarketcap.com/account/
api_key = 'f04699ce-768b-41c3-8966-996380933287'

headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("My Cryptocurrency Portfolio")
print()

portfolio_value = 0.00  # this is the total value of our portfolio

table = PrettyTable(['Asset', 'Amount Owned', local_currency + ' Value', 'Price', '1h', '24h', '7d'])

with open('my_portfolio.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        # Line[0] is the symbol
        if '\ufeff' in line[0]:
            # line[0] = line[0].replace('\ufeff', '')
            line[0] = line[0][1:].upper()
        else:
            line[0] = line[0].upper()

        symbol = line[0]
        amount = line[1]  # line[1] is the amount owned

        quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol
        request = requests.get(quote_url, headers=headers)
        results = request.json()

        print(json.dumps(results, sort_keys=True, indent=4))
        try:
            currency = results['data'][symbol]
        except KeyError:
            continue
        name = currency['name']

        quote = currency['quote'][local_currency]  # Get the quote in local currency

        hour_change = round(quote['percent_change_1h'], 1)
        day_change = round(quote['percent_change_24h'], 1)
        week_change = round(quote['percent_change_7d'], 1)

        price = quote['price']

        value = float(price) * float(amount)
        portfolio_value += value  # add the value of the crypto to the total portfolio value

        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL
        if week_change > 0:
            week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL
        price_string = local_symbol + '{:,}'.format(round(price, 2))
        value_string = local_symbol + '{:,}'.format(round(value, 2))

        # Add values to table

        table.add_row([name + ' (' + symbol + ')',
                       amount,
                       value_string,
                       price_string,
                       str(hour_change),
                       str(day_change),
                       str(week_change)])
    print(table)
    print()

    portfolio_value_string = local_symbol + '{:,}'.format(round(portfolio_value, 2))
    print("Total Portfolio Value: " + Back.GREEN + portfolio_value_string +Style.RESET_ALL)

    print()
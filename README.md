# CoinMarketCap
Retrieving cryptocurrencies information from coinmarketcap Api. 

coincap_global retrieves following information from the CoinMarketCap API:
1) Bitcoin dominance
2) Ethereum dominance
3) Total market cap of all cryptocurrencies
4) Total volume (24h) of all cryptocurrencies


coincap_listings retrieves the top 100 cryptocurrencies from the CoinMarketCap API
For each of the 100 cryptocurrencies it lists:
1) Name, along with the symbol
2) Rank
3) Price
4) Market cap
5) Hour change
6) Day change
7) Week change
8) Percent change 24h
9) Total supply
10) Circulating supply
11) Volume

coincap_quotes lets you retrieve information for a specific cryptocurrency. You can enter the symbol of the cryptocurrency, for example BTC for Bitcoin, and it will display the information about BTC

Moving onto the projects directory now.
portfolio.py reads information stored in an excel file about what cryptocurrencies and how much of it the user has bought, and it displays to the user important information about it in an easy to read table (as seen below)
![image](https://user-images.githubusercontent.com/55329336/213912283-88066dd1-46a9-4003-8ba5-5b3495eaf965.png)

The purpose of the alerts.py is to alert the user once their cryptocurrency hits a specific amount. The user stores the cryptocurrency symbol along with the value in an excel file and whenever that cryptocurrency reaches that value, the user is alerted, stating the time when it hit that value. 
For the time being, the program needs to run on the user's personal computer, but the next steps for this app is to run it on the cloud and send a message to the user using the Twilio API.

top_hundred_crypto.py lists the top 100 cryptocurrencies based on either Market Cap, 24 hour Percent Change, or 24 Hour Volume, in a nice readable table, as you can see in the image below.
![image](https://user-images.githubusercontent.com/55329336/213912644-aa5c23fb-cbdf-4bc3-8cf9-54a47cb99b35.png)

research.py lets the user know what the future value of the cryptocurrencies would be, based on a number of factors.  
![image](https://user-images.githubusercontent.com/55329336/213912872-7f6cf438-4949-4b86-a374-3180709dbe55.png)

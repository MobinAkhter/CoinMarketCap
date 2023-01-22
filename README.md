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

portfolio.py reads information stored in an excel file about what cryptocurrencies and how much of it the user has bought, and it displays to the user important information about it in an easy to read table
![image](https://user-images.githubusercontent.com/55329336/213912283-88066dd1-46a9-4003-8ba5-5b3495eaf965.png)

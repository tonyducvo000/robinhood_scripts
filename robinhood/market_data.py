import os
import requests
import robin_stocks as rs
from collections import Counter

usr_name = os.environ.get("robinhood_username")
pass_word = os.environ.get("robinhood_password")

base_url = "https://api.robinhood.com/instruments/" #used to get instrument data

mkt = []

##get auth token
login = rs.robinhood.authentication.login(username=usr_name,
         password=pass_word,
         expiresIn=86400,
         by_sms=True)

#returns a dictionary with ticker symbol as key, value is a dictionary
hold = rs.robinhood.account.build_holdings(with_dividends=True)

#geneate dict template: {'symbol': {}, 'symbol': {}, etc}
sd = {} #stock data
for keys in hold:
    sd.update({keys:{}})

#parse through the dictionaries to retrieve data
for key, value in hold.items():

    #GETs
    stock_info = requests.request("GET", base_url+value['id'])
    #stock_info = requests.request("GET", sd[key]['url_info'])
    market = requests.request("GET", stock_info.json()['market'])
    #mic = market.json()['mic']
    mrkt_acronym = market.json()['acronym']
    mkt.append(mrkt_acronym) #for Counter function

count = Counter(mkt).most_common()
num_of_positions = len(hold.values())

for index in count:
    print(str(index[1]) + " (" + "{:.0%}".format(index[1]/num_of_positions) + ")" + " of your position(s) are on the " + index[0] + " market. \n")


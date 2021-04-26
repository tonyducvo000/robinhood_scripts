# robinhood_scripts
Script to get the number and percentage of what market your positions are on.  To run the script, users need to run ```set robinhood_username=your_username_here``` and ```set robinhood_password=your_password_here``` in the windows command line or ```export robinhood_username="your_username_here"``` and ```export robinhood_password="your_password_here"``` for Mac and Linux.  

```rs.robinhood.account.build_holdings(with_dividends=True)``` is used to get information of all the holdings, where the key are the ticker symbols, and the values are dictionaries containing stock information.  Using a for loop through each holding, the stock ID (extracted from build_holdings endpoint) is appended to a base url, namely ```base_url = "https://api.robinhood.com/instruments/"``` and a request is sent.  The return is a dictionary where a url for market information is stored, thus another request is made using ```market = requests.request("GET", stock_info.json()['market'])```.  The market acronym is then retrieved from the market info endpoint and stored in a list.  This list can be passed to a Counter function, where the number of markets are counted.  The number and percentage of stocks on a market is then printed.

This script is helpful to assess what market your positions are on.

Example output:

27 (68%) of your position(s) are on the NASDAQ market. 

7 (18%) of your position(s) are on the AMEX market. 

5 (12%) of your position(s) are on the NYSE market. 

1 (2%) of your position(s) are on the OTCM market. 

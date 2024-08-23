import pandas as pd
import yfinance as yf
im

tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

data = pd.DataFrame(columns=tickers_list)
date_now = datetime.datetime.now()


for ticker in tickers_list:
    data[ticker] = yf.download(ticker,'2016-01-01','2019-08-01')['Adj Close']


print(data.head())
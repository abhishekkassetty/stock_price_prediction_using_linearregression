import pandas as pd
import pandas_datareader.data as pdr
from datetime import datetime
# api's for stock data
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf


def stock_data(ticker):
    end = datetime.now()
    start = datetime(end.year-4,end.month,end.day)
    data = yf.download(ticker,start=start,end=end)#first trying to get data using yahoo finance
    df = pd.DataFrame(data=data)
    df.to_csv(''+ticker+'.csv')
    if(df.empty):#if we get any error using yahoo finance we are using alpha vantage api 
        df = pdr.DataReader(ticker+".BSE", "av-daily", start=datetime(2017, 2, 9),end=datetime(2021, 4, 21),api_key=api_key)
        df.to_csv(''+ticker+'.csv')
    return 
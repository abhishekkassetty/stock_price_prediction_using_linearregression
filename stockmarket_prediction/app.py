from flask import Flask,render_template,request
import pandas as pd
#data
from data import *
#models

from linearregression_model import *
import os

app = Flask(__name__)
#key for alpha vantage
api_key = 'NY59PBPMWLPHBD8R'

@app.route("/",methods = ["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["GET","POST"])
def analysis():
    ticker = request.form['ticker']#getting name of stock    
    try:
        stock_data(ticker)
    except:
        return render_template('index.html',not_found=True)
    else:#preprocessing data to train model
        df = pd.read_csv(''+ticker+'.csv')
        print("before prepocessing data")
        print(df.head())
        if(len(df.columns)>6):
            df.drop(['Open','High','Low','Adj Close','Volume'],axis=1,inplace=True)
        else:
            df.drop(['open','high','low','volume'],axis=1,inplace=True)
        df.columns=["Date","close"]
        print("after prepocessing data")
        print(df.head())
        df['Date']=pd.to_datetime(df['Date'])
        df.set_index('Date',inplace=True)

        LR_prediction,forecast_set,LR_error = LIN_ALGO(df)
        

        return render_template('results.html',ticker=ticker,lr_pred=round(LR_prediction,2),lr_error=LR_error)


if __name__=="__main__":
    app.run(debug=True)

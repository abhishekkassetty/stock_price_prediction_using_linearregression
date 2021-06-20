import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error





def LIN_ALGO(df):
    feature_days = 5
    df['Close after n days'] = df['close'].shift(-feature_days)
    df_new=df[['close','Close after n days']]
    df_new.head()
    y =np.array(df_new.iloc[:-feature_days,-1])
    y=np.reshape(y, (-1,1))
    X=np.array(df_new.iloc[:-feature_days,0:-1])
    X_to_be_forecasted=np.array(df_new.iloc[-feature_days:,0:-1])
    X_train=X[0:int(0.8*len(df)),:]
    X_test=X[int(0.8*len(df)):,:]
    y_train=y[0:int(0.8*len(df)),:]
    y_test=y[int(0.8*len(df)):,:]
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)        
    X_to_be_forecasted=sc.transform(X_to_be_forecasted)
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    y_test_pred=clf.predict(X_test)
    y_test_pred=y_test_pred*(1.04)
    error_lr = math.sqrt(mean_squared_error(y_test, y_test_pred))
    forecast_set = clf.predict(X_to_be_forecasted)
    forecast_set=forecast_set*(1.04)
    lr_pred=forecast_set[0,0]
    return lr_pred,forecast_set, error_lr
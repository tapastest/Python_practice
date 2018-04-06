import pandas as pd
import numpy as np
import quandl
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import datetime

df = quandl.get("WIKI/AMZN")

print(df.tail())

df = df[['Adj. Close']]
                # predicting 30 days into future
forecast_out = int(30)

print("predicting 30 days into future:   ", forecast_out)
                #  label column with data shifted 30 units up
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)
                # set X_forecast equal to last 30
X_forecast = X[-forecast_out:]
                # remove last 30 from X
X = X[:-forecast_out]

y = np.array(df['Prediction'])
y = y[:-forecast_out]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# Training
clf = LinearRegression()
clf.fit(X_train, y_train)
# Testing
confidence = clf.score(X_test, y_test)
print("confidence: ", confidence)

forecast_prediction = clf.predict(X_forecast)
print("Forecast : ", forecast_prediction)



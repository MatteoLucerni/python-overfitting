import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", sep=r'\s+', names=["CRIM", "ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PRATIO","B","LSTAT","MEDV"])
boston.head()

# simulazione un caso di overfitting

X = boston.drop('MEDV', axis=1).values
Y = boston['MEDV'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

pf = PolynomialFeatures(degree=2)

X_train_poly = pf.fit_transform(X_train)
X_test_poly = pf.transform(X_test)

ss = StandardScaler()

X_train_poly = ss.fit_transform(X_train_poly)
X_test_poly = ss.transform(X_test_poly)

lr = LinearRegression()
lr.fit(X_train_poly, Y_train)

# test
Y_preds = lr.predict(X_test_poly)

mse = mean_squared_error(Y_test, Y_preds)
r2s = r2_score(Y_test, Y_preds)

print('Test Score: ' +  str(r2s) + ' / Error: ' + str(mse))

# train
Y_preds_train = lr.predict(X_train_poly)

mse_train = mean_squared_error(Y_train, Y_preds_train)
r2s_train = r2_score(Y_train, Y_preds_train)

print('Train Score: ' +  str(r2s_train) + ' / Error: ' + str(mse_train))
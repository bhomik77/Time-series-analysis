import numpy as np
import pandas as pd
from models import *


data2 = pd.read_csv("final.csv")
data = pd.read_csv("Book.csv")


from sklearn import preprocessing
scaler = preprocessing.StandardScaler().fit(data2)
data2 = scaler.transform(data2)


y_reg = data["Return (%)"]
y_reg = y_reg[1:]
y_reg =  np.asarray(y_reg)
y_reg = np.reshape(y_reg, (len(y_reg), 1))
y_reg = y_reg[1:,:]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(np.asarray(data2), np.asarray(y), test_size=0.30, random_state=20)
# printing the accuracy of the models used.
print(LogisticRegression(X_train, y_train, X_test, y_test))

print(SIBC(X_train, y_train, X_test, y_test))

X_train, X_test, y_train, y_test = train_test_split(np.asarray(data2), np.asarray(y_reg), test_size=0.40, random_state=10)

print(linear_Regression(X_train, y_train, X_test, y_test))

print(ridge(X_train, y_train, X_test, y_test))

print(lasso(X_train, y_train, X_test, y_test))

print(elastic_net(X_train, y_train, X_test, y_test, 2))


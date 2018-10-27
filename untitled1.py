# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:59:08 2018

@author: user
"""
import pandas as pd
import numpy as np
from sklearn import linear_model
df = pd.read_excel(r"C:\Users\user\Desktop\test.xlsx")
x=df['first']
x_data=np.array(x)
x_data=np.reshape(x_data,(len(df),1))
#print(x_data)

y=df['second']
y_data=np.array(y)
y_data=np.reshape(y_data,(len(df),1))
#print(y_data)

x_train = x_data[0:10]
y_train = y_data[0:10]
print(x_train)
print(y_train)
regr = linear_model.LinearRegression()
regr.fit(x_train,y_train)
x_test = x_data[10:15]
y_test = regr.predict(x_test)
print(y_test)


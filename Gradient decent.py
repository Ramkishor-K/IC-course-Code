# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:59:08 2018

@author: user
"""
import pandas as pd
import numpy as np
#from sklearn import linear_model

df = pd.read_excel(r"C:\Users\user\Desktop\Book1.xlsx")
x=df['first']
x_data=np.array(x)
x_data=np.reshape(x_data,(len(df),1))
#print(x_data)

y=df['second']
y_data=np.array(y)
y_data=np.reshape(y_data,(len(df),1))

for index in range(0,10):
    x_value = (x_data[index] - np.min(x_data))/(np.max(x_data) - np.min(x_data))
print(x_value)



# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 09:47:09 2018

@author: user
"""

import pandas as pd
import numpy as np

df = pd.read_excel(r"C:\Users\user\Desktop\cloth_data.xlsx")

x=df['height']
x_data=np.array(x)
x_data=np.reshape(x_data,(len(df),1))

y=df['weight']
y_data=np.array(y)
y_data=np.reshape(y_data,(len(df),1))

s=df['size']
s_data=np.array(s)
s_data=np.reshape(s_data,(len(df),1))
s_train = s_data[0:18]

x_train = x_data[0:18]
y_train = y_data[0:18]

test_height = 161
test_weight = 61
z = np.sqrt(np.square(x_train - test_height) + np.square(y_train - test_weight))
print(z)
mini = np.min(z)    
print(mini)  
b = z  
print(b[1])
z = sorted(z)
for index in range(0,18):
    if(mini == b[index]):
        print(s_train[index])


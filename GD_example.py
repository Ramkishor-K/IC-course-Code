# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:54:43 2018

@author: user
"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import style
xs = np.array([150,153,155,158,159,162,165,170])
#print(xs)
ys = np.array([45,46,48,52,40,56,60,66])
xmean = mean(xs)
ymean = mean(ys)
sumx = sum(xs)
sumy = sum(ys)
sumxy = sum(xs*ys)
sumxx = sum(xs*xs)
sumsqx = sum(xs)*sum(xs)
sumxay = sum(xs)*sum(ys)
n = len(ys)
b1 = (n*sumxy-sumxay)/(n*sumxx-sumsqx)
b0 = ymean - b1*xmean 
y = b0 + b1*xs
print (y)
#plt.plot(xs,y,color = "g")
print(b0)
print(b1)
diff = ys - y
print(diff)
plt.plot(xs,diff,color = "g")
plt.scatter(xs,diff)
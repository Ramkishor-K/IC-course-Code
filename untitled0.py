from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import style
xs = np.array([1,2,3,4,5,6,7,8],dtype= np.float64)
print(xs)
ys = xs*2
plt.scatter(xs,ys)
xmean = mean(xs)
ymean = xmean
sumx = sum(xs)
sumy = sumx
sumxy = sum(xs*ys)
sumxx = sum(xs*xs)
sumsqx = sum(xs)*sum(xs)
sumxay = sum(xs)*sum(ys)
n = len(xs)
b1 = (n*sumxy-sumxay)/(n*sumxx-sumsqx)
b0 = (1/n)*ymean - b1*xmean 
y = b0 + b1*xs
print (y)
plt.plot(xs,y,color = "g")
print(b0)
print(b1)
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:32:31 2020

@author: satya
"""

import pandas as pd
n = int(input("Enter number of observations "))
xdata=[]
ydata=[]
for i in range(n):
    x=float(input("Enter "+str(i+1)+" X data "))
    xdata.append(x)
for i in range(n):
    y=float(input("Enter "+str(i+1)+" Y data "))
    ydata.append(y)
    
#df = pd.DataFrame(data, columns = ['Score', 'Index']) 
#print(xdata)
#print(ydata)
df=pd.DataFrame({'X':xdata, 'Y': ydata})
#print(df.head(n))
print(df.corr())
print(" ")
sumX=df['X'].sum()
sumY=df['Y'].sum()
sumXsumY=sumX*sumY
sumXY=0
sumXX=0
sumYY=0
for i in df['X']:
    sumXX=sumXX+i*i
for i in df['Y']:
    sumYY=sumYY+i*i
for i in range(n):
    sumXY=sumXY+xdata[i]*ydata[i]
print("Sum of X = " +str(sumX))
print("Square of Sum of X = " +str(sumX*sumX))
print("Sum of Y =" +str(sumY))
print("Square of Sum of Y = " +str(sumY*sumY))
print("Sum of sumX*sumY = " +str(sumXsumY))
print("Sum of XX = " +str(sumXX))
print("Sum of YY = " +str(sumYY))
print("Sum of XY = "+str(sumXY))
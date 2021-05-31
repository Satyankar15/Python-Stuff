# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:08:22 2020

@author: satya
"""

count=dict()
arr=list()
l=int(input("Enter number of values "))
for i in range(l):
    x=input("Enter number "+str(i+1)+" ")
    arr.append(x)
arr.sort()
for i in arr:
    count[i]=count.get(i,0)+1
print(count)
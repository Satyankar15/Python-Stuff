# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:13:37 2021

@author: satya
"""

buff=dict()
def first(prod,name):
    x=Pro[prod] #prod is only used for list
    for i in x:
        j=i.split('|')
        for k in j:
            flag=1
            for m in range(len(k)):
                if k[m] in T:
                    if flag==1:
                        if name in buff:
                            if k[m] not in buff[name]:
                                buff[name].append(k[m])
                        else:
                            buff[name]=list(k[m])
                        flag=0
                elif k[m]==prod or  k[m]==name: break    
                elif (m==0):
                    first(k[m],name)
        
        
        #print(str(name)+": ")

    
    
    
    
    
V = input("Enter Non terminals: ").split()
T = input("Enter terminals: ").split()
n = int(input("Enter No. of productions: "))
Pro={}
for i in range(0,n):
    temp=input().split("->")
    if temp[0] in Pro:
        Pro[temp[0]].append(temp[1].split("/"))
    else:
        Pro[temp[0]]=temp[1].split("/")

for i in range(len(V)):       
    first(V[i],V[i])
print(buff)
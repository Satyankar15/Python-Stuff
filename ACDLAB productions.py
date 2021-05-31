# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:34:34 2021

@author: satya
"""
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
Start=V[0]
T0=0
T1=1
T2=1
T3=1
flag=0
for i in Pro:
    for j in T: 
        b=str(Pro[i])
        if j in b:   
            T0=T0+1
            break
if(T0==len(V)):
    T0=1
else: 
    T0=-1
if(Start==list(Pro.keys())[0]):
    Z=Pro[Start]
    z=Z[0].split('|')
    if('$' in z):   flag=1
if(T0==1):
    for keys,values in Pro.items():
        for v in values:
            w=v.split('|')
            for i in w:
                if(Start in i): 
                    if(flag==1): T1=-1
                if(len(keys)>len(i)):
                    T1=-1
                    break
                else:   continue


if(T1==1):
    for key in Pro.keys():
        if(len(key)>1): T2=-1
else:   T2=-1


side=0
if(T2==1):
    for key,value in Pro.items(): #vale is  list of array
        for v in value: #v is array
            w=v.split('|')
            for i in w:
                vflag=1
                for j in range(len(i)):
                    if i[j] in V:
                        vflag=vflag-1
                        if(side!=0):
                            if(j==0):   
                                if(len(i)==1): continue
                                if(side==-1):    continue
                                else:
                                    T3=0
                                    break
                            else:#nont terminal on right
                                if(j!=len(i)-1):
                                    T3=0
                                    break
                                if(side==-1):
                                    T3=0
                                    break
                                else:
                                    if(vflag<0):
                                        T3=0
                                        break
                        elif(j==0):   side=-1
                        else:   side=1
                        if(vflag<0):
                            T3=0
                            break
else: T3=0
    
if(T3==1): print("Type 3")
elif(T2==1):    print("Type 2")
elif(T1==1):    print("Type 1")
elif(T0==1):    print("Type 0")
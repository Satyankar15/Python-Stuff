# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:39:26 2020

@author: satya
"""

from numpy import random
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`|=+'''
x=random.randint(25)
#print(x)
crypt=list()
message=input("Enter message ")
for i in message:
    #print(i)
    crypt.append(chr(ord(i)+x%26))
print(' '.join(crypt))

print("Possible Decryptions")
decrypt=list()
x=0
while x<26:
    for i in crypt:
        c=(chr(ord(i)-x%26))
        if c in punctuations : break
        decrypt.append(c)
    if(len(decrypt)==len(crypt)) : print(' '.join(decrypt))
    decrypt.clear()
    x=x+1
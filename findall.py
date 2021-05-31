# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:29:12 2020

@author: satya
"""

import re
sum=0
hand=open('sum.txt')
for line in hand:
    line=line.rstrip();
    y=re.findall('([0-9]+)',line)
    for i in y:
        sum=sum+int(i)
print(sum)
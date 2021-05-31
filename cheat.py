# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:55:25 2020

@author: satya
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    
    print (s[position-1])
    print (t[position-1])
    url = (s[position-1])
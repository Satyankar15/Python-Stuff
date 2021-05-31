import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
translator = str.maketrans('', '', string.punctuation)
fh=open("HeyJude.txt","r")
words=list()
for line in fh:
    line = line.translate(translator)
    line=line.lower()
    word=line.split()
    for i in range(len(word)):
        #if(len(word[i])<4): continue
        words.append(word[i])
lyrics=dict()
for i in words:
    lyrics[i]=lyrics.get(i,0)+1
#print(lyrics.items())
#df=pd.DataFrame(data=lyrics.items(), columns=(['Word', 'Frequency']))


pt.figure(figsize=(200.0,10.0))
pt.plot(lyrics.keys(),lyrics.values())
pt.xlabel('Words')
pt.ylabel("Frequency")
pt.show()
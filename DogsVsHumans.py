import numpy as np
from matplotlib import pyplot as plt
from math import log
X=np.arange(0,16,1)
#X2=np.arange(0,80,1)
print(X)
Y=list()
for i in X:
    if(i==0): val=0
    else:    val=16*log(i)+31
    Y.append(val)
print(Y)
plt.plot(X,Y,label='Dogs')
Z=np.arange(0,80,1)
plt.plot(Z,label='Humans')
plt.legend()
plt.title("Dog Years vs Human Years")
plt.show()
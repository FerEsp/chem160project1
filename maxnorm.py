import numpy as np
from matplotlib import pyplot as plt
x = 201
ntrials = 5000
f=[]
n=[]
for N in range(1,x):
    sum=0
    for trial in range(0,ntrials-1):
        r = np.random.normal(0,1,N)
        m = np.amax(r)
        sum += m
    Avg_Max = sum/trial
    f.append(Avg_Max)
    n.append(N)
plt.plot(n,f)
plt.grid()
plt.xlabel('N')
plt.ylabel('Avg_max')
plt.title("MaxNorm")
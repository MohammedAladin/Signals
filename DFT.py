#calculate DFT of a given signal x[n]
import numpy as np

N = int(input("Enter the number of samples: "))
p = int(input("Enter the number of zero padding samples : "))
#add zero padding
x = [0]*(N+p)

for k in range(0,N):
    sum = 0
    for n in range(0,N+p):
        x[n] = (np.sin(2*np.pi*n*k/N))
        sum = sum + x[n]*(np.exp((-2*np.pi*1j*k*n)/N))
    print(sum)

#calculate inverse DFT with N samples 


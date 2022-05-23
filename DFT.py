#calculate DFT of a given signal
import numpy as np
x = [None]
N = int(input("Enter the number of samples: "))
for k in range(0,N):
    sum = 0

    for n in range(0,N):
        sum = sum + (1/N)*(np.exp(-2*np.pi*1j*k*n/N))*(np.sin(2*np.pi*n*k/N))
    print(sum)


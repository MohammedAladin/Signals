import numpy as np
#calculate DFT of a given signal x[n]
x = [3,2] #input signal

def DFT(x):
    N = len(x) #length of the signal
    X = [0]*N #initialize X
    for k in range(N):
        for n in range(N):
            X[k] += x[n]*np.exp(-2j*np.pi*n*k/N)
    return X
print(DFT(x))

#recursive function to calculate FFT
def FFT(x):
    N = len(x)
    if N <= 1:
        return x
    even = FFT(x[0::2]) #take even terms
    odd = FFT(x[1::2]) #take odd terms
    T = [np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] 
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

print(FFT(x))


import numpy as np
import matplotlib.pyplot as plt
import cmath
 
#[Convolution and LTI system] 
y=[]
h =[None]*99 
x=[None]*500 
x[0]=1

#[plotting the impulse response]
graph1 = plt.figure(figsize=(15,7))
Impulse_Response = graph1.add_subplot(111)
Impulse_Response.set_title("Impulse response plots")


for n in range(0,99):
     val = 0.31752 * np.sin(0.314159 * (n-49.00001)) / (n-49.00001)
     h[n] = val * (0.54 - 0.46 * np.cos(0.0641114 * n))
     Impulse_Response.plot(n,h[n],'og')

#-------------------------------------------------------------------------------

#[Fisrt convolution y[n] = x[n-k]*h[n] ]

graph2 = plt.figure(figsize=(15,7))
Input_Signal = graph2.add_subplot(111)
Input_Signal.set_title("Input First Signal")

# plotting the first input signal x[n]=1 when n=0 , x[n]=0 otherWise
x=[0]*500 
x[0]=1
for i in range(0,500):
    Input_Signal.plot(i,x[i],'ob')

graph3 = plt.figure(figsize=(15,7))
Output_Signal = graph3.add_subplot(111)
Output_Signal.set_title("Output First Signal")

# convolution y[n] = x[n-k]*h[n]
y = np.convolve(x,h,mode="full")
for n in range(1,598):
      Output_Signal.plot(n,y[n],'ob')
#-------------------------------------------------------------------------------

#[Generate a more complicated test signal]
#amplitude*sin(w) , where w = (2*pi*k)/N, where k = (6,44) 

graph4 = plt.figure(figsize=(15,7))
Input_Signal_With_Noise = graph4.add_subplot(111)
Input_Signal_With_Noise.set_title("Input Noise Signal")

# plotting the comlicated input signal x[n]
for i in range(1,500):
    x[i] =  np.sin(2*np.pi*6*i/500) + 0.5*np.sin(2*np.pi*44*i/500)
    Input_Signal_With_Noise.plot(i,x[i],'or')

graph5 = plt.figure(figsize=(15,7))
Output_Signal_With_Filter = graph5.add_subplot(111)
Output_Signal_With_Filter.set_title("Output Filter Signal")

# convolution y[n] = x[n-k]*h[n]
y = np.convolve(x,h,mode="full")
for n in range(1,598):
      Output_Signal_With_Filter.plot(n,y[n],'or') 

plt.show() 
#-------------------------------------------------------------------------------

#second convolution y[n] = x[n-k]*h[n] --> y[n] is the is the same if we make 
#the conv with only first input x[n] = np.sin(2*np.pi*6*i/500) 
#because the secound one make 44 cycle in 500 samples and the filter passes
#sinusoids that have fewer than 25 cycles in 500 samples, 
#and blocks sinusoids with a higher frequency so it passes only
#fisrt sinsoid signal that makes 6 cycles in 500 samples and blockes the other one 
#-------------------------------------------------------------------------------




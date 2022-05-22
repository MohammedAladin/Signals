import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import scipy.fft
import simpleaudio as sa
import librosa

Record_path = "/content/Recording (2).wav"


Mohammed_Record, Sampling_Rate = librosa.load(Record_path) # load record as a wave 


def magnitude(Record, s):        # calculate the Fast Fourier Trasnsform and get the magnitude of fft 
    fourier_transform = np.fft.fft(Record)
    magnitude = np.abs(fourier_transform)
    plt.figure(figsize=(16,5))
    freq = np.linspace(0,s,len(magnitude))
    num_freq = int(len(freq)*0.1)

    plt.plot(freq[:num_freq], magnitude[:num_freq])
    plt.xlabel("Frequency")
    plt.title("Magnitude Spectrum")
    plt.show

def Invesre_magnitude(Record, s):
    fourier_transform_Inverse = np.fft.ifft(np.fft.fft(Record))
    inv_magnitude = np.abs(fourier_transform_Inverse)
    plt.figure(figsize=(16,5))
    time = np.linspace(0,s,len(inv_magnitude))
    num_time = int(len(time)*0.1)

    plt.plot(time[:num_time], inv_magnitude[:num_time])
    plt.xlabel("t")
    plt.title("Inverse Magnitude")
    plt.show
    sf.write('Produced Record.wav', inv_magnitude, 20000, 'PCM_24')  # write the result in wave file 


magnitude(Mohammed_Record,  Sampling_Rate) #plotting the magnitude signal 
Invesre_magnitude(Mohammed_Record,  Sampling_Rate) #plotting the magnitude signal
'''PUNTO 12
Generar dos tonos senoidales de 50 Hz y 51 Hz respectivamente, de 2 segundos de duración cada
uno y muestreados a fs = 44100 Hz. Para una señal que consista en la superposición de dichos
tonos, analice qué ventana y de qué longitud mínima N debe usar para ser capaz de reconocer las
dos componentes armónicas, en las siguientes condiciones:
*Las amplitudes de las senoides son iguales (A1 = A2).
*Las amplitudes relativas difieren en un factor de 100 (A1 = 100A2).
*Generalizar la situación anterior analizando el caso de que las amplitudes relativas difieran
en un factor de K (A1 = K A2).'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal.windows as wds
from scipy.fft import fft, fftshift
import Utils

def graficar():
    inicio = 0
    fin = 2
    dur = fin - inicio #Duración
    fs_Hz = 44100 #Frecuencia de muestreo
    φ = 0 #Fase

    # Definir el rango "t".
    t = np.linspace(inicio, fin, dur*fs_Hz, endpoint=None)

    senoide_50Hz = Utils.generar_senoide(t, 1, 50, φ)
    senoide_51Hz = Utils.generar_senoide(t, 1, 51, φ)
    suma_senoides = senoide_50Hz + senoide_51Hz

    ##
    window1 = wds.get_window('boxcar', dur*fs_Hz)
    #plt.plot(window)
    #plt.title("Boxcar window")
   # plt.ylabel("Amplitude")
   # plt.xlabel("Sample")

    señal = suma_senoides * window1

    A = np.fft.rfft(señal, n=2*fs_Hz)
    freq = np.fft.rfftfreq(2*fs_Hz, d=1/fs_Hz)
    response = 20 * np.log10(np.abs(A))
    plt.plot(freq, response)

    plt.xlim(0, 100)
    #plt.axis([-0.5, 0.5, -120, 0])
    #plt.title("Frequency response of the boxcar window")
    #plt.ylabel("Normalized magnitude [dB]")
    #plt.xlabel("Normalized frequency [cycles per sample]")

    ##

    #plt.plot(t, suma_senoides, color='red', label='cuadrada')

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

    senoide_51hz_alta_amp = Utils.generar_senoide(t, 100, 53, φ) #con 51Hz no se pueden distinguir los lobulos ni siquiera con la ventana kaiser. En todo caso preguntar
    suma_senoides2 = senoide_50Hz + senoide_51hz_alta_amp
    window2 = wds.get_window(('kaiser', 10), dur*fs_Hz)

    señal2 = suma_senoides2 * window2

    A = np.fft.rfft(señal2, n=8*fs_Hz)
    freq = np.fft.rfftfreq(8*fs_Hz, d=1/fs_Hz)
    response = 20 * np.log10(np.abs(A))
    plt.plot(freq, response)

    plt.xlim(0, 100)
    #plt.axis([-0.5, 0.5, -120, 0])
    #plt.title("Frequency response of the boxcar window")
    #plt.ylabel("Normalized magnitude [dB]")
    #plt.xlabel("Normalized frequency [cycles per sample]")

    ##

    #plt.plot(t, suma_senoides, color='red', label='cuadrada')

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

graficar()#python3 TP7-Punto12.py
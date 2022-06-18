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

def generar_senoide(t, A, frec_Hz, φ):
    return A * np.sin(2 * np.pi * frec_Hz * t + φ)

def graficar():
    inicio = 0
    fin = 2
    dur = fin - inicio #Duración
    fs_Hz = 44100 #Frecuencia de muestreo
    A_50 = 1 #amplitud
    A_51 = 1*100
    φ = 0 #Fase

    # Definir el rango "t".
    t = np.linspace(inicio, fin, dur*fs_Hz, endpoint=None)

    senoide_50Hz = generar_senoide(t, A_50, 50, φ)
    senoide_51Hz = generar_senoide(t, A_51, 51, φ)
    suma_senoides = senoide_50Hz + senoide_51Hz

    ##
    window = wds.boxcar(88200)
    #plt.plot(window)
    #plt.title("Boxcar window")
   # plt.ylabel("Amplitude")
   # plt.xlabel("Sample")

    señal = suma_senoides * window

    #plt.figure()
    A = fft(señal, 2048, norm='forward') / (len(window)/2.0)
    print(A)
    freq = np.linspace(-0.5, 0.5, len(A))
    response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
    plt.plot(freq, response)
    plt.axis([-0.5, 0.5, -120, 0])
    plt.title("Frequency response of the boxcar window")
    plt.ylabel("Normalized magnitude [dB]")
    plt.xlabel("Normalized frequency [cycles per sample]")

    ##

    #plt.plot(t, suma_senoides, color='red', label='cuadrada')

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

graficar()#python3 TP7-Punto12.py
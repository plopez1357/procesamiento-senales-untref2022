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

def obtener_suma_senoides(t, A_1, A_2, f_1, f_2, φ):
    senoide_1 = Utils.generar_senoide(t, A_1, f_1, φ)
    senoide_2 = Utils.generar_senoide(t, A_2, f_2, φ)
    return senoide_1 + senoide_2

def obtener_señal_ventaneada(señal, window, n, d):
    señal_ventana = señal * window
    A = np.fft.rfft(señal_ventana, n)
    freq = np.fft.rfftfreq(n, d)
    señal_ventaneada = 20 * np.log10(np.abs(A))
    return freq, señal_ventaneada

def grafico_igual_amplitud(t, φ, fs_Hz):
    suma_senoides = obtener_suma_senoides(t, 1, 1, 50, 51, φ)

    window_boxcar = wds.get_window('boxcar', len(t))

    freq, señal_ventaneada = obtener_señal_ventaneada(suma_senoides, window_boxcar, len(t), 1/fs_Hz)

    plt.plot(freq, señal_ventaneada, label='señal venteneada rectangular')

    plt.title("Señal con armonicas de 50 y 51 Hz y amplitud A1 = A2 ventaneada con ventana rectangular. N = 2*fs")

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud (dB)")

    plt.xlim(40, 60)

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

def grafico_distinta_aplitud(t, φ, fs_Hz):
    suma_senoides = obtener_suma_senoides(t, 1, 100, 50, 52, φ)

    window_kaiser = wds.get_window('hamming', len(t))

    freq, señal_ventaneada = obtener_señal_ventaneada(suma_senoides, window_kaiser, len(t), 1/fs_Hz)

    plt.plot(freq, señal_ventaneada, label='señal venteneada hamming')

    plt.title("Señal con armonicas de 50 y 52 Hz y amplitud A2 = 100 * A1 ventaneada con ventana hamming. N = 2*fs")

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud (dB)")

    plt.xlim(40, 60)

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

def graficar():
    inicio = 0
    fin = 2
    dur = fin - inicio #Duración
    fs_Hz = 44100 #Frecuencia de muestreo
    φ = 0 #Fase

    # Definir el rango "t".
    t = np.linspace(inicio, fin, dur*fs_Hz, endpoint=None)

    grafico_igual_amplitud(t, φ, fs_Hz)

    grafico_distinta_aplitud(t, φ, fs_Hz)

graficar()#python3 TP7-Punto12.py
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


def graficar():
    T = 1 #Periodo
    N = 5 #Cantidad de períodos
    inicio = 0
    fin = 10 # El fin de la señal es la cantidad de períodos
    dur = fin - inicio #Duración
    
    frec_Hz_seno1 = 50;  
    frec_Hz_seno2 = 51; 

    fs_Hz = 44100 #Frecuencia de muestreo

    # Definir el rango "t".
    t = np.linspace(inicio, fin, dur*fs, endpoint=None)

    #plt.plot(eje_frec, espectro_cuadrada, color='red', label='cuadrada')
    #plt.plot(eje_frec, espectro_aperiodica, color='black', label='aperiodica')

    plt.legend()
    plt.grid()
    plt.show()

graficar()#python3 TP7-Punto12.py
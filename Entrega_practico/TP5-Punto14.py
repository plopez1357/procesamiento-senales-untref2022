'''PUNTO 14
Generar N períodos de alguna señal 'r (t) que no sea senoidal, por ejemplo una cuadrada, una
dientes de sierra o de algún otro tipo. Generar luego una señal aperiódica r (t) de la misma longitud,
que sea igual a 'r (t) sobre un período únicamente. Graficar los espectros de ambas y compararlos.'''

import numpy as np
import matplotlib.pyplot as plt
import Utils

def obtener_un_periodo(señal, T, fs):
    señal_un_periodo = np.array(señal[0:T * fs])
    return np.concatenate((señal_un_periodo, np.zeros(len(señal) - len(señal_un_periodo))))

def graficar():
    T = 500 #Periodo
    N = 2 #Cantidad de períodos
    inicio = 0
    fin = int(T * N) # El fin de la señal es la cantidad de períodos
    dur = fin - inicio #Duración
    fs = 200 #Frecuencia de muestreo

    # Definir el rango "t".
    t = np.linspace(inicio, fin, dur*fs, endpoint=None)

    señal_cuadrada = Utils.generar_señal_cuadrada(t, T)
    señal_cuadrada_aperiodica = obtener_un_periodo(señal_cuadrada, T, fs)

    espectro_cuadrada = Utils.obtener_modulo_espectro(señal_cuadrada)
    espectro_aperiodica = Utils.obtener_modulo_espectro(señal_cuadrada_aperiodica)

    eje_frec = np.linspace(0, fs, len(espectro_cuadrada), endpoint=None)

    plt.plot(eje_frec, espectro_cuadrada, color='red', label='cuadrada')
    plt.plot(eje_frec, espectro_aperiodica, color='black', label='aperiodica')

    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

graficar()#python3 TP5-Punto14.py
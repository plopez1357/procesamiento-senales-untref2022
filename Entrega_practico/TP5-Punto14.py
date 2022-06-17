'''PUNTO 14
Generar N períodos de alguna señal 'r (t) que no sea senoidal, por ejemplo una cuadrada, una
dientes de sierra o de algún otro tipo. Generar luego una señal aperiódica r (t) de la misma longitud,
que sea igual a 'r (t) sobre un período únicamente. Graficar los espectros de ambas y compararlos.'''

import numpy as np
import matplotlib.pyplot as plt
import math

def obtener_espectro(señal):
    #Trasnfomamos de nuevo para tener obtener el espectro
    señal_transformada = np.fft.fft(señal, norm='forward')
    señal_modulo = np.abs(señal_transformada)
    return señal_modulo
    
def generar_aperiodica(t):
    return np.array([x**2 for x in t])

def generar_cuadrada(t):
    return np.array([10 if math.floor(2 * x) % 2 == 0 else 0 for x in t])

def graficar():
    t = np.linspace(0, 5, 1000)
    señal_cuadrada = generar_cuadrada(t)
    señal_aperiodica = generar_aperiodica(t)

    espectro_cuadrada = obtener_espectro(señal_cuadrada)
    espectro_aperiodica = obtener_espectro(señal_aperiodica)

    plt.plot(t, espectro_cuadrada, label = 'cuadrada')
    plt.plot(t, espectro_aperiodica, label = 'aperiodica')
    plt.legend()
    plt.show()

graficar()
#python3 TP5-Punto14.py
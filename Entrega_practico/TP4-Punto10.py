'''PUNTO 10
Construir un algoritmo que permita, dada una señal de entrada periódica cualquiera, calcular de
forma aproximada los n primeros coeficientes de su desarrollo en serie de Fourier. Debe hacerlo
implementando la ecuación de análisis en su forma polar, generando las senoides adecuadas con
la misma frecuencia demuestreo que la señal original.'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy import signal

# Señal de entrada periódica 
def f(t):
    #return np.sin(t)
    #return np.cos(t)
    return signal.square(t) #función cuadrada con periodo 2π

# Expansión en serie de Fourier de la función f(t).
def Sf(t, T, L, w, n):
    a0 = a(0, T, L, w)
    sum = np.zeros(np.size(t))
    for i in np.arange(0, n):
        sum += ((a(i, T, L, w) * np.cos(i * w * t)) + (b(i, T, L, w) * np.sin(i * w * t)))
    return (a0 / 2) + sum

# Coeficiente "an".
def a(n, T, L, w):
    return (2 / T) * integrate.quad(lambda t: f(t) * np.cos(n * w * t), -L, L)[0]

# Coeficiente "bn".
def b(n, T, L, w):
    return (2 / T) * integrate.quad(lambda t: f(t) * np.sin(n * w * t), -L, L)[0]

def graficar():
    T = 2 * np.pi #Periodo T de la función.
    L = T / 2 #Intervalo de integración
    w = (2 * np.pi) / T #Frecuencia angular de f.
    inicio = 0
    fin = 10
    dur = fin - inicio #Duración
    fs = 200 #Frecuencia de muestreo
    n = 14 #Cantidad de armónicos

    # Definir el rango "t".
    t = np.linspace(inicio, fin, dur*fs, endpoint=None)

    # Señal Original.
    plt.plot(t, f(t), color='black', label='Señal original')

    # Aproximación de la señal con la serie de fourier.
    plt.plot(t, Sf(t, T, L, w, n), '.', color='red', label='Aproximación Fourier')

    plt.legend()
    plt.grid()
    plt.show()

graficar() #python3 TP4-Punto10.py
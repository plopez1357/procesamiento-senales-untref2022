'''PUNTO 10
Construir un algoritmo que permita, dada una señal de entrada periódica cualquiera, calcular de
forma aproximada los n primeros coeficientes de su desarrollo en serie de Fourier. Debe hacerlo
implementando la ecuación de análisis en su forma polar, generando las senoides adecuadas con
la misma frecuencia demuestreo que la señal original.'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Define "t" range.
t = np.linspace(0, 10, 1000)

# Periodo T de la función.
T = 2

L = T / 2
w = (2 * np.pi) / T # es la frecuencia angular de f.

# "f(t)" -> sen(2πt) + cos(4πt) + sen(πt).
def f(t): 
    return np.sin(2 * np.pi * t) + np.cos(4 * np.pi * t) + np.sin(np.pi * t)

# "a" coefficient calculation.
def a(n):
    return (1 / L) * integrate.quad(lambda t: f(t) * np.cos(n * w * t), -L, L)[0]

# "b" coefficient calculation.
def b(n):
    return (1 / L) * integrate.quad(lambda t: f(t) * np.sin(n * w * t), -L, L)[0]

# Fourier series.   
def Sf(x, L, n = 10):
    a0 = a(0, L)
    sum = np.zeros(np.size(x))
    for i in np.arange(1, n + 1):
        sum += ((a(i, L) * np.cos(i * w * t)) + (b(i, L) * np.sin(i * w * x)))
    return (a0 / 2) + sum

def graficar():
    # x axis.
    plt.plot(t, np.zeros(np.size(t)), color = 'black')

    # y axis.
    plt.plot(np.zeros(np.size(t)), t, color = 'black')

    # Original signal.
    plt.plot(t, f(t), linewidth = 1.5, label = 'Signal')

    # Approximation signal (Fourier series coefficients).
    plt.plot(t, Sf(t, L, 8), '.', color = 'red', linewidth = 1.5, label = 'Fourier series')

    # Specify x and y axes limits.
    plt.xlim([0, 5])
    plt.ylim([-3, 3])

    plt.legend(loc = 'upper right', fontsize = '10')

    plt.show()

graficar() #python3 TP4-Punto10.py
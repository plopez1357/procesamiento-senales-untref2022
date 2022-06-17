'''PUNTO 10
Construir un algoritmo que permita, dada una señal de entrada periódica cualquiera, calcular de
forma aproximada los n primeros coeficientes de su desarrollo en serie de Fourier. Debe hacerlo
implementando la ecuación de análisis en su forma polar, generando las senoides adecuadas con
la misma frecuencia demuestreo que la señal original.'''

import numpy as np
import matplotlib.pyplot as plt

# Define "x" range.
x = np.linspace(0, 10, 1000)

# Define "T", i.e functions' period.
T = 2
L = T / 2

# "f(x)" function definition.
def f(x): 
    return np.sin((np.pi) * x) + np.sin((2 * np.pi) * x) + np.sin((5 * np.pi) * x)

# "a" coefficient calculation.
def a(n, L, accuracy = 1000):
    a, b = -L, L
    dx = (b - a) / accuracy
    integration = 0
    for x in np.linspace(a, b, accuracy):
        integration += f(x) * np.cos((n * np.pi * x) / L)
    integration *= dx
    return (1 / L) * integration

# "b" coefficient calculation.
def b(n, L, accuracy = 1000):
    a, b = -L, L
    dx = (b - a) / accuracy
    integration = 0
    for x in np.linspace(a, b, accuracy):
        integration += f(x) * np.sin((n * np.pi * x) / L)
    integration *= dx
    return (1 / L) * integration

# Fourier series.   
def Sf(x, L, n = 10):
    a0 = a(0, L)
    sum = np.zeros(np.size(x))
    for i in np.arange(1, n + 1):
        sum += ((a(i, L) * np.cos((i * np.pi * x) / L)) + (b(i, L) * np.sin((i * np.pi * x) / L)))
    return (a0 / 2) + sum   

# x axis.
plt.plot(x, np.zeros(np.size(x)), color = 'black')

# y axis.
plt.plot(np.zeros(np.size(x)), x, color = 'black')

# Original signal.
plt.plot(x, f(x), linewidth = 1.5, label = 'Signal')

# Approximation signal (Fourier series coefficients).
plt.plot(x, Sf(x, L), '.', color = 'red', linewidth = 1.5, label = 'Fourier series')

# Specify x and y axes limits.
plt.xlim([0, 5])
plt.ylim([-2.2, 2.2])

plt.legend(loc = 'upper right', fontsize = '10')

plt.show()

#python3 Punto1.py
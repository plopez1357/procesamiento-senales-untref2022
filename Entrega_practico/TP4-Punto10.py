'''PUNTO 10
Construir un algoritmo que permita, dada una señal de entrada periódica cualquiera, calcular de
forma aproximada los n primeros coeficientes de su desarrollo en serie de Fourier. Debe hacerlo
implementando la ecuación de análisis en su forma polar, generando las senoides adecuadas con
la misma frecuencia demuestreo que la señal original.'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import Utils

# Señal de entrada periódica 
def f(t, T):
    return Utils.generar_señal_cuadrada(t, T)

# Expansión en serie de Fourier de la función f(t).
def Sf(t, T, L, w, n):
    a0 = a(0, T, L, w)
    sum = np.zeros(np.size(t))
    for i in np.arange(0, n):
        sum += ((a(i, T, L, w) * np.cos(i * w * t)) + (b(i, T, L, w) * np.sin(i * w * t)))
    return (a0 / 2) + sum

# Coeficiente "an".
def a(n, T, L, w):
    return (2 / T) * integrate.quad(lambda t: f(t, T) * np.cos(n * w * t), -L, L)[0]

# Coeficiente "bn".
def b(n, T, L, w):
    return (2 / T) * integrate.quad(lambda t: f(t, T) * np.sin(n * w * t), -L, L)[0]

def graficar_sub_plot(axs, t, T, L, w, n):
    axs.plot(t, f(t, T), color='black', label='Señal original')
    axs.plot(t, Sf(t, T, L, w, n), '.', color='red', label='Aproximación Fourier')
    axs.set_title('n = ' + str(n))
    axs.legend(loc='upper right', fontsize = '6')
    axs.grid()

def graficar():
    T = 2 #Periodo T de la función.
    L = T / 2 #Intervalo de integración
    w = (2 * np.pi) / T #Frecuencia angular de f.
    inicio = 0
    fin = 10
    dur = fin - inicio #Duración
    fs = 200 #Frecuencia de muestreo

    # Definir el rango "t".
    t = np.linspace(inicio, fin, dur*fs, endpoint=None)

    fig, axs = plt.subplots(2, 2, sharey=True, figsize=[14, 11])

    graficar_sub_plot(axs[0][0], t, T, L, w, 3)
    graficar_sub_plot(axs[0][1], t, T, L, w, 6)
    graficar_sub_plot(axs[1][0], t, T, L, w, 9)
    graficar_sub_plot(axs[1][1], t, T, L, w, 12)
    plt.show()

graficar() #python3 TP4-Punto10.py
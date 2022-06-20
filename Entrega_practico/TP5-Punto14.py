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

def generar_espectros(T, N):
    #T = Periodo
    #N = Cantidad de períodos
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

    return eje_frec, espectro_cuadrada, espectro_aperiodica

def graficar():

    fig, axs = plt.subplots(2, 2, sharey=False, figsize=[14, 11])

    label1 = 'Cuadrada'
    label2 = 'Aperiodica'
    eje_frec_100, espectro_cuadrada_100, espectro_aperiodica_100 = generar_espectros(2, 3)
    eje_frec_400, espectro_cuadrada_400, espectro_aperiodica_400 = generar_espectros(4, 3)
    eje_frec_800, espectro_cuadrada_800, espectro_aperiodica_800 = generar_espectros(8, 3)
    eje_frec_1600, espectro_cuadrada_1600, espectro_aperiodica_1600 = generar_espectros(16, 3)
    

    Utils.graficar_sub_plot(axs[0][0], eje_frec_100, espectro_cuadrada_100, espectro_aperiodica_100, label1, label2, 'Periodo = 100')
    axs[0][0].set_xlim(0, 100)
    axs[0][0].set_ylim(0, 0.3)

    Utils.graficar_sub_plot(axs[0][1], eje_frec_400, espectro_cuadrada_400, espectro_aperiodica_400, label1, label2, 'Periodo = 400')
    axs[0][1].set_xlim(0, 100)
    axs[0][1].set_ylim(0, 0.3)

    Utils.graficar_sub_plot(axs[1][0], eje_frec_800, espectro_cuadrada_800, espectro_aperiodica_800, label1, label2, 'Periodo = 800')
    axs[1][0].set_xlim(0, 100)
    axs[1][0].set_ylim(0, 0.3)
    
    Utils.graficar_sub_plot(axs[1][1], eje_frec_1600, espectro_cuadrada_1600, espectro_aperiodica_1600, label1, label2, 'Periodo = 1600')
    axs[1][1].set_xlim(0, 100)
    axs[1][1].set_ylim(0, 0.3)

    plt.show()

graficar()#python3 TP5-Punto14.py
'''PUNTO 7
Construir un algoritmo que, dada una señal modulada senoidalmente en amplitud con frecuencia
de portadora conocida, la demodule y recupere la señal moduladora. Por simpleza, considere que
todas las señales están en fase.'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import Utils
import Punto1
import Punto6

"""
# Demodular una funcion.

:param señal: señal de entrada modulada
:param fs: frecuencia de muestreo
:returns: Señal demodulada """
def demodular_señal(señal, fp, fs):
    frec_angular= 2*np.pi*fp
    eje_t = np.linspace(0, len(señal)/fs, len(señal), endpoint=None)
    #señal_demodulada = np.array(señal)*np.array([np.exp(-1j*frec_angular*t) for t in eje_t])
    señal_demodulada = np.array(señal)*np.array([(np.cos(frec_angular*t)) - 1j*np.sin(frec_angular*t) for t in eje_t])
    return señal_demodulada

def run():
    frec_muestreo, señal_wav = wavfile.read('Tonocuadrado440Hz3seg.wav');
    longitud = len(señal_wav)
    ganancia = 1
    frec_corte = 2500
    fp = 10000 # A donde queremos trasladar la señal

    filtro = Punto1.filtro_pasa_bajos(frec_corte, frec_muestreo, longitud, ganancia)
    señal_filtrada = Utils.aplicar_filtro(señal_wav, filtro)
    espectro_filtrado = Utils.obtener_espectro(señal_filtrada)

    señal_filtrada_a = señal_filtrada * 2
    espectro_filtrado_a = Utils.obtener_espectro(señal_filtrada_a)

    Utils.graficar_tiempo(señal_filtrada, frec_muestreo, 'fp = señal_filtrada ')
    Utils.graficar(espectro_filtrado, frec_muestreo, ' espectro_filtrado')
    Utils.graficar_tiempo(señal_filtrada_a, frec_muestreo, 'fp = señal_filtrada A')
    Utils.graficar(espectro_filtrado_a, frec_muestreo, ' espectro_filtrado A')

run()
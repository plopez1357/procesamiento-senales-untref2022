'''PUNTO 6
Construir un algoritmo que, dada una señal (restringirse por simpleza a señales de tipo senoidal),
la module en amplitud sobre una senoide portadora. La frecuencia de la señal portadora debe ser
parámetro de entrada; considere que su amplitud es 1.'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import Utils
import Punto1

"""
# Traslada señal a un punto wp.

:param señal: señal de entrada
:param wp: punto donde se debe trasladar
:param fs: frecuencia de muestreo
:returns: Señal modulada """
def modular_sobre_señal_portadora(señal, wp, fs):
    frec_hertz = 2*np.pi*wp
    eje_t = np.linspace(0, len(señal)/fs, len(señal), endpoint=None)
    # Para trasladar la señal en el espectro tenemos que convolucionar con una delta.
    # En tiempo multiplicamos por la transformada (e**(j*wp*t) -> cos(...) + jsen(...)).
    señal_modulada = np.array(señal)*np.array([np.exp(1j*frec_hertz*t) for t in eje_t]) # Señal portadora
    #señal_modulada = np.array(señal)*np.array([(np.cos(frec_hertz*t)) + 1j*np.sin(frec_hertz*t) for t in eje_t])
    return señal_modulada

def run():
    frec_muestreo, señal_wav = wavfile.read('Tonocuadrado440Hz3seg.wav');
    longitud = len(señal_wav)
    ganancia = 1
    frec_corte = 2500
    wp = 10000 # A donde queremos trasladar la señal

    filtro = Punto1.filtro_pasa_bajos(frec_corte, frec_muestreo, longitud, ganancia)
    señal_filtrada = Utils.aplicar_filtro(señal_wav, filtro)
    señal_modulada = modular_sobre_señal_portadora(señal_filtrada, wp, frec_muestreo)
    espectro_modulado = Utils.obtener_espectro(señal_modulada)
    espectro_filtrado = Utils.obtener_espectro(señal_filtrada)

    #Utils.graficar(espectro_filtrado, frec_muestreo, 'Señal filtrada')
    #Utils.graficar(espectro_modulado, frec_muestreo, 'wp = ' + str(wp))

run()
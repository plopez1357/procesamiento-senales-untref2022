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
from scipy.io import wavfile
import Utils

"""
#El filtro se aplica sobre el eje de la frecuencia
#Deja pasar las bajas frecuencias, todo lo que sea menor a fc tomando de 0 a fs/2

:param fc: frecuencia de corte
:param fs: frecuencia de muestreo
:param longitud: longitud de la señal
:param ganancia: amplitud del filtro en la región de aceptación
:returns: filtro pasa bajos """
def filtro_pasa_bajos(fc, fs, longitud, ganancia):
    eje_frec = np.linspace(0, fs, longitud, endpoint=None)
    filtro = np.zeros(longitud, dtype=complex)
    for i in range(len(eje_frec)):
        if(eje_frec[i] < fc or eje_frec[i] > fs-fc):
            filtro[i] = 1*ganancia
    return filtro

def run():
    frec_muestreo, señal_wav = wavfile.read('Tonocuadrado440Hz3seg.wav');
    longitud = len(señal_wav)
    ganancia = 1
    frec_corte = 2500

    filtro = filtro_pasa_bajos(frec_corte, frec_muestreo, longitud, ganancia)
    señal_filtrada = Utils.aplicar_filtro(señal_wav, filtro)
    espectro_filtrado = Utils.obtener_espectro(señal_filtrada)

    #Utils.graficar(señal_wav, frec_muestreo)
    #Utils.graficar(espectro_filtrado, frec_muestreo)

run()#python3 Punto1.py
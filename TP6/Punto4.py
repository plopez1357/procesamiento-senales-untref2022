'''PUNTO 4
Generar sendas funciones que permitan construir filtros pasabanda y rechazabanda, recibiendo
como parámetros de entrada las dos frecuencias de corte y la ganancia.'''

import numpy as np
from scipy.io import wavfile
import Utils

"""
#El filtro se aplica sobre el eje de la frecuencia.
#No permite el paso de señales cuyas frecuencias se encuentran
#comprendidas entre las frecuencias de corte superior e inferior.

:param fc1: frecuencias de corte inferior
:param fc2: frecuencias de corte superior
:param fs: frecuencia de muestreo
:param longitud: longitud de la señal
:param ganancia: amplitud del filtro en la región de aceptación
:returns: filtro rechaza bandas """
def filtro_rechaza_banda(fc1, fc2, fs, longitud, ganancia):
    eje_frec = np.linspace(0, fs, longitud, endpoint=None)
    filtro = np.zeros(longitud, dtype=complex)
    for i in range(len(eje_frec)):
        if((eje_frec[i] < fc1 or eje_frec[i] > fc2) and (eje_frec[i] < fs-fc2 or eje_frec[i] > fs-fc1)):
            filtro[i] = 1*ganancia
    return filtro

def filtro_pasa_banda(fc1, fc2, fs, longitud, ganancia):
    eje_frec = np.linspace(0, fs, longitud, endpoint=None)
    filtro = np.zeros(longitud, dtype=complex)
    for i in range(len(eje_frec)):
       if(eje_frec[i] > fc1 and eje_frec[i]<fc2) or (eje_frec[i] < fs-fc1 and eje_frec[i] > fs-fc2):
            filtro[i] = 1*ganancia
    return filtro

def run():
    fs, señal_wav = wavfile.read('Tonocuadrado440Hz3seg.wav');
    longitud = len(señal_wav)
    ganancia = 1
    frecuencia_corte_inferior = 3000
    frecuencia_corte_superior = 10000

    filtro_rb = filtro_rechaza_banda(frecuencia_corte_inferior, frecuencia_corte_superior, fs, longitud, ganancia)
    señal_filtrada_rb = Utils.aplicar_filtro(señal_wav, filtro_rb)
    espectro_filtrado_rb = Utils.obtener_espectro_filtrado(señal_filtrada_rb)

    filtro_pb = filtro_pasa_banda(frecuencia_corte_inferior, frecuencia_corte_superior, fs, longitud, ganancia)
    señal_filtrada_pb = Utils.aplicar_filtro(señal_wav, filtro_pb)
    espectro_filtrado_pb = Utils.obtener_espectro(señal_filtrada_pb)

    #Utils.graficar(señal_wav, fs)
    #Utils.graficar(espectro_filtrado_rb, fs)
    #Utils.graficar(espectro_filtrado_pb, fs)


run() #python3 Punto4.py
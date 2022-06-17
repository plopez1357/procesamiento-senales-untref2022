'''PUNTO 2
Con las mismas especificaciones que el punto anterior, generar una función que construya filtros pasaaltos.

Punto 3 -> Modificar las funciones obtenidas en los puntos anteriores para que reciban un 
parámetro adicional G, la ganancia del filtro, valor que representa la amplitud del filtro en la 
región de aceptación.'''
import numpy as np
from scipy.io import wavfile
import Utils

"""
#El filtro se aplica sobre el eje de la frecuencia
#Deja pasar las altas frecuencias, todo lo que sea mayor a fc tomando de 0 a fs/2

:param fc: frecuencia de corte
:param fs: frecuencia de muestreo
:param longitud: longitud de la señal
:param ganancia: amplitud del filtro en la región de aceptación
:returns: filtro pasa altos """
def filtro_pasa_altos(fc, fs, longitud, ganancia):
    eje_frec = np.linspace(0, fs, longitud, endpoint=None)
    filtro = np.zeros(longitud, dtype=complex)
    for i in range(len(eje_frec)):
        if(eje_frec[i] > fc and eje_frec[i] < fs-fc):
            filtro[i] = 1*ganancia
    return filtro

def run():
    fs, señal_wav = wavfile.read('Tonocuadrado440Hz3seg.wav');
    longitud = len(señal_wav)
    ganancia = 1
    frecuencia_corte = 10000

    filtro = filtro_pasa_altos(frecuencia_corte, fs, longitud, ganancia)
    señal_filtrada = Utils.aplicar_filtro(señal_wav, filtro)

    espectro_filtrado = Utils.obtener_espectro(señal_filtrada)

    #Utils.graficar(señal_wav, fs)
    #Utils.graficar(espectro_filtrado, fs)

run() #python3 Punto2.py
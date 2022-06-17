'''PUNTO 1
Generar una función que construya filtros pasabajos ideales en el dominio de la frecuencia,
entendiendo estos como funciones que valen 0 a la derecha de cierta frecuencia de corte y 1 a la
izquierda de la misma. La frecuencia de corte debe ser un parámetro de entrada.

Punto 3 -> Modificar las funciones obtenidas en los puntos anteriores para que reciban un 
parámetro adicional G, la ganancia del filtro, valor que representa la amplitud del filtro en la 
región de aceptación.'''

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
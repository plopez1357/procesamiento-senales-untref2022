'''PUNTO 7
Construir un algoritmo que, dada una señal modulada senoidalmente en amplitud con frecuencia
de portadora conocida, la demodule y recupere la señalmoduladora. Por simpleza, considere que
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
def demodular_señal(señal, fp, fs, phi):
    longitud = len(señal)
    ganancia = 2
    frec_corte = 3000

    señal_modulada_2 = modular_sobre_señal_portadora(señal, fp, fs, phi)
    filtro = Punto1.filtro_pasa_bajos(frec_corte, fs, longitud, ganancia)
    señal_filtrada = Utils.aplicar_filtro(señal_modulada_2, filtro)
    return señal_filtrada

def modular_sobre_señal_portadora(señal, wp, fs, phi):
    frec_hertz = 2*np.pi*wp
    eje_t = np.linspace(0, len(señal)/fs, len(señal), endpoint=None)
    señal_modulada = np.array(señal)*np.array([(np.cos(frec_hertz*t + phi)) for t in eje_t])
    return señal_modulada

def run():
    frec_muestreo, señal_wav = wavfile.read('Tonocuadrado440Hz3seg.wav');
    longitud = len(señal_wav)
    ganancia1 = 1/2
    ganancia2 = 1
    ganancia3 = 2
    fc1 = 1500
    fc2 = 2500
    fc3 = 3500

    fp1 = 4000
    fp2 = 10500
    fp3 = 17000

    filtro1 = Punto1.filtro_pasa_bajos(fc1, frec_muestreo, longitud, ganancia1)
    señal_filtrada1 = Utils.aplicar_filtro(señal_wav, filtro1)
    #espectro1 = Utils.obtener_espectro(señal_filtrada1)
    señal_modulada1 = modular_sobre_señal_portadora(señal_filtrada1, fp1, frec_muestreo, 0)

    filtro2 = Punto1.filtro_pasa_bajos(fc2, frec_muestreo, longitud, ganancia2)
    señal_filtrada2 = Utils.aplicar_filtro(señal_wav, filtro2)
    #espectro2 = Utils.obtener_espectro(señal_filtrada2)
    señal_modulada2 = modular_sobre_señal_portadora(señal_filtrada2, fp2, frec_muestreo, 0)

    filtro3 = Punto1.filtro_pasa_bajos(fc3, frec_muestreo, longitud, ganancia3)
    señal_filtrada3 = Utils.aplicar_filtro(señal_wav, filtro3)
    #espectro3 = Utils.obtener_espectro(señal_filtrada3)
    señal_modulada3 = modular_sobre_señal_portadora(señal_filtrada3, fp3, frec_muestreo, 0)
    

    eje_frec = np.linspace(0, frec_muestreo, len(señal_wav), endpoint=None)

    señal_multiplexada = señal_modulada1 + señal_modulada2 + señal_modulada3
    espectro_multiplexado = Utils.obtener_espectro(señal_multiplexada)

    #demultiplexar -> 3 copias de la señal multiplezada, y filtrar con 3 filtros pasa bandas y demudular cada una

    fig, axs = plt.subplots()
    axs.plot(eje_frec, espectro_multiplexado)
    axs.set_title('Espectro Filtro1')
   # axs[1].plot(eje_frec, señal_modulada2)
   # axs[1].set_title('Espectro Filtro2')
   # axs[2].plot(eje_frec, espectro2)
   # axs[2].set_title('Espectro Filtro3')
   # plt.show()

    '''
    frec_corte = 2500
    fp = 6000 # A donde queremos trasladar la señal

    phi1 = 0
    phi2 = np.pi/2

    filtro = Punto1.filtro_pasa_bajos(frec_corte, frec_muestreo, longitud, ganancia)
    señal_filtrada = Utils.aplicar_filtro(señal_wav, filtro)
    señal_modulada = modular_sobre_señal_portadora(señal_filtrada, fp, frec_muestreo, phi1)
    señal_demodulada = demodular_señal(señal_modulada, fp, frec_muestreo, phi2)
    #espectro_filtrado = Utils.obtener_espectro(señal_filtrada)
    espectro_modulado = Utils.obtener_espectro(señal_modulada)
    espectro_demodulado = Utils.obtener_espectro(señal_demodulada)

    #Utils.graficar(espectro_filtrado, frec_muestreo, 'Señal filtrada')
    #Utils.graficar_tiempo(señal_modulada, frec_muestreo, 'fp = ' + str(fp))
    Utils.graficar(espectro_modulado, frec_muestreo, 'Señal espectro_modulado')
    Utils.graficar(espectro_demodulado, frec_muestreo, 'Señal espectro_demodulado')
    #Utils.graficar_tiempo(np.imag(señal_demodulada), frec_muestreo, 'Señal imag')'''

run()
import numpy as np
import matplotlib.pyplot as plt

def obtener_espectro(señal):
    #Trasnfomamos de nuevo para tener obtener el espectro
    señal_transformada = np.fft.fft(señal, norm='forward')
    señal_modulo = np.abs(señal_transformada)
    return señal_modulo

def aplicar_filtro(señal, filtro):
    #Transaformada para aplicar el filtro en frecuencia
    señal_transformada = np.fft.fft(señal, norm='forward')
    señal_filtrada = señal_transformada*filtro

    #Antitrasnformada para obtener la función en tiempo
    return np.fft.ifft(señal_filtrada, norm='forward')

def graficar(señal, fs, titulo=''):
    eje_x = np.linspace(0, fs, len(señal), endpoint=None)

    plt.stem(eje_x, señal ,'r', use_line_collection=True)
    plt.title(titulo)
    plt.grid()
    plt.show()

def graficar_tiempo(señal, fs, titulo=''):
    eje_t = np.linspace(0, len(señal)/fs, len(señal), endpoint=None)

    plt.plot(eje_t, señal)
    plt.title(titulo)
    plt.grid()
    plt.show()
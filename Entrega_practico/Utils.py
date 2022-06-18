import numpy as np
from scipy import signal

def generar_señal_cuadrada(t, T):
    return signal.square((2 * np.pi / T) * t)

def obtener_modulo_espectro(señal):
    #Trasnfomamos de nuevo para tener obtener el espectro
    señal_transformada = np.fft.fft(señal, norm='forward')
    señal_modulo = np.abs(señal_transformada)
    return señal_modulo

def generar_senoide(t, A, frec_Hz, φ):
    return A * np.sin(2 * np.pi * frec_Hz * t + φ)
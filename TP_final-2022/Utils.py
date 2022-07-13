import numpy as np
from scipy import signal

def generar_señal_cuadrada(t, T):
    return signal.square((2 * np.pi / T) * t)

def generarSeno(t, f, A):
    return A * np.sin(2 * np.pi * f * t)
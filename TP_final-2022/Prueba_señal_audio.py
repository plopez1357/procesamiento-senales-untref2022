from matplotlib.collections import LineCollection
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import Transmisor
import Receptor

#Armado de señales de prueba
fs1, señal1 = wav.read('./audios/clarinete.wav')

fs2, señal2 = wav.read('./audios/saxo.wav')

fs3, señal3 = wav.read('./audios/trompeta.wav')

d = int(len(señal1) / fs1)
t = np.linspace(0, d, fs1 * d)

señales = [señal1, señal2, señal3]

#Grafico las 3 señales
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

ax1.stem(t, señal1, 'r', markerfmt = ' ', use_line_collection = True)
ax1.set_title('Señal Audio Clarinete')
ax1.set_ylabel('Amplitud (A)')
ax1.set_xlabel('Tiempo (t)')

ax2.stem(t, señal2, 'y', markerfmt = ' ', use_line_collection = True)
ax2.set_title('Señal Audio Saxo')
ax2.set_ylabel('Amplitud (A)')
ax2.set_xlabel('Tiempo (t)')

ax3.stem(t, señal3, 'b', markerfmt = ' ', use_line_collection = True)
ax3.set_title('Señal Audio Trompeta')
ax3.set_ylabel('Amplitud (A)')
ax3.set_xlabel('Tiempo (t)')

fig.tight_layout(pad=0.8)

plt.show()

#Transmitiendo señal
señalMultiplexada = Transmisor.multiplexarSeñal(señales)

#Grafico la señal multiplexada 
cantCanales = len(señales) #3
dTotal = d * cantCanales
tCanal = np.linspace(0, dTotal, fs1 * dTotal)

plt.figure(figsize=(12,2))
plt.stem(tCanal[0::3], señalMultiplexada[0::3], 'r', markerfmt = ' ', use_line_collection = True)
plt.stem(tCanal[1::3], señalMultiplexada[1::3], 'y', markerfmt = ' ', use_line_collection = True)
plt.stem(tCanal[2::3], señalMultiplexada[2::3], 'b', markerfmt = ' ', use_line_collection = True)
plt.title('Señal multiplexada')
plt.ylabel('Amplitud (A)')
plt.xlabel('Tiempo (t)')

plt.show()

#recibiendo  señal 
señalDemultiplexada = Receptor.demultiplexarSeñal(señalMultiplexada, cantCanales)

#Grafico las señales demultiplexadas
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

senal1_demultiplexada = señalDemultiplexada[0]
ax1.stem(t, senal1_demultiplexada, 'r', markerfmt = ' ', use_line_collection = True)
ax1.set_title('Señal 1 demultiplexada')
ax1.set_ylabel('Amplitud (A)')
ax1.set_xlabel('Tiempo (t)')

senal2_demultiplexada = señalDemultiplexada[1]
ax2.stem(t, senal2_demultiplexada, 'y', markerfmt = ' ', use_line_collection = True)
ax2.set_title('Señal 2 demultiplexada')
ax2.set_ylabel('Amplitud (A)')
ax2.set_xlabel('Tiempo (t)')

senal3_demultiplexada = señalDemultiplexada[2]
ax3.stem(t, senal3_demultiplexada, 'b', markerfmt = ' ', use_line_collection = True)
ax3.set_title('Señal 3 demultiplexada')
ax3.set_ylabel('Amplitud (A)')
ax3.set_xlabel('Tiempo (t)')

fig.tight_layout(pad=0.8)

plt.show()
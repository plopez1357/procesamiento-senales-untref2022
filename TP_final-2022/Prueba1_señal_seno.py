import numpy as np
import matplotlib.pyplot as plt
import Utils
import Transmisor
import Receptor

############### Genéro las señales de prueba ################
# Senal 1 ====> f = 400hz, A = 1, duración = 1
# Senal 2 ====> f = 600hz, A = 1, duración = 1
# Senal 2 ====> f = 1khz, A = 1, duración = 1
#############################################################
fs = 100
A = 1
d = 1

t = np.linspace(0, d, fs * d)

f1 = 200
señal1 = Utils.generarSeno(t, f1, A)

f2 = 300
señal2 = Utils.generarSeno(t, f2, A)

f3 = 500
señal3 = Utils.generarSeno(t, f3, A)

señales = [señal1, señal2, señal3]
############## Fin generación señales de prueba #############

############## Grafico las 3 señales originales #############
#############################################################
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

ax1.stem(t, señal1, 'r')
ax1.set_title('Señal original 1')
ax1.set_ylabel('Amplitud (A)')
ax1.set_xlabel('Tiempo (t)')

ax2.stem(t, señal2, 'y')
ax2.set_title('Señal original 2')
ax2.set_ylabel('Amplitud (A)')
ax2.set_xlabel('Tiempo (t)')

ax3.stem(t, señal3, 'b')
ax3.set_title('Señal original 3')
ax3.set_ylabel('Amplitud (A)')
ax3.set_xlabel('Tiempo (t)')

fig.tight_layout(pad=0.8)
plt.show()
########### Fin gráfico de las señales originales ###########

################### Simulación TRANSMISOR #######################
#############################################################
señalMultiplexada = Transmisor.multiplexarSeñal(señales)
################## Fin simulación TRANSMISOR ####################

########### Grafico la señal multiplexada por TDM ###########
#############################################################

cantCanales = len(señales) #3
dTotal = d * cantCanales
tCanal = np.linspace(0, dTotal, fs * dTotal)

plt.figure(figsize=(10,2))
plt.stem(tCanal[0::3], señalMultiplexada[0::3], 'r')
plt.stem(tCanal[1::3], señalMultiplexada[1::3], 'y')
plt.stem(tCanal[2::3], señalMultiplexada[2::3], 'b')
plt.title(f'Señal multiplexada TDM - Duración: {dTotal} segs')
plt.ylabel('Amplitud (A)')
plt.xlabel('Tiempo (t)')

plt.show()
########## Fin gráfico señal multiplexada por TDM ###########

#################### Simulación RECEPTOR ####################
#############################################################
señalDemultiplexada = Receptor.demultiplexarSeñal(señalMultiplexada, cantCanales)
################## Fin simulación RECEPTOR ##################

############# Grafico las señales recuperadas ###############
#############################################################
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

senal1_recuperada = señalDemultiplexada[0]
ax1.stem(t, senal1_recuperada, 'r')
ax1.set_title('Señal 1 recuperada')
ax1.set_ylabel('Amplitud (A)')
ax1.set_xlabel('Tiempo (t)')

senal2_recuperada = señalDemultiplexada[1]
ax2.stem(t, senal2_recuperada, 'y')
ax2.set_title('Señal 2 recuperada')
ax2.set_ylabel('Amplitud (A)')
ax2.set_xlabel('Tiempo (t)')

senal3_recuperada = señalDemultiplexada[2]
ax3.stem(t, senal3_recuperada, 'b')
ax3.set_title('Señal 3 recuperada')
ax3.set_ylabel('Amplitud (A)')
ax3.set_xlabel('Tiempo (t)')

fig.tight_layout(pad=0.8)
############ Fin grafico señales recuperadas ################

plt.show()
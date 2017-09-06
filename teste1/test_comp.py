import matplotlib.pyplot as plt
import numpy as np


##########################
#### Ex1: Amostragem #####
##########################

ra = 169574

#Soma os 3 ultimos digitos do RA com 15Hz
f = 15 + sum(map(int, str(ra%1000)))
#Freq de amostragem
fs1 = float(300)

#Array de amostras normalizadas
x1 = (np.arange(fs1))/fs1

#Gera os pontos da onda cos(2*pi*f*t)
y1 = [ np.cos(2*np.pi*f * i) for i in x1]

yt = [ np.cos(2*np.pi*(fs1-f) * i) for i in x1]
# showing the exact location of the smaples
plt.figure()
plt.stem(x1,y1, linefmt='b-', markerfmt='b.', basefmt='b-')
plt.plot(x1,y1)
plt.xlabel("Tempo [s]")
plt.title("$x_1(t) = cos(2\pi"+str(f)+"\cdot t)$ com Fs = "+str(fs1)+" Hz")

fs2 = float(300+200) # sample rate

x2 = (np.arange(fs2))/fs2 # the points on the x axis for plotting

# compute the value (amplitude) of the sin wave at the for each sample
y2 = [ np.cos(2*np.pi*f * i) for i in x2]
# showing the exact location of the smaples
plt.figure()
plt.stem(x2,y2, linefmt='b-', markerfmt='b.', basefmt='b-')
plt.plot(x2,y2)
plt.xlabel("Tempo [s]")
plt.title("$x_2(t) = cos(2\pi"+str(f)+"\cdot t)$ com Fs = "+str(fs2)+" Hz")

x4 = x2
y4 = [ np.cos(2*np.pi*60 * i) for i in x4]

x3 = x4
y3 = np.add(y2, y4)
plt.figure()
plt.stem(x3,y3, linefmt='b-', markerfmt='b.', basefmt='b-')
plt.plot(x3,y3)
plt.xlabel("Tempo [s]")
plt.title("$x_3(t) = ( cos(2\pi"+str(f)+"\cdot t) + cos(2\pi60\cdot t) )$ com Fs = "+str(fs2)+" Hz")

########################
#### Ex2: Espectro #####
########################

#FFT do modulo de x1(t)
X1 = np.abs(np.fft.fft(y1))
#Descarta metade simetrica da FFT
#X1 = X1[0:int(np.ceil(X1.size/2))]
#Plota grafico
plt.figure()
plt.plot(X1)
plt.xlabel("Frequencia [Hz]")
plt.title("FFT de $x_1(t) = cos(2\pi"+str(f)+"\cdot t)$ com Fs = "+str(fs1)+" Hz")

#FFT do modulo de x2(t)
X2 = np.abs(np.fft.fft(y2))
#Descarta metade simetrica da FFT
#X2 = X2[0:int(np.ceil(X2.size/2))]
#Plota grafico
plt.figure()
plt.plot(X2)
plt.xlabel("Frequencia [Hz]")
plt.title("FFT de $x_2(t) = cos(2\pi"+str(f)+"\cdot t)$ com Fs = "+str(fs2)+" Hz")

#FFT do modulo de x3(t)
X3 = np.abs(np.fft.fft(y3))
#Descarta metade simetrica da FFT
#X3 = X3[0:int(np.ceil(X3.size/2))]
#Plota grafico
plt.figure()
plt.plot(X3)
plt.xlabel("Frequencia [Hz]")
plt.title("FFT de $x_3(t) = ( cos(2\pi"+str(f)+"\cdot t) + cos(2\pi60\cdot t) )$ com Fs = "+str(fs2)+" Hz")

plt.show()

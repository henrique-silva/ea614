import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

fs = 12
t = np.linspace(0, 1, fs, endpoint=False)
x = signal.sawtooth(2 * np.pi * t)

#Impulso deslocado em 0.25s com 8 amostras
h = signal.unit_impulse(len(t), int(0.25*fs))
h8 = h[:8]

plt.figure()
plt.stem(t, x, linefmt='b-', markerfmt='bo')
#plt.stem(t[:8], h, linefmt='r-', markerfmt='ro')

#Convolucao da onda dente-de-serra com o impulso deslocado
y = np.convolve(x, h8)

plt.figure()
plt.stem(y)

X_fft = np.fft.fft(x)
X_fft_mod = np.abs(X_fft)
H_fft = np.fft.fft(h)
H_fft_mod = np.abs(H_fft)
H8_fft = np.fft.fft(h8)
H8_fft_mod = np.abs(H8_fft)

plt.figure()
plt.plot(X_fft_mod[0:int(np.ceil(X_fft_mod.size/2))])
plt.plot(H8_fft_mod[0:int(np.ceil(H8_fft_mod.size/2))])

Y = np.multiply(X_fft,H_fft)
plt.figure()
plt.title("Y = X*H")
plt.plot(Y[0:int(np.ceil(Y.size/2))])

y_inv = np.fft.ifft(Y)
plt.figure()
plt.plot(y_inv)
plt.plot(y)

x_pad = np.pad(x,(0,(len(y)-len(x))), 'constant', constant_values=(0))
h_pad = np.pad(x,(0,(len(y)-len(h))), 'constant', constant_values=(0))

X_pad = np.fft.fft(x_pad)
H_pad = np.fft.fft(h_pad)

Y_pad = np.multiply(X_pad,H_pad)
y_pad_inv = np.fft.ifft(Y_pad)

plt.figure()
#plt.plot(Y_pad[0:int(np.ceil(Y_pad.size/2))])
#plt.plot(Y[0:int(np.ceil(Y.size/2))])
plt.plot(y)
plt.plot(y_inv)
plt.plot(y_pad_inv)

plt.show()

import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np

ra = 169574

f = 15+ sum(map(int, str(ra%1000)))# the frequency of the signal
fs = float(300) # sample rate

x1 = np.arange(fs) # the points on the x axis for plotting
x1 = x1/fs
x1 = x1[0:(int(fs/f)+1)]

# compute the value (amplitude) of the sin wave at the for each sample
y1 = [ np.cos(2*np.pi*f * (i/fs)) for i in np.arange(fs)]
y1 = y1[0:(int(fs/f)+1)]

f1 = np.fft.fft(y1)
# showing the exact location of the smaples
plt.figure()
plt.stem(x1,y1, linefmt='b-', markerfmt='b.', basefmt='b-')
plt.plot(x1,y1)
plt.xlabel("Tempo [s]")
plt.title("$x_1(t) = cos(2\pi"+str(f)+"\cdot t)$ com Fs = "+str(fs)+" Hz")


fs = float(300+200) # sample rate

x2 = np.arange(fs) # the points on the x axis for plotting
x2 = x2/fs

# compute the value (amplitude) of the sin wave at the for each sample
y2 = [ np.cos(2*np.pi*f * (i/fs)) for i in np.arange(fs)]
# showing the exact location of the smaples
plt.figure()
plt.stem(x2,y2, linefmt='b-', markerfmt='b.', basefmt='b-')
plt.plot(x2,y2)
plt.xlabel("Tempo [s]")
plt.title("$x_2(t) = cos(2\pi"+str(f)+"\cdot t)$ com Fs = "+str(fs)+" Hz")

x4 = x2
y4 = [ np.cos(2*np.pi*60 * (i/fs)) for i in np.arange(fs)]

x3 = x4
y3 = np.add(y2, y4)
plt.figure()
plt.stem(x3,y3, linefmt='b-', markerfmt='b.', basefmt='b-')
plt.plot(x3,y3)
plt.xlabel("Tempo [s]")
plt.title("$x_3(t) = ( cos(2\pi"+str(f)+"\cdot t) + cos(2\pi60\cdot t) )$ com Fs = "+str(fs)+" Hz")
plt.show()

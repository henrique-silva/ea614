import matplotlib.pyplot as plt
import numpy as np

Fs = float(1000)
f = 1
x = (np.arange(Fs))/Fs
x_p = (np.arange(Fs*4))/Fs


sig_M = [ np.sin(2*np.pi*f * i) for i in x]
sig_O = [ np.sin(2*np.pi*(f*2) * i) for i in x]
sig_A = [ np.cos(2*np.pi*f * i) for i in x]
sig_L = [ np.cos(2*np.pi*(f*2) * i) for i in x]

codigos = {'M':sig_M, 'O':sig_O, 'A':sig_A, 'L':sig_L}

def codifica( palavra ):
    buf = []
    for letra in palavra:
        if letra in codigos:
            buf = np.concatenate((buf,codigos[letra]))
        else:
            print('[ERRO]: A letra '+letra+' nao faz parte do codigo!')
            return
    return buf


t1 = codifica('LOMA')
t2 = codifica('AMOL')
t3 = codifica('MOLA')

plt.figure()
plt.plot(t1)
plt.figure()
plt.plot(t2)
plt.figure()
plt.plot(t3)
plt.show()

t4 = codifica('FOLA')

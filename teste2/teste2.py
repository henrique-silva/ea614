import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import itertools


Fs = float(1000)
f = 10
x = (np.arange(Fs))/Fs
x_p = (np.arange(Fs*4))/Fs

#Gera os sinais de todas as letras
sig_M = [ np.sin(2*np.pi*f * i) for i in x]
sig_O = [ np.sin(2*np.pi*(f*2) * i) for i in x]
sig_A = [ np.cos(2*np.pi*f * i) for i in x]
sig_L = [ np.cos(2*np.pi*(f*2) * i) for i in x]

#Cria dicionario com a letras e seus respectivos codigos
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


#Deteccao de pico: https://dsp.stackexchange.com/questions/22923/dominating-frequency-in-a-clear-50-hz-signal
def decodifica_fft( buf ):
    palavra = []
    split_buf = np.reshape(buf, (4, len(buf)/4))
    for letra in split_buf:
        fft_letra = np.fft.fft(letra)
        freqs = np.fft.fftfreq(len(letra),(1/Fs))
        freqs = freqs[np.where(freqs >= 0)]
        mag = np.abs(fft_letra[np.where(freqs >= 0)])
        peak = np.argmax(mag)
        print('Pico: '+str(peak)+' Hz')
        if peak == f:
            palavra.append('M')
        elif peak == (2*f):
            palavra.append('O')
        else:
            print('[ERRO] Frequencia nao indexada: '+str(peak)+' Hz')
    return ''.join(palavra)

def decodifica( buf ):
    palavra = []
    match = 0
    split_buf = np.reshape(buf, (4, len(buf)/4))
    for chunk in split_buf:
        for key in codigos:
            result = np.subtract(chunk, codigos[key])
            #print(np.std(result))
            if (np.std(result) < 0.7):
                palavra.append(key)
                match = 1
        if match == 0:
            palavra.append("_")
    return ''.join(palavra)

#Ruido Branco
noise = np.random.normal(0, 1, size=4000)/1.44

#Cria todas a permutacoes possiveis dos simbolos
permut = list(itertools.permutations(list('LOMA')))
permut = [ ''.join(palavra) for palavra in permut]

#Codifica todas as palavras
permut_cod = [ codifica(palavra) for palavra in permut ]

#Adiciona ruido
permut_noise = [ np.add(sinal, noise) for sinal in permut_cod ]


for sig in permut_cod:
    print('Palavra decodificada: '+decodifica(sig))

for sig in permut_noise:
    print('Palavra decodificada (n): '+decodifica(sig))

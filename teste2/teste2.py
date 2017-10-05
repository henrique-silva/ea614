#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import numpy as np
import itertools

#Parseador de argumentos
parser = argparse.ArgumentParser()
parser.add_argument('-s','--sampling', required=False, type=float, default=1000.0, help='Sampling frequency')
parser.add_argument('-f','--frequency', required=False, type=float, default=10.0, help='Base signal frequency')
parser.add_argument('-n','--noise_std', required=False, type=float, default=0.0, help='White noise standard deviation')
parser.add_argument('-p','--plot', required=False, action='store_true', help='Plot coded word graphs')
parser.add_argument('palavras', nargs='+', type=str, help='Words to encode/decode')

args = parser.parse_args()

#Periodo de 1 ciclo
x = np.linspace(0, 1/args.frequency, args.sampling)

#Gera os sinais de todas as letras
sig_M = [ np.sin(2*np.pi*args.frequency * i) for i in x]
sig_O = [ np.sin(2*np.pi*(args.frequency*2) * i) for i in x]
sig_A = [ np.cos(2*np.pi*args.frequency * i) for i in x]
sig_L = [ np.cos(2*np.pi*(args.frequency*2) * i) for i in x]

#Cria dicionario com a letras e seus respectivos codigos
codigos = {'M':sig_M, 'O':sig_O, 'A':sig_A, 'L':sig_L}

def codifica( palavra ):
    buf = []
    for letra in palavra:
        if letra in codigos:
            buf = np.concatenate((buf,np.add(codigos[letra], np.random.normal(0, args.noise_std, size=len(x)))))
        else:
            print('[ERRO]: A letra '+letra+' nao faz parte do codigo!')
            return
    return buf

def decodifica( buf ):
    palavra = []
    split_buf = np.reshape(buf, (4, len(buf)/4))
    for chunk in split_buf:
        match = 0
        for key in codigos:
            result = np.subtract(chunk, codigos[key])
            #print(np.std(result))
            if (np.std(result) < 0.7):
                palavra.append(key)
                match = 1
        if match == 0:
            palavra.append("_")
    return ''.join(palavra)

def SNR( sinal ):
    #Gera Ruido Branco de referencia
    ruido = np.random.normal(0, args.noise_std, size=len(sinal))
    #Calcula a potencia do pico da FFT
    Psinal = np.amax(20*np.log10(np.abs(np.fft.rfft(sinal))))
    #Calcula a potencia do ruido
    Pruido = np.mean(20*np.log10(np.abs(np.fft.rfft(ruido))))
    return Psinal-Pruido


############## Teste de Permutacoes #####################
###Cria todas a permutacoes possiveis dos simbolos
##permut = list(itertools.permutations(codigos.keys()))
##permut = [ ''.join(palavra) for palavra in permut]
##args.palavras.extend(permut)


for item in args.palavras:
    item_cod = codifica(item)
    result_decod = decodifica(item_cod)
    print('Palavra decodificada: '+result_decod),
    print('SNR: {} dB'.format(SNR(item_cod)))
    if args.plot:
        plt.figure()
        plt.plot(item_cod)
        plt.title('Palavra \"'+item+'\" codificada (adicionado ruido com std:'+str(args.noise_std)+')')

plt.show()

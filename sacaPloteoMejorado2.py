from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import os
import re

with open ('gestualidad.xml', 'r') as f:
     data = f.read()

bs_data = BeautifulSoup(data, 'xml')

def extraeDatos (etiqueta):
    respuestas = []
    print (etiqueta)
    datos = bs_data.find_all(etiqueta)
    for dato in datos:
        valor = str(dato)
        print (valor)
        #limpio = valor.strip(f'<{etiqueta}>').strip(f'</{etiqueta}>')
        if valor == f'<{etiqueta}>1</{etiqueta}>':
            respuestas.append(1)
        elif valor == f'<{etiqueta}>2</{etiqueta}>':
            respuestas.append(2)
        elif valor == f'<{etiqueta}>3</{etiqueta}>':
            respuestas.append(3)
        elif valor == f'<{etiqueta}>4</{etiqueta}>':
            respuestas.append(4)        # elif valor == '5':
        elif valor == f'<{etiqueta}>5</{etiqueta}>':
            respuestas.append(5)
        # elif valor == f'<{etiqueta}>""</{etiqueta}>':
        #     respuestas.append(0)
        # else:
        #     pass
    print (respuestas)
    print ('+++++++++++++++++++++++++++++++')
    return respuestas

etiquetasPretest = ['QID94_45', 'QID97_1', 'QID95_1', 'QID98_1', 'QID99_1', 'QID100_1',
'QID101_1', 'QID102_1','QID103_1','QID104_1','QID105_1','QID106_1','QID107_15',
'QID108_1','QID109_1']

for etiqueta in etiquetasPretest:
    respuestas = extraeDatos (etiqueta)
    plt.title(f'Frecuencia de respuestas a la {etiqueta}')
    #plt.style.use('fivethirtyeight')
    plt.hist(respuestas)
    plt.xlabel('valores del 1 al 5')
    plt.ylabel('total respondents')
    #plt.tight_layout()
    plt.show()

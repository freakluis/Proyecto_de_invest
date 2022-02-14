###Este programa es capaz de reconocer a qué condición fueron expuestos
###los candidatos y puede graficar las respuestas según la condición


from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import os
import re
import pandas

textoPreguntas = pandas.read_csv('textoPreguntas.csv')
ID = textoPreguntas['ID']
texto = textoPreguntas ['texto']

with open ('gestualidadPiloto.xml', 'r') as f:
     data = f.read()

bs_data = BeautifulSoup(data, 'xml')

###Este trozo de código descubre qué participantes fuerone expuestos a qué
###condición y los guarda en una lista según corresponda
umstaende = bs_data.find_all('QID202')

def tellsConditionsAppart():
    condicionG = []
    condicionSG = []

    etiqueta = 'QID202'

    for indice, dato in enumerate(umstaende):
        valor = str(dato)
        if valor == f'<{etiqueta}>Aus Dortmund.</{etiqueta}>':
            condicionSG.append(indice)
        else:
            condicionG.append(indice)
    # print ('Participantes en condicion G:', condicionG)
    # print ('Participantes en condicion SG:', condicionSG)
    return condicionG, condicionSG

condicionG, condicionSG = tellsConditionsAppart()

print (condicionG)
print (condicionSG)

combinada = condicionG + condicionSG
combinada.sort()

print (combinada)
###Este trozo de código recorre el xml en busca de respuestas

def extraeDatos (etiqueta, condicion):
    respuestas = []
    print (etiqueta)
    datos = bs_data.find_all(etiqueta)
    for indice, dato in enumerate(datos):
        if indice in condicion:
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

etiquetasPosttest = ['QID187_45', 'QID188_1', 'QID189_1', 'QID190_1', 'QID191_1',
'QID192_1', 'QID193_1', 'QID194_1', 'QID195_1', 'QID196_1', 'QID197_1', 'QID198_1',
'QID199_15', 'QID200_1', 'QID201_1']

###Este trozo de es el programa en sí. Aquí se eligen dos parámetros. Por un lado
###se puede elegir si se procesa el pre-test o el pos-test. Además aquí es donde
###se elige si se utiliza una u otra condición. Finalmente se grafican los resultados
###obtenidos
###https://www.geeksforgeeks.org/how-to-plot-two-histograms-together-in-matplotlib/

for i, etiqueta in enumerate(etiquetasPosttest):
    posTest = extraeDatos (etiqueta, combinada)
    preTest = extraeDatos (etiquetasPretest[i], combinada)
    # respuestas = extraeDatos (etiqueta, condicionSG)
    # ripostas = extraeDatos (etiqueta, condicionG)
    plt.title(f'Respuestas a "{texto[i]}" en pre-test y en post-test')
    #plt.style.use('fivethirtyeight')
    plt.hist(posTest, label='series1', alpha=.8, edgecolor='red')
    plt.hist(preTest, label='series2', alpha=0.7, edgecolor='yellow')
    # plt.hist(respuestas)
    # plt.hist(respuestas)
    plt.xlabel('En escala de Likert del 1 al 5 (pre-test en naranja, post-test en azul)' )
    plt.ylabel('Respuestas totales')
    #plt.tight_layout()
    plt.show()

###Esta variante del programa grafica los resultados según condición y sirve
###para sumar de forma manual los resultados para graficar y ver diferencias

###Este programa es capaz de reconocer a qué condición fueron expuestos
###los candidatos y puede graficar las respuestas según la condición
###Se mejoró la línea 44 para que pueda diferenciar mejor la condición a la que fueron expuestos los candidatos

from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import os
import re
import pandas

textoPreguntas = pandas.read_csv('textoPreguntas.csv')
ID = textoPreguntas['ID']
text = textoPreguntas ['texto']
texto = []
texto1 = text[3]
texto2 = text[10]
texto3 = text[12]

texto.append(texto1)
texto.append(texto2)
texto.append(texto3)


with open ('Gestualidad+didáctica+en+la+enseñanza+de+los+verbos+separables+en+la+clase+de+ALE+Condición+SG_December+16,+2021SinCandidatosQueNoVieronVideo.xml', 'r') as f:
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
        elif valor == f'<{etiqueta}>Aus Berlin.</{etiqueta}>':
            condicionSG.append(indice)
        elif valor == f'<{etiqueta}>Aus Hamburg.</{etiqueta}>':
            condicionSG.append(indice)
        else:
            condicionG.append(indice)
    # print ('Participantes en condicion G:', condicionG)
    # print ('Participantes en condicion SG:', condicionSG)
    return condicionG, condicionSG

condicionG, condicionSG = tellsConditionsAppart()

print ('CondicionG: ', len(condicionG))
print ('CondicionSG: ', len(condicionSG))

combinada = condicionG + condicionSG
combinada.sort()

print ('Combinada: ', combinada)
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

# etiquetasPretest = ['QID94_45', 'QID97_1', 'QID95_1', 'QID98_1', 'QID99_1', 'QID100_1',
# 'QID101_1', 'QID102_1','QID103_1','QID104_1','QID105_1','QID106_1','QID107_15',
# 'QID108_1','QID109_1']

etiquetasPretestDeInteres = ['QID98_1','QID105_1','QID107_15']

# etiquetasPosttest = ['QID187_45', 'QID188_1', 'QID189_1', 'QID190_1', 'QID191_1',
# 'QID192_1', 'QID193_1', 'QID194_1', 'QID195_1', 'QID196_1', 'QID197_1', 'QID198_1',
# 'QID199_15', 'QID200_1', 'QID201_1']

etiquetasPosttestDeInteres = ['QID190_1','QID197_1','QID199_15']

###Este trozo de es el programa en sí. Aquí se eligen dos parámetros. Por un lado
###se puede elegir si se procesa el pre-test o el pos-test. Además aquí es donde
###se elige si se utiliza una u otra condición. Finalmente se grafican los resultados
###obtenidos
###https://www.geeksforgeeks.org/how-to-plot-two-histograms-together-in-matplotlib/

for i, etiqueta in enumerate(etiquetasPosttestDeInteres):
    posTest = extraeDatos (etiqueta, condicionG)
    preTest = extraeDatos (etiquetasPretestDeInteres[i], condicionG)
    # respuestas = extraeDatos (etiqueta, condicionSG)
    # ripostas = extraeDatos (etiqueta, condicionG)
    plt.title(f'Respuestas a "{texto[i]}" en pre-test y en post-test')
    #plt.style.use('fivethirtyeight')
    plt.hist(posTest, label='series1', alpha=.8, edgecolor='red')
    plt.hist(preTest, label='series2', alpha=0.7, edgecolor='blue')
    # plt.hist(respuestas)
    # plt.hist(respuestas)
    plt.xlabel('En escala de Likert del 1 al 5 (pre-test en naranja, post-test en azul)' )
    plt.ylabel('Respuestas totales')
    #plt.tight_layout()
    # plt.show()

###Para graficar las sumas manuales por condición

postTestG = [5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 3, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5]
pretestG = [1, 3, 4, 5, 5, 4, 4, 5, 1, 5, 2, 3, 5, 2, 4, 5, 1, 1, 4, 5, 4, 3, 5, 4, 1, 5, 5, 2, 5, 2, 4, 3, 5, 2, 1, 5, 4, 5, 2]
postTestSG = [5, 5, 5, 5, 2, 4, 4, 4, 5, 1, 5, 5, 5, 4, 5, 5, 3, 4, 3, 5, 1, 5, 2, 5, 2, 5, 1, 2, 3, 2, 1, 2, 2]
pretestSG = [3, 5, 1, 4, 1, 3, 3, 4, 3, 1, 2, 5, 3, 3, 3, 4, 5, 4, 4, 2, 3, 2, 4, 5, 1, 3, 1, 3, 3, 3, 3, 2, 2]







plt.title(f'Respuestas a los reactivos de interés en pre-test y en post-test condicionSG')
plt.bar(pretestSG, label='series1', edgecolor='red', color = "gray")
plt.bar(postTestSG, label='series2', edgecolor='yellow', color = "red")
plt.xlabel('En escala de Likert del 1 al 5 (pretest en gris, postTest en rojo)' )
plt.ylabel('Respuestas totales')
plt.show()

plt.title(f'Respuestas a los reactivos de interés en pre-test y en post-test condicionG')
plt.bar(pretestG, label='series3', alpha=.8, edgecolor='red', color = "skyblue")
plt.bar(postTestG, label='series4', alpha=0.7, edgecolor='yellow', color = "magenta")
plt.xlabel('En escala de Likert del 1 al 5 (pretest en azul cielo, postTest en magenta)' )
plt.ylabel('Respuestas totales')
plt.show()

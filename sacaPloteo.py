from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import os
import re
#Fuentes:
#https://www.studytonight.com/python-howtos/how-to-read-xml-file-in-python
#https://linuxhint.com/parse_xml_python_beautifulsoup/
#https://www.kite.com/python/examples/3471/xml-get-the-child-elements-of-an-xml-element



################PARTE 1#################
#Lee los datos del archivo xml y los pasa a una variable con el nombre de data
#además extrae los IDs y el contenido de los tweets

with open ('gestualidad.xml', 'r') as f:
     data = f.read()
# Pasa los datos guardados a un parser de beautifulsoup
bs_data = BeautifulSoup(data, 'xml')
# pasa los IDs de los tweets a una variable
# identificadores = bs_data.find_all('tweetid')
# nombres = extraeDatos ('QID1', 'heiße')

# datos = bs_data.find_all('QID1')
# print (datos)



def extraeDatos (etiqueta):
    respuestas = []
    # suma_unos = 0
    # suma_dos = 0
    # suma_tres = 0
    # suma_cuatro = 0
    # suma_cinco = 0
    # unos = []
    # dos = []
    # tres = []
    # cuatro = []
    # cinco = []
    print (etiqueta)
    datos = bs_data.find_all(etiqueta)
    # print (datos)
    for dato in datos:
        valor = str(dato)
        limpio = valor.strip(f'<{etiqueta}>').strip(f'</{etiqueta}>')
        if limpio == '1':
            respuestas.append(1)
            #suma_unos = suma_unos+1
        elif limpio == '2':
            respuestas.append(2)
            #suma_dos=suma_dos+1
        elif limpio == '3':
            respuestas.append(3)
            #suma_tres=suma_tres+1
        elif limpio == '4':
            respuestas.append(4)
            #suma_cuatro=suma_cuatro+1
        elif limpio == '5':
            respuestas.append(5)
            #suma_cinco=suma_cinco+1
        elif limpio == '':
            pass
        else:
            pass

        # print (limpio)
    # print (suma_unos)
    # # histograma.append([suma_unos])
    # print(suma_dos)
    # print(suma_tres)
    # print(suma_cuatro)
    # print(suma_cinco)
    print ('+++++++++++++++++++++++++++++++')

    return respuestas

preguntas = ['QID94_45', 'QID97_1', 'QID95_1', 'QID98_1', 'QID99_1', 'QID100_1',
'QID101_1', 'QID102_1', 'QID102_1','QID104_1','QID105_1','QID106_1','QID107_1',
'QID108_1','QID109_1']

for pregunta in preguntas:
    respuestas = extraeDatos (pregunta)
    # respuestas = []
    # for element in histograma:
    #     for i in range (0,element[1]):
    #         respuestas.append(element[0])


    # respuestas = [1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 5, 5, 5]

    # print (respuestas)

    # frecuencias = []
    # etiquetas = []
    #
    # for element in histograma:
    #     etiquetas.append(element[0])
    #     frecuencias.append(element[1])


    # valoresC = [1,3,2]
    # valoresD = [6,1,2]
    # axs[0].hist(x, bins=n_bins)
    # axs[1].hist(y, bins=n_bins)
    plt.title(f'Frecuencia de respuestas a la {pregunta}')
    plt.style.use('fivethirtyeight')

    plt.hist(respuestas, bins=5)
    #plt.plot(etiquetas, frecuencias, 'b-', marker='o')
    #plt.hist (frecuencias, density = True, bins=5)
    # plt.plot(x, y, 'b-', marker='x')
    #plt.plot(histograma)
    # plt.plot(valoresC, precisionTest, 'b-.', marker='x', label='precision on test')
    # plt.plot(valoresC, recallTest, 'g-', marker='^', label='recall on test')
    # plt.plot(valoresC, f1_scoreTest, 'y-', marker='2', label='micro F1 on test')
    # plt.legend(loc=3)
    # plt.title(f'Desempeño por SVM en IMDB por {tipo}')
    plt.xlabel('valores del 1 al 5')
    plt.ylabel('total respondents')

    plt.tight_layout()
    plt.show()

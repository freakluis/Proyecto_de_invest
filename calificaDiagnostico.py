from bs4 import BeautifulSoup
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


# datos = bs_data.find_all('QID1')
# print (datos)

def extraeDatos (etiqueta, expected_value):
    datos = bs_data.find_all(etiqueta)
    # print (datos)
    for dato in datos:
        valor = str(dato)
        limpio = valor.strip(f'<{etiqueta}>').strip(f'</{etiqueta}>')
        if limpio == expected_value:
            print (1)
        else:
            print (0)

#nombres = extraeDatos ('QID1', 'heiße')
preguntas_y_respuestas = [('QID1', 'heiße'), ('QID5', 'Wie geht es dir?'),
('QID7', 'Wann'), ('QID20', 'hatten'), ('QID9', 'sind'), ('QID11', 'keine'),
('QID13', 'einen'), ('QID15', 'Möchtest'), ('QID19', 'mich'),
('QID23', 'rufe dich am Nachmittag an'), ('QID184', 'stehe immer früh auf'),
('QID185', 'findet um 19 Uhr statt')]

for indice, element in enumerate(preguntas_y_respuestas):
    nombres = extraeDatos (element[0], element[1])
    print (element[1])
    print ('+++++++++++++++++++++++++++++++++++++')



    # for item in respuestas:
    #     hijos = list(item.children)
    #     # valor = str(hijos[1][1])
    #     print (hijos)
    #     print ('\n', '\n', '++++++++++++++++++++++++++++++++++++++++++++++++++++')

# nombres = bs_data.find_all('QID35_TEXT')
# respuestas = bs_data.find_all('Response')
#
# for nombre in nombres:
#     valor = str(nombre)
#     limpio = valor.strip('<QID35_TEXT>').strip('</QID35_TEXT>')
#     # print (limpio)
# for item in respuestas:
#     hijos = list(item.children)
#     # valor = str(hijos[1][1])
#     print (hijos)
#     print ('\n', '\n', '++++++++++++++++++++++++++++++++++++++++++++++++++++')

#Pasa el contenido de los tweets a una variable
# texto = bs_data.find_all('content')
#polaridad = bs_data.find_all('polarity')
# listaValores = []
#############PARTE 2####################
#Recupera las polaridades principales de cada uno de los tweets (hay polaridades secundarias según el punto de vista),
#hace un conteo de tweets de acuerdo a su polaridad y obtiene un número de índice que luego será útil para guardar los
#tweets de acuerdo a su polaridad

# sumaPos = 0
# sumaNeg = 0
# sumaNeu = 0
# sumaNone = 0
# sobrantes = []
# #Los textos se clasificarán en sus respectivos fólders de acuerdo a la siguiente lista
# master = []
#
# for indice, item in enumerate(bs_data.find_all('sentiments')):
#
#     #print ('----------', indice, '----------')
#     hijos = list(item.children)
#     valor = str(list(hijos[1])[1])
#     limpio = valor.strip('<value>').strip('</value>')
#     master.append(limpio)
#
#     if limpio == 'P':
#         sumaPos = sumaPos + 1
#     elif limpio == 'N':
#         sumaNeg = sumaNeg + 1
#     elif limpio == 'NEU':
#         sumaNeu = sumaNeu + 1
#     elif limpio == 'NONE':
#         sumaNone = sumaNone + 1
#     else:
#         sobrantes.append(limpio)
#
# print ('Positivos: ', sumaPos)
# print ('Negativos: ', sumaNeg)
# print ('Neutros: ', sumaNeu)
# print ('None: ', sumaNone)
# print ('Sobrantes: ', len(sobrantes))
#
# print ('SumaTotal = ', sumaPos + sumaNeg + sumaNeu + sumaNone + len(sobrantes))
#
# # for indice, elementx in enumerate(master, start=1):
# #     print (indice, elementx)
#     # listaValores.append(limpio)
#     #print ('----------', indice, '----------', '\n', limpio)
#
#
# #############PARTE 3####################
# #Limpia los textos de los tweets de hashtags, websites y menciones.
# #Luego crea un sistema de directorios que constituirán el corpus del trabajo
# #Finalmente guarda los textos en donde corresponden según su polaridad
#
#
# #os.mkdir('neu')
# #
# etiquetas = []
# for indice, element in enumerate(identificadores, start=1):
#     etiquetas.append(str(element))
#
# ###Sirve para colocar los textos dentro de los archivos
# textos = []
# finales = []
#
# for klebrig in texto:
#     textos.append(str(klebrig))
# #Se complilan las regex necesarias para limpiar el texto de menciones, hashtags y sitios web:
# menciones = re.compile(r'@[A-Za-z0-9á-ú_]*')
# hashtags = re.compile(r'#[A-Za-z0-9á-ú_]*')
# websites = re.compile(r'http://[A-Za-z0-9\W]*')
#
# for indice, elemento in enumerate(textos, start = 1):
#     kleber = elemento.strip('<content>').strip('</content>')
#     cadena = kleber
#     w = re.sub(menciones, "", cadena)
#     x = re.sub(hashtags, "", w)
#     y = re.sub(websites, "", x)
#     z = y.strip()
#     # print (indice, '\n', z, '\n', '--------------------------------------')
#     finales.append(z)
#     # tag = elemento.replace('<tweetid>', ' ')
#     # tagalo = tag.replace('</tweetid>', ' ')
#
# ###Crea el árbol de fólders que se utilizarán y luego cambia a ~/Corpus/train/pos/
# os.mkdir('Corpus')
# os.chdir('Corpus')
# os.mkdir('test')
# os.mkdir('train')
# os.chdir('test')
# os.mkdir('neg')
# os.mkdir('pos')
# os.chdir('..')
# os.chdir('train')
# os.mkdir('neg')
# os.mkdir('pos')
# os.chdir('pos')
# # os.chdir('..')
# # os.chdir('..')
# ###Esta última nos dice que estamos en tweets Etiquetados
# # print (os.getcwd())
# # os.chdir('Corpus')
# # os.chdir('train')
# # os.chdir('pos')
# ###Esta sección divide el corpus en partes iguales y lo guarda correctamente
#
# # def divideLista(suma):
# #     w = suma
# #     x = w%2
# #
# #     if x == 1:
# #         y = (w-1)/2
# #
# #         z = (w-y)-1
# #
# #         y = int(y)
# #         z = int(z)
# #
# #     else:
# #         y = w/2
# #         z = w - y
# #         y = int(y)
# #         z = int(z)
# #
# #     # larga = lista[0:y]
# #     # sobrante = lista[-1]
# #     # corta = lista [z:-1]
# #     # corta.append(sobrante)
# #
# #     print (y)
# #     print (z)
# #
# # positive = divideLista(sumaPos)
# # negative = divideLista(sumaNeg)
# ###Guarda los txt positivos donde corresponden
# sumPos = 0
# sumNeg = 0
# for indice, elemento in enumerate(etiquetas):
#     tag = elemento.strip('<tweetid>').strip('</tweetid>')
#     # tagalo = tag.replace('</tweetid>', '')
#     if master[indice]=='P':
#         sumPos = sumPos + 1
#         if sumPos <= sumaPos/2:
#             # os.chdir('Corpus')
#             # os.chdir()
#             archivo = open (f'{tag}.txt', 'w')
#             archivo.write(finales[indice])
# sumPos = 0
# os.chdir('..')
# os.chdir('..')
# os.chdir('test')
# os.chdir('pos')
# # print (os.getcwd())
#
# for indice, elemento in enumerate(etiquetas):
#     tag = elemento.strip('<tweetid>').strip('</tweetid>')
#     # tagalo = tag.replace('</tweetid>', '')
#     if master[indice]=='P':
#         sumPos = sumPos + 1
#         if sumPos >= sumaPos/2:
#             # os.chdir('Corpus')
#             # os.chdir()
#             archivo = open (f'{tag}.txt', 'w')
#             archivo.write(finales[indice])
#
# os.chdir('..')
# os.chdir('..')
# os.chdir('train')
# os.chdir('neg')
# print (os.getcwd())
# ###Guarda los txt negativos donde corresponden
# # os.chdir('..')
# # os.chdir('neg')
# for indice, elemento in enumerate(etiquetas):
#     tag = elemento.strip('<tweetid>').strip('</tweetid>')
#     # tagalo = tag.replace('</tweetid>', '')
#     if master[indice]=='N':
#         sumNeg = sumNeg + 1
#         if sumNeg <= sumaNeg/2:
#             #os.chdir('Corpus')
#             archivo = open (f'{tag}.txt', 'w')
#             archivo.write(finales[indice])
#
# sumNeg = 0
# os.chdir('..')
# os.chdir('..')
# os.chdir('test')
# os.chdir('neg')
#
# for indice, elemento in enumerate(etiquetas):
#     tag = elemento.strip('<tweetid>').strip('</tweetid>')
#     # tagalo = tag.replace('</tweetid>', '')
#     if master[indice]=='N':
#         sumNeg = sumNeg + 1
#         if sumNeg >= sumaNeg/2:
#             #os.chdir('Corpus')
#             archivo = open (f'{tag}.txt', 'w')
#             archivo.write(finales[indice])
# ###PRUEBAS QUE NO FUNCIONARON
#
# #Printing content one at a time
# # for indice, element in enumerate (b_unique, start=1):
# #     print (indice, element)
# # print(b_unique)
#
# # Using find() to extract attributes of the first instance of the tag
# # b_name = bs_data.find('user', {'name':'Acer'})
# # print(b_name)
#
# # Extracting the data stored in a specific attribute of the `child` tag
# # value = b_name.get('qty')
# # print(value)
#
# # print (listaValores)
#     #print (list(hijos[1]))
#     # for index, element in enumerate(item.children):
#         #print (index, element)
#     #print (indice, list(item.children))
#
# # for
# #
# # if vale.parent == 'polarity'
# #     if polarity.parent == 'sentiment'
# #         lista.append(list(element.parent))
# #for element in value:
# 	#parent = list(element.parent)
# 	#print (parent)
#
# # for indice, element in enumerate(value):
# # 	print (indice, element)
#
#
# #print (result)
#
# # b_name = bs_data.find('user', {'name':'Acer'})
#
#
# #for indice, element in enumerate(sentiment):
# 	#print (indice, element)

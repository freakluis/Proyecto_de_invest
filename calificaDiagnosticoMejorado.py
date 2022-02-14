from bs4 import BeautifulSoup
import os
import re
#Fuentes:
#https://www.studytonight.com/python-howtos/how-to-read-xml-file-in-python
#https://linuxhint.com/parse_xml_python_beautifulsoup/
#https://www.kite.com/python/examples/3471/xml-get-the-child-elements-of-an-xml-element

################PARTE 1#################
#Lee los datos del archivo xml y los pasa a una variable con el nombre de data
with open ('gestualidad.xml', 'r') as f:
     data = f.read()
# Pasa los datos guardados a un parser de beautifulsoup
bs_data = BeautifulSoup(data, 'xml')
###Sacamos los nombres de los candidatos y los guardamos en una lista que se
###aprovechará al final
nombres = []

names = bs_data.find_all('QID35_TEXT')

for nombre in names:
    valor = str(nombre)
    limpio = valor.strip('<QID35_TEXT>').strip('</QID35_TEXT>')
    nombres.append(limpio)

###Se declaran las etiquetas de las preguntas y las respuestas esperadas
###Aquí se pueden declarar tantas preguntas como haya

preguntas_y_respuestas_diagnostico = [('QID1', 'heiße'), ('QID5', 'Wie geht es dir?'),
('QID7', 'Wann'), ('QID20', 'hatten'), ('QID9', 'sind'), ('QID11', 'keine'),
('QID13', 'einen'), ('QID15', 'Möchtest'), ('QID19', 'mich'),
('QID23', 'rufe dich am Nachmittag an'), ('QID184', 'stehe immer früh auf'),
('QID185', 'findet um 19 Uhr statt')]

preguntas_y_respuestas_estimulos = [('QID202', 'Aus Dortmund.'), ('QID203', 'Jeden Abend.'),
('QID204', 'Helga'), ('QID205', 'Auf ein Examen.'), ('QID206', 'Aus Dortmund.'), ('QID207', 'Jeden Abend.'),
('QID208', 'Helga'), ('QID209', 'Auf ein Examen.') ]


###Se hace una lista de listas de preguntas existentes
#preguntas = [preguntas_y_respuestas_diagnostico, preguntas_y_respuestas_estimulos]
preguntas = [preguntas_y_respuestas_diagnostico]
#preguntas = [preguntas_y_respuestas_estimulos]

for frage in preguntas:

    etiquetas = []
    for element in frage:
        etiquetas.append(element[0])

    ###Se extraen las respuestas del archivo xml para poder tratarlas individualmente.
    responses = bs_data.find_all('Response')
    ###Se hace una lista con los índices correspondientes a los participantes.
    ###Este índice servirá en el programa principal
    participantes = []
    for i in range (0,len(nombres)):
        participantes.append(i)
    ###Éste es el programa principal de evaluación. Primero evalúa el diagnóstico.
    ###Corre tantas veces como participantes haya registrados y da el procentaje
    ###De preguntas respondidas correctamente del diagnóstico. Este porcentaje es
    ###el que se utilizará para decidir si se toman en cuenta las respuestas del
    ###participante o no. Al final el programa imprime qué participante no
    for participante in participantes:
        primera_respuesta = responses[participante]
        suma = 0
        for indice, pregunta in enumerate(frage):
            respuesta = primera_respuesta.find_all(pregunta[0])
            for item in respuesta:
                valor = str(item)
                limpio = valor.strip(f'<{etiquetas[indice]}>').strip(f'</{etiquetas[indice]}>')
                if limpio == pregunta[1]:
                    suma = suma + 1
                else:
                    suma = suma
        if (suma*100)/len(frage) < 50:
            print (f'Las respuestas del participante "{nombres[participante]}" no deben tomarse en cuenta.' )
        #print (f'El porcentaje de respuestas correctas de {nombres[participante]} en el diagnóstico es del', (suma*100)/len(frage), 'por ciento.')

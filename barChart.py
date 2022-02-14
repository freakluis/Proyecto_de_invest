from matplotlib import pyplot as plt

############################################
#       Éste es el ejemplo                 #
############################################
# numOscars = [5, 8 , 3, 8 , 11]
#
# movies = ['Con Air', 'The fast and the furious', 'John Wick', 'Kingsmann', 'Trainspotting']
#
# plt.bar(range(len(movies)), numOscars)
# plt.title('My favorite movies')
# plt.ylabel('# of academy awards')
#
# #label x-axis with movie names at bar centers
# plt.xticks(range(len(movies)), movies)

#plt.show()

############################################
#       Éste es el que se va a usar        #
############################################

postTestG = [5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 3, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5]
pretestG = [1, 3, 4, 5, 5, 4, 4, 5, 1, 5, 2, 3, 5, 2, 4, 5, 1, 1, 4, 5, 4, 3, 5, 4, 1, 5, 5, 2, 5, 2, 4, 3, 5, 2, 1, 5, 4, 5, 2]
postTestSG = [5, 5, 5, 5, 2, 4, 4, 4, 5, 1, 5, 5, 5, 4, 5, 5, 3, 4, 3, 5, 1, 5, 2, 5, 2, 5, 1, 2, 3, 2, 1, 2, 2]
pretestSG = [3, 5, 1, 4, 1, 3, 3, 4, 3, 1, 2, 5, 3, 3, 3, 4, 5, 4, 4, 2, 3, 2, 4, 5, 1, 3, 1, 3, 3, 3, 3, 2, 2]

movies = [ str(i) for i in range (1,6)]

def obtieneConteos (lista):
    conteos = []
    for valor in movies:
        sum = 0
        for element in lista:
            if element == int(valor):
                sum += 1
        conteos.append((sum/len(lista))*100)
        #print (sum)

    print (conteos)
    return conteos
##### Trozo de código para dibujar las respuestas integradas en condición SG
postTestSinGestulidad = obtieneConteos(postTestSG)
preTestSinGestulidad = obtieneConteos(pretestSG)

plt.bar(range(len(movies)), postTestSinGestulidad)
plt.bar(range(len(movies)), preTestSinGestulidad, alpha=0.7)
plt.title('Respuestas a los reactivos de interés en pre- y post-test en condición SG')
plt.xlabel('En escala de Likert de 1 al 5 (pre-test en naranja y post-test en azul)')
plt.ylabel('Respuestas totales expresadas en %')
plt.xticks(range(len(movies)), movies)
plt.show()

##### Trozo de código para dibujar las respuestas integradas en condición G
postTestConGestulidad = obtieneConteos(postTestG)
preTestConGestulidad = obtieneConteos(pretestG)

plt.bar(range(len(movies)), postTestConGestulidad)
plt.bar(range(len(movies)), preTestConGestulidad, alpha=0.7)
plt.title('Respuestas a los reactivos de interés en pre- y post-test en condición G')
plt.xlabel('En escala de Likert de 1 al 5 (pre-test en naranja y post-test en azul)')
plt.ylabel('Respuestas totales expresadas en %')
plt.xticks(range(len(movies)), movies)
plt.show()

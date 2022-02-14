from bs4 import BeautifulSoup


with open ('gestualidad.xml', 'r') as f:
     data = f.read()

bs_data = BeautifulSoup(data, 'xml')
umstaende = bs_data.find_all('QID202')

def tellsConditionsAppart():
    condicionG = []
    condicionSG = []

    etiqueta = 'QID202'

    for indice, dato in enumerate(umstaende,start=1):
        valor = str(dato)
        if valor == f'<{etiqueta}>Aus Dortmund.</{etiqueta}>':
            condicionSG.append(indice)
        else:
            condicionG.append(indice)
    # print ('Participantes en condicion G:', condicionG)
    # print ('Participantes en condicion SG:', condicionSG)
    return condicionG, condicionSG

condicionG, condicionSG = tellsConditionsAppart()

print ('Participantes en condicion G:', condicionG)
print ('Participantes en condicion SG:', condicionSG)

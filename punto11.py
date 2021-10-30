import random

def quicksort(lista):
    izq = []
    mitad = []
    der = []
    length = len(lista)
    if len(lista) >= 2:
        referencia = lista[int(length/2)]
        for k in lista:
            if (k < referencia):
                izq.append(k)
            elif (k > referencia):
                der.append(k)
            elif (k == referencia):
                mitad.append(k)
        return quicksort(izq) + mitad + quicksort(der)
    else:
        return lista

listaA = [0]*100
listaB = [0]*60

for i in range (100):
    listaA[i] = random.randint(1,50)

for i in range (60):
    listaB[i] = random.randint(1,50)

print(quicksort(listaA))
print(quicksort(listaB))

listaC = listaA + listaB

print(quicksort(listaC))
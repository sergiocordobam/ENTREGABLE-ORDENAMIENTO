##Eficiencia del método: O(n Log n) y la eficiencia del punto 1 es O(n)

def quickSort(lista):
    izq = []
    mitad = []
    der = []

    if len(lista) > 1:
        pivote = lista[-1]

        for i in lista:
            if (i < pivote):
                izq.append(i)
            elif (i > pivote):
                der.append(i)
            elif (i == pivote):
                mitad.append(i)
        return quickSort(izq) + mitad + quickSort(der)
    else:
        return lista

lista = [2,3,4,5,5,5,6,7,7,8,6,9,2]
print(quickSort(lista))

sin_duplicados = []
for i in lista:
    if i not in sin_duplicados:
        sin_duplicados.append(i)
print(sin_duplicados)

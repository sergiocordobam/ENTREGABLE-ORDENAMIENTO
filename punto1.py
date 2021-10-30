def eliminarDuplicados(unaLista):
    sinDuplicados = []
    for i in unaLista:
        if i not in sinDuplicados:
            sinDuplicados.append(i)
    print(sinDuplicados)

unaLista = [4,7,11,4,9,5,11,7,3,5]
print(unaLista)
eliminarDuplicados(unaLista)
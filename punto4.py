#Con el uso del algoritmo de ordenacion Shell, se realizan un total de tres pasadas:
# En la primera pasada se intercambian el 43 y 18, 40 y 7.
# En la segunda pasada se intercambian el 17 y 7, el 43 y 11, el 18 y 6, el 18 y 16, el 40 y 97
# el 8 y 7, el 17 y 11.
# En la tercera pasada se intercambian el 7 y 6, el 16 y 11, el 18 y 17
# Y así finaliza el ordenamiento.

def shell_sort(lista, n):
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = lista[i]
            j = i
            while j >= h and lista[j - h] > t:
                lista[j] = lista[j - h]
                j -= h
            lista[j] = t
        h = h // 2
        print(lista)

lista = [8,43,17,6,40,16,18,97,11,7]

n = len(lista)
print(lista)
shell_sort(lista, n)
##print(lista)
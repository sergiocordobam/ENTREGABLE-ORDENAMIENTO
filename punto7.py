import time
start = time.time()

def negativos(lista):
    negativo = []
    for i in lista:
        if i < 0:
            negativo.append(i)
    return negativo

lista = [0,3,6,-1,6,-3,9,-15,-10]
print(negativos(lista))

end = time.time()
print( end - start )

## El tiempo de ejecución de algortimo es de 0.00046706199645996094 s
## En todos los casos el algortimo va a tener que recorrer todas las posiciones del arreglo, por lo que no
## existiría peor caso; todos serían iguales.
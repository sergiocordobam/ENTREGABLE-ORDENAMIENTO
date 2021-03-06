## El resultado después de tres llamadas recursivas es [54]. Esto debido a que en el ordenamiento
## por mezcla se divide la lista original en listas más pequeñas (por la mitad en cada iteración). 

## En la primera iteración no queda que [54, 26, 93, 17],
## Luego tenemos que [54, 26]  y en la tercera iteración nos queda como resultado [54]

def Omerge(unaLista):
    print("Dividir ",unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        ## LLamada recursiva para cada lista 
        Omerge(mitadIzquierda)
        Omerge(mitadDerecha)
        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while i < len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",unaLista)

unaLista = [54,26,93,17,77,31,44,55,20]
Omerge(unaLista)
print(unaLista)
## El método de ordenamiento que se utiliza es el Bubblesort,
## debido a que se comparan los dos primeros elementos y si no estan
## en el orden que les corresponde los intercambia. Se repite el proceso
## con los dos siguientes numeros hasta llegar al final.

def bubbleSortMenor(arr):
    for i in range(0, len(arr)-1):
        for j in range(0,len(arr)-(i+1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr
lista = [47,3,21,32,56,92]
print(bubbleSortMenor(lista))
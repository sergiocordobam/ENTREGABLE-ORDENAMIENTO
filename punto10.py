#Se ingresa una matriz ordenada
matrix = [  [1,2,2,2,3,4],
            [1,2,3,3,4,5],
            [3,4,4,4,4,6],
            [4,5,6,7,8,9]]

def busqueda(matrix, elemento):
    for c in range (len(matrix[0])):
        for f in range (len(matrix)):
            if (elemento == matrix[f][c]):
                print("El elemento se encuentra en la matriz")
                return 
            if (elemento < matrix[f][c]):
                print("El elemento no se encuentra en la matriz")
                return
    print("El elemento no se encuentra en la matriz")


busqueda(matrix, 9)


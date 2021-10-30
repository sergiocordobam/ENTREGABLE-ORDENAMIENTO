##La complejidad del algortimo es de O(n)
def ganadorEleccion(lista):
    contador1 = 0
    contador2 = 0
    contador3 = 0
    for i in lista:
        if i == 1:
            contador1 += 1
        elif i == 2:
            contador2 += 1
        elif i == 3:
            contador3 += 1
    
    if contador1 > contador2 and contador1 > contador3:
        print("El ganador es el 1 con:",contador1,"votos")
    elif contador2 > contador1 and contador2 > contador3:
        print("El ganador es el 2 con:",contador2,"votos")
    elif contador3 > contador1 and contador3 > contador2:
        print("El ganador es el 3 con:",contador3,"votos")
    elif contador1 == contador2 and contador1 != contador3:
        print("Candidato 1 empató con el candidato 2 con:",contador1,"votos" )
    elif contador1 == contador3 and contador1 != contador2:
        print("Candidato 1 empató con el candidato 3 con:",contador1,"votos" )
    elif contador2 == contador3 and contador2 != contador1:
        print("Candidato 2 empató con el candidato 3 con:",contador2,"votos" )
    else:
        print("Todos los candidatos quedaron empatados con:",contador1,"votos")

lista = [2,2,1,1,1,3,3,3]
ganadorEleccion(lista)

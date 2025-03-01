#matriz bidimensional con valores numéricos
Matriz= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#función que realice una búsqueda en la matriz para encontrar un valor específico
def buscar_el_valor(matriz,valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i,j
    return -1,-1


#busqueda del numero dentro de la matriz
Numero_a_buscar =8

#resultado
Respuesta= buscar_el_valor(Matriz,Numero_a_buscar)
if Respuesta:
    print(f"el numero buscado {Numero_a_buscar} se encuentra en la posición:{Respuesta[0]},{Respuesta[1]}.")
else:
    print(f"el nuemro no se encontro en la matriz.")



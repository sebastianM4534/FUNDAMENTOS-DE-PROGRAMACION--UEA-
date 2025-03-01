def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila  # Agregar return para que devuelva la fila ordenada

def ordenar_fila_matriz(matriz, fila_a_ordenar):
    matriz[fila_a_ordenar] = bubble_sort_fila(matriz[fila_a_ordenar])
    return matriz

# Definir la matriz 3x3
matriz = [
    [9, 3, 5],
    [4, 1, 8],
    [7, 6, 2]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1, que es la segunda fila, índice 1)
fila_a_ordenar = 1

# Ordenar la fila específica
ordenar_fila_matriz(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila", fila_a_ordenar, "ordenada.:")
for fila in matriz:
    print(fila)

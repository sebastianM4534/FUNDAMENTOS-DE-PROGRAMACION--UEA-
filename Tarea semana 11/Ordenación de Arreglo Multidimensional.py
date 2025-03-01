def bubble_sort_columna(matriz, columna):
    n = len(matriz)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[j][columna] > matriz[j + 1][columna]:
                matriz[j][columna], matriz[j + 1][columna] = matriz[j + 1][columna], matriz[j][columna]

def ordenar_columna_matriz(matriz, columna_a_ordenar):
    bubble_sort_columna(matriz, columna_a_ordenar)
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

# Columna a ordenar (por ejemplo, la columna 0, que es la primera columna, índice 0)
columna_a_ordenar = 0

# Ordenar la columna específica
ordenar_columna_matriz(matriz, columna_a_ordenar)

# Mostrar la matriz con la columna ordenada
print("\nMatriz con la columna", columna_a_ordenar, "ordenada:")
for fila in matriz:
    print(fila)

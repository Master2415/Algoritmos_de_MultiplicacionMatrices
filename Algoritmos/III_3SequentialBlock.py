def lll_3_sequential_block(matrizA, matrizB, size):
    """
    Realiza la multiplicación de matrices de forma secuencial utilizando bloques.

    Parameters:
    - matrizA (list of lists): Matriz de tamaño 'size' x 'size'.
    - matrizB (list of lists): Matriz de tamaño 'size' x 'size'.
    - size (int): Tamaño de la matriz cuadrada.
    """
    # Calcula el tamaño de bloque
    bsize = int(size ** 0.5)
    # Crea la matriz de resultados
    matrizResultado = [[0.0] * size for _ in range(size)]
    # Itera sobre los bloques de la matriz
    for i1 in range(0, size, bsize):
        for j1 in range(0, size, bsize):
            for k1 in range(0, size, bsize):
                # Itera dentro de cada bloque
                for i in range(i1, min(i1 + bsize, size)):
                    for j in range(j1, min(j1 + bsize, size)):
                        for k in range(k1, min(k1 + bsize, size)):
                            # Calcula la multiplicación de matrices en cada elemento
                            matrizResultado[i][j] += matrizA[i][k] * matrizB[k][j]

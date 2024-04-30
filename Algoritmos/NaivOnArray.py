def NaivOnArray(matrizA, matrizB, matrizC, N, P, M):
    """
    Realiza la multiplicación de matrices utilizando el algoritmo de multiplicación
    ingenua (naive) con desenrollado de bucles en Python.

    Parámetros:
    matrizA (list): Matriz A de dimensiones NxP.
    matrizB (list): Matriz B de dimensiones PxM.
    matrizC (list): Matriz C donde se almacenará el resultado de la multiplicación.
    N (int): Número de filas de la matriz A y la matriz C.
    P (int): Número de columnas de la matriz A y número de filas de la matriz B.
    M (int): Número de columnas de la matriz B y la matriz C.
    """
    for i in range(N):  # Recorre las filas de la matriz A y C
        for j in range(M):  # Recorre las columnas de la matriz B y C
            matrizC[i][j] = 0.0  # Inicializa el elemento (i, j) de la matriz C a 0
            for k in range(P):  # Recorre las columnas de la matriz A y las filas de la matriz B
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]  # Multiplica y suma los elementos correspondientes



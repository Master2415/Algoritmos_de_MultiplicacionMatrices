
def NaivOnArray_(matrizA, matrizB, matrizC, N, P, M):
    # Bucle externo que recorre las filas de la matriz C
    for i in range(N):
        # Bucle interno que recorre las columnas de la matriz C
        for j in range(M):
            # Inicializa el valor de la celda (i, j) en la matriz C a 0.0
            matrizC[i][j] = 0.0
            # Bucle interno que realiza la multiplicación y suma de elementos de la matriz A y B
            for k in range(P):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    return matrizC

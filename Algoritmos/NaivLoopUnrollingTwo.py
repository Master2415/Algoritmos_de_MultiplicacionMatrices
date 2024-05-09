def NaivLoopUnrollingTwo(matrizA, matrizB, matrizC, N, P, M):
    # Multiplicación de matrices utilizando el algoritmo Naive Loop Unrolling Two
    if P % 2 == 0:  # Verificar si el número de columnas de la matriz B es par
        for i in range(N):  # Iterar sobre las filas de la matriz A y matriz C
            for j in range(M):  # Iterar sobre las columnas de la matriz B y matriz C
                aux = 0.0  # Reiniciar la variable auxiliar para cada posición de la matriz C
                for k in range(0, P, 2):  # Iterar sobre las columnas de la matriz A y B con paso 2
                    # Sumar el producto de los elementos desenrollados de las matrices A y B
                    aux += matrizA[i][k] * matrizB[k][j] + matrizA[i][k + 1] * matrizB[k + 1][j]
                matrizC[i][j] = aux  # Asignar el resultado parcial a la posición (i, j) de la matriz C
    else:  # Caso donde el número de columnas de la matriz B es impar
        PP = P - 1  # Última columna par de la matriz B
        for i in range(N):  # Iterar sobre las filas de la matriz A y matriz C
            for j in range(M):  # Iterar sobre las columnas de la matriz B y matriz C
                aux = 0.0  # Reiniciar la variable auxiliar para cada posición de la matriz C
                for k in range(0, PP, 2):  # Iterar sobre las columnas pares de la matriz A y B con paso 2
                    # Sumar el producto de los elementos desenrollados de las matrices A y B
                    aux += matrizA[i][k] * matrizB[k][j] + matrizA[i][k + 1] * matrizB[k + 1][j]
                # Sumar el producto de la última columna impar de A y la última columna de B
                matrizC[i][j] = aux + matrizA[i][PP] * matrizB[PP][j]

    return matrizC

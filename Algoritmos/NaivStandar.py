def naiv_standard(matrizA, matrizB, matrizC, N, P, M):
    # Ciclo para recorrer las filas de la matriz A
    for i in range(N):
        # Ciclo para recorrer las columnas de la matriz B
        for j in range(M):
            aux = 0.0  # Inicializar la variable auxiliar en 0
            # Ciclo para realizar la multiplicación y acumulación de elementos de la matriz A y B
            for k in range(P):
                aux += matrizA[i][k] * matrizB[k][j]  # Multiplicar elementos y acumular el resultado en aux
            matrizC[i][j] = aux  # Almacenar el resultado final en la matriz C

    return matrizC
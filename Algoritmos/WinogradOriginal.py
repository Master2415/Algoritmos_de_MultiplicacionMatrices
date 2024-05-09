def WinogradOriginal(A, B, Result, N, P, M):
    i, j, k = 0, 0, 0
    aux = 0.0
    upsilon = P % 2
    gamma = P - upsilon
    y = [0.0] * M  # Lista para almacenar valores intermedios y[i]
    z = [0.0] * N  # Lista para almacenar valores intermedios z[i]

    # Calcula y[i] para cada fila de A
    for i in range(M):  # Ciclo externo para recorrer cada fila de A
        aux = 0.0
        for j in range(0, gamma, 2):  # Ciclo interno para recorrer las columnas de A
            aux += A[i][j] * A[i][j + 1]  # Suma de productos de elementos consecutivos de A
        y[i] = aux  # Almacena el resultado en la lista y

    # Calcula z[i] para cada columna de B
    for i in range(N):  # Ciclo externo para recorrer cada columna de B
        aux = 0.0
        for j in range(0, gamma, 2):  # Ciclo interno para recorrer las filas de B
            aux += B[j][i] * B[j + 1][i]  # Suma de productos de elementos consecutivos de B
        z[i] = aux  # Almacena el resultado en la lista z

    # Calcula la multiplicación de matrices usando el algoritmo de Winograd Original
    if upsilon == 1:  # Caso cuando P es impar
        PP = P - 1
        for i in range(M):  # Ciclo externo para recorrer cada fila de A
            for k in range(N):  # Ciclo externo para recorrer cada columna de B
                aux = 0.0
                for j in range(0, gamma, 2):  # Ciclo interno para recorrer las columnas de A y filas de B
                    # Multiplicación y suma de elementos según el algoritmo de Winograd
                    aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                Result[i][k] = aux - y[i] - z[k] + A[i][PP] * B[PP][k]  # Asigna el resultado a la matriz Result
    else:  # Caso cuando P es par
        for i in range(M):  # Ciclo externo para recorrer cada fila de A
            for k in range(N):  # Ciclo externo para recorrer cada columna de B
                aux = 0.0
                for j in range(0, gamma, 2):  # Ciclo interno para recorrer las columnas de A y filas de B
                    # Multiplicación y suma de elementos según el algoritmo de Winograd
                    aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                Result[i][k] = aux - y[i] - z[k]  # Asigna el resultado a la matriz Result

    # Liberar memoria al finalizar
    y = None
    z = None

    return Result

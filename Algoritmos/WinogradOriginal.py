def WinogradOriginal(A, B, Result, N, P, M):

    i, j, k = 0, 0, 0
    aux = 0.0
    upsilon = P % 2
    gamma = P - upsilon
    y = [0.0] * M
    z = [0.0] * N

    # Calcula y[i] para cada fila de A
    for i in range(M):
        aux = 0.0
        for j in range(0, gamma, 2):
            aux += A[i][j] * A[i][j + 1]
        y[i] = aux

    # Calcula z[i] para cada columna de B
    for i in range(N):
        aux = 0.0
        for j in range(0, gamma, 2):
            aux += B[j][i] * B[j + 1][i]
        z[i] = aux

    # Calcula la multiplicación de matrices usando el algoritmo de Winograd Original
    if upsilon == 1:
        PP = P - 1
        for i in range(M):
            for k in range(N):
                aux = 0.0
                for j in range(0, gamma, 2):
                    aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                Result[i][k] = aux - y[i] - z[k] + A[i][PP] * B[PP][k]
    else:
        for i in range(M):
            for k in range(N):
                aux = 0.0
                for j in range(0, gamma, 2):
                    aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                Result[i][k] = aux - y[i] - z[k]

    # Liberar memoria al finalizar
    y = None
    z = None

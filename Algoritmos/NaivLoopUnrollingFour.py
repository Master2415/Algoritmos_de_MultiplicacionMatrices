def NaivLoopUnrollingFour(A, B, Result, N, P, M):
    i, j, k = 0, 0, 0  # Inicializar variables de iteración
    aux = 0.0  # Variable auxiliar para almacenar el resultado parcial de la multiplicación

    # Verificar dimensiones de las matrices
    if len(A[0]) != P or len(B) != P or len(Result) != N or len(Result[0]) != M:
        raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")

    # Multiplicación de matrices utilizando el algoritmo Naive Loop Unrolling Four
    if P % 4 == 0:  # Si el número de columnas de B es divisible por 4
        for i in range(N):  # Iterar sobre las filas de A y Result
            for j in range(M):  # Iterar sobre las columnas de B y Result
                aux = 0.0  # Reiniciar la variable auxiliar para cada posición de Result
                for k in range(0, P, 4):  # Iterar sobre las columnas de A y B con paso 4
                    # Sumar el producto de los elementos desenrollados de A y B
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux  # Asignar el resultado parcial a la posición (i, j) de Result
    elif P % 4 == 1:  # Si el número de columnas de B deja residuo 1 al dividir por 4
        PP = P - 1
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, PP, 4):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux + A[i][PP] * B[PP][j]
    elif P % 4 == 2:  # Si el número de columnas de B deja residuo 2 al dividir por 4
        PP = P - 2
        PPP = P - 1
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, PP, 4):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux + A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j]
    else:  # Si el número de columnas de B deja residuo 3 al dividir por 4
        PP = P - 3
        PPP = P - 2
        PPPP = P - 1
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(0, PP, 4):
                    aux += A[i][k] * B[k][j] + A[i][k + 1] * B[k + 1][j] + A[i][k + 2] * B[k + 2][j] + A[i][k + 3] * B[k + 3][j]
                Result[i][j] = aux + A[i][PP] * B[PP][j] + A[i][PPP] * B[PPP][j] + A[i][PPPP] * B[PPPP][j]

    return Result

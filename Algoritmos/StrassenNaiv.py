import math


def StrassenNaiv(matrizA, matrizB, matrizC, N, P, M):
    # Calcula el tamaño máximo entre N y P
    MaxSize = max(N, P)
    # Asegura que MaxSize sea al menos 16 para evitar problemas de tamaño en la descomposición
    if MaxSize < 16:
        MaxSize = 16

    # Calcula k y m según el algoritmo de Strassen
    k = int(math.floor(math.log(MaxSize) / math.log(2))) - 4
    m = int(math.floor(MaxSize * 2 ** (-k))) + 1
    NewSize = m * 2 ** k  # Tamaño de las matrices ampliadas para Strassen

    # Crea matrices ampliadas con ceros para usar el algoritmo de Strassen
    NewA = [[0.0] * NewSize for _ in range(NewSize)]
    NewB = [[0.0] * NewSize for _ in range(NewSize)]
    AuxResult = [[0.0] * NewSize for _ in range(NewSize)]

    # Copia los datos de matrizA y matrizB a las matrices ampliadas
    for i in range(N):
        for j in range(P):
            NewA[i][j] = matrizA[i][j]

    for i in range(P):
        for j in range(M):
            NewB[i][j] = matrizB[i][j]

    # Llama a la función strassen_naiv_step para realizar la multiplicación de Strassen
    strassen_naiv_step(NewA, NewB, AuxResult, NewSize, m)

    # Extrae el resultado de la matriz auxiliar (producto de Strassen) y lo asigna a matrizC
    for i in range(N):
        for j in range(M):
            matrizC[i][j] = AuxResult[i][j]


def max(N, P):
    # Devuelve el máximo entre N y P
    return max(N, P) if N < P else N


def minus(A, B, Result, N, M):
    # Recorre cada fila de A y B
    for i in range(N):
        # Recorre cada columna de A y B en la misma fila
        for j in range(M):
            # Resta el elemento de la misma posición en A y B y asigna el resultado a Result
            Result[i][j] = A[i][j] - B[i][j]


def plus(A, B, Result, N, M):
    # Recorre cada fila de A y B
    for i in range(N):
        # Recorre cada columna de A y B en la misma fila
        for j in range(M):
            # Suma el elemento de la misma posición en A y B y asigna el resultado a Result
            Result[i][j] = A[i][j] + B[i][j]


def strassen_naiv_step(A, B, Result, N, m):
    # Verifica si N es par y mayor que m para aplicar el algoritmo de Strassen
    if N % 2 == 0 and N > m:
        # Divide la matriz en cuatro partes
        NewSize = N // 2
        A11 = [row[:NewSize] for row in A[:NewSize]]
        A12 = [row[NewSize:] for row in A[:NewSize]]
        A21 = [row[:NewSize] for row in A[NewSize:]]
        A22 = [row[NewSize:] for row in A[NewSize:]]
        B11 = [row[:NewSize] for row in B[:NewSize]]
        B12 = [row[NewSize:] for row in B[:NewSize]]
        B21 = [row[:NewSize] for row in B[NewSize:]]
        B22 = [row[NewSize:] for row in B[NewSize:]]

        # Inicializa matrices auxiliares
        ResultPart11 = [[0.0] * NewSize for _ in range(NewSize)]
        ResultPart12 = [[0.0] * NewSize for _ in range(NewSize)]
        ResultPart21 = [[0.0] * NewSize for _ in range(NewSize)]
        ResultPart22 = [[0.0] * NewSize for _ in range(NewSize)]
        Helper1 = [[0.0] * NewSize for _ in range(NewSize)]
        Helper2 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux1 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux2 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux3 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux4 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux5 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux6 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux7 = [[0.0] * NewSize for _ in range(NewSize)]

        # Operaciones de suma y resta entre bloques de A y B
        plus(A11, A22, Helper1, NewSize, NewSize)
        plus(B11, B22, Helper2, NewSize, NewSize)
        strassen_naiv_step(Helper1, Helper2, Aux1, NewSize, m)

        plus(A21, A22, Helper1, NewSize, NewSize)
        strassen_naiv_step(Helper1, B11, Aux2, NewSize, m)

        minus(B12, B22, Helper1, NewSize, NewSize)
        strassen_naiv_step(A11, Helper1, Aux3, NewSize, m)

        minus(B21, B11, Helper1, NewSize, NewSize)
        strassen_naiv_step(A22, Helper1, Aux4, NewSize, m)

        plus(A11, A12, Helper1, NewSize, NewSize)
        strassen_naiv_step(Helper1, B22, Aux5, NewSize, m)

        minus(A21, A11, Helper1, NewSize, NewSize)
        plus(B11, B12, Helper2, NewSize, NewSize)
        strassen_naiv_step(Helper1, Helper2, Aux6, NewSize, m)

        minus(A12, A22, Helper1, NewSize, NewSize)
        plus(B21, B22, Helper2, NewSize, NewSize)
        strassen_naiv_step(Helper1, Helper2, Aux7, NewSize, m)

        # Operaciones finales para obtener el resultado
        plus(Aux1, Aux4, ResultPart11, NewSize, NewSize)
        minus(ResultPart11, Aux5, ResultPart11, NewSize, NewSize)
        plus(ResultPart11, Aux7, ResultPart11, NewSize, NewSize)

        plus(Aux3, Aux5, ResultPart12, NewSize, NewSize)

        plus(Aux2, Aux4, ResultPart21, NewSize, NewSize)

        plus(Aux1, Aux3, ResultPart22, NewSize, NewSize)
        minus(ResultPart22, Aux2, ResultPart22, NewSize, NewSize)
        plus(ResultPart22, Aux6, ResultPart22, NewSize, NewSize)

        # Copia los resultados parciales en la matriz Result final
        for i in range(NewSize):
            for j in range(NewSize):
                Result[i][j] = ResultPart11[i][j]

        for i in range(NewSize):
            for j in range(NewSize):
                Result[i][NewSize + j] = ResultPart12[i][j]

        for i in range(NewSize):
            for j in range(NewSize):
                Result[NewSize + i][j] = ResultPart21[i][j]

        for i in range(NewSize):
            for j in range(NewSize):
                Result[NewSize + i][NewSize + j] = ResultPart22[i][j]

    else:
        # Si N no cumple las condiciones, usa un método estándar (Naive Standard)
        naivStandard(A, B, Result, N, N, N)


def naivStandard(matrizA, matrizB, matrizC, N, P, M):
    # Recorre cada fila de la matriz A
    for i in range(N):
        # Recorre cada columna de la matriz B
        for j in range(M):
            aux = 0.0
            # Multiplica y suma los elementos correspondientes de A y B
            for k in range(P):
                aux += matrizA[i][k] * matrizB[k][j]
            # Asigna el resultado a la posición correspondiente en la matriz C
            matrizC[i][j] = aux


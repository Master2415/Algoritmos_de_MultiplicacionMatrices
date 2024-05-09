from Algoritmos import NaivStandar


def strassen_naiv_step(A, B, Result, N, m):
    if N % 2 == 0 and N > m:
        NewSize = N // 2

        # decompose A and B
        # create ResultPart, Aux1,...,Aux7 and Helper1, Helper2
        A11 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        A12 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        A21 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        A22 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        B11 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        B12 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        B21 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        B22 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

        ResultPart11 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        ResultPart12 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        ResultPart21 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        ResultPart22 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

        Helper1 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        Helper2 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

        Aux1 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        Aux2 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        Aux3 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        Aux4 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        Aux5 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        Aux6 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]
        Aux7 = [[0 for _ in range(NewSize)] for _ in range(NewSize)]

        # fill new matrices
        for i in range(NewSize):
            for j in range(NewSize):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][NewSize + j]
                A21[i][j] = A[NewSize + i][j]
                A22[i][j] = A[NewSize + i][NewSize + j]
                B11[i][j] = B[i][j]
                B12[i][j] = B[i][NewSize + j]
                B21[i][j] = B[NewSize + i][j]
                B22[i][j] = B[NewSize + i][NewSize + j]

        # computing the seven aux. variables
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

        # computing the four parts of the result
        plus(Aux1, Aux4, ResultPart11, NewSize, NewSize)
        minus(ResultPart11, Aux5, ResultPart11, NewSize, NewSize)
        plus(ResultPart11, Aux7, ResultPart11, NewSize, NewSize)

        plus(Aux3, Aux5, ResultPart12, NewSize, NewSize)

        plus(Aux2, Aux4, ResultPart21, NewSize, NewSize)

        plus(Aux1, Aux3, ResultPart22, NewSize, NewSize)
        minus(ResultPart22, Aux2, ResultPart22, NewSize, NewSize)
        plus(ResultPart22, Aux6, ResultPart22, NewSize, NewSize)

        # store results in the "result matrix"
        for i in range(NewSize):
            for j in range(NewSize):
                Result[i][j] = ResultPart11[i][j]
                Result[i][NewSize + j] = ResultPart12[i][j]
                Result[NewSize + i][j] = ResultPart21[i][j]
                Result[NewSize + i][NewSize + j] = ResultPart22[i][j]

    else:
        # use naive algorithm
        NaivStandar.naiv_standard(A, B, Result, N, N, N)


def minus(A, B, Result, N, M):
    # Itera sobre las filas de las matrices A, B y Result
    for i in range(N):
        # Itera sobre las columnas de las matrices A, B y Result
        for j in range(M):
            # Realiza la resta entre los elementos correspondientes de A y B, y lo asigna a Result
            Result[i][j] = A[i][j] - B[i][j]


def plus(A, B, Result, N, M):
    # Itera sobre las filas de las matrices A, B y Result
    for i in range(N):
        # Itera sobre las columnas de las matrices A, B y Result
        for j in range(M):
            # Realiza la suma entre los elementos correspondientes de A y B, y lo asigna a Result
            Result[i][j] = A[i][j] + B[i][j]

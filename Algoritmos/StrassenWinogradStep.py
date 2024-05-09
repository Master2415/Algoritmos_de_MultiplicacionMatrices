import NaivStandar


def strassen_winograd_step(A, B, Result, N, m):
    if N % 2 == 0 and N > m:
        NewSize = N // 2

        # Decompose A and B
        A1 = [[0.0] * NewSize for _ in range(NewSize)]
        A2 = [[0.0] * NewSize for _ in range(NewSize)]
        B1 = [[0.0] * NewSize for _ in range(NewSize)]
        B2 = [[0.0] * NewSize for _ in range(NewSize)]

        A11 = [[0.0] * NewSize for _ in range(NewSize)]
        A12 = [[0.0] * NewSize for _ in range(NewSize)]
        A21 = [[0.0] * NewSize for _ in range(NewSize)]
        A22 = [[0.0] * NewSize for _ in range(NewSize)]
        B11 = [[0.0] * NewSize for _ in range(NewSize)]
        B12 = [[0.0] * NewSize for _ in range(NewSize)]
        B21 = [[0.0] * NewSize for _ in range(NewSize)]
        B22 = [[0.0] * NewSize for _ in range(NewSize)]

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
        Aux8 = [[0.0] * NewSize for _ in range(NewSize)]
        Aux9 = [[0.0] * NewSize for _ in range(NewSize)]

        # Fill new matrices
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

        # Computing the 4 + 9 aux. variables
        minus(A11, A21, A1, NewSize, NewSize)
        minus(A22, A1, A2, NewSize, NewSize)
        minus(B22, B12, B1, NewSize, NewSize)
        plus(B1, B11, B2, NewSize, NewSize)

        strassen_winograd_step(A11, B11, Aux1, NewSize, m)
        strassen_winograd_step(A12, B21, Aux2, NewSize, m)
        strassen_winograd_step(A2, B2, Aux3, NewSize, m)
        plus(A21, A22, Helper1, NewSize, NewSize)
        minus(B12, B11, Helper2, NewSize, NewSize)
        strassen_winograd_step(Helper1, Helper2, Aux4, NewSize, m)
        strassen_winograd_step(A1, B1, Aux5, NewSize, m)
        minus(A12, A2, Helper1, NewSize, NewSize)
        strassen_winograd_step(Helper1, B22, Aux6, NewSize, m)
        minus(B21, B2, Helper1, NewSize, NewSize)
        strassen_winograd_step(A22, Helper1, Aux7, NewSize, m)
        plus(Aux1, Aux3, Aux8, NewSize, NewSize)
        plus(Aux8, Aux4, Aux9, NewSize, NewSize)

        # Computing the four parts of the result
        plus(Aux1, Aux2, ResultPart11, NewSize, NewSize)
        plus(Aux9, Aux6, ResultPart12, NewSize, NewSize)
        plus(Aux8, Aux5, Helper1, NewSize, NewSize)
        plus(Helper1, Aux7, ResultPart21, NewSize, NewSize)
        plus(Aux9, Aux5, ResultPart22, NewSize, NewSize)

        # Store results in the "result matrix"
        for i in range(NewSize):
            for j in range(NewSize):
                Result[i][j] = ResultPart11[i][j]
                Result[i][NewSize + j] = ResultPart12[i][j]
                Result[NewSize + i][j] = ResultPart21[i][j]
                Result[NewSize + i][NewSize + j] = ResultPart22[i][j]

    else:
        # Use naive algorithm
        NaivStandar.naiv_standard(A, B, Result, N, N, N)


def minus(A, B, Result, N, M):
    for i in range(N):
        for j in range(M):
            Result[i][j] = A[i][j] - B[i][j]


def plus(A, B, Result, N, M):
    for i in range(N):
        for j in range(M):
            Result[i][j] = A[i][j] + B[i][j]

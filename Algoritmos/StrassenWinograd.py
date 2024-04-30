import math
import NaivStandar

class StrassenWinograd(NaivStandar):
    def max(self, N, P):
        if N < P:
            return P
        else:
            return N

    def strassen_winograd(self, matrizA, matrizB, matrizC, N, P, M):
        MaxSize = self.max(N, P)
        MaxSize = self.max(MaxSize, M)
        if MaxSize < 16:
            MaxSize = 16  # de lo contrario, no es posible calcular k

        k = int(math.floor(math.log(MaxSize) / math.log(2))) - 4
        m = int(math.floor(MaxSize * math.pow(2, -k))) + 1
        NewSize = m * int(math.pow(2, k))

        # Agrega filas y columnas de ceros para usar el algoritmo de Strassen
        NewA = [[0.0] * NewSize for _ in range(NewSize)]
        NewB = [[0.0] * NewSize for _ in range(NewSize)]
        AuxResult = [[0.0] * NewSize for _ in range(NewSize)]

        for i in range(N):
            for j in range(P):
                NewA[i][j] = matrizA[i][j]

        for i in range(P):
            for j in range(M):
                NewB[i][j] = matrizB[i][j]

        self.strassen_winograd_step(NewA, NewB, AuxResult, NewSize, m)

        # Extraer el resultado
        for i in range(N):
            for j in range(M):
                matrizC[i][j] = AuxResult[i][j]

    def strassen_winograd_step(self, A, B, Result, N, m):
        if N % 2 == 0 and N > m:
            NewSize = N // 2

            # decomponer A y B
            A1 = [row[:NewSize] for row in A]
            A2 = [row[NewSize:] for row in A]
            B1 = [row[:NewSize] for row in B]
            B2 = [row[NewSize:] for row in B]

            A11 = [row[:NewSize] for row in A1]
            A12 = [row[NewSize:] for row in A1]
            A21 = [row[:NewSize] for row in A2]
            A22 = [row[NewSize:] for row in A2]
            B11 = [row[:NewSize] for row in B1]
            B12 = [row[NewSize:] for row in B1]
            B21 = [row[:NewSize] for row in B2]
            B22 = [row[NewSize:] for row in B2]

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

            # Calcula las variables auxiliares
            self.minus(A11, A21, A1, NewSize, NewSize)
            self.minus(A22, A1, A2, NewSize, NewSize)
            self.minus(B22, B12, B1, NewSize, NewSize)
            self.plus(B1, B11, B2, NewSize, NewSize)

            self.strassen_winograd_step(A11, B11, Aux1, NewSize, m)
            self.strassen_winograd_step(A12, B21, Aux2, NewSize, m)
            self.strassen_winograd_step(A2, B2, Aux3, NewSize, m)
            self.plus(A21, A22, Helper1, NewSize, NewSize)
            self.minus(B12, B11, Helper2, NewSize, NewSize)
            self.strassen_winograd_step(Helper1, Helper2, Aux4, NewSize, m)
            self.strassen_winograd_step(A1, B1, Aux5, NewSize, m)
            self.minus(A12, A2, Helper1, NewSize, NewSize)
            self.strassen_winograd_step(Helper1, B22, Aux6, NewSize, m)
            self.minus(B21, B2, Helper1, NewSize, NewSize)
            self.strassen_winograd_step(A22, Helper1, Aux7, NewSize, m)
            self.plus(Aux1, Aux3, Aux8, NewSize, NewSize)
            self.plus(Aux8, Aux4, Aux9, NewSize, NewSize)

            # Calcula las partes del resultado
            self.plus(Aux1, Aux2, ResultPart11, NewSize, NewSize)
            self.plus(Aux9, Aux6, ResultPart12, NewSize, NewSize)
            self.plus(Aux8, Aux5, Helper1, NewSize, NewSize)
            self.plus(Helper1, Aux7, ResultPart21, NewSize, NewSize)
            self.plus(Aux9, Aux5, ResultPart22, NewSize, NewSize)

            # Almacena los resultados en la matriz Result
            for i in range(NewSize):
                for j in range(NewSize):
                    Result[i][j] = ResultPart11[i][j]
                    Result[i][NewSize + j] = ResultPart12[i][j]
                    Result[NewSize + i][j] = ResultPart21[i][j]
                    Result[NewSize + i][NewSize + j] = ResultPart22[i][j]
        else:
            # Usa el algoritmo naiv
            self.naiv_standard(A, B, Result, N, N, N)

    def minus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] - B[i][j]

    def plus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] + B[i][j]

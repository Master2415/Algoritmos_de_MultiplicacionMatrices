import math
import NaivStandar

class StrassenNaiv(NaivStandar):
    def strassen_naiv(self, matrizA, matrizB, matrizC, N, P, M):
        MaxSize = max(N, P)
        if MaxSize < 16:
            MaxSize = 16
        k = int(math.floor(math.log(MaxSize) / math.log(2))) - 4
        m = int(math.floor(MaxSize * 2**(-k))) + 1
        NewSize = m * 2**k

        # Agregar filas y columnas de ceros para usar el algoritmo de Strassen
        NewA = [[0.0] * NewSize for _ in range(NewSize)]
        NewB = [[0.0] * NewSize for _ in range(NewSize)]
        AuxResult = [[0.0] * NewSize for _ in range(NewSize)]

        for i in range(N):
            for j in range(P):
                NewA[i][j] = matrizA[i][j]

        for i in range(P):
            for j in range(M):
                NewB[i][j] = matrizB[i][j]

        self.strassen_naiv_step(NewA, NewB, AuxResult, NewSize, m)

        # Extraer el resultado
        for i in range(N):
            for j in range(M):
                matrizC[i][j] = AuxResult[i][j]

    def max(self, N, P):
        return max(N, P) if N < P else N

    def minus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] - B[i][j]

    def plus(self, A, B, Result, N, M):
        for i in range(N):
            for j in range(M):
                Result[i][j] = A[i][j] + B[i][j]

    def strassen_naiv_step(self, A, B, Result, N, m):
        if N % 2 == 0 and N > m:
            NewSize = N // 2

            # Descomponer A y B
            A11 = [row[:NewSize] for row in A[:NewSize]]
            A12 = [row[NewSize:] for row in A[:NewSize]]
            A21 = [row[:NewSize] for row in A[NewSize:]]
            A22 = [row[NewSize:] for row in A[NewSize:]]
            B11 = [row[:NewSize] for row in B[:NewSize]]
            B12 = [row[NewSize:] for row in B[:NewSize]]
            B21 = [row[:NewSize] for row in B[NewSize:]]
            B22 = [row[NewSize:] for row in B[NewSize:]]

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

            self.plus(A11, A22, Helper1, NewSize, NewSize)
            self.plus(B11, B22, Helper2, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, Helper2, Aux1, NewSize, m)

            self.plus(A21, A22, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, B11, Aux2, NewSize, m)

            self.minus(B12, B22, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(A11, Helper1, Aux3, NewSize, m)

            self.minus(B21, B11, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(A22, Helper1, Aux4, NewSize, m)

            self.plus(A11, A12, Helper1, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, B22, Aux5, NewSize, m)

            self.minus(A21, A11, Helper1, NewSize, NewSize)
            self.plus(B11, B12, Helper2, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, Helper2, Aux6, NewSize, m)

            self.minus(A12, A22, Helper1, NewSize, NewSize)
            self.plus(B21, B22, Helper2, NewSize, NewSize)
            self.strassen_naiv_step(Helper1, Helper2, Aux7, NewSize, m)

            self.plus(Aux1, Aux4, ResultPart11, NewSize, NewSize)
            self.minus(ResultPart11, Aux5, ResultPart11, NewSize, NewSize)
            self.plus(ResultPart11, Aux7, ResultPart11, NewSize, NewSize)

            self.plus(Aux3, Aux5, ResultPart12, NewSize, NewSize)

            self.plus(Aux2, Aux4, ResultPart21, NewSize, NewSize)

            self.plus(Aux1, Aux3, ResultPart22, NewSize, NewSize)
            self.minus(ResultPart22, Aux2, ResultPart22, NewSize, NewSize)
            self.plus(ResultPart22, Aux6, ResultPart22, NewSize, NewSize)

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
            self.naiv_standard(A, B, Result, N, N, N)

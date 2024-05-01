import math
from Algoritmos import StrassenNaiv


def StrassenWinograd(matrizA, matrizB, matrizC, N, P, M):
    # Calcula el tamaño máximo entre N, P y M
    MaxSize = maxi(N, P)  # Obtener el máximo entre N y P
    MaxSize = maxi(MaxSize, M)  # Obtener el máximo entre el resultado anterior y M

    # Si el tamaño máximo es menor que 16, se establece como 16
    if MaxSize < 16:
        MaxSize = 16

    # Calcular k y m para el algoritmo de Strassen
    k = int(math.floor(math.log(MaxSize) / math.log(2))) - 4  # Calcular k
    m = int(math.floor(MaxSize * math.pow(2, -k))) + 1  # Calcular m
    NewSize = m * int(math.pow(2, k))  # Calcular el nuevo tamaño para las matrices

    # Crear nuevas matrices con tamaño NewSize y llenarlas con ceros
    NewA = [[0.0] * NewSize for _ in range(NewSize)]  # Crear matriz NewA
    NewB = [[0.0] * NewSize for _ in range(NewSize)]  # Crear matriz NewB
    AuxResult = [[0.0] * NewSize for _ in range(NewSize)]  # Crear matriz AuxResult

    # Copiar los valores de matrizA a NewA
    for i in range(N):  # Recorrer las filas de matrizA
        for j in range(P):  # Recorrer las columnas de matrizA
            NewA[i][j] = matrizA[i][j]  # Copiar el valor de matrizA a NewA

    # Copiar los valores de matrizB a NewB
    for i in range(P):  # Recorrer las filas de matrizB
        for j in range(M):  # Recorrer las columnas de matrizB
            NewB[i][j] = matrizB[i][j]  # Copiar el valor de matrizB a NewB

    # Llamar al método strassen_winograd_step para realizar la multiplicación de matrices
    strassenWinogradStep(NewA, NewB, AuxResult, NewSize, m)

    # Copiar el resultado de la multiplicación a la matrizC
    for i in range(N):  # Recorrer las filas del resultado
        for j in range(M):  # Recorrer las columnas del resultado
            matrizC[i][j] = AuxResult[i][j]  # Copiar el valor del resultado a matrizC


def maxi(N, P):
    # Verifica cuál de los dos valores es mayor
    if N < P:
        return P  # Retorna P si es mayor
    else:
        return N  # Retorna N si es mayor o iguales


def strassenWinogradStep(A, B, Result, N, m):
    # Verifica si N es par y mayor que m para aplicar el algoritmo
    if N % 2 == 0 and N > m:
        NewSize = N // 2  # Calcula el nuevo tamaño

        # Descomponer matrices A y B en submatrices
        A1 = [row[:NewSize] for row in A]
        A2 = [row[NewSize:] for row in A]
        B1 = [row[:NewSize] for row in B]
        B2 = [row[NewSize:] for row in B]

        # Descomponer las submatrices en bloques más pequeños
        A11 = [row[:NewSize] for row in A1]
        A12 = [row[NewSize:] for row in A1]
        A21 = [row[:NewSize] for row in A2]
        A22 = [row[NewSize:] for row in A2]
        B11 = [row[:NewSize] for row in B1]
        B12 = [row[NewSize:] for row in B1]
        B21 = [row[:NewSize] for row in B2]
        B22 = [row[NewSize:] for row in B2]

        # Inicializar matrices para las partes del resultado
        ResultPart11 = [[0.0] * NewSize for _ in range(NewSize)]
        ResultPart12 = [[0.0] * NewSize for _ in range(NewSize)]
        ResultPart21 = [[0.0] * NewSize for _ in range(NewSize)]
        ResultPart22 = [[0.0] * NewSize for _ in range(NewSize)]

        # Inicializar matrices auxiliares y ayudantes
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

        # Calcula las diferencias y sumas necesarias
        minus(A11, A21, A1, NewSize, NewSize)
        minus(A22, A1, A2, NewSize, NewSize)
        minus(B22, B12, B1, NewSize, NewSize)
        plus(B1, B11, B2, NewSize, NewSize)

        # Realiza las llamadas recursivas para los bloques más pequeños
        strassenWinogradStep(A11, B11, Aux1, NewSize, m)
        strassenWinogradStep(A12, B21, Aux2, NewSize, m)
        strassenWinogradStep(A2, B2, Aux3, NewSize, m)
        plus(A21, A22, Helper1, NewSize, NewSize)
        minus(B12, B11, Helper2, NewSize, NewSize)
        strassenWinogradStep(Helper1, Helper2, Aux4, NewSize, m)
        strassenWinogradStep(A1, B1, Aux5, NewSize, m)
        minus(A12, A2, Helper1, NewSize, NewSize)
        strassenWinogradStep(Helper1, B22, Aux6, NewSize, m)
        minus(B21, B2, Helper1, NewSize, NewSize)
        strassenWinogradStep(A22, Helper1, Aux7, NewSize, m)
        plus(Aux1, Aux3, Aux8, NewSize, NewSize)
        plus(Aux8, Aux4, Aux9, NewSize, NewSize)

        # Calcular las partes del resultado final
        plus(Aux1, Aux2, ResultPart11, NewSize, NewSize)
        plus(Aux9, Aux6, ResultPart12, NewSize, NewSize)
        plus(Aux8, Aux5, Helper1, NewSize, NewSize)
        plus(Helper1, Aux7, ResultPart21, NewSize, NewSize)
        plus(Aux9, Aux5, ResultPart22, NewSize, NewSize)

        # Almacenar las partes del resultado en la matriz Result
        for i in range(NewSize):
            for j in range(NewSize):
                Result[i][j] = ResultPart11[i][j]
                Result[i][NewSize + j] = ResultPart12[i][j]
                Result[NewSize + i][j] = ResultPart21[i][j]
                Result[NewSize + i][NewSize + j] = ResultPart22[i][j]
    else:
        # Usar el algoritmo naiv si las condiciones no se cumplen
        StrassenNaiv.naivStandard(A, B, Result, N, N, N)


def minus(A, B, Result, N, M):
    # Iterar sobre las filas
    for i in range(N):
        # Iterar sobre las columnas
        for j in range(M):
            # Restar los elementos correspondientes de A y B
            Result[i][j] = A[i][j] - B[i][j]


def plus(A, B, Result, N, M):
    # Iterar sobre las filas
    for i in range(N):
        # Iterar sobre las columnas
        for j in range(M):
            # Sumar los elementos correspondientes de A y B
            Result[i][j] = A[i][j] + B[i][j]

from Algoritmos import WinogradOriginal
import math
import numpy as np


def WinogradScaled_(A, B, Result, N, P, M):
    # Crear copias escaladas de A y B
    CopyA = np.copy(A)
    CopyB = np.copy(B)

    # Calcular factores de escala
    a = NormInf(A, N, P)
    b = NormInf(B, P, M)
    lambda_val = math.floor(0.5 + math.log(b / a) / math.log(4))

    # Escalar matrices
    MultiplyWithScalar(A, CopyA, N, P, 2 ** lambda_val)
    MultiplyWithScalar(B, CopyB, P, M, 2 ** (-lambda_val))

    # Utilizar Winograd con las matrices escaladas
    WinogradOriginal.WinogradOriginal(CopyA, CopyB, Result, N, P, M)  # Reemplazar con la implementación de WinogradOriginal
    return Result


# Función que multiplica una matriz por un escalar y almacena el resultado en otra matriz
def MultiplyWithScalar(inputMatrix, outputMatrix, rows, cols, scalar):
    for i in range(rows):
        for j in range(cols):
            outputMatrix[i][j] = inputMatrix[i][j] * scalar


# Función que calcula la norma infinito de una matriz
def NormInf(matrix, rows, cols):
    maxNorm = 0.0
    for i in range(rows):
        rowNorm = sum(abs(matrix[i][j]) for j in range(cols))
        maxNorm = max(maxNorm, rowNorm)
    return maxNorm

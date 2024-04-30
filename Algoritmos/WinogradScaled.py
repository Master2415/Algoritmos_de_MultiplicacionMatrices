import numpy as np
from Algoritmos import WinogradOriginal


def WinogradScaled(A, B, Result, N, P, M):
    """
    Multiplica dos matrices utilizando el algoritmo Winograd con escalado.

    Args:
    - A (np.ndarray): Matriz A de tamaño NxP.
    - B (np.ndarray): Matriz B de tamaño PxM.
    - Result (np.ndarray): Matriz resultante de tamaño NxM para almacenar el resultado de la multiplicación.
    - N (int): Número de filas de la matriz A y de la matriz Result.
    - P (int): Número de columnas de la matriz A y número de filas de la matriz B.
    - M (int): Número de columnas de la matriz B y de la matriz Result.

    Returns:
    - None: La función modifica la matriz Result directamente.
    """
    # Crear copias escaladas de A y B
    CopyA = np.zeros((N, P))  # Matriz copia escalada de A
    CopyB = np.zeros((P, M))  # Matriz copia escalada de B

    # Calcular los factores de escala
    a = np.max(np.abs(A))  # Factor de escala para A
    b = np.max(np.abs(B))  # Factor de escala para B
    lambda_val = int(np.floor(0.5 + np.log(b / a) / np.log(4)))  # Calcular lambda según la fórmula del algoritmo

    # Escalar las matrices A y B
    CopyA = A * (2 ** lambda_val)  # Escalar A multiplicando por 2^lambda
    CopyB = B * (2 ** -lambda_val)  # Escalar B multiplicando por 2^-lambda

    # Utilizar el algoritmo de Winograd con las matrices escaladas
    WinogradOriginal.WinogradOriginal(CopyA, CopyB, Result, N, P, M)  # Llamar al algoritmo de Winograd con las matrices escaladas

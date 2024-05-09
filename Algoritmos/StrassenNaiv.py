from Algoritmos import StrassenNaivStep
import math
import numpy as np


def StrassenNaiv_(matrizA, matrizB, matrizC, N, P, M):
    # Variables para cálculos relacionados con el tamaño de las matrices y el método de Strassen
    MaxSize = max(N, P)
    # Si el tamaño máximo es menor que 16, se ajusta a 16 para garantizar que se pueda calcular 'k'
    if MaxSize < 16:
        MaxSize = 16

    # Calcula 'k' para el método de Strassen
    k = int(math.floor(math.log(MaxSize) / math.log(2)) - 4)
    m = int(math.floor(MaxSize * math.pow(2, -k)) + 1)

    # Calcula el nuevo tamaño basado en 'm' y 'k'
    NewSize = m * int(math.pow(2, k))

    # Crea matrices con el nuevo tamaño para usar el algoritmo de Strassen
    NewA = np.zeros((NewSize, NewSize))
    NewB = np.zeros((NewSize, NewSize))
    AuxResult = np.zeros((NewSize, NewSize))

    # Copia los elementos de las matrices originales a las nuevas matrices
    NewA[:N, :P] = matrizA
    NewB[:P, :M] = matrizB

    # Llama al método StrassenNaivStep para realizar la multiplicación con el algoritmo de Strassen
    StrassenNaivStep.strassen_naiv_step(NewA, NewB, AuxResult, NewSize, m)

    # Extrae el resultado de la matriz auxiliar y lo almacena en la matriz resultado
    matrizC[:N, :M] = AuxResult[:N, :M]
    return matrizC


def max(N, P):
    return max(N, P) if N < P else N

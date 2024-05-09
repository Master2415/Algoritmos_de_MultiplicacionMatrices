from Algoritmos import StrassenNaivStep
from Algoritmos import StrassenNaiv
import math
import numpy as np


def StrassenWinograd_(matrizA, matrizB, matrizC, N, P, M):
    MaxSize = StrassenNaiv.max(N, P)
    MaxSize = StrassenNaiv.max(MaxSize, M)
    if MaxSize < 16:
        MaxSize = 16

    k = int(math.floor(math.log(MaxSize) / math.log(2)) - 4)
    m = int(math.floor(MaxSize * math.pow(2, -k)) + 1)
    NewSize = m * int(math.pow(2, k))

    # add zero rows and columns to use Strassen's algorithm
    NewA = np.zeros((NewSize, NewSize))
    NewB = np.zeros((NewSize, NewSize))
    AuxResult = np.zeros((NewSize, NewSize))

    # copy elements from original matrices to new matrices
    NewA[:N, :P] = matrizA
    NewB[:P, :M] = matrizB

    # call StrassenWinogradStep method to perform multiplication using Strassen's algorithm
    StrassenNaivStep.strassen_naiv_step(NewA, NewB, AuxResult, NewSize, m)  # Replace with the implementation of StrassenWinogradStep

    # extract the result
    matrizC[:N, :M] = AuxResult[:N, :M]
    return matrizC


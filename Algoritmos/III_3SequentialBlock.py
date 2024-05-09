import math
import numpy as np


def lll_3SequentialBlock(matrizA, matrizB, size):
    # Calcula el tamaño de bloque basado en la raíz cuadrada del tamaño total.
    bsize = int(math.sqrt(size))
    # Crea una matriz para almacenar el resultado de la multiplicación.
    matrizResultado = np.zeros((size, size))

    # Bucle externo para recorrer la matriz por bloques.
    for i1 in range(0, size, bsize):
        for j1 in range(0, size, bsize):
            for k1 in range(0, size, bsize):
                # Bucle interno para multiplicar los bloques.
                for i in range(i1, min(i1 + bsize, size)):
                    for j in range(j1, min(j1 + bsize, size)):
                        for k in range(k1, min(k1 + bsize, size)):
                            # Multiplica los elementos de los bloques y suma al resultado.
                            matrizResultado[i][j] += matrizA[i][k] * matrizB[k][j]
    return matrizResultado


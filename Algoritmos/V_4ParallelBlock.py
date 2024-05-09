import math
import numpy as np
from concurrent.futures import ThreadPoolExecutor


def v_4ParallelBlock(matrizA, matrizB, size):
    # Calcula el tamaño de bloque basado en la raíz cuadrada del tamaño total.
    bsize = int(math.sqrt(size))
    # Crea una matriz para almacenar el resultado de la multiplicación.
    matrizResultado = np.zeros((size, size))

    # Define una función para realizar la multiplicación por bloques en paralelo
    def multiply_blocks(i1, j1, k1):
        for i in range(i1, min(i1 + bsize, size)):  # Recorre filas del bloque de matrizA
            for j in range(j1, min(j1 + bsize, size)):  # Recorre columnas del bloque de matrizA
                for k in range(k1, min(k1 + bsize, size)):  # Recorre elementos del bloque de matrizA
                    matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]  # Multiplica y suma al resultado

    # Utiliza ThreadPoolExecutor para ejecutar las multiplicaciones en paralelo
    with ThreadPoolExecutor() as executor:
        # Bucle externo para recorrer la matriz por bloques en paralelo.
        for i1 in range(0, size, bsize):  # Recorre filas de la matrizA por bloques
            for j1 in range(0, size, bsize):  # Recorre columnas de la matrizA por bloques
                for k1 in range(0, size, bsize):  # Recorre bloques para la multiplicación
                    executor.submit(multiply_blocks, i1, j1, k1)

    return matrizResultado

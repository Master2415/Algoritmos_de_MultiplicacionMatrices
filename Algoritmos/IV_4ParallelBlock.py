import math
import numpy as np
from concurrent.futures import ThreadPoolExecutor


def lV_4ParallelBlock_(matrizA, matrizB, size):
    # Calcula el tamaño de bloque basado en la raíz cuadrada del tamaño total.
    bsize = int(math.sqrt(size))
    # Crea una matriz para almacenar el resultado de la multiplicación.
    matrizResultado = np.zeros((size, size))

    # Función para procesar un bloque en paralelo
    def process_block(i1):
        for j1 in range(0, size, bsize):  # Recorre columnas de la matrizA por bloques
            for k1 in range(0, size, bsize):  # Recorre bloques para la multiplicación
                # Bucle interno para multiplicar los bloques correspondientes.
                for i in range(i1 * bsize, min((i1 + 1) * bsize, size)):  # Recorre filas del bloque de matrizA
                    for j in range(j1, min(j1 + bsize, size)):  # Recorre columnas del bloque de matrizA
                        for k in range(k1, min(k1 + bsize, size)):  # Recorre elementos del bloque para multiplicación
                            matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]  # Multiplica y suma al resultado

    # Crea un ThreadPoolExecutor para manejar los hilos en paralelo
    with ThreadPoolExecutor(max_workers=size // bsize) as executor:
        # Ejecuta los bloques en paralelo
        executor.map(process_block, range(size // bsize))

    return matrizResultado

import math
import numpy as np
from concurrent.futures import ThreadPoolExecutor


def lV_5EnhancedParallelBlock(matrizA, matrizB, matrizC, size):
    bsize = int(math.sqrt(size))
    matrizResultado = np.zeros((size, size))

    # Función para procesar un bloque en paralelo
    def process_block(start_i, end_i):
        for i1 in range(start_i, end_i, bsize):  # Recorre filas de la matriz A por bloques
            for j1 in range(0, size, bsize):  # Recorre columnas de A por bloques
                for k1 in range(0, size, bsize):  # Recorre bloques para la multiplicación
                    # Bucle interno para multiplicar los bloques correspondientes.
                    for i in range(i1, min(i1 + bsize, end_i)):  # Recorre filas del bloque de A
                        for j in range(j1, min(j1 + bsize, size)):  # Recorre columnas del bloque de A
                            for k in range(k1, min(k1 + bsize, size)):  # Recorre elementos del bloque de A
                                matrizResultado[i][k] += matrizB[i][j] * matrizC[j][k]  # Multiplica y suma al resultado

    # Crea un ThreadPoolExecutor para manejar los hilos en paralelo
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Ejecuta los bloques en paralelo
        executor.submit(process_block, 0, size // 2)  # Primer bloque para la primera mitad de A
        executor.submit(process_block, size // 2, size)  # Segundo bloque para la segunda mitad de A

    return matrizResultado

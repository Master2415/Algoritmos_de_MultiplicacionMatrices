import math
import numpy as np
import os
from concurrent.futures import ThreadPoolExecutor

def lll_ParallelDo(A, B, C, size):
    # Calcula el tamaño de bloque basado en la raíz cuadrada del tamaño total.
    bsize = int(math.sqrt(size))

    # Crea un ThreadPoolExecutor para manejar los hilos.
    executor = ThreadPoolExecutor(max_workers=os.cpu_count())

    # Primer bloque para procesar la primera mitad de la matriz A en paralelo
    def process_block1():
        for i1 in range(0, size // 2, bsize):  # Recorre filas de la primera mitad de A
            for j1 in range(0, size, bsize):  # Recorre columnas de A
                for k1 in range(0, size, bsize):  # Recorre bloques de multiplicación
                    for i in range(i1, min(i1 + bsize, size)):  # Recorre filas del bloque de A
                        for j in range(j1, min(j1 + bsize, size)):  # Recorre columnas del bloque de A
                            for k in range(k1, min(k1 + bsize, size)):  # Recorre elementos del bloque de A
                                A[i][j] += B[i][k] * C[k][j]  # Realiza la multiplicación y suma al resultado

    # Segundo bloque para procesar la segunda mitad de la matriz A en paralelo
    def process_block2():
        for i1 in range(size // 2, size, bsize):  # Recorre filas de la segunda mitad de A
            for j1 in range(0, size, bsize):  # Recorre columnas de A
                for k1 in range(0, size, bsize):  # Recorre bloques de multiplicación
                    for i in range(i1, min(i1 + bsize, size)):  # Recorre filas del bloque de A
                        for j in range(j1, min(j1 + bsize, size)):  # Recorre columnas del bloque de A
                            for k in range(k1, min(k1 + bsize, size)):  # Recorre elementos del bloque de A
                                A[i][j] += B[i][k] * C[k][j]  # Realiza la multiplicación y suma al resultado

    # Ejecuta los bloques de procesamiento en paralelo
    executor.submit(process_block1)
    executor.submit(process_block2)

    # Cierra el ThreadPoolExecutor para detener la ejecución de nuevos hilos y espera a que todos los hilos terminen.
    executor.shutdown(wait=True)

    # Retorna la matriz resultante A después de la multiplicación.
    return A



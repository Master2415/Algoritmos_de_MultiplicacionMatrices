import math
import numpy as np
import threading
import multiprocessing


def lll_4ParallelBlock(matrizA, matrizB, size):
    # Calcula el tamaño de bloque basado en la raíz cuadrada del tamaño total.
    bsize = int(math.sqrt(size))
    # Crea una matriz para almacenar el resultado de la multiplicación.
    matrizResultado = np.zeros((size, size))

    # Función que ejecuta la multiplicación de bloques en paralelo
    def multiplicar_bloques(threadIndex):
        nonlocal matrizResultado
        for i1 in range(threadIndex * bsize, size, bsize * threads_count):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                matrizResultado[i][j] += matrizA[i][k] * matrizB[k][j]

    # Obtiene la cantidad de núcleos de procesamiento disponibles
    threads_count = min(threading.active_count(), multiprocessing.cpu_count())
    threads = []

    # Inicia los hilos para procesamiento paralelo
    for t in range(threads_count):
        thread = threading.Thread(target=multiplicar_bloques, args=(t,))
        thread.start()  # Inicia el hilo
        threads.append(thread)

    # Espera a que todos los hilos terminen su trabajo
    for thread in threads:
        thread.join()  # Espera a que el hilo termine

    return matrizResultado


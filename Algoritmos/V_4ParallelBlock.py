import numpy as np
from multiprocessing import Pool


class V_4ParallelBlock:
    def v_4_parallel_block(self, matrizA, matrizB, size):
        # Calcular el tamaño de bloque
        bsize = int(np.sqrt(size))
        # Inicializar la matriz resultado con ceros
        matrizResultado = np.zeros((size, size))

        def multiply_block(i1):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                # Calcular el producto y sumarlo a la matriz resultado
                                matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]

        # Crear un pool de procesos para ejecutar las multiplicaciones de bloques en paralelo
        with Pool() as pool:
            pool.map(multiply_block, range(0, size, bsize))

        return matrizResultado

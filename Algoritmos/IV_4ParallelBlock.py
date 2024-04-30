import math
from concurrent.futures import ThreadPoolExecutor

class IV_4ParallelBlock:
    def lV_4_parallel_block(self, matrizA, matrizB, size):
        # Calcula el tamaño de bloque
        bsize = int(math.sqrt(size))
        # Crea la matriz de resultados
        matrizResultado = [[0.0] * size for _ in range(size)]

        def block_multiply(i1):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1 * bsize, min((i1 + 1) * bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]

        # Usando ThreadPoolExecutor para ejecutar los bloques en paralelo
        with ThreadPoolExecutor() as executor:
            executor.map(block_multiply, range(size // bsize))

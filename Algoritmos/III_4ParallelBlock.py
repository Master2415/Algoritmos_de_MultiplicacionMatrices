import math
from multiprocessing import Pool

class III_4ParallelBlock:
    def lll_4_parallel_block(self, matrizA, matrizB, size):
        # Calcula el tamaño de bloque
        bsize = int(math.sqrt(size))
        # Crea la matriz de resultados
        matrizResultado = [[0.0] * size for _ in range(size)]

        # Define una función para procesar un bloque
        def process_block(i1):
            for i1 in range(0, size, bsize):
                for j1 in range(0, size, bsize):
                    for k1 in range(0, size, bsize):
                        # Itera dentro de cada bloque
                        for i in range(i1, min(i1 + bsize, size)):
                            for j in range(j1, min(j1 + bsize, size)):
                                for k in range(k1, min(k1 + bsize, size)):
                                    # Calcula la multiplicación de matrices en cada elemento
                                    matrizResultado[i][j] += matrizA[i][k] * matrizB[k][j]

        # Define el número de procesos a utilizar (puedes ajustar esto según tu máquina)
        num_processes = 4  # Ejemplo: utilizar 4 procesos

        # Crea un pool de procesos y ejecuta la función de procesamiento para cada bloque
        with Pool(num_processes) as pool:
            pool.map(process_block, range(num_processes))

import math


class IV_3SequentialBlock:
    def lV_3_sequential_block(self, matrizA, matrizB, size):
        # Calcula el tamaño de bloque
        bsize = int(math.sqrt(size))
        # Crea la matriz de resultados
        matrizResultado = [[0.0] * size for _ in range(size)]

        # Itera sobre los bloques de la matriz
        for i1 in range(0, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    # Itera dentro de cada bloque
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                # Calcula la multiplicación de matrices en cada elemento
                                matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]

import numpy as np


class V_3SequentialBlock:
    def v_3_sequential_block(self, matrizA, matrizB):
        # Obtener el tamaño de la matriz
        size = len(matrizA)
        # Calcular el tamaño de bloque
        bsize = int(np.sqrt(size))
        # Inicializar la matriz resultado con ceros
        matrizResultado = np.zeros((size, size))

        # Iterar sobre los bloques de la matriz
        for i1 in range(0, size, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    # Iterar dentro de cada bloque
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                # Calcular el producto y sumarlo a la matriz resultado
                                matrizResultado[i][k] += matrizA[i][j] * matrizB[j][k]

        return matrizResultado

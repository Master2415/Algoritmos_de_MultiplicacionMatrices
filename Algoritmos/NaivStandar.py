class NaivStandar:
    def naiv_standard(self, matrizA, matrizB, matrizC, N, P, M):
        # Recorre cada fila de la matriz A
        for i in range(N):
            # Recorre cada columna de la matriz B
            for j in range(M):
                aux = 0.0
                # Multiplica y suma los elementos correspondientes de A y B
                for k in range(P):
                    aux += matrizA[i][k] * matrizB[k][j]
                # Asigna el resultado a la posición correspondiente en la matriz C
                matrizC[i][j] = aux

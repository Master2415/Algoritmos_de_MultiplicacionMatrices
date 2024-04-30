class NaivLoopUnrollingTwo:
    def NaivLoopUnrollingTwo(self, matrizA, matrizB, matrizC, N, P, M):
        i, j, k = 0, 0, 0
        aux = 0.0
        if P % 2 == 0:
            for i in range(N):
                for j in range(M):
                    aux = 0.0
                    for k in range(0, P, 2):
                        aux += matrizA[i][k] * matrizB[k][j] + matrizA[i][k + 1] * matrizB[k + 1][j]
                    matrizC[i][j] = aux
        else:
            PP = P - 1
            for i in range(N):
                for j in range(M):
                    aux = 0.0
                    for k in range(0, PP, 2):
                        aux += matrizA[i][k] * matrizB[k][j] + matrizA[i][k + 1] * matrizB[k + 1][j]
                    matrizC[i][j] = aux + matrizA[i][PP] * matrizB[PP][j]

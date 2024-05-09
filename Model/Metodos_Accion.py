import numpy as np
from Algoritmos import NaivOnArray
from Algoritmos import NaivLoopUnrollingTwo
from Algoritmos import NaivLoopUnrollingFour
from Algoritmos import WinogradOriginal
from Algoritmos import WinogradScaled
from Algoritmos import StrassenNaiv
from Algoritmos import StrassenWinograd
from Algoritmos import III_3SequentialBlock
from Algoritmos import III_4ParallelBlock
from Algoritmos import III_5_Enhanced_Parallel_Block
from Algoritmos import IV_3SequentialBlock
from Algoritmos import IV_4ParallelBlock
from Algoritmos import IV_5_Enhanced_Parallel_Block
from Algoritmos import V_3SequentialBlock
from Algoritmos import V_4ParallelBlock


def x_naiv_on_array():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = NaivOnArray.NaivOnArray_(matriz1, matriz2, matrizC, potencia, potencia, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_NaivLoopUnrollingTwo():
    for i in range(1, 9):
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultadoMultiplicacion = NaivLoopUnrollingTwo.NaivLoopUnrollingTwo(matriz1, matriz2, matrizC, potencia,
                                                                            potencia, potencia)


def x_NaivLoopUnrollingFour():
    for i in range(1, 9):
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultadoMultiplicacion = NaivLoopUnrollingFour.NaivLoopUnrollingFour(matriz1, matriz2, matrizC, potencia,
                                                                              potencia, potencia)


def x_WinogradOriginal():
    for i in range(1, 9):
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultadoMultiplicacion = WinogradOriginal.WinogradOriginal(matriz1, matriz2, matrizC, potencia, potencia,
                                                                    potencia)


def x_WinogradScaled():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = WinogradScaled.WinogradScaled_(matriz1, matriz2, matrizC, potencia, potencia, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_StrassenNaiv():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = StrassenNaiv.StrassenNaiv_(matriz1, matriz2, matrizC, potencia, potencia, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_StrassenWinograd():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = StrassenWinograd.StrassenWinograd_(matriz1, matriz2, matrizC, potencia, potencia,
                                                                      potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_lll_3SequentialBlock():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = III_3SequentialBlock.lll_3SequentialBlock(matriz1, matriz2, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_lll_4ParallelBlock():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = III_4ParallelBlock.lll_4ParallelBlock(matriz1, matriz2, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_III_5_Enhanced_Parallel_Block():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = III_5_Enhanced_Parallel_Block.lll_ParallelDo(matriz1, matriz2, matrizC, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_lV_3SequentialBlock_():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = IV_3SequentialBlock.lV_3SequentialBlock_(matriz1, matriz2, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_IV_4ParallelBlock():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = IV_4ParallelBlock.lV_4ParallelBlock_(matriz1, matriz2, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_IV_5_Enhanced_Parallel_Block():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = IV_5_Enhanced_Parallel_Block.lV_5EnhancedParallelBlock(matriz1, matriz2,matrizC, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_v_3SequentialBlock():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = V_3SequentialBlock.v_3SequentialBlock(matriz1, matriz2, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""


def x_v_4ParallelBlock():
    for i in range(1, 9):
        # Leer las dos matrices desde archivos
        matriz1 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.1.txt')
        matriz2 = np.loadtxt(f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {i}.2.txt')
        potencia = 2 ** i
        matrizC = np.zeros((potencia, potencia))

        resultado_multiplicacion = V_4ParallelBlock.v_4ParallelBlock(matriz1, matriz2, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""
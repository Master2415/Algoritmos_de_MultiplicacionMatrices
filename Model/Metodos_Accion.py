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


def run_metodos():
    # Con este metodo podemos verificar el resultado de las multiplicaciones, se debe quitar el comentario a cada metodo
    prueba_NaivOnArray()
    prueba_NaivLoopUnrollingTwo()
    prueba_NaivLoopUnrollingFour()
    prueba_WinogradOriginal()
    prueba_WinogradScaled()
    prueba_StrassenNaiv()
    prueba_StrassenWinograd()
    prueba_lll_3SequentialBlock()
    prueba_lll_4SequentialBlock()
    prueba_lll_5SequentialBlock()
    prueba_lV_3SequentialBlock()
    prueba_lV_4SequentialBlock()
    prueba_llV_5EnhancedParallelBlock()
    prueba_v_3SequentialBlock()
    prueba_v_4ParallelBlock()


matriz1_prueba = np.array([
    [1.0, 2.0, 3.0, 4.0],
    [5.0, 6.0, 7.0, 8.0],
    [9.0, 10.0, 11.0, 12.0],
    [13.0, 14.0, 15.0, 16.0]
])

matriz2_prueba = np.array([
    [0.5, 1.5, 2.5, 3.5],
    [4.5, 5.5, 6.5, 7.5],
    [8.5, 9.5, 10.5, 11.5],
    [12.5, 13.5, 14.5, 15.5]
])

zicePrueba = 4
matrizCPrueba = np.zeros((zicePrueba, zicePrueba))


def prueba_NaivOnArray():
    resultadoPrueba = NaivOnArray.NaivOnArray_(matriz1_prueba, matriz2_prueba, matrizCPrueba, zicePrueba, zicePrueba,
                                               zicePrueba)
    numero_resultado = 'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/NaivOnArray.txt'
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_NaivLoopUnrollingTwo():
    resultadoPrueba = NaivLoopUnrollingTwo.NaivLoopUnrollingTwo(matriz1_prueba, matriz2_prueba, matrizCPrueba,
                                                                zicePrueba, zicePrueba,
                                                                zicePrueba)
    numero_resultado = 'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/NaivLoopUnrollingTwo.txt'
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_NaivLoopUnrollingFour():
    resultadoPrueba = NaivLoopUnrollingFour.NaivLoopUnrollingFour(matriz1_prueba, matriz2_prueba, matrizCPrueba,
                                                                  zicePrueba, zicePrueba,
                                                                  zicePrueba)
    numero_resultado = 'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/NaivLoopUnrollingFour.txt'
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_WinogradOriginal():
    resultadoPrueba = WinogradOriginal.WinogradOriginal(matriz1_prueba, matriz2_prueba, matrizCPrueba,
                                                        zicePrueba, zicePrueba,
                                                        zicePrueba)
    numero_resultado = ('C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados'
                        '/WinogradOriginal.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_WinogradScaled():
    resultadoPrueba = WinogradScaled.WinogradScaled_(matriz1_prueba, matriz2_prueba, matrizCPrueba,
                                                     zicePrueba, zicePrueba,
                                                     zicePrueba)
    numero_resultado = ('C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/WinogradScaled'
                        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_StrassenNaiv():
    resultadoPrueba = StrassenNaiv.StrassenNaiv_(matriz1_prueba, matriz2_prueba, matrizCPrueba,
                                                 zicePrueba, zicePrueba,
                                                 zicePrueba)
    numero_resultado = ('C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/StrassenNaiv'
                        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_StrassenWinograd():
    resultadoPrueba = StrassenWinograd.StrassenWinograd_(matriz1_prueba, matriz2_prueba, matrizCPrueba,
                                                         zicePrueba, zicePrueba,
                                                         zicePrueba)
    numero_resultado = ('C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/StrassenWinograd'
                        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_lll_3SequentialBlock():
    resultadoPrueba = III_3SequentialBlock.lll_3SequentialBlock(matriz1_prueba, matriz2_prueba,
                                                                zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/III_3SequentialBlock'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_lll_4SequentialBlock():
    resultadoPrueba = III_4ParallelBlock.lll_4ParallelBlock(matriz1_prueba, matriz2_prueba,
                                                            zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/III_4ParallelBlock'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_lll_5SequentialBlock():
    resultadoPrueba = III_5_Enhanced_Parallel_Block.lll_ParallelDo(matriz1_prueba, matriz2_prueba, matrizCPrueba,
                                                                   zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/III_5_Enhanced_Parallel_Block'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_lV_3SequentialBlock():
    resultadoPrueba = IV_3SequentialBlock.lV_3SequentialBlock_(matriz1_prueba, matriz2_prueba,
                                                               zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/IV_3SequentialBlock'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_lV_4SequentialBlock():
    resultadoPrueba = IV_4ParallelBlock.lV_4ParallelBlock_(matriz1_prueba, matriz2_prueba,
                                                           zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/IV_4ParallelBlock'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_llV_5EnhancedParallelBlock():
    resultadoPrueba = IV_5_Enhanced_Parallel_Block.lV_5EnhancedParallelBlock(matriz1_prueba, matriz2_prueba,
                                                                             matrizCPrueba,
                                                                             zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/IV_5_Enhanced_Parallel_Block'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_v_3SequentialBlock():
    resultadoPrueba = V_4ParallelBlock.v_4ParallelBlock(matriz1_prueba, matriz2_prueba,
                                                        zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/V_4ParallelBlock'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


def prueba_v_4ParallelBlock():
    resultadoPrueba = V_4ParallelBlock.v_4ParallelBlock(matriz1_prueba, matriz2_prueba,
                                                        zicePrueba)
    numero_resultado = (
        'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/V_4ParallelBlock'
        '.txt')
    np.savetxt(numero_resultado, resultadoPrueba, fmt='%.2f')


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

        resultado_multiplicacion = WinogradScaled.WinogradScaled_(matriz1, matriz2, matrizC, potencia, potencia,
                                                                  potencia)

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

        resultado_multiplicacion = IV_5_Enhanced_Parallel_Block.lV_5EnhancedParallelBlock(matriz1, matriz2, matrizC,
                                                                                          potencia)

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

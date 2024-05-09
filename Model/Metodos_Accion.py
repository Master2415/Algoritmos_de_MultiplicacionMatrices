import numpy as np
from Algoritmos import NaivOnArray
from Algoritmos import NaivLoopUnrollingTwo
from Algoritmos import NaivLoopUnrollingFour
from Algoritmos import WinogradOriginal
from Algoritmos import WinogradScaled
from Algoritmos import StrassenNaiv
from Algoritmos import StrassenWinograd


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

        resultado_multiplicacion = StrassenWinograd.StrassenWinograd_(matriz1, matriz2, matrizC, potencia, potencia, potencia)

        """numero_resultado = f'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/resultados/ {i}.resultado.txt'
        np.savetxt(numero_resultado, resultado_multiplicacion)"""




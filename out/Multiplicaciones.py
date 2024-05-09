import time
from Algoritmos import (NaivOnArray,
                        NaivLoopUnrollingTwo,
                        NaivLoopUnrollingFour,
                        WinogradOriginal,
                        WinogradScaled,
                        StrassenNaiv,
                        StrassenWinograd,
                        III_3SequentialBlock,
                        III_4ParallelBlock)
from Model import Crear


def x_naivOnArray():
    # Crear un diccionario para almacenar las matrices que se van a multiplicar
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)
            matrices_por_numero[num].append(matriz)

    multiplicador = NaivOnArray
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.NaivOnArray(matriz_A, matriz_B, matriz_C, N, P, M)

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_NaivLoopUnrollingTwo():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)
            matrices_por_numero[num].append(matriz)

    multiplicador = NaivLoopUnrollingTwo
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.NaivLoopUnrollingTwo(matriz_A, matriz_B, matriz_C, N, P, M)

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_NaivLoopUnrollingFour():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)
            matrices_por_numero[num].append(matriz)

    multiplicador = NaivLoopUnrollingFour
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.NaivLoopUnrollingFour(matriz_A, matriz_B, matriz_C, N, P, M)

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_WinogradOriginal():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)
            matrices_por_numero[num].append(matriz)

    multiplicador = WinogradOriginal
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.WinogradOriginal(matriz_A, matriz_B, matriz_C, N, P, M)

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_WinogradScaled():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)
            matrices_por_numero[num].append(matriz)

    multiplicador = WinogradScaled
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.WinogradScaled(matriz_A, matriz_B, matriz_C, N, P, M)

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_StrassenNaiv():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)
            matrices_por_numero[num].append(matriz)

    multiplicador = StrassenNaiv
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.StrassenNaiv(matriz_A, matriz_B, matriz_C, N, P, M)

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_StrassenWinograd():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 5):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)
            matrices_por_numero[num].append(matriz)

    multiplicador = StrassenWinograd
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.StrassenWinograd(matriz_A, matriz_B, matriz_C, N, P, M)

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_lll_3_sequential_block():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)  # Supongo que tienes una función para leer la matriz
            matrices_por_numero[num].append(matriz)

    multiplicador = III_3SequentialBlock
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.lll_3_sequential_block(matriz_A, matriz_B, N)  # Llama a la función multiplicadora

            # Imprimir el resultado
            """print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""


def x_lll_4_sequential_block():
    matrices_por_numero = {}

    # Leer las matrices desde archivos y organizarlas por número
    for num in range(1, 9):  # matrices con números del 1 al 8
        matrices_por_numero[num] = []
        for sub_num in range(1, 3):  # Suponemos que hay sub-matrices con números del 1 al 2
            ruta_matriz = f"C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Persistencia/matriz {num}.{sub_num}.txt"
            matriz = Crear.leer_matriz(ruta_matriz)  # Supongo que tienes una función para leer la matriz
            matrices_por_numero[num].append(matriz)

    multiplicador = III_4ParallelBlock
    start_time = time.time()  # Marcar el tiempo de inicio

    for num in matrices_por_numero:
        matrices = matrices_por_numero[num]
        for i in range(len(matrices) - 1):
            matriz_A = matrices[i]
            matriz_B = matrices[i + 1]
            N = len(matriz_A)
            P = len(matriz_A[0])
            M = len(matriz_B[0])
            matriz_C = [[0 for _ in range(M)] for _ in range(N)]
            multiplicador.lll_4_parallel_block(matriz_A, matriz_B, N)  # Llama a la función multiplicadora

            # Imprimir el resultado
            print(f"Resultado de multiplicar matriz {num}.{i + 1} con matriz {num}.{i + 2}:")
            """for fila in matriz_C:
                print(fila)
            print()

            end_time = time.time()  # Marcar el tiempo de finalización
            elapsed_time_ms = (end_time - start_time) * 1000  # Calcular el tiempo transcurrido en milisegundos
            print(f"Tiempo transcurrido: {elapsed_time_ms:.2f} ms")"""
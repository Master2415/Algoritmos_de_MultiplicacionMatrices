import time
import matplotlib.pyplot as plt
from out import Multiplicaciones


def medir_Tiempos():
    # Medir el tiempo para NaivOnArray
    start_time_naivOnArray = time.time()
    Multiplicaciones.x_naivOnArray()
    end_time_naivOnArray = time.time()
    elapsed_time_naivOnArray = (end_time_naivOnArray - start_time_naivOnArray) * 1000

    # Medir el tiempo para NaivLoopUnrollingTwo
    start_time_NaivLoopUnrollingTwo = time.time()
    Multiplicaciones.x_NaivLoopUnrollingTwo()
    end_time_NaivLoopUnrollingTwo = time.time()
    elapsed_time_NaivLoopUnrollingTwo = (end_time_NaivLoopUnrollingTwo - start_time_NaivLoopUnrollingTwo) * 1000

    # Medir el tiempo para NaivLoopUnrollingFour
    start_time_NaivLoopUnrollingFour = time.time()
    Multiplicaciones.x_NaivLoopUnrollingFour()
    end_time_NaivLoopUnrollingFour = time.time()
    elapsed_time_NaivLoopUnrollingFour = (end_time_NaivLoopUnrollingFour - start_time_NaivLoopUnrollingFour) * 1000

    # Medir el tiempo para WinogradOriginal
    start_time_WinogradOriginal = time.time()
    Multiplicaciones.x_WinogradOriginal()
    end_time_WinogradOriginal = time.time()
    elapsed_time_WinogradOriginal = (end_time_WinogradOriginal - start_time_WinogradOriginal) * 1000

    # Medir el tiempo para WinogradScaled
    start_time_WinogradScaled = time.time()
    Multiplicaciones.x_WinogradScaled()
    end_time_WinogradScaled = time.time()
    elapsed_time_WinogradScaled = (end_time_WinogradScaled - start_time_WinogradScaled) * 1000

    # Medir el tiempo para StrassenNaiv
    start_time_StrassenNaiv = time.time()
    Multiplicaciones.x_StrassenNaiv()
    end_time_StrassenNaiv = time.time()
    elapsed_time_StrassenNaiv = (end_time_StrassenNaiv - start_time_StrassenNaiv) * 1000

    # Medir el tiempo para StrassenWinograd
    start_time_StrassenWinograd = time.time()
    Multiplicaciones.x_StrassenWinograd()
    end_time_StrassenWinograd = time.time()
    elapsed_time_StrassenWinograd = (end_time_StrassenWinograd - start_time_StrassenWinograd) * 1000

    # Medir el tiempo para lll_3_sequential_block
    start_time_lll_3_sequential_block = time.time()
    Multiplicaciones.x_lll_3_sequential_block()
    end_time_lll_3_sequential_block = time.time()
    elapsed_time_lll_3_sequential_block = (end_time_lll_3_sequential_block - start_time_lll_3_sequential_block) * 1000

    """""# Medir el tiempo para lll_4_parallel_block
    start_time_lll_4_parallel_block = time.time()
    Multiplicaciones.x_lll_4_sequential_block()
    end_time_lll_4_parallel_block = time.time()
    elapsed_time_lll_4_parallel_block = (end_time_lll_4_parallel_block - start_time_lll_4_parallel_block) * 1000"""""

    return (elapsed_time_naivOnArray,
            elapsed_time_NaivLoopUnrollingTwo,
            elapsed_time_NaivLoopUnrollingFour,
            elapsed_time_WinogradOriginal,
            elapsed_time_WinogradScaled,
            elapsed_time_StrassenNaiv,
            elapsed_time_StrassenWinograd,
            elapsed_time_lll_3_sequential_block)


def mostrar_en_consola(elapsed_time_naivOnArray,
                       elapsed_time_NaivLoopUnrollingTwo,
                       elapsed_time_NaivLoopUnrollingFour,
                       elapsed_time_WinogradOriginal,
                       elapsed_time_WinogradScaled,
                       elapsed_time_StrassenNaiv,
                       elapsed_time_StrassenWinograd,
                       elapsed_time_lll_3_sequential_block):
    # Mostrar los tiempos en la consola
    print(f"Tiempo de ejecución para 1. NaivOnArray: {elapsed_time_naivOnArray:.2f} ms")
    print(f"Tiempo de ejecución para 2. NaivLoopUnrollingTwo: {elapsed_time_NaivLoopUnrollingTwo:.2f} ms")
    print(f"Tiempo de ejecución para 3. NaivLoopUnrollingFour: {elapsed_time_NaivLoopUnrollingFour:.2f} ms")
    print(f"Tiempo de ejecución para 4. WinogradOriginal: {elapsed_time_WinogradOriginal:.2f} ms")
    print(f"Tiempo de ejecución para 5. WinogradScaled: {elapsed_time_WinogradScaled:.2f} ms")
    print(f"Tiempo de ejecución para 6. StrassenNaiv: {elapsed_time_StrassenNaiv:.2f} ms")
    print(f"Tiempo de ejecución para 7. StrassenWinograd: {elapsed_time_StrassenWinograd:.2f} ms")
    print(f"Tiempo de ejecución para 8. lll_3_sequential_block: {elapsed_time_lll_3_sequential_block:.2f} ms")


def mostrar_Graficas(elapsed_time_naivOnArray,
                     elapsed_time_NaivLoopUnrollingTwo,
                     elapsed_time_NaivLoopUnrollingFour,
                     elapsed_time_WinogradOriginal,
                     elapsed_time_WinogradScaled,
                     elapsed_time_StrassenNaiv,
                     elapsed_time_StrassenWinograd,
                     elapsed_time_lll_3_sequential_block):

    # Graficar los tiempos
    methods = ['1', '2', '3', '4', '5', '6', '7', '8']
    times = [elapsed_time_naivOnArray,
             elapsed_time_NaivLoopUnrollingTwo,
             elapsed_time_NaivLoopUnrollingFour,
             elapsed_time_WinogradOriginal,
             elapsed_time_WinogradScaled,
             elapsed_time_StrassenNaiv,
             elapsed_time_StrassenWinograd,
             elapsed_time_lll_3_sequential_block]
    plt.bar(methods, times)
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.title('Comparación de tiempos de ejecución')
    plt.show()



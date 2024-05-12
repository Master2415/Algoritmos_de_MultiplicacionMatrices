
import time
from Model import Metodos_Accion


def run_Tiempo_txt():
    guardarTiempo("NaivOnArray_Python")
    guardarTiempo("NaivLoopUnrollingTwo_Python")
    guardarTiempo("NaivLoopUnrollingFour_Python")
    guardarTiempo("WinogradOriginal_Python")
    guardarTiempo("WinogradScaled_Python")
    guardarTiempo("StrassenNaiv_Python")
    guardarTiempo("StrassenWinograd_Python")
    guardarTiempo("lll_3SequentialBlock_Python")
    guardarTiempo("lll_4ParallelBlock_Python")
    guardarTiempo("III_5_Enhanced_Parallel_Block_Python")
    guardarTiempo("lV_3SequentialBlock_Python")
    guardarTiempo("lV_4ParallelBlock_Python")
    guardarTiempo("lV_5EnhancedParallelBlock_Python")
    guardarTiempo("V_3SequentialBlock_Python")
    guardarTiempo("V_4ParallelBlock_Python")


def guardarTiempo(nombre_metodo):
    # Con este metodo Guardamos en un txt el tiempo registrado de cada metodo
    inicio_tiempo = time.time_ns()
    # Simulando el llamado a los métodos de metodosAccion
    if nombre_metodo == "NaivOnArray_Python":
        Metodos_Accion.x_naiv_on_array()
    elif nombre_metodo == "NaivLoopUnrollingTwo_Python":
        Metodos_Accion.x_NaivLoopUnrollingTwo()
    elif nombre_metodo == "NaivLoopUnrollingFour_Python":
        Metodos_Accion.x_NaivLoopUnrollingFour()
    elif nombre_metodo == "WinogradOriginal_Python":
        Metodos_Accion.x_WinogradOriginal()
    elif nombre_metodo == "WinogradScaled_Python":
        Metodos_Accion.x_WinogradScaled()
    elif nombre_metodo == "StrassenNaiv_Python":
        Metodos_Accion.x_StrassenNaiv()
    elif nombre_metodo == "StrassenWinograd_Python":
        Metodos_Accion.x_StrassenWinograd()
    elif nombre_metodo == "lll_3SequentialBlock_Python":
        Metodos_Accion.x_lll_3SequentialBlock()
    elif nombre_metodo == "lll_4ParallelBlock_Python":
        Metodos_Accion.x_lll_4ParallelBlock()
    elif nombre_metodo == "III_5_Enhanced_Parallel_Block_Python":
        Metodos_Accion.x_III_5_Enhanced_Parallel_Block()
    elif nombre_metodo == "lV_3SequentialBlock_Python":
        Metodos_Accion.x_lV_3SequentialBlock_()
    elif nombre_metodo == "lV_4ParallelBlock_Python":
        Metodos_Accion.x_IV_4ParallelBlock()
    elif nombre_metodo == "lV_5EnhancedParallelBlock_Python":
        Metodos_Accion.x_IV_5_Enhanced_Parallel_Block()
    elif nombre_metodo == "V_3SequentialBlock_Python":
        Metodos_Accion.x_v_3SequentialBlock()
    elif nombre_metodo == "V_4ParallelBlock_Python":
        Metodos_Accion.x_v_4ParallelBlock()
    else:
        print("Nombre de método no válido")
        return

    fin_tiempo = time.time_ns()
    resultado = fin_tiempo - inicio_tiempo

    # Guardar el resultado en el archivo
    with open("C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Tiempo_Registrado/tiempos.txt", "a") as file:
        file.write(f"{resultado}: {nombre_metodo}\n")


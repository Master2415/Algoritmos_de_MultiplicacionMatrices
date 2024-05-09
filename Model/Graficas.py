import matplotlib.pyplot as plt
from datetime import datetime
from Model import Metodos_Accion


def run_Tiempo_Graficas():
    try:
        generarGrafica()
    except Exception as e:
        print(f"Error al generar la gráfica: {str(e)}")


def generarGrafica():
    # Crear el dataset para almacenar los tiempos de ejecución
    metodos = [
        "NaivOnArray", "NaivLoopUnrollingTwo", "NaivLoopUnrollingFour", "WinogradOriginal", "WinogradScaled",
        "StrassenNaiv", "StrassenWinograd", "III.3 Sequential block", "III.4 Parallel Block",
        "III.5 Enhanced Parallel Block", "IV.3 Sequential block", "IV.4 Parallel Block", "IV.5 Enhanced Parallel Block",
        "V.3 Sequential block", "V.4 Parallel Block"
    ]
    tiempos = []

    for metodo in metodos:
        tiempo_metodo = obtenerTiempo(lambda: ejecutar_metodo(metodo))
        tiempos.append(tiempo_metodo)
        print(f"Tiempo {metodo}: {tiempo_metodo} ns")

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.barh(metodos, tiempos, color='gray')
    plt.xlabel('Tiempo (nanosegundos)')
    plt.title('Tiempos de ejecución de métodos')
    plt.gca().invert_yaxis()  # Invertir el eje y para que el método más rápido esté arriba
    plt.show()


def ejecutar_metodo(metodo):
    try:
        if metodo == "NaivOnArray":
            Metodos_Accion.x_naiv_on_array()
        elif metodo == "NaivLoopUnrollingTwo":
            Metodos_Accion.x_NaivLoopUnrollingTwo()
        elif metodo == "NaivLoopUnrollingFour":
            Metodos_Accion.x_NaivLoopUnrollingFour()
        elif metodo == "WinogradOriginal":
            Metodos_Accion.x_WinogradOriginal()
        elif metodo == "WinogradScaled":
            Metodos_Accion.x_WinogradScaled()
        elif metodo == "StrassenNaiv":
            Metodos_Accion.x_StrassenNaiv()
        elif metodo == "StrassenWinograd":
            Metodos_Accion.x_StrassenWinograd()
        elif metodo == "III.3 Sequential block":
            Metodos_Accion.x_lll_3SequentialBlock()
        elif metodo == "III.4 Parallel Block":
            Metodos_Accion.x_lll_4ParallelBlock()
        elif metodo == "III.5 Enhanced Parallel Block":
            Metodos_Accion.x_III_5_Enhanced_Parallel_Block()
        elif metodo == "IV.3 Sequential block":
            Metodos_Accion.x_lV_3SequentialBlock_()
        elif metodo == "IV.4 Parallel Block":
            Metodos_Accion.x_IV_4ParallelBlock()
        elif metodo == "IV.5 Enhanced Parallel Block":
            Metodos_Accion.x_IV_5_Enhanced_Parallel_Block()
        elif metodo == "V.3 Sequential block":
            Metodos_Accion.x_v_3SequentialBlock()
        elif metodo == "V.4 Parallel Block":
            Metodos_Accion.x_v_4ParallelBlock()
    except Exception as e:
            raise RuntimeError(str(e))


def obtenerTiempo(metodo):
    inicio = datetime.now()
    metodo()
    fin = datetime.now()
    return (fin - inicio).total_seconds() * 1e9  # Convertir segundos a nanosegundos

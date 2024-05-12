from Model.Crear import crear_matriz_main
from Model.Graficas import run_Tiempo_Graficas
from Model.Metodos_Accion import run_metodos
from Model.Metodos_Tiempo import run_Tiempo_txt



def main():
    run()


def run():
    """crear_matriz_main()"""  # Creamos las matrices
    run_metodos() # Llamado para guardar el resultado de las multiplicaciones
    # run_Tiempo_Graficas() # Generamos la graficas obtenidas de la duracion por tiempo
    # run_Tiempo_txt()  # Se ejecuta el guardado de tiempos en txt


main()

import random


def crear_matriz_main():
    """
    Crea y guarda matrices con potencias de 2 en archivos de texto.
    Llama a la función 'crear_matriz' para generar las matrices y guardarlas en archivos.
    """
    for i in range(1, 9):
        potencia = 2 ** i
        for j in range(1, 3):
            crear_matriz(f"{i}.{j}", potencia)


def crear_matriz(numero_matriz, n):
    """
    Crea una matriz de tamaño n x n con valores aleatorios y la guarda en un archivo.

    Parámetros:
    numero_matriz (str): Nombre para la matriz y el archivo.
    n (int): Tamaño de la matriz.
    """
    matriz = [[random.randint(0, 999999) for _ in range(n)] for _ in range(n)]
    guardar_matrices(matriz, numero_matriz)


def guardar_matrices(matriz, numero_matriz):
    """
    Guarda una matriz en un archivo de texto.

    Parámetros:
    matriz (list): La matriz a guardar.
    numero_matriz (str): Nombre para el archivo de la matriz.
    """
    matriz_escrita = "\n".join([" ".join(map(str, fila)) for fila in matriz])
    guardar_archivo(f"C:/ALL/Codigos/WS_Python/WS/ProyectoAnalisis/Persistencia/matriz {numero_matriz}.txt",
                    matriz_escrita, False)


def guardar_archivo(ruta, contenido, flag_anexar_contenido):
    """
    Guarda el contenido en un archivo en la ruta especificada.
    Parámetros:
    ruta (str): Ruta del archivo.
    contenido (str): Contenido a guardar.
    flag_anexar_contenido (bool): Indica si se debe anexar el contenido al archivo existente.
    """
    with open(ruta, "a" if flag_anexar_contenido else "w") as archivo:
        archivo.write(contenido)


def leer_matriz(ruta):
    """
    Lee una matriz de un archivo de texto.

    Parámetros:
    ruta (str): Ruta del archivo que contiene la matriz.

    Retorna:
    list: La matriz leída desde el archivo.
    """
    matriz = []
    with open(ruta) as archivo:
        for linea in archivo:
            valores = linea.strip().split(" ")
            fila = [float(valor) for valor in valores]
            matriz.append(fila)
    return matriz

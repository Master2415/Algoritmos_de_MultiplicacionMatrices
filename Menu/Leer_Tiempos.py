import matplotlib.pyplot as plt


def leer_archivo(ruta_archivo):
    datos = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en partes separadas por ": "
            partes = linea.strip().split(': ')
            if len(partes) == 2:
                # Extraer el valor numérico
                valor_str = partes[0]
                try:
                    valor = int(valor_str)
                    datos.append(valor)
                except ValueError:
                    print(f"Error: No se pudo convertir '{valor_str}' a entero.")
    return datos


def graficar_barras(datos):
    etiquetas = [f"Método {i + 1}" for i in range(len(datos))]  # Etiquetas genéricas para cada dato

    plt.figure(figsize=(10, 6))
    plt.barh(etiquetas, datos, color='skyblue')
    plt.xlabel('Tiempo (nanosegundos)')
    plt.title('Tiempo de ejecución de diferentes métodos')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


# Ingresa la ruta del archivo aquí
ruta_archivo = 'C:/ALL/Codigos/WS_Python/WS/Metodos_de_multiplicacion/Tiempo_Registrado/tiempos.txt'

# Lee el archivo y obtiene los datos
datos = leer_archivo(ruta_archivo)

# Genera la gráfica de barras
graficar_barras(datos)

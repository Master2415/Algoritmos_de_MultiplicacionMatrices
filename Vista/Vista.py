import matplotlib.pyplot as plt
import pandas as pd
from modelo import Crear


# Crear matrices y calcular tiempos
matrices = Crear.crear_matriz_main()

# Crear DataFrame para la tabla de estadísticas
data = {'Matriz': [], 'Media': [], 'Rango': [], 'Desviacion Estandar': [], 'Varianza': []}
for matriz in matrices:
    data['Matriz'].append(matriz.nombre_matriz)
    data['Media'].append(matriz.media)
    data['Rango'].append(matriz.rango)
    data['Desviacion Estandar'].append(matriz.desviacion_estandar)
    data['Varianza'].append(matriz.varianza)
df = pd.DataFrame(data)

# Mostrar la tabla de estadísticas
print(df)

# Crear gráfico de barras para tiempos medios
plt.figure(figsize=(10, 6))
plt.bar(df['Matriz'], df['Media'], color='gray')
plt.xlabel('Matrices')
plt.ylabel('Tiempo Medio (nanosegundos)')
plt.title('Tiempos Medios de Multiplicación de Matrices')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Crear gráfico de barras para tiempos medios ordenados
df_sorted = df.sort_values(by='Media')
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['Matriz'], df_sorted['Media'], color='gray')
plt.xlabel('Matrices (Ordenadas)')
plt.ylabel('Tiempo Medio (nanosegundos)')
plt.title('Tiempos Medios de Multiplicación de Matrices (Ordenadas)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Crear gráfico de líneas para los tiempos de cada matriz
plt.figure(figsize=(12, 6))
for matriz in matrices:
    plt.plot(range(len(matriz.tiempos)), matriz.tiempos, label=matriz.nombre_matriz)
plt.xlabel('Iteración')
plt.ylabel('Tiempo (nanosegundos)')
plt.title('Tiempos de Multiplicación de Matrices')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

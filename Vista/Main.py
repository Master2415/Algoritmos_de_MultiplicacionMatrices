import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd
from time import time
from collections import defaultdict

    
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main App")
        self.geometry("800x600")

        # Creación de pestañas
        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(expand=1, fill="both")

        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="📊 Grafica")

        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text="📈 Grafica orden creciente")

        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text="📊 Estadistica")

        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab4, text="📍 Punto en el plano")

        # Inicializar componentes de las pestañas
        self.init_tab1()
        self.init_tab2()
        self.init_tab3()
        self.init_tab4()

    def init_tab1(self):
        # Componentes de la pestaña 1
        self.graficaOrdenCreciente = tk.Frame(self.tab1)
        self.graficaOrdenCreciente.pack(fill=tk.BOTH, expand=1)

        self.plot_bar_chart(self.graficaOrdenCreciente)

    def init_tab2(self):
        # Componentes de la pestaña 2
        self.panel1 = tk.Frame(self.tab2)
        self.panel1.pack(fill=tk.BOTH, expand=1)

        self.plot_bar_chart(self.panel1)

    def init_tab3(self):
        # Componentes de la pestaña 3
        self.jTable1 = ttk.Treeview(self.tab3)
        self.jTable1.pack(fill=tk.BOTH, expand=1)

        # Configurar columnas
        self.jTable1["columns"] = ("Matriz", "Media", "Rango", "Desviacion Estandar", "Varianza")
        self.jTable1.column("#0", width=0, stretch=tk.NO)  # Espacio vacío
        self.jTable1.column("Matriz", anchor=tk.W, width=100)
        self.jTable1.column("Media", anchor=tk.W, width=100)
        self.jTable1.column("Rango", anchor=tk.W, width=100)
        self.jTable1.column("Desviacion Estandar", anchor=tk.W, width=150)
        self.jTable1.column("Varianza", anchor=tk.W, width=150)

        # Encabezados
        self.jTable1.heading("#0", text="")
        self.jTable1.heading("Matriz", text="Matriz")
        self.jTable1.heading("Media", text="Media")
        self.jTable1.heading("Rango", text="Rango")
        self.jTable1.heading("Desviacion Estandar", text="Desviacion Estandar")
        self.jTable1.heading("Varianza", text="Varianza")

        self.fill_statistics_table()

    def init_tab4(self):
        # Componentes de la pestaña 4
        self.jPanel5 = tk.Frame(self.tab4)
        self.jPanel5.pack(fill=tk.BOTH, expand=1)

        self.plot_line_chart(self.jPanel5)

    def plot_bar_chart(self, parent):
        # Datos de ejemplo
        matriz_nombres = ["Matriz1", "Matriz2", "Matriz3"]
        tiempos = [100, 200, 150]

        fig, ax = plt.subplots()
        ax.bar(matriz_nombres, tiempos)
        ax.set_xlabel('Matrices')
        ax.set_ylabel('Tiempo en nanosegundos')
        ax.set_title('Tiempos Matrices')

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def fill_statistics_table(self):
        # Datos de ejemplo para la tabla de estadísticas
        matriz_nombres = ["Matriz1", "Matriz2", "Matriz3"]
        medias = [10, 20, 15]
        rangos = [5, 8, 6]
        desviaciones = [2.5, 3.2, 2.8]
        varianzas = [6.25, 10.24, 7.84]

        for i in range(len(matriz_nombres)):
            self.jTable1.insert("", "end", text="", values=(
                matriz_nombres[i], medias[i], rangos[i], desviaciones[i], varianzas[i]))

    def plot_line_chart(self, parent):
        # Datos de ejemplo para el gráfico de líneas
        x = np.arange(10)
        y1 = np.random.rand(10)
        y2 = np.random.rand(10)

        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Matriz1')
        ax.plot(x, y2, label='Matriz2')
        ax.set_xlabel('Tamaño Matriz')
        ax.set_ylabel('Tiempo')
        ax.set_title('Grafica Tiempos')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

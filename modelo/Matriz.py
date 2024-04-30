import math


class Matriz:
    def __init__(self, nombreMatriz, tiempos):
        self.nombreMatriz = nombreMatriz
        self.tiempos = tiempos
        self.media = 0
        self.rango = 0
        self.varianza = 0
        self.desviacionEstandar = 0
        self.calcular_estadisticas()

    def calcular_estadisticas(self):
        self.calcular_media()
        self.calcular_rango()
        self.calcular_varianza()
        self.calcular_desviacion_estandar()

    def calcular_media(self):
        suma = sum(self.tiempos)
        self.media = suma / len(self.tiempos)

    def calcular_rango(self):
        maximo = max(self.tiempos)
        minimo = min(self.tiempos)
        self.rango = maximo - minimo

    def calcular_varianza(self):
        suma_cuadrados = sum((tiempo - self.media) ** 2 for tiempo in self.tiempos)
        cantidad_elementos = len(self.tiempos)
        self.varianza = suma_cuadrados / (cantidad_elementos - 1)

    def calcular_desviacion_estandar(self):
        self.desviacionEstandar = math.sqrt(self.varianza)

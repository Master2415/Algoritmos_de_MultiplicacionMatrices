from modelo import MedicionTiempo
from modelo import Matriz
from modelo import Crear


class CalcularTiempoAlgoritmos:
    def __init__(self):
        self.matrices_organizadas = []
        self.matrices = []
        self.tiempo = MedicionTiempo
        self.matriz1 = None
        self.matriz2 = None

    def run_calculos(self):
        self.calcular_tiempo()

    def calcular_tiempo(self):
        # Definir listas para almacenar los tiempos de cada algoritmo
        naiv_on_array = []
        naiv_unrolling_two = []
        naiv_loop_unrolling_four = []
        winograd_original = []
        winograd_scaled = []
        strassen_naiv = []
        strassen_winograd = []
        lll_3_sequential_block = []
        lll_4_parallel_block = []
        lv__3_sequential_block = []
        lv_4_parallel_block = []
        v_3_sequential_block = []
        v_4_parallel_block = []

        for i in range(1, 9):
            # Leer las dos matrices desde archivos
            self.matriz1 = Crear.leer_matriz(f"TiempoMatrices/src/Persistencia/matriz {i}.1.txt")
            self.matriz2 = Crear.leer_matriz(f"TiempoMatrices/src/Persistencia/matriz {i}.2.txt")
            potencia = 2 ** i

            # Calcular tiempos para diferentes algoritmos y agregarlos a las listas correspondientes
            # 1. naivOnArray
            naiv_on_array.append(self.tiempo.tiempo_naiv_on_array(self.matriz1, self.matriz2, potencia))
            print("naivOnArray")
            # 2. NaivLoopUnrollingTwo
            naiv_unrolling_two.append(self.tiempo.tiempo_naiv_loop_unrolling_two(self.matriz1, self.matriz2, potencia))
            print("naivUnrollingTwo")
            # 3. NaivLoopUnrollingFour
            naiv_loop_unrolling_four.append(
                self.tiempo.tiempo_naiv_loop_unrolling_four(self.matriz1, self.matriz2, potencia))
            print("naivLoopUnrollingFour")
            # 4. WinogradOriginal
            winograd_original.append(self.tiempo.tiempo_winograd_original(self.matriz1, self.matriz2, potencia))
            print("winogradOriginal")
            # 5. WinogradScaled
            winograd_scaled.append(self.tiempo.tiempo_winograd_scaled(self.matriz1, self.matriz2, potencia))
            print("winogradScaled")
            # 6. StrassenNaiv
            strassen_naiv.append(self.tiempo.tiempo_strassen_naiv(self.matriz1, self.matriz2, potencia))
            print("strassenNaiv")
            # 7. StrassenWinograd
            strassen_winograd.append(self.tiempo.tiempo_strassen_winograd(self.matriz1, self.matriz2, potencia))
            print("strassenWinograd")
            # 8. III.3 Sequential block
            lll_3_sequential_block.append(
                self.tiempo.tiempo_iii_3_sequential_block(self.matriz1, self.matriz2, potencia))
            print("lll_3SequentialBlock")
            # 9. III.4 Parallel Block
            lll_4_parallel_block.append(self.tiempo.tiempo_iii_4_parallel_block(self.matriz1, self.matriz2, potencia))
            print("lll_4ParallelBlock")
            # 10. III.5 Enhanced Parallel Block

            # 11. IV.3 Sequential block
            lv__3_sequential_block.append(
                self.tiempo.tiempo_iv_3_sequential_block(self.matriz1, self.matriz2, potencia))
            print("lv__3SequentialBlock")
            # 12. IV.4 Parallel Block
            lv_4_parallel_block.append(self.tiempo.tiempo_iv_4_parallel_block(self.matriz1, self.matriz2, potencia))
            print("lv_4ParallelBlock")
            # 13. IV. 5 Enhanced Parallel Block

            # 14. V.3 Sequential block
            v_3_sequential_block.append(self.tiempo.tiempo_v_3_sequential_block(self.matriz1, self.matriz2, potencia))
            print("v_3SequentialBlock")
            # 15. V.4 Parallel Block
            v_4_parallel_block.append(self.tiempo.tiempo_v_4_parallel_block(self.matriz1, self.matriz2, potencia))
            print("v_4ParallelBlock")

            # Imprimir información de progreso
            print(f"Calculando tiempos para potencia {potencia}")

        # Agregar los resultados a la lista de matrices
        self.matrices.append(Matriz("naivOnArray", naiv_on_array))
        self.matrices.append(Matriz("naivUnrollingTwo", naiv_unrolling_two))
        self.matrices.append(Matriz("naivLoopUnrollingFour", naiv_loop_unrolling_four))
        self.matrices.append(Matriz("winogradOriginal", winograd_original))
        self.matrices.append(Matriz("winogradScaled", winograd_scaled))
        self.matrices.append(Matriz("strassenNaiv", strassen_naiv))
        self.matrices.append(Matriz("strassenWinograd", strassen_winograd))
        self.matrices.append(Matriz("lll_3SequentialBlock", lll_3_sequential_block))
        self.matrices.append(Matriz("lll_4ParallelBlock", lll_4_parallel_block))
        self.matrices.append(Matriz("lv__3SequentialBlock", lv__3_sequential_block))
        self.matrices.append(Matriz("lv_4ParallelBlock", lv_4_parallel_block))
        self.matrices.append(Matriz("v_3SequentialBlock", v_3_sequential_block))
        self.matrices.append(Matriz("v_4ParallelBlock", v_4_parallel_block))

        self.reporte_tiempo()

    def reporte_tiempo(self):
        # Obtiene el tamaño de los tiempos de la primera matriz en la lista de matrices
        tamanotiempos = len(self.matrices[0].tiempos)
        # Crea un StringBuilder para almacenar el contenido del reporte
        contenido = []

        # Itera sobre cada matriz en la lista
        for matrix in self.matrices:
            # Agrega el nombre de la matriz al contenido del reporte
            contenido.append(f"\n{matrix.nombre}")

            # Itera sobre los tiempos de la matriz actual
            for j in range(tamanotiempos):
                # Calcula la potencia actual
                potencia2 = 2 ** (j + 1)
                # Agrega la información de tiempo al contenido del reporte
                contenido.append(f"\nMatriz de {potencia2}*{potencia2}: {matrix.tiempos[j]}")

        # Guarda el contenido del reporte en un archivo
        Crear.guardar_archivo("Persistencia/tiempo ", "\n".join(contenido), False)
        # Agrega todas las matrices a la lista de matrices organizadas
        self.matrices_organizadas.extend(self.matrices)
        # Ordena la lista de matrices organizadas
        self.ordenar_matriz(self.matrices_organizadas)

    def ordenar_matriz(self, matrices_organizadas):
        n = len(matrices_organizadas)
        intercambio = True
        i = 0
        j = n - 1

        while intercambio:
            intercambio = False

            for k in range(i, j):
                if matrices_organizadas[k].get_media() > matrices_organizadas[k + 1].get_media():
                    matriz = matrices_organizadas[k]
                    matrices_organizadas[k] = matrices_organizadas[k + 1]
                    matrices_organizadas[k + 1] = matriz
                    intercambio = True

            j -= 1

            for k in range(j, i, -1):
                if matrices_organizadas[k].get_media() < matrices_organizadas[k - 1].get_media():
                    matriz = matrices_organizadas[k]
                    matrices_organizadas[k] = matrices_organizadas[k - 1]
                    matrices_organizadas[k - 1] = matriz
                    intercambio = True

            i += 1

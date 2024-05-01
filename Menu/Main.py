from Model import Graficas
from Model import Crear


class Main:
    @staticmethod
    def main():
        # Crear matrices
        # Crear.crear_matriz_main()

        # Medir tiempos
        (elapsed_time_naivOnArray,
         elapsed_time_NaivLoopUnrollingTwo,
         elapsed_time_NaivLoopUnrollingFour,
         elapsed_time_WinogradOriginal,
         elapsed_time_WinogradScaled,
         elapsed_time_StrassenNaiv,
         elapsed_time_StrassenWinograd,
         elapsed_time_lll_3_sequential_block) = Graficas.medir_Tiempos()

        # Mostrar en consola
        Graficas.mostrar_en_consola(elapsed_time_naivOnArray,
                                    elapsed_time_NaivLoopUnrollingTwo,
                                    elapsed_time_NaivLoopUnrollingFour,
                                    elapsed_time_WinogradOriginal,
                                    elapsed_time_WinogradScaled,
                                    elapsed_time_StrassenNaiv,
                                    elapsed_time_StrassenWinograd,
                                    elapsed_time_lll_3_sequential_block)

        # Mostrar gráficas
        Graficas.mostrar_Graficas(elapsed_time_naivOnArray,
                                  elapsed_time_NaivLoopUnrollingTwo,
                                  elapsed_time_NaivLoopUnrollingFour,
                                  elapsed_time_WinogradOriginal,
                                  elapsed_time_WinogradScaled,
                                  elapsed_time_StrassenNaiv,
                                  elapsed_time_StrassenWinograd,
                                  elapsed_time_lll_3_sequential_block)


# Ejecutar el método main de la clase Main
Main.main()

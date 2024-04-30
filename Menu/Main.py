from Model import Graficas


class Main:
    @staticmethod
    def main():
        # Medir tiempos
        (elapsed_time_naivOnArray,
         elapsed_time_NaivLoopUnrollingTwo,
         elapsed_time_NaivLoopUnrollingFour,
         elapsed_time_WinogradOriginal,
         elapsed_time_WinogradScaled,
         elapsed_time_StrassenNaiv) = Graficas.medir_Tiempos()

        # Mostrar en consola
        Graficas.mostrar_en_consola(elapsed_time_naivOnArray,
                                    elapsed_time_NaivLoopUnrollingTwo,
                                    elapsed_time_NaivLoopUnrollingFour,
                                    elapsed_time_WinogradOriginal,
                                    elapsed_time_WinogradScaled,
                                    elapsed_time_StrassenNaiv)

        # Mostrar gráficas
        Graficas.mostrar_Graficas(elapsed_time_naivOnArray,
                                  elapsed_time_NaivLoopUnrollingTwo,
                                  elapsed_time_NaivLoopUnrollingFour,
                                  elapsed_time_WinogradOriginal,
                                  elapsed_time_WinogradScaled,
                                  elapsed_time_StrassenNaiv)


# Ejecutar el método main de la clase Main
Main.main()

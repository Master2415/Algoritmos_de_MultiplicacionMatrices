import time
from Algoritmos.NaivOnArray import NaivOnArray
from Algoritmos.NaivLoopUnrollingFour import NaivLoopUnrollingFour
from Algoritmos.NaivLoopUnrollingTwo import NaivLoopUnrollingTwo
from Algoritmos.WinogradOriginal import WinogradOriginal
from Algoritmos.WinogradScaled import WinogradScaled
from Algoritmos.StrassenNaiv import StrassenNaiv
from Algoritmos.StrassenWinograd import StrassenWinograd
from Algoritmos.III_3SequentialBlock import III_3SequentialBlock
from Algoritmos.III_4ParallelBlock import III_4ParallelBlock
from Algoritmos.IV_3SequentialBlock import IV_3SequentialBlock
from Algoritmos.IV_4ParallelBlock import IV_4ParallelBlock
from Algoritmos.V_3SequentialBlock import V_3SequentialBlock
from Algoritmos.V_4ParallelBlock import V_4ParallelBlock


class MedicionTiempo:
    def __init__(self):
        self.naiv_on_array = NaivOnArray()
        self.naiv_loop_unrolling_four = NaivLoopUnrollingFour()
        self.naiv_loop_unrolling_two = NaivLoopUnrollingTwo()
        self.winograd_original = WinogradOriginal()
        self.winograd_scaled = WinogradScaled()
        self.strassen_naiv = StrassenNaiv()
        self.strassen_winograd = StrassenWinograd()
        self.iii_3_sequential_block = III_3SequentialBlock()
        self.iii_4_parallel_block = III_4ParallelBlock()
        self.iv_3_sequential_block = IV_3SequentialBlock()
        self.iv_4_parallel_block = IV_4ParallelBlock()
        self.v_3_sequential_block = V_3SequentialBlock()
        self.v_4_parallel_block = V_4ParallelBlock()


def tiempo_naiv_on_array(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()
    matrizC = [[0.0] * tamano for _ in range(tamano)]

    self.naiv_on_array.NaivOnArray(matrizA, matrizB, matrizC, tamano, tamano, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_naiv_loop_unrolling_four(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()
    matrizC = [[0.0] * tamano for _ in range(tamano)]

    self.naiv_loop_unrolling_four.NaivLoopUnrollingFour(matrizA, matrizB, matrizC, tamano, tamano, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_naiv_loop_unrolling_two(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()
    matrizC = [[0.0] * tamano for _ in range(tamano)]

    self.naiv_unrolling_two.naiv_loop_unrolling_two(matrizA, matrizB, matrizC, tamano, tamano, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_winograd_original(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()
    matrizC = [[0.0] * tamano for _ in range(tamano)]

    self.winograd_original.winograd_original(matrizA, matrizB, matrizC, tamano, tamano, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_winograd_scaled(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()
    matrizC = [[0.0] * tamano for _ in range(tamano)]

    self.winograd_scaled.winograd_scaled(matrizA, matrizB, matrizC, tamano, tamano, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_strassen_naiv(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()
    matrizC = [[0.0] * tamano for _ in range(tamano)]

    self.strassen_naiv.strassen_naiv(matrizA, matrizB, matrizC, tamano, tamano, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_strassen_winograd(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()
    matrizC = [[0.0] * tamano for _ in range(tamano)]

    self.strassen_winograd.strassen_winograd(matrizA, matrizB, matrizC, tamano, tamano, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_iii_3_sequential_block(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()

    self.iii_3_sequential_block.lll_3SequentialBlock(matrizA, matrizB, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_iii_4_parallel_block(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()

    self.iii_4_parallel_block.lll_4ParallelBlock(matrizA, matrizB, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_iv_3_sequential_block(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()

    self.iv_3_sequential_block.lV_3SequentialBlock(matrizA, matrizB, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_iv_4_parallel_block(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()

    self.iv_4_parallel_block.lV_4ParallelBlock(matrizA, matrizB, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_v_3_sequential_block(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()

    self.v_3_sequential_block.v_3SequentialBlock(matrizA, matrizB, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo


def tiempo_v_4_parallel_block(self, matrizA, matrizB, tamano):
    inicio_tiempo = time.time_ns()

    self.v_4_parallel_block.v_4ParallelBlock(matrizA, matrizB, tamano)

    fin_tiempo = time.time_ns()
    return fin_tiempo - inicio_tiempo



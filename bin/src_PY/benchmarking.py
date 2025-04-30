from metodos_ordenamiento import metodos_ordenamiento
from src_PY.metodos_ordenamiento import metodos_ordenamiento

import random
import time

class Benchmarking:
    def __init__(self):
        print("Benchmarking instanciado")
        self.mb = metodos_ordenamiento()

        arreglo = self.build_arreglo(1000)

        resultados = {
            "Burbuja": self.contar_con_nano_time(lambda: self.mb.metodo_sort_bubble(arreglo)),
            "Burbuja Mejorado": self.contar_con_nano_time(lambda: self.mb.metodo_sort_bubble_mejorado(arreglo)),
            "Inserción": self.contar_con_nano_time(lambda: self.mb.metodo_sort_insercion(arreglo)),
            "Selección": self.contar_con_nano_time(lambda: self.mb.metodo_sort_seleccion(arreglo)),
        }

        for metodo, tiempo in resultados.items():
            print(f"Tiempo de {metodo}: {tiempo:.2f} ns")

        metodo_mas_eficiente = min(resultados, key=resultados.get)
        print(f"\nEl método más eficiente fue: {metodo_mas_eficiente}")

    def build_arreglo(self, tamaño):
        return [random.randint(0, 9999) for _ in range(tamaño)]

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return fin - inicio

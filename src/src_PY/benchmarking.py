import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print("Benchmarking instanciado")
        self.mb = MetodosOrdenamiento()
        self.arreglo = self.build_arreglo(1000)

    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio

    def build_arreglo(self, tamanio):
        return [random.randint(0, 9999) for _ in range(tamanio)]

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return fin - inicio

    def ejecutar_benchmark(self):
        resultados = {
            "Burbuja": self.contar_con_nano_time(lambda: self.mb.metodo_sort_bubble(self.arreglo)),
            "Burbuja Mejorado": self.contar_con_nano_time(lambda: self.mb.metodo_sort_bubble_mejorado(self.arreglo)),
            "Inserción": self.contar_con_nano_time(lambda: self.mb.metodo_sort_insercion(self.arreglo)),
            "Selección": self.contar_con_nano_time(lambda: self.mb.metodo_sort_seleccion(self.arreglo)),
        }

        for metodo, tiempo in resultados.items():
            print(f"Tiempo de {metodo}: {tiempo:.2f} ns")

        metodo_mas_eficiente = min(resultados, key=resultados.get)
        print(f"\nEl método más eficiente fue: {metodo_mas_eficiente}")

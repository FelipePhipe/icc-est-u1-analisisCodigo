from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
import time
from datetime import datetime

if __name__ == "__main__":
    print("funciona")

    bench = Benchmarking()
    metodosO = MetodosOrdenamiento()

    tamanios = [500, 1000, 2000]
    resultados = []

    metodos_dic = {
        "burbuja": metodosO.metodo_sort_bubble,
        "burbuja_mejorado": metodosO.metodo_sort_bubble_mejorado,
        "seleccion": metodosO.metodo_sort_seleccion,
        "shell": sorted
    }

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)
        for nombre, metodo in metodos_dic.items():
            tiempo = bench.medir_tiempo(metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo))

    tiempos_by_metodo = {nombre: [] for nombre in metodos_dic}
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

  
    plt.figure(figsize=(12, 6))

    now = datetime.now()
    plt.suptitle(f"FELIPE PARRA - {now.strftime('%d/%m/%Y %H:%M:%S')}", fontsize=12, weight='bold')

  
    ax1 = plt.subplot(1, 2, 1)
    colores = {
        "burbuja": "blue",
        "burbuja_mejorado": "orange",
        "seleccion": "green",
        "shell": "red"
    }

    for nombre, tiempos in tiempos_by_metodo.items():
        ax1.plot(tamanios, tiempos, label=nombre, marker="o", color=colores[nombre])

    ax1.set_title("Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento")
    ax1.set_xlabel("Tamaño del arreglo")
    ax1.set_ylabel("Tiempo de ejecución (segundos)")
    ax1.grid(True)
    ax1.legend()

 
    ax2 = plt.subplot(1, 2, 2)
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    ax2.plot(x, y, label="Línea 1", color="blue")
    ax2.set_title("Gráfico de Ejemplo con Matplotlib")
    ax2.set_xlabel("Eje X")
    ax2.set_ylabel("Eje Y")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

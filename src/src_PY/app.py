from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print("funciona")

    bench = Benchmarking()
    metodosO = MetodosOrdenamiento()

    tamanios = [5000, 10000, 15000]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)  

        metodos_dic = {
            "burbuja": metodosO.metodo_sort_bubble,
            "burbuja mejorado": metodosO.metodo_sort_bubble_mejorado,
            "seleccion": metodosO.metodo_sort_seleccion,
            "insercion": metodosO.metodo_sort_insercion,
        }

        for nombre, metodo in metodos_dic.items():
            time_resultado = bench.medir_tiempo(metodo, arreglo_base)
            tupla_resultado = (tam, nombre, time_resultado)  
            resultados.append(tupla_resultado)

    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, nombre método: {nombre}, tiempo: {tiempo:.6f} segundos")

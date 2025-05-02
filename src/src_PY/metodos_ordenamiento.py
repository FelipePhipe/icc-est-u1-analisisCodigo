class MetodosOrdenamiento:
    def metodo_sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def metodo_sort_bubble_mejorado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            intercambio = False
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    intercambio = True
            if not intercambio:
                break
        return arreglo

    def metodo_sort_insercion(self, array):
        arreglo = array.copy()
        for i in range(1, len(arreglo)):
            clave = arreglo[i]
            j = i - 1
            while j >= 0 and clave < arreglo[j]:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = clave
        return arreglo

    def metodo_sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_idx]:
                    min_idx = j
            arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        return arreglo
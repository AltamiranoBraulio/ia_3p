# Importamos la biblioteca random para generar números aleatorios
import random
# Importamos la biblioteca math para usar logaritmos (necesario para visualizar el árbol)
import math

# Función que imprime visualmente la estructura del heap como si fuera un árbol
def mostrar_heap_arbol(heap):
    n = len(heap)  # Obtenemos el número total de elementos en el heap
    niveles = int(math.log2(n)) + 1  # Calculamos cuántos niveles tiene el árbol (basado en log base 2)
    max_anchura = 2 ** (niveles + 1)  # Determinamos el ancho máximo del árbol para formatear bien la salida

    index = 0  # Índice para recorrer los elementos del heap
    # Recorremos cada nivel del árbol desde la raíz hasta las hojas
    for nivel in range(niveles):
        nivel_elementos = 2 ** nivel  # Número de nodos que debería haber en este nivel (potencias de 2)
        linea = ""  # Inicializamos la línea que imprimiremos en consola
        espacio = max_anchura // (2 ** nivel + 1)  # Calculamos el espacio entre nodos para alinear bien el árbol
        for i in range(nivel_elementos):
            if index < n:  # Verificamos que no nos pasamos del número de nodos
                linea += " " * espacio + str(heap[index]) + " " * espacio  # Añadimos el nodo a la línea con espacios
                index += 1  # Pasamos al siguiente nodo
        print(linea.center(max_anchura * 2))  # Imprimimos la línea centrada
    print("\n")  # Imprimimos una línea en blanco al final

# Función que realiza la operación "heapify" sobre un subárbol
# Esta operación asegura que el árbol cumpla la propiedad de Max Heap
def heapify(arr, n, i):
    largest = i          # Inicializamos el nodo actual como el más grande
    left = 2 * i + 1      # Calculamos el índice del hijo izquierdo
    right = 2 * i + 2     # Calculamos el índice del hijo derecho

    # Si el hijo izquierdo existe y es mayor que el nodo actual
    if left < n and arr[left] > arr[largest]:
        largest = left  # Actualizamos el índice del más grande

    # Si el hijo derecho existe y es mayor que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right  # Actualizamos el índice del más grande

    # Si el más grande no es el nodo actual, hacemos un intercambio
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiamos los valores
        heapify(arr, n, largest)  # Llamamos recursivamente heapify sobre el subárbol afectado

# Función principal que implementa el algoritmo Heap Sort
def heap_sort(arr):
    n = len(arr)  # Obtenemos el tamaño de la lista

    # Fase 1: Construimos un Max Heap a partir del arreglo
    # Empezamos desde el último nodo padre hasta la raíz
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)  # Aplicamos heapify en cada nodo padre

    # Mostramos la estructura del heap antes de ordenar
    print("Árbol como Max Heap:")
    mostrar_heap_arbol(arr)

    # Fase 2: Extraemos elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Movemos el valor máximo (en la raíz) al final
        heapify(arr, i, 0)  # Reestablecemos la propiedad de Max Heap en el heap reducido

    return arr  # Devolvemos el arreglo ya ordenado

# Bloque principal: se ejecuta solo si este archivo es ejecutado directamente
if __name__ == "__main__":
    # Creamos una lista con 15 números aleatorios entre 10 y 99
    datos = [random.randint(10, 99) for _ in range(15)]

    # Mostramos la lista original
    print("Lista original:")
    print(datos)

    # Ordenamos la lista usando Heap Sort y guardamos el resultado
    ordenado = heap_sort(datos.copy())  # Usamos .copy() para no modificar la original

    # Mostramos la lista ordenada
    print("Lista ordenada con Heap Sort:")
    print(ordenado)

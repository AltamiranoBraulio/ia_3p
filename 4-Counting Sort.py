"""
Counting Sort - Implementación Avanzada con Aplicaciones en IA

Documentación general del módulo:
Este bloque docstring explica que Counting Sort es ideal para datos con rango conocido
y distribución uniforme. Destaca su utilidad en preprocesamiento de datos para IA.
"""

# Importación de librerías:
# numpy para operaciones numéricas eficientes
# defaultdict para manejo avanzado de diccionarios
# matplotlib.pyplot para visualizaciones
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def counting_sort(arr, key=lambda x: x, visualize=False):
    """
    Función principal de Counting Sort mejorada.
    
    Parámetros:
        arr: Lista/array de elementos a ordenar (números, strings, objetos)
        key: Función que extrae el valor clave para ordenar (por defecto el elemento mismo)
        visualize: Flag para mostrar visualización del proceso (False por defecto)
    
    Retorna:
        Lista ordenada según la clave especificada
    
    Características especiales:
        - Soporta claves personalizadas para objetos complejos
        - Visualización interactiva del proceso
        - Maneja valores negativos
        - Trabaja con datos multidimensionales
    """
    
    # Validación de entrada: si la lista está vacía, retornar inmediatamente
    if not arr:
        return arr
    
    # Extracción de claves:
    # Aplica la función key a cada elemento para obtener los valores de ordenación
    keys = [key(x) for x in arr]
    
    # Determinación del rango:
    # Encuentra los valores mínimo y máximo para definir el rango de conteo
    min_key, max_key = min(keys), max(keys)
    
    # Creación del arreglo de conteo:
    # Tamaño calculado como (max - min + 1) para cubrir todos los valores posibles
    count_size = max_key - min_key + 1
    count = [0] * count_size  # Inicializa con ceros
    
    # Fase 1: Conteo de ocurrencias
    # Incrementa el contador correspondiente a cada valor clave
    for k in keys:
        count[k - min_key] += 1  # Ajusta el índice restando min_key
    
    # Visualización opcional del conteo inicial
    if visualize:
        plt.figure(figsize=(10, 4))  # Crea figura de 10x4 pulgadas
        plt.bar(range(min_key, max_key+1), count)  # Gráfico de barras
        plt.title("Fase 1: Conteo de Elementos")  # Título
        plt.xlabel("Valores")  # Etiqueta eje X
        plt.ylabel("Conteo")  # Etiqueta eje Y
        plt.show()  # Muestra el gráfico
    
    # Fase 2: Acumulación de conteos
    # Transforma el arreglo de conteo en posiciones finales
    for i in range(1, count_size):
        count[i] += count[i-1]  # Cada posición acumula las anteriores
    
    # Visualización opcional del conteo acumulado
    if visualize:
        plt.figure(figsize=(10, 4))
        plt.bar(range(min_key, max_key+1), count)
        plt.title("Fase 2: Conteo Acumulativo")
        plt.xlabel("Valores")
        plt.ylabel("Conteo acumulado")
        plt.show()
    
    # Fase 3: Construcción del resultado ordenado
    output = [None] * len(arr)  # Lista de salida del mismo tamaño que la entrada
    
    # Procesa los elementos en orden inverso para mantener estabilidad
    for x in reversed(arr):
        k = key(x)  # Obtiene la clave del elemento actual
        # Calcula la posición correcta en el output y coloca el elemento
        output[count[k - min_key] - 1] = x
        count[k - min_key] -= 1  # Decrementa el contador para ese valor
    
    return output  # Retorna la lista ordenada

def counting_sort_2d(matrix, axis=0, key=lambda x: x):
    """
    Versión extendida para matrices 2D que permite ordenar por filas o columnas.
    
    Parámetros:
        matrix: Matriz 2D (lista de listas) a ordenar
        axis: Eje para ordenar (0=columnas, 1=filas)
        key: Función clave para ordenamiento
    
    Retorna:
        Matriz ordenada según el eje especificado
    """
    if axis == 0:
        # Ordenamiento por columnas:
        # 1. Transpone la matriz (zip(*matrix)) para convertir columnas en filas
        # 2. Ordena cada columna (ahora fila) con counting_sort
        # 3. Vuelve a transponer para restaurar estructura original
        return [list(x) for x in zip(*[counting_sort(col, key=key) for col in zip(*matrix)])]
    else:
        # Ordenamiento por filas:
        # Aplica counting_sort a cada fila directamente
        return [counting_sort(row, key=key) for row in matrix]

class AdvancedCountingSort:
    """
    Versión orientada a objetos para ordenamiento más complejo.
    Permite separar las fases del algoritmo y reutilizar resultados.
    """
    
    def __init__(self, data, key=lambda x: x):
        """
        Constructor: Inicializa el ordenador con datos y función clave.
        
        Parámetros:
            data: Datos a ordenar
            key: Función para extraer valores de ordenación
        """
        self.data = data  # Almacena los datos originales
        self.key = key  # Función clave para ordenamiento
        self._count = None  # Arreglo de conteo (se calcula luego)
        self._sorted = None  # Resultado ordenado (se calcula luego)
    
    def build_count(self):
        """Construye y retorna el arreglo de conteo de frecuencias."""
        keys = [self.key(x) for x in self.data]  # Extrae claves
        min_key, max_key = min(keys), max(keys)  # Encuentra rango
        self._count = [0] * (max_key - min_key + 1)  # Inicializa conteo
        
        # Cuenta ocurrencias de cada valor clave
        for k in keys:
            self._count[k - min_key] += 1
        
        return self._count  # Retorna arreglo de conteo
    
    def sort(self):
        """Ejecuta el algoritmo completo y retorna los datos ordenados."""
        if not self._count:  # Si no se ha construido el conteo
            self.build_count()  # Lo calcula primero
        
        # Fase de acumulación:
        # Convierte conteos en posiciones finales
        for i in range(1, len(self._count)):
            self._count[i] += self._count[i-1]
        
        # Fase de construcción del resultado:
        output = [None] * len(self.data)  # Prepara lista de salida
        
        # Procesa elementos en orden inverso para mantener estabilidad
        for x in reversed(self.data):
            k = self.key(x)  # Obtiene clave del elemento
            # Calcula posición y coloca el elemento
            output[self._count[k - min(self._count)] - 1] = x
            # Decrementa el contador para esa clave
            self._count[k - min(self._count)] -= 1
        
        self._sorted = output  # Almacena resultado
        return self._sorted  # Retorna datos ordenados

# Bloque principal de ejecución (solo se ejecuta al llamar directamente al script)
if __name__ == "__main__":
    # Ejemplo 1: Ordenamiento básico de números
    print("=== EJEMPLO 1: Ordenamiento básico ===")
    datos = [4, 2, 2, 8, 3, 3, 1]  # Lista de prueba
    print("Original:", datos)
    ordenado = counting_sort(datos, visualize=True)  # Ordena con visualización
    print("Ordenado:", ordenado)
    
    # Ejemplo 2: Ordenamiento de objetos por clave personalizada
    print("\n=== EJEMPLO 2: Ordenamiento por clave personalizada ===")
    personas = [
        {'nombre': 'Ana', 'edad': 25},
        {'nombre': 'Juan', 'edad': 30},
        {'nombre': 'Maria', 'edad': 22}
    ]
    print("Original:", personas)
    # Ordena por edad usando lambda para extraer la clave
    ordenado_edad = counting_sort(personas, key=lambda x: x['edad'])
    print("Ordenado por edad:", ordenado_edad)
    
    # Ejemplo 3: Ordenamiento de matriz 2D por columnas
    print("\n=== EJEMPLO 3: Ordenamiento de matriz 2D ===")
    matriz = [  # Matriz de prueba 3x3
        [3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]
    ]
    print("Matriz original:")
    for fila in matriz:  # Imprime la matriz original
        print(fila)
    
    # Ordena columnas (axis=0) y muestra resultado
    print("\nMatriz con columnas ordenadas:")
    ordenada_col = counting_sort_2d(matriz, axis=0)
    for fila in ordenada_col:
        print(fila)
    
    # Ejemplo 4: Uso de la versión orientada a objetos
    print("\n=== EJEMPLO 4: Uso de la clase AdvancedCountingSort ===")
    sorter = AdvancedCountingSort(datos)  # Crea instancia con datos
    print("Conteo:", sorter.build_count())  # Construye y muestra conteo
    print("Resultado ordenado:", sorter.sort())  # Ordena y muestra resultado

    # Aplicación práctica en IA: Normalización de características
    print("\n=== APLICACIÓN EN IA: Normalización de características ===")
    # Genera matriz aleatoria 10x5 con valores 0-100
    features = np.random.randint(0, 100, size=(10, 5))
    print("Features originales (primeras 5 filas):")
    print(features[:5])  # Muestra primeras 5 filas
    
    # Normalización:
    # 1. Ordena columnas con counting_sort_2d
    # 2. Convierte a array numpy
    # 3. Normaliza dividiendo por 100 para llevar al rango [0,1]
    features_normalized = counting_sort_2d(features.tolist(), axis=0)
    features_normalized = np.array(features_normalized) / 100.0
    print("\nFeatures normalizadas (primeras 5 filas):")
    print(features_normalized[:5])  # Muestra resultado
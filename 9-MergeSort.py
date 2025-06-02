"""
Documentación principal del módulo:
Explica que este código implementa MergeSort con características avanzadas como:
- Visualización animada del proceso de ordenamiento
- Versión paralela para mejor rendimiento
- Aplicaciones prácticas en Inteligencia Artificial
- Implementaciones tanto iterativas como recursivas
"""

# Importación de librerías necesarias:
# matplotlib.pyplot - Para crear visualizaciones gráficas
# numpy - Para operaciones numéricas eficientes (usado en IA)
# concurrent.futures - Para implementar la versión paralela
# time - Para medir tiempos de ejecución
# typing - Para anotaciones de tipo (mejor documentación)
import matplotlib.pyplot as plt
import numpy as np
import concurrent.futures
import time
from typing import List, Callable, Any

class MergeSortVisualizer:
    """
    Clase para visualizar el proceso de MergeSort de manera animada.
    Crea una representación gráfica de barras que muestra cómo se ordenan los datos.
    """
    
    def __init__(self, data: List[float], title: str = "MergeSort Process"):
        """
        Constructor que inicializa el visualizador con los datos a ordenar.
        
        Args:
            data: Lista de números que se van a ordenar
            title: Título que aparecerá en la visualización
        """
        # Copia los datos para no modificar la lista original
        self.data = data.copy()
        
        # Crea una figura y ejes para el gráfico con tamaño 10x6 pulgadas
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        
        # Crea las barras del gráfico, una por cada elemento en los datos
        # Color inicial: azul cielo ('skyblue')
        self.bars = self.ax.bar(range(len(data)), self.data, color='skyblue')
        
        # Configuración del título y etiquetas de los ejes
        self.title = title
        self.ax.set_title(title)
        self.ax.set_xlabel("Index")  # Etiqueta eje X
        self.ax.set_ylabel("Value")  # Etiqueta eje Y
        
        # Contadores para métricas de rendimiento
        self.comparisons = 0  # Número de comparaciones realizadas
        self.operations = 0  # Número total de operaciones
    
    def update_plot(self, left: int = None, right: int = None, 
                   merge: bool = False, description: str = ""):
        """
        Actualiza la visualización para reflejar el estado actual del ordenamiento.
        
        Args:
            left: Índice izquierdo del subarray que se está procesando
            right: Índice derecho del subarray que se está procesando
            merge: Booleano que indica si es una operación de mezcla (merge)
            description: Texto descriptivo del paso actual
        """
        # Actualiza la altura de cada barra según los datos actuales
        for i, bar in enumerate(self.bars):
            bar.set_height(self.data[i])
            
            # Cambia el color de las barras en el rango actual (left-right)
            if left is not None and right is not None and left <= i <= right:
                # Verde claro para operaciones de merge, salmón para divisiones
                bar.set_color('lightgreen' if merge else 'salmon')
            else:
                # Azul cielo para elementos no involucrados en la operación actual
                bar.set_color('skyblue')
        
        # Actualiza el título con la descripción del paso actual
        self.ax.set_title(f"{self.title}\n{description}")
        
        # Pausa breve para crear efecto de animación (0.5 segundos)
        plt.pause(0.5)
    
    def reset_colors(self):
        """
        Restablece todos los colores de las barras al color original (azul cielo).
        Se usa al finalizar una operación para preparar la visualización para el siguiente paso.
        """
        for bar in self.bars:
            bar.set_color('skyblue')
        plt.pause(0.1)  # Pausa breve

def merge_sort_recursive(data: List[float], visualizer: MergeSortVisualizer = None, 
                         left: int = 0, right: int = None) -> List[float]:
    """
    Implementación clásica recursiva (top-down) del algoritmo MergeSort.
    Puede mostrar una visualización animada si se provee un objeto visualizer.
    
    Args:
        data: Lista de elementos a ordenar
        visualizer: Objeto para visualización (opcional)
        left: Índice izquierdo del subarray actual (para recursión)
        right: Índice derecho del subarray actual (para recursión)
    
    Returns:
        Lista ordenada de elementos
    """
    # Si right es None, es la primera llamada, usamos todo el array
    if right is None:
        right = len(data) - 1
    
    # Caso base: si el subarray tiene más de un elemento
    if left < right:
        # Calcula el punto medio para dividir el array
        mid = (left + right) // 2
        
        # Visualiza la división si hay un visualizer
        if visualizer:
            visualizer.update_plot(left, right, False, 
                                 f"Dividiendo: {left}-{right}")
        
        # Llamadas recursivas para ordenar ambas mitades
        merge_sort_recursive(data, visualizer, left, mid)
        merge_sort_recursive(data, visualizer, mid + 1, right)
        
        # Visualiza el merge si hay un visualizer
        if visualizer:
            visualizer.update_plot(left, right, True, 
                                 f"Uniendo: {left}-{right}")
        
        # Une las dos mitades ordenadas
        merge(data, left, mid, right, visualizer)
        
        # Visualiza el resultado del merge si hay un visualizer
        if visualizer:
            visualizer.update_plot(left, right, True, 
                                 f"Unión completada: {left}-{right}")
            time.sleep(0.5)  # Pausa para observar el resultado
            visualizer.reset_colors()  # Prepara para el siguiente paso
    
    return data

def merge_sort_iterative(data: List[float]) -> List[float]:
    """
    Implementación iterativa (bottom-up) de MergeSort.
    No usa recursión, por lo que es más adecuada para listas muy grandes.
    
    Args:
        data: Lista de elementos a ordenar
    
    Returns:
        Lista ordenada de elementos
    """
    n = len(data)
    current_size = 1  # Tamaño inicial de los subarrays a mergear
    
    # Continúa hasta que el tamaño del subarray abarca toda la lista
    while current_size < n:
        left = 0  # Índice izquierdo inicial
        
        # Mergeamos subarrays de tamaño current_size
        while left < n - 1:
            # Calcula los índices mid y right, asegurando no salirnos de los límites
            mid = min(left + current_size - 1, n - 1)
            right = min(left + 2 * current_size - 1, n - 1)
            
            # Mergea los subarrays data[left...mid] y data[mid+1...right]
            merge(data, left, mid, right)
            
            # Avanza al siguiente par de subarrays
            left += 2 * current_size
        
        # Duplica el tamaño para la siguiente iteración
        current_size *= 2
    
    return data

def merge(data: List[float], left: int, mid: int, right: int, 
          visualizer: MergeSortVisualizer = None) -> None:
    """
    Función auxiliar que une dos subarrays ordenados en un solo array ordenado.
    
    Args:
        data: Lista original que contiene los subarrays
        left: Índice izquierdo del primer subarray
        mid: Índice final del primer subarray
        right: Índice final del segundo subarray
        visualizer: Objeto para visualización (opcional)
    """
    temp = []  # Array temporal para almacenar el resultado
    i = left    # Índice para el primer subarray
    j = mid + 1 # Índice para el segundo subarray
    
    # Compara elementos de ambos subarrays y copia el menor al array temporal
    while i <= mid and j <= right:
        if data[i] <= data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1
        
        # Actualiza contadores de comparaciones y operaciones si hay visualizador
        if visualizer:
            visualizer.comparisons += 1
            visualizer.operations += 1
    
    # Copia los elementos restantes del primer subarray, si los hay
    while i <= mid:
        temp.append(data[i])
        i += 1
        if visualizer:
            visualizer.operations += 1
    
    # Copia los elementos restantes del segundo subarray, si los hay
    while j <= right:
        temp.append(data[j])
        j += 1
        if visualizer:
            visualizer.operations += 1
    
    # Copia los elementos ordenados del array temporal al array original
    for k in range(len(temp)):
        data[left + k] = temp[k]
        if visualizer:
            visualizer.operations += 1
            # Actualiza la visualización durante el merge
            visualizer.update_plot(left, right, True, 
                                 f"Uniendo: {left}-{right}")

def parallel_merge_sort(data: List[float], max_workers: int = 4) -> List[float]:
    """
    Implementación paralela de MergeSort que usa ThreadPoolExecutor
    para ordenar subarrays en hilos separados.
    
    Args:
        data: Lista de elementos a ordenar
        max_workers: Número máximo de hilos a usar
    
    Returns:
        Lista ordenada de elementos
    """
    # Caso base: arrays de tamaño 0 o 1 ya están ordenados
    if len(data) <= 1:
        return data
    
    # Punto medio para dividir el array
    mid = len(data) // 2
    
    # Crea un ThreadPoolExecutor para manejar los hilos
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Ordena la primera mitad en un hilo
        left_future = executor.submit(parallel_merge_sort, data[:mid], max_workers)
        # Ordena la segunda mitad en otro hilo
        right_future = executor.submit(parallel_merge_sort, data[mid:], max_workers)
        
        # Obtiene los resultados de ambos hilos
        left = left_future.result()
        right = right_future.result()
    
    # Une las dos mitades ordenadas
    return merge_parallel(left, right)

def merge_parallel(left: List[float], right: List[float]) -> List[float]:
    """
    Función auxiliar para unir dos listas ordenadas.
    Versión simplificada de merge() para usar con la implementación paralela.
    
    Args:
        left: Primera lista ordenada
        right: Segunda lista ordenada
    
    Returns:
        Lista combinada ordenada
    """
    result = []
    i = j = 0  # Índices para ambas listas
    
    # Compara elementos de ambas listas y añade el menor al resultado
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Añade los elementos restantes de ambas listas
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def benchmark_sorting(data: List[float], sort_func: Callable, 
                     func_name: str, **kwargs) -> dict:
    """
    Ejecuta una función de ordenamiento y mide su tiempo de ejecución.
    También verifica que el resultado esté correctamente ordenado.
    
    Args:
        data: Datos a ordenar
        sort_func: Función de ordenamiento a evaluar
        func_name: Nombre descriptivo de la función
        kwargs: Argumentos adicionales para la función de ordenamiento
    
    Returns:
        Diccionario con los resultados del benchmark:
        - name: Nombre del algoritmo
        - time: Tiempo de ejecución en segundos
        - sorted_data: Datos ordenados
        - is_sorted: Booleano que indica si el resultado está correctamente ordenado
    """
    # Crea una copia para no modificar los datos originales
    data_copy = data.copy()
    
    # Mide el tiempo de ejecución
    start_time = time.time()
    
    # Ejecuta la función de ordenamiento con los argumentos adicionales si los hay
    sorted_data = sort_func(data_copy, **kwargs) if kwargs else sort_func(data_copy)
    
    end_time = time.time()
    
    # Retorna un diccionario con los resultados
    return {
        'name': func_name,
        'time': end_time - start_time,
        'sorted_data': sorted_data,
        'is_sorted': sorted_data == sorted(data_copy)  # Verifica el orden
    }

def apply_to_ai_dataset(data: np.ndarray, sort_func: Callable) -> np.ndarray:
    """
    Aplica ordenamiento a un dataset de IA, normalizando y ordenando cada característica.
    
    Args:
        data: Dataset numpy (muestras x características)
        sort_func: Función de ordenamiento a aplicar
    
    Returns:
        Dataset con las características ordenadas individualmente
    """
    # Normaliza cada característica al rango [0, 1]
    normalized_data = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))
    
    # Ordena cada columna (característica) independientemente
    sorted_features = []
    for col in range(normalized_data.shape[1]):
        sorted_col = sort_func(normalized_data[:, col].tolist())
        sorted_features.append(sorted_col)
    
    # Reconstruye la matriz con las características ordenadas
    return np.column_stack(sorted_features)

if __name__ == "__main__":
    """
    Bloque principal que se ejecuta cuando el script es llamado directamente.
    Realiza demostraciones del algoritmo en diferentes escenarios:
    1. Visualización animada con un dataset pequeño
    2. Benchmark de diferentes implementaciones
    3. Aplicación a un dataset de IA
    """
    
    # Configuración inicial
    np.random.seed(42)  # Para reproducibilidad
    original_data = np.random.randint(0, 100, 20).tolist()  # Dataset pequeño para visualización
    large_data = np.random.randint(0, 10000, 10000).tolist()  # Dataset grande para benchmark
    
    # 1. Demostración con visualización
    print("=== Visualización de MergeSort ===")
    visualizer = MergeSortVisualizer(original_data)  # Crea el visualizador
    plt.ion()  # Activa el modo interactivo de matplotlib
    sorted_data = merge_sort_recursive(original_data.copy(), visualizer)  # Ordena con visualización
    plt.ioff()  # Desactiva el modo interactivo
    plt.show()  # Muestra la ventana con la visualización final
    print("Datos ordenados:", sorted_data)
    print(f"Comparaciones: {visualizer.comparisons}, Operaciones: {visualizer.operations}")
    
    # 2. Comparación de rendimiento entre implementaciones
    print("\n=== Benchmark de Implementaciones ===")
    # Lista de algoritmos a comparar
    algorithms = [
        (merge_sort_recursive, "Recursivo"),
        (merge_sort_iterative, "Iterativo"),
        (parallel_merge_sort, "Paralelo (4 hilos)"),
        (sorted, "Timsort (Python built-in)")  # Algoritmo nativo de Python como referencia
    ]
    
    results = []  # Almacena los resultados del benchmark
    for algo, name in algorithms:
        # Para la versión recursiva, usa un subconjunto por limitaciones de recursión
        if name == "Recursivo":
            test_data = large_data[:1000].copy()
        else:
            test_data = large_data.copy()
        
        # Ejecuta el benchmark y guarda resultados
        result = benchmark_sorting(test_data, algo, name)
        results.append(result)
        print(f"{name}: {result['time']:.4f} segundos - Ordenado: {result['is_sorted']}")
    
    # 3. Aplicación en IA: Procesamiento de características
    print("\n=== Aplicación en IA: Ordenamiento de Características ===")
    # Crea un dataset ficticio (100 muestras, 5 características)
    ai_data = np.random.rand(100, 5) * 100
    print("Dataset original (primeras 5 filas):")
    print(ai_data[:5])  # Muestra las primeras 5 filas
    
    # Procesa el dataset ordenando cada característica
    processed_data = apply_to_ai_dataset(ai_data, merge_sort_iterative)
    print("\nDataset con características ordenadas (primeras 5 filas):")
    print(processed_data[:5])
    
    # 4. Gráfico comparativo de los tiempos de ejecución
    plt.figure(figsize=(12, 6))  # Crea una nueva figura
    # Gráfico de barras con los nombres y tiempos de cada algoritmo
    plt.bar([r['name'] for r in results], [r['time'] for r in results])
    plt.title("Comparación de Tiempos de Ejecución")
    plt.ylabel("Tiempo (segundos)")
    plt.yscale('log')  # Escala logarítmica para mejor visualización de diferencias
    plt.show()  # Muestra el gráfico
# Importamos el módulo math para usar la función floor()
import math

def bucket_sort(arr, bucket_size=10):
    """
    Implementación detallada del algoritmo Bucket Sort para ordenar números flotantes.
    
    Este algoritmo es particularmente eficiente cuando los datos están uniformemente distribuidos
    en un rango conocido. Funciona dividiendo el rango de entrada en 'cubetas' (buckets),
    distribuyendo los elementos en estas cubetas, ordenando cada cubeta individualmente,
    y finalmente concatenando los resultados.
    
    Parámetros:
        arr (list): Lista de números flotantes a ordenar. Idealmente en el rango [0,1).
        bucket_size (int): Cantidad de cubetas a utilizar. Por defecto 10.
        
    Retorna:
        list: Lista ordenada de los elementos de entrada.
        
    Complejidad:
        - Mejor caso: O(n + k) cuando los datos están uniformemente distribuidos
        - Peor caso: O(n^2) cuando todos los elementos caen en la misma cubeta
    """
    
    # --- PASO 1: Validación de entrada ---
    # Si la lista está vacía, retornamos inmediatamente
    if len(arr) == 0:
        return arr

    # --- PASO 2: Encontrar rango de valores ---
    # Calculamos el valor mínimo y máximo para normalizar los datos
    min_val = min(arr)  # Valor mínimo en la lista
    max_val = max(arr)  # Valor máximo en la lista
    
    # --- PASO 3: Inicialización de cubetas ---
    # Creamos una lista de listas vacías para representar las cubetas
    # Usamos una comprensión de lista para crear 'bucket_size' cubetas vacías
    buckets = [[] for _ in range(bucket_size)]
    
    # --- PASO 4: Distribución de elementos en cubetas ---
    # Iteramos sobre cada número en la lista de entrada
    for num in arr:
        # Normalizamos el número al rango [0,1) para asignarlo a una cubeta
        # Añadimos 1e-10 (un valor muy pequeño) para evitar división por cero
        # en caso de que min_val == max_val
        normalized = (num - min_val) / (max_val - min_val + 1e-10)
        
        # Calculamos el índice de la cubeta multiplicando por el número de cubetas
        # y tomando el piso del resultado con math.floor()
        bucket_idx = math.floor(normalized * bucket_size)
        
        # Aseguramos que el índice esté dentro de los límites válidos
        # usando max() y min() para evitar índices fuera de rango
        bucket_idx = max(0, min(bucket_idx, bucket_size - 1))
        
        # Añadimos el número a la cubeta correspondiente
        buckets[bucket_idx].append(num)
    
    # --- PASO 5: Ordenamiento interno de cubetas ---
    # Iteramos sobre cada cubeta para ordenar sus elementos
    # Usamos el método sort() de Python que implementa TimSort (híbrido de MergeSort e InsertionSort)
    for bucket in buckets:
        bucket.sort()  # Ordenamos in-place para ahorrar memoria
    
    # --- PASO 6: Concatenación de resultados ---
    # Creamos una lista vacía para almacenar el resultado final
    sorted_arr = []
    
    # Iteramos sobre cada cubeta ya ordenada
    for bucket in buckets:
        # Extendemos la lista resultado con los elementos de la cubeta actual
        # extend() es más eficiente que + para listas grandes
        sorted_arr.extend(bucket)
    
    # Retornamos la lista completamente ordenada
    return sorted_arr


# --- EJEMPLO DE USO Y DEMOSTRACIÓN ---
if __name__ == "__main__":
    # Datos de ejemplo: valores de probabilidades típicos en modelos de IA
    # Estos valores representan salidas de un clasificador, por ejemplo
    data = [0.42, 0.32, 0.87, 0.12, 0.99, 0.55, 0.73, 0.01, 0.25, 0.68]
    
    # Mostramos los datos originales
    print("Datos originales:", data)
    
    # Ordenamos los datos usando Bucket Sort con 5 cubetas
    # Usamos 5 cubetas para demostrar cómo se distribuyen los valores
    sorted_data = bucket_sort(data, bucket_size=5)
    
    # Mostramos el resultado ordenado
    print("Datos ordenados:", sorted_data)
  
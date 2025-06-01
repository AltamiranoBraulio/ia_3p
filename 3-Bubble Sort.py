"""
Bubble Sort - Implementación Hiper-Comentada

Este bloque es un docstring multi-línea que sirve como documentación general del módulo.
Explica que Bubble Sort es un algoritmo simple pero ineficiente para listas grandes,
y menciona sus aplicaciones en IA para pequeños conjuntos de datos o como componente
de algoritmos más complejos.
"""

def bubble_sort(arr, ascending=True, verbose=False):
    """
    Función principal de Bubble Sort con parámetros adicionales para controlar el orden
    y mostrar el proceso detallado.
    
    Args (Argumentos):
        arr (list): La lista de elementos a ordenar. Puede ser números, strings o cualquier
                   tipo comparable con operadores > y <
        ascending (bool): Bandera que determina el orden. True para ascendente (default),
                         False para descendente
        verbose (bool): Si es True, muestra información detallada del proceso de ordenamiento
        
    Returns (Retorna):
        list: Una nueva lista con los elementos ordenados (no modifica la original)
        
    Complejidad Computacional:
        - Mejor caso (lista ya ordenada): O(n) - solo requiere una pasada
        - Peor caso (lista en orden inverso): O(n^2) - requiere n*(n-1)/2 comparaciones
    """
    
    # Creamos una copia de la lista original para no modificarla directamente
    # Esto es importante para mantener inmutabilidad en el parámetro de entrada
    sorted_arr = arr.copy()
    
    # Obtenemos la longitud de la lista una vez para no calcularla en cada iteración
    n = len(sorted_arr)
    
    # Bucle externo: controla el número total de pasadas necesarias
    # En el peor caso necesitamos n-1 pasadas para ordenar completamente la lista
    for i in range(n):
        
        # Si verbose está activado, imprimimos información de la pasada actual
        if verbose:
            # Usamos f-strings para formatear el mensaje con el número de pasada
            print(f"\nPasada {i+1}:")
        
        # Flag (bandera) de optimización: indica si hubo al menos un intercambio
        # en esta pasada. Inicialmente asumimos que no hubo intercambios.
        swapped = False
        
        # Bucle interno: realiza las comparaciones entre elementos adyacentes
        # El rango disminuye con cada pasada externa porque los elementos más
        # grandes ya están en su posición correcta (n-i-1)
        for j in range(0, n-i-1):
            
            # Si verbose está activado, mostramos qué elementos estamos comparando
            if verbose:
                # Usamos end="" para evitar salto de línea y poder agregar el resultado después
                print(f"  Comparando {sorted_arr[j]} y {sorted_arr[j+1]}", end="")
            
            # Condición de ordenamiento: depende del parámetro 'ascending'
            # Para orden ascendente, comparamos si el actual es mayor que el siguiente
            # Para orden descendente, comparamos si el actual es menor que el siguiente
            if (ascending and sorted_arr[j] > sorted_arr[j+1]) or (not ascending and sorted_arr[j] < sorted_arr[j+1]):
                
                # Realizamos el intercambio (swap) de elementos usando asignación múltiple
                # Esta es la forma pitónica de intercambiar valores en Python
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
                
                # Marcamos que hubo un intercambio en esta pasada
                swapped = True
                
                # Si verbose está activado, indicamos que se hizo un intercambio
                if verbose:
                    print(" -> Intercambiados")
            else:
                # Si verbose está activado, indicamos que no hubo intercambio
                if verbose:
                    print(" -> No se intercambian")
        
        # Optimización: si no hubo intercambios en toda la pasada, la lista ya está ordenada
        if not swapped:
            if verbose:
                print("  No hubo intercambios en esta pasada. Terminando temprano.")
            # Salimos del bucle externo prematuramente
            break
            
        # Si verbose está activado, mostramos el estado actual de la lista
        if verbose:
            print(f"  Estado actual: {sorted_arr}")
    
    # Retornamos la lista ordenada
    return sorted_arr


# Versión con visualización gráfica del proceso
def bubble_sort_visual(arr, title="Bubble Sort"):
    """
    Versión especial de Bubble Sort que muestra una visualización gráfica animada
    del proceso de ordenamiento, usando matplotlib.
    
    Args:
        arr (list): Lista de números a ordenar
        title (str): Título opcional para la visualización gráfica
        
    Returns:
        list: La lista ordenada (modifica la lista original)
    """
    # Importamos las librerías necesarias para la visualización
    # Estos imports están aquí y no al inicio para que sean opcionales
    import matplotlib.pyplot as plt
    import time
    
    # Creamos una figura y eje para nuestro gráfico
    fig, ax = plt.subplots()
    
    # Creamos las barras iniciales del gráfico
    # Usamos un color 'skyblue' para las barras
    bars = ax.bar(range(len(arr)), arr, color='skyblue')
    
    # Establecemos el título del gráfico
    ax.set_title(title)
    
    # Obtenemos la longitud de la lista
    n = len(arr)
    
    # Bucle externo (mismo principio que en bubble_sort)
    for i in range(n):
        swapped = False
        
        # Bucle interno
        for j in range(0, n-i-1):
            # Comparamos elementos adyacentes
            if arr[j] > arr[j+1]:
                # Intercambiamos los elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
                # Actualizamos la visualización:
                # 1. Actualizamos la altura de cada barra
                for bar, height in zip(bars, arr):
                    bar.set_height(height)
                
                # 2. Actualizamos la etiqueta del eje x con información del paso actual
                ax.set_xlabel(f"Pasada {i+1}, Comparación {j+1}: Intercambiando {arr[j+1]} y {arr[j]}")
                
                # 3. Pausamos brevemente para crear el efecto de animación
                plt.pause(0.1)
        
        # Si no hubo intercambios, terminamos temprano
        if not swapped:
            break
    
    # Mostramos el gráfico final
    plt.show()
    
    # Retornamos la lista ordenada
    return arr


# Bloque principal de ejecución
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo cuando el script es llamado directamente,
    no cuando es importado como módulo. Contiene ejemplos de uso.
    """
    
    # Caso 1: Ordenamiento básico con verbosity
    print("=== EJEMPLO BÁSICO ===")
    
    # Creamos una lista de ejemplo
    datos = [64, 34, 25, 12, 22, 11, 90]
    
    # Mostramos los datos originales
    print("Datos originales:", datos)
    
    # Ordenamos con verbosity activado
    datos_ordenados = bubble_sort(datos, verbose=True)
    
    # Mostramos el resultado final
    print("\nResultado final:", datos_ordenados)
    
    # Caso 2: Ordenamiento descendente
    print("\n=== ORDENAMIENTO DESCENDENTE ===")
    
    # Mostramos mensaje explicativo
    print("Ordenamiento descendente:")
    
    # Ordenamos en orden descendente con verbosity
    datos_desc = bubble_sort(datos, ascending=False, verbose=True)
    
    # Mostramos resultado final descendente
    print("\nResultado final descendente:", datos_desc)
    
    # Caso 3: Visualización gráfica (comentado por defecto)
    # print("\n=== VISUALIZACIÓN GRÁFICA ===")
    # datos_visual = [64, 34, 25, 12, 22, 11, 90]
    # bubble_sort_visual(datos_visual)
    # print("Datos después de visualización:", datos_visual)


"""
SECCIÓN DE APLICACIONES EN INTELIGENCIA ARTIFICIAL

Esta sección documenta posibles usos de Bubble Sort en el campo de IA,
a pesar de no ser el algoritmo más eficiente, tiene nichos de aplicación.
"""

"""
Aplicaciones de Bubble Sort en IA:

1. Procesamiento de pequeñas muestras de datos:
   - En algoritmos online que procesan datos en pequeños lotes
   - Ejemplo concreto: Actualización de pesos en una red neuronal con pocas características
     donde el overhead de algoritmos más complejos no justifica su uso

2. Educación y debugging:
   - Como herramienta pedagógica para enseñar conceptos básicos de ordenamiento
   - Para verificar el comportamiento de sistemas de aprendizaje automático en etapas tempranas
     de desarrollo, donde la simplicidad es más importante que la eficiencia

3. Preprocesamiento de datos:
   - En pipelines de datos donde se trabaja con conjuntos muy pequeños
   - Caso de uso: Ordenar las primeras n muestras en un stream de datos antes de aplicar
     transformaciones más complejas

4. Como componente de algoritmos más complejos:
   - En combinación con otros métodos para casos específicos donde Bubble Sort puede ser
     más eficiente para pequeños segmentos de datos casi ordenados
"""


# Versión especializada para IA con función key
def bubble_sort_key(arr, key_func, ascending=True):
    """
    Variante de Bubble Sort que acepta una función key para determinar el orden,
    similar al parámetro key en la función sorted() de Python.
    
    Args:
        arr (list): Lista a ordenar (puede contener elementos complejos)
        key_func (function): Función que extrae el valor clave para comparación
        ascending (bool): Controla el orden (True=ascendente, False=descendente)
        
    Returns:
        list: Lista ordenada (modifica la lista original)
    """
    # Obtenemos la longitud de la lista
    n = len(arr)
    
    # Bucle externo
    for i in range(n):
        swapped = False
        
        # Bucle interno
        for j in range(0, n-i-1):
            # Aplicamos la función key a los elementos a comparar
            a = key_func(arr[j])
            b = key_func(arr[j+1])
            
            # Condición de ordenamiento considerando la dirección
            if (a > b and ascending) or (a < b and not ascending):
                # Intercambiamos los elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # Optimización: salir temprano si no hubo intercambios
        if not swapped:
            break
    
    return arr


# Ejemplos de uso con key function
if __name__ == "__main__":
    """
    Ejemplos adicionales que muestran el uso de la versión con key function,
    particularmente útil para ordenar estructuras de datos complejas.
    """
    
    print("\n=== EJEMPLOS CON KEY FUNCTION ===")
    
    # Creamos una lista de diccionarios para demostración
    datos_complejos = [
        {'nombre': 'Alice', 'edad': 25},
        {'nombre': 'Bob', 'edad': 30},
        {'nombre': 'Charlie', 'edad': 20}
    ]
    
    # Caso 1: Ordenamiento por edad
    print("\nOrdenamiento por edad:")
    
    # Ordenamos usando una lambda function que extrae la edad
    ordenado_edad = bubble_sort_key(datos_complejos.copy(), key_func=lambda x: x['edad'])
    
    # Mostramos resultado
    print(ordenado_edad)
    
    # Caso 2: Ordenamiento por nombre
    print("\nOrdenamiento por nombre:")
    
    # Ordenamos usando una lambda function que extrae el nombre
    ordenado_nombre = bubble_sort_key(datos_complejos.copy(), key_func=lambda x: x['nombre'])
    
    # Mostramos resultado
    print(ordenado_nombre)
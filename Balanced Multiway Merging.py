# Importamos las librerías necesarias:
# - heapq: Para usar estructuras de datos de tipo "min-heap" (cola de prioridad).
# - os: Para operaciones con archivos (ej. eliminar archivos temporales).
# - random: Para generar números aleatorios.
import heapq
import os
import random

# --- FUNCIÓN 1: Generar un archivo con datos aleatorios ---
def generate_large_file(filename, size=1_000_000, max_num=10_000):
    """
    Genera un archivo con números aleatorios para simular un dataset grande.
    
    Args:
        filename (str): Nombre del archivo donde se guardarán los datos.
        size (int): Cantidad de números a generar (por defecto 1,000,000).
        max_num (int): Valor máximo de los números generados (por defecto 10,000).
    """
    # Abre el archivo en modo escritura ('w')
    with open(filename, 'w') as f:
        # Genera 'size' números aleatorios y los escribe en el archivo
        for _ in range(size):
            # Escribe un número aleatorio entre 1 y max_num, seguido de un salto de línea
            f.write(f"{random.randint(1, max_num)}\n")

# --- FUNCIÓN 2: Ordenar un chunk en memoria ---
def sort_chunk(chunk):
    """
    Ordena una lista (chunk) de números en memoria usando el método sorted() de Python.
    
    Args:
        chunk (list): Lista de números a ordenar.
    
    Returns:
        list: Lista ordenada.
    """
    return sorted(chunk)  # Retorna la lista ordenada

# --- FUNCIÓN 3: Dividir el archivo en runs ordenados ---
def split_into_sorted_runs(filename, chunk_size=100_000):
    """
    Divide un archivo grande en chunks más pequeños, los ordena y guarda en archivos temporales.
    
    Args:
        filename (str): Nombre del archivo grande a procesar.
        chunk_size (int): Tamaño de cada chunk (por defecto 100,000 líneas).
    
    Returns:
        list: Lista con los nombres de los archivos temporales generados.
    """
    temp_files = []  # Almacena los nombres de los archivos temporales
    
    # Abre el archivo grande en modo lectura ('r')
    with open(filename, 'r') as f:
        i = 0  # Contador para nombrar los archivos temporales
        
        # Bucle infinito hasta que se procese todo el archivo
        while True:
            chunk = []  # Lista para almacenar los números del chunk actual
            
            # Lee 'chunk_size' líneas del archivo
            for _ in range(chunk_size):
                line = f.readline()  # Lee una línea
                if not line:  # Si no hay más líneas, termina el bucle
                    break
                chunk.append(int(line))  # Convierte la línea a entero y la añade al chunk
            
            # Si el chunk está vacío, termina el proceso
            if not chunk:
                break
            
            # Ordena el chunk en memoria
            chunk_sorted = sort_chunk(chunk)
            
            # Crea un nombre para el archivo temporal (ej. 'temp_run_0.txt')
            temp_file = f'temp_run_{i}.txt'
            
            # Escribe el chunk ordenado en el archivo temporal
            with open(temp_file, 'w') as tf:
                # Convierte los números a strings y los une con saltos de línea
                tf.write('\n'.join(map(str, chunk_sorted)))
            
            # Añade el nombre del archivo temporal a la lista
            temp_files.append(temp_file)
            i += 1  # Incrementa el contador para el próximo archivo
    
    return temp_files  # Retorna la lista de archivos temporales

# --- FUNCIÓN 4: Mezcla multiway de los runs ordenados ---
def multiway_merge(temp_files, output_file='sorted_output.txt'):
    """
    Mezcla los archivos temporales (runs ordenados) en un único archivo ordenado usando un min-heap.
    
    Args:
        temp_files (list): Lista de nombres de archivos temporales.
        output_file (str): Nombre del archivo de salida ordenado (por defecto 'sorted_output.txt').
    """
    handles = []  # Almacena los descriptores de archivo (file handles)
    
    # Abre cada archivo temporal en modo lectura y guarda su descriptor
    for file in temp_files:
        handles.append(open(file, 'r'))
    
    heap = []  # Estructura de min-heap para mezcla eficiente
    
    # Inicializa el heap con el primer elemento de cada archivo temporal
    for i, handle in enumerate(handles):
        line = handle.readline()  # Lee la primera línea del archivo
        if line:  # Si la línea no está vacía
            # Añade una tupla (número, índice_archivo) al heap
            heapq.heappush(heap, (int(line), i))
    
    # Abre el archivo de salida en modo escritura
    with open(output_file, 'w') as out:
        # Mientras el heap no esté vacío
        while heap:
            # Extrae el número más pequeño del heap
            num, i = heapq.heappop(heap)
            # Escribe el número en el archivo de salida, seguido de un salto de línea
            out.write(f"{num}\n")
            
            # Lee el siguiente número del archivo que contenía el número extraído
            next_line = handles[i].readline()
            if next_line:  # Si hay más números en el archivo
                # Añade el nuevo número al heap
                heapq.heappush(heap, (int(next_line), i))
    
    # Cierra todos los descriptores de archivo
    for handle in handles:
        handle.close()
    
    # Elimina los archivos temporales
    for file in temp_files:
        os.remove(file)

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    # Nombre del archivo de entrada y salida
    input_file = 'large_data.txt'
    output_file = 'sorted_data.txt'
    
    # Paso 1: Generar archivo con datos aleatorios
    print("✅ Generando archivo grande con datos aleatorios...")
    generate_large_file(input_file, size=1_000_000)
    
    # Paso 2: Dividir en runs ordenados
    print("🔀 Dividiendo en runs ordenados...")
    temp_files = split_into_sorted_runs(input_file, chunk_size=100_000)
    
    # Paso 3: Mezclar multiway
    print("🧠 Mezclando multiway...")
    multiway_merge(temp_files, output_file)
    
    # Mensaje final
    print(f"✨ ¡Datos ordenados guardados en '{output_file}'!")
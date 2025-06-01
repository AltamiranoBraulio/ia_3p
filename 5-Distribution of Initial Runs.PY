"""
Distribution of Initial Runs - Algoritmo para ordenamiento externo de grandes archivos

Este bloque de documentación (docstring) explica que este algoritmo está diseñado
para ordenar archivos demasiado grandes para caber en la memoria principal RAM.
La estrategia consiste en dividir los datos en segmentos llamados "runs" que sí caben
en memoria, ordenarlos individualmente, y luego mezclarlos de manera eficiente.
"""

# Importación de módulos necesarios:
# os - Para operaciones con el sistema de archivos
# heapq - Para implementar la cola de prioridad (min-heap) usada en la mezcla
# TemporaryFile - Para crear archivos temporales (aunque no se usa directamente aquí)
# partial - Para crear funciones parciales (aunque no se usa directamente aquí)
import os
import heapq
from tempfile import TemporaryFile
from functools import partial

def sort_and_save_chunk(chunk, chunk_size, temp_dir, run_number):
    """
    Esta función toma un fragmento (chunk) de datos, lo ordena en memoria y lo guarda
    en un archivo temporal como un "run" ordenado.
    
    Args (Argumentos):
        chunk (list): Lista de elementos a ordenar (normalmente números)
        chunk_size (int): Tamaño máximo que puede tener el chunk (para verificación)
        temp_dir (str): Directorio donde se guardarán los archivos temporales
        run_number (int): Número secuencial para identificar este run
        
    Returns (Retorna):
        str: La ruta completa al archivo temporal creado con los datos ordenados
    """
    # Primero ordenamos el chunk en memoria usando el método sort() de Python
    # que implementa TimSort (un algoritmo híbrido eficiente)
    chunk.sort()
    
    # Construimos la ruta completa para el archivo temporal usando os.path.join
    # que maneja correctamente las diferencias entre sistemas operativos
    temp_file_path = os.path.join(temp_dir, f"run_{run_number}.tmp")
    
    # Abrimos el archivo en modo escritura ('w') usando un context manager (with)
    # que se encargará de cerrar el archivo automáticamente al terminar
    with open(temp_file_path, 'w') as f:
        # Escribimos cada elemento del chunk ordenado en una línea separada
        for item in chunk:
            f.write(f"{item}\n")  # f-string para formateo moderno
    
    # Retornamos la ruta al archivo temporal creado
    return temp_file_path

def create_initial_runs(input_file, chunk_size, temp_dir):
    """
    Esta función lee el archivo de entrada grande y lo divide en runs (segmentos)
    ordenados de tamaño manejable, guardando cada run en un archivo temporal.
    
    Args:
        input_file (str): Ruta al archivo de entrada que contiene los datos a ordenar
        chunk_size (int): Número máximo de elementos que contendrá cada run
        temp_dir (str): Directorio donde se guardarán los archivos temporales
        
    Returns:
        list: Lista de rutas a los archivos temporales creados (los runs ordenados)
    """
    # Inicializamos una lista vacía para almacenar las rutas de los archivos temporales
    runs = []
    
    # Contador para asignar números únicos a cada run
    run_number = 0
    
    # Lista temporal para acumular los elementos del chunk actual
    current_chunk = []
    
    # Abrimos el archivo de entrada en modo lectura ('r') usando un context manager
    with open(input_file, 'r') as f:
        # Leemos el archivo línea por línea (para manejar archivos grandes)
        for line in f:
            # Convertimos la línea a entero y la añadimos al chunk actual
            # strip() elimina espacios en blanco y saltos de línea
            current_chunk.append(int(line.strip()))
            
            # Cuando el chunk actual alcanza el tamaño máximo permitido
            if len(current_chunk) == chunk_size:
                # Ordenamos y guardamos el chunk actual como un run temporal
                runs.append(sort_and_save_chunk(current_chunk, chunk_size, temp_dir, run_number))
                
                # Reiniciamos el chunk actual para comenzar uno nuevo
                current_chunk = []
                
                # Incrementamos el contador de runs
                run_number += 1
        
        # Después de leer todo el archivo, verificamos si quedó algún dato en el chunk
        if current_chunk:
            # Ordenamos y guardamos el último chunk (que puede ser menor que chunk_size)
            runs.append(sort_and_save_chunk(current_chunk, chunk_size, temp_dir, run_number))
    
    # Retornamos la lista con las rutas de todos los runs creados
    return runs

def merge_runs(run_files, output_file):
    """
    Esta función toma múltiples archivos con runs ordenados y los mezcla
    en un único archivo de salida completamente ordenado, usando un min-heap.
    
    Args:
        run_files (list): Lista de rutas a los archivos con los runs ordenados
        output_file (str): Ruta donde se guardará el resultado ordenado final
    """
    # Abrimos todos los archivos de runs en modo lectura
    # Usamos una lista comprehension para crear una lista de file handles
    file_handles = [open(run_file, 'r') for run_file in run_files]
    
    # Inicializamos un min-heap (cola de prioridad) vacío
    heap = []
    
    # Inicializamos el heap con el primer elemento de cada run
    # enumerate nos da tanto el índice como el file handle
    for i, fh in enumerate(file_handles):
        # Leemos la primera línea de cada archivo
        line = fh.readline()
        
        # Si el archivo no está vacío, añadimos su primer elemento al heap
        if line:
            # La tupla contiene (valor, índice_archivo) para saber de dónde vino
            heapq.heappush(heap, (int(line.strip()), i))
    
    # Abrimos el archivo de salida en modo escritura
    with open(output_file, 'w') as out_f:
        # Mientras el heap no esté vacío (todavía hay elementos por procesar)
        while heap:
            # Extraemos el elemento más pequeño del heap (raíz del min-heap)
            smallest, file_idx = heapq.heappop(heap)
            
            # Escribimos este elemento en el archivo de salida
            out_f.write(f"{smallest}\n")
            
            # Leemos el siguiente elemento del run del que provino el elemento que acabamos de procesar
            next_line = file_handles[file_idx].readline()
            
            # Si todavía hay elementos en ese run, lo añadimos al heap
            if next_line:
                heapq.heappush(heap, (int(next_line.strip()), file_idx))
    
    # Cerramos todos los archivos de runs que habíamos abierto
    for fh in file_handles:
        fh.close()

def external_sort(input_file, output_file, chunk_size=100000, temp_dir='./temp'):
    """
    Función principal que coordina todo el proceso de ordenamiento externo:
    1. Crear runs iniciales ordenados
    2. Mezclar los runs en un archivo final ordenado
    3. Limpiar archivos temporales
    
    Args:
        input_file (str): Ruta al archivo de entrada con datos desordenados
        output_file (str): Ruta donde se guardará el archivo ordenado
        chunk_size (int): Tamaño máximo de cada run (default: 100,000 elementos)
        temp_dir (str): Directorio para archivos temporales (default: './temp')
    """
    # Creamos el directorio temporal si no existe
    # exist_ok=True evita errores si el directorio ya existe
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Paso 1: Crear los runs iniciales ordenados
        print("Creando runs iniciales...")
        runs = create_initial_runs(input_file, chunk_size, temp_dir)
        print(f"Creados {len(runs)} runs ordenados")
        
        # Paso 2: Mezclar todos los runs en un archivo ordenado final
        print("Mezclando runs...")
        merge_runs(runs, output_file)
        print("Mezcla completada")
        
    finally:
        # Bloque finally asegura que la limpieza se ejecute incluso si hay errores
        print("Limpiando archivos temporales...")
        for run_file in runs:
            try:
                # Intentamos eliminar cada archivo temporal
                os.remove(run_file)
            except:
                # Si hay algún error (ej. archivo no existe), lo ignoramos
                pass

def generate_large_file(file_path, num_items=1000000, max_num=1000000):
    """
    Función auxiliar para generar archivos grandes con datos aleatorios de prueba.
    
    Args:
        file_path (str): Ruta donde se creará el archivo
        num_items (int): Número de elementos a generar (default: 1,000,000)
        max_num (int): Valor máximo de los números aleatorios (default: 1,000,000)
    """
    import random
    # Abrimos el archivo en modo escritura
    with open(file_path, 'w') as f:
        # Generamos num_items números aleatorios
        for _ in range(num_items):
            # Escribimos cada número en una línea separada
            f.write(f"{random.randint(1, max_num)}\n")

if __name__ == "__main__":
    """
    Bloque principal que se ejecuta cuando el script es invocado directamente.
    Configura y ejecuta todo el proceso de ordenamiento externo.
    """
    
    # Configuración de rutas y parámetros
    INPUT_FILE = "large_input.txt"  # Archivo de entrada con datos desordenados
    OUTPUT_FILE = "sorted_output.txt"  # Archivo de salida ordenado
    CHUNK_SIZE = 100000  # Número de elementos por run (ajustar según memoria disponible)
    
    # Paso 0: Generar archivo de prueba con datos aleatorios
    # (Comentar esta línea si ya se tiene un archivo de entrada)
    print("Generando archivo de prueba...")
    generate_large_file(INPUT_FILE)
    
    # Paso 1-2: Ejecutar el ordenamiento externo completo
    print("\nIniciando ordenamiento externo...")
    external_sort(INPUT_FILE, OUTPUT_FILE, CHUNK_SIZE)
    
    # Mensaje final con la ubicación del resultado
    print("\nProceso completado. Archivo ordenado guardado en:", OUTPUT_FILE)
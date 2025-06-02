# Simula el método de ordenamiento Natural Merging aplicado a pedidos de una pastelería

# -----------------------------------------
# Función que detecta "runs" naturales, es decir,
# subsecuencias ordenadas ascendentemente ya presentes en la lista
# -----------------------------------------
def detectar_runs(lista):
    runs = []  # Lista donde se guardarán todas las subsecuencias ordenadas encontradas
    run_actual = [lista[0]]  # Iniciamos la primera subsecuencia con el primer elemento de la lista

    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        # Si el elemento actual es mayor o igual al anterior, continúa la secuencia creciente
        if lista[i] >= lista[i - 1]:
            run_actual.append(lista[i])  # Agregamos el elemento actual a la subsecuencia actual
        else:
            # Si el orden ascendente se rompe, guardamos la subsecuencia completa encontrada
            runs.append(run_actual)
            # Comenzamos una nueva subsecuencia con el elemento actual
            run_actual = [lista[i]]
    
    # Una vez terminada la iteración, agregamos la última subsecuencia encontrada
    runs.append(run_actual)

    # Retornamos la lista de todas las subsecuencias ordenadas naturales encontradas
    return runs

# -----------------------------------------
# Función que fusiona dos subsecuencias (runs) ordenadas en una sola ordenada
# Similar al paso de merge en Merge Sort
# -----------------------------------------
def fusionar_runs(run1, run2):
    resultado = []  # Lista vacía donde se colocarán los elementos fusionados y ordenados
    i = j = 0       # Inicializamos los índices de ambas runs en 0

    # Mientras no hayamos terminado de recorrer alguna de las dos listas
    while i < len(run1) and j < len(run2):
        # Comparar los elementos actuales de ambas listas
        if run1[i] <= run2[j]:
            resultado.append(run1[i])  # Si el elemento de run1 es menor o igual, lo agregamos
            i += 1  # Avanzamos al siguiente elemento de run1
        else:
            resultado.append(run2[j])  # Si el elemento de run2 es menor, lo agregamos
            j += 1  # Avanzamos al siguiente elemento de run2

    # Agregamos al resultado cualquier elemento restante en run1 o run2 (solo una de estas líneas tendrá efecto)
    resultado.extend(run1[i:])
    resultado.extend(run2[j:])

    # Devolvemos la lista fusionada y ordenada
    return resultado

# -----------------------------------------
# Algoritmo principal: Natural Merge Sort
# Utiliza la detección de subsecuencias ordenadas y las fusiona iterativamente
# hasta obtener una única lista ordenada completamente
# -----------------------------------------
def natural_merge_sort(lista):
    # Repetimos el proceso mientras haya más de una subsecuencia ordenada
    while True:
        runs = detectar_runs(lista)  # Identificamos todas las subsecuencias naturales actuales

        # Si solo hay una subsecuencia, la lista ya está completamente ordenada
        if len(runs) == 1:
            break  # Salimos del bucle principal

        nueva_lista = []  # Lista temporal donde iremos colocando las subsecuencias ya fusionadas
        i = 0  # Índice para recorrer la lista de subsecuencias

        # Fusionamos las subsecuencias de dos en dos
        while i < len(runs):
            # Si hay una pareja de runs para fusionar
            if i + 1 < len(runs):
                fusion = fusionar_runs(runs[i], runs[i + 1])  # Fusionamos las dos subsecuencias
                nueva_lista.extend(fusion)  # Agregamos la secuencia resultante a la lista nueva
                i += 2  # Avanzamos dos posiciones porque fusionamos dos runs
            else:
                # Si queda una run sin pareja, la agregamos tal como está
                nueva_lista.extend(runs[i])
                i += 1  # Avanzamos una sola posición

        # La lista original ahora se reemplaza por la nueva fusionada
        lista = nueva_lista

    # Devolvemos la lista completamente ordenada
    return lista

# -----------------------------------------
# Función auxiliar para mostrar la lista de pedidos de forma legible
# Cada pedido contiene un número de ticket y una descripción
# -----------------------------------------
def mostrar_pedidos(pedidos):
    print("📦 Pedidos (ticket - descripción):")
    # Iteramos por cada tupla de pedido y mostramos los datos
    for p in pedidos:
        print(f"🧾 Ticket #{p[0]} - {p[1]}")
    print()  # Línea en blanco al final para mejor formato

# -----------------------------------------
# Bloque principal del programa (se ejecuta si el archivo se ejecuta directamente)
# -----------------------------------------
if __name__ == "__main__":
    # Lista simulada de pedidos. Cada uno es una tupla (número de ticket, descripción del pedido)
    pedidos = [
        (101, "Pastel de chocolate"),      # Ordenado
        (102, "Galletas de vainilla"),     # Ordenado
        (95, "Panqué de limón"),           # Comienza una nueva subsecuencia
        (96, "Cupcakes de zanahoria"),     # Ordenado
        (120, "Brownies"),                 # Ordenado
        (105, "Donas"),                    # Comienza otra subsecuencia
        (106, "Pan de elote"),             # Ordenado
        (89, "Empanadas de fresa")         # Nueva subsecuencia final
    ]

    # Mostramos la lista de pedidos original, tal como fue ingresada
    print("📋 Pedidos en bandeja (desordenados parcialmente):")
    mostrar_pedidos(pedidos)

    # Aplicamos el algoritmo Natural Merge Sort para ordenar los pedidos por número de ticket
    pedidos_ordenados = natural_merge_sort(pedidos)

    # Mostramos el resultado final, completamente ordenado
    print("✅ Pedidos ordenados por número de ticket:")
    mostrar_pedidos(pedidos_ordenados)

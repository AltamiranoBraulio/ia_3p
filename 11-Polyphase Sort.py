import random

# Función que genera un pedido aleatorio con su número de ticket y descripción
def generar_pedido(ticket):
    return (ticket, f"Pedido #{ticket} - Producto random")

# Genera una lista de pedidos desordenados
def generar_pedidos(cantidad):
    tickets = list(range(100, 100 + cantidad))  # Crea una secuencia de tickets
    random.shuffle(tickets)  # Mezcla aleatoriamente los tickets
    return [generar_pedido(t) for t in tickets]  # Devuelve tuplas con el número de ticket y descripción

# Divide la lista de pedidos en pequeñas sublistas (runs) que ya están ordenadas
def dividir_en_runs(lista, tamaño_run):
    runs = []
    for i in range(0, len(lista), tamaño_run):  # Se recorre por bloques del tamaño de run
        run = sorted(lista[i:i + tamaño_run])   # Ordena cada bloque individualmente
        runs.append(run)  # Agrega el bloque ordenado a la lista de runs
    return runs

# Fusión de dos runs ordenadas, similar al merge de Merge Sort
def fusionar_runs(run1, run2):
    resultado = []  # Lista vacía donde se guardará la fusión ordenada
    i = j = 0  # Índices para recorrer run1 y run2

    while i < len(run1) and j < len(run2):
        if run1[i] <= run2[j]:
            resultado.append(run1[i])
            i += 1
        else:
            resultado.append(run2[j])
            j += 1

    # Agrega lo que sobra de cada run
    resultado.extend(run1[i:])
    resultado.extend(run2[j:])
    return resultado

# Implementación simplificada de Polyphase Sort usando 3 cintas (listas)
def polyphase_sort(pedidos, tamaño_run=4):
    runs = dividir_en_runs(pedidos, tamaño_run)  # Paso 1: dividir en runs ordenadas
    buffer = []  # Buffer temporal para almacenar fusiones

    # Mientras haya más de una run para fusionar
    while len(runs) > 1:
        new_runs = []  # Lista para nuevas runs tras fusión

        # Se fusionan de dos en dos
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                # Si hay pareja para fusionar
                fusion = fusionar_runs(runs[i], runs[i + 1])
                new_runs.append(fusion)
            else:
                # Si queda una sola run sin pareja, se pasa tal cual
                new_runs.append(runs[i])

        runs = new_runs  # Actualizamos las runs a las nuevas fusionadas

    return runs[0]  # Solo queda una run, que es la lista completamente ordenada

# Función para mostrar los pedidos de forma legible
def mostrar_pedidos(pedidos):
    for p in pedidos:
        print(f"🧾 Ticket #{p[0]} - {p[1]}")

# Bloque principal
if __name__ == "__main__":
    pedidos = generar_pedidos(20)  # Creamos 20 pedidos aleatorios
    print("📋 Pedidos desordenados:")
    mostrar_pedidos(pedidos)

    pedidos_ordenados = polyphase_sort(pedidos, tamaño_run=4)  # Ordenamos con Polyphase Sort

    print("\n✅ Pedidos ordenados por número de ticket (Polyphase Sort):")
    mostrar_pedidos(pedidos_ordenados)

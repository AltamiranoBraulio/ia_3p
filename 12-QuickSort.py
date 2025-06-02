# ------------------------------------------
# Función que ordena una lista de videojuegos por precio usando el algoritmo QuickSort
# ------------------------------------------

def quicksort_juegos(juegos):
    # Verificamos si la lista es de tamaño 0 o 1. Si es así, ya está ordenada y la devolvemos tal cual.
    if len(juegos) <= 1:
        return juegos

    # Seleccionamos el primer juego de la lista como pivote para comparar los precios
    pivote = juegos[0]

    # Creamos tres listas vacías:
    menores = []  # Aquí guardaremos los juegos con precio menor al del pivote
    iguales = []  # Aquí guardaremos los juegos con precio igual al del pivote
    mayores = []  # Aquí guardaremos los juegos con precio mayor al del pivote

    # Recorremos cada juego en la lista original
    for juego in juegos:
        # Si el precio del juego actual es menor que el del pivote, lo agregamos a la lista 'menores'
        if juego["precio"] < pivote["precio"]:
            menores.append(juego)
        # Si el precio es mayor, lo agregamos a la lista 'mayores'
        elif juego["precio"] > pivote["precio"]:
            mayores.append(juego)
        # Si el precio es igual, lo agregamos a la lista 'iguales'
        else:
            iguales.append(juego)

    # Llamamos recursivamente a la función para ordenar las listas 'menores' y 'mayores'
    # Luego las unimos en orden: menores + iguales + mayores
    return quicksort_juegos(menores) + iguales + quicksort_juegos(mayores)


# ------------------------------------------
# Función para mostrar en pantalla la lista de juegos en un formato amigable
# ------------------------------------------

def mostrar_inventario(juegos):
    # Imprime un título decorado
    print("🎮 Inventario de Juegos:")

    # Recorre la lista de juegos y muestra su información formateada
    for juego in juegos:
        # Se accede a cada campo del diccionario: nombre, género y precio
        print(f"🔸 {juego['nombre']} | Género: {juego['género']} | Precio: ${juego['precio']}")

    # Imprime una línea vacía al final para separación visual
    print()


# ------------------------------------------
# Bloque principal del programa: se ejecuta solo si este archivo se corre directamente
# ------------------------------------------

if __name__ == "__main__":
    # Creamos una lista de diccionarios, cada uno representa un juego con su nombre, género y precio
    inventario = [
        {"nombre": "Elden Ring", "género": "RPG", "precio": 59.99},
        {"nombre": "FIFA 24", "género": "Deportes", "precio": 49.99},
        {"nombre": "Minecraft", "género": "Sandbox", "precio": 26.95},
        {"nombre": "Call of Duty", "género": "Shooter", "precio": 69.99},
        {"nombre": "Stardew Valley", "género": "Simulación", "precio": 14.99},
        {"nombre": "Cyberpunk 2077", "género": "Acción", "precio": 39.99},
        {"nombre": "Hades", "género": "Roguelike", "precio": 24.99},
        {"nombre": "Red Dead Redemption 2", "género": "Western", "precio": 59.99},
    ]

    # Mostramos el inventario original antes de aplicar el ordenamiento
    print("📋 Inventario antes de ordenar:")
    mostrar_inventario(inventario)

    # Ordenamos el inventario con la función quicksort_juegos (sin modificar la lista original)
    inventario_ordenado = quicksort_juegos(inventario)

    # Mostramos el inventario ya ordenado de menor a mayor según el precio
    print("✅ Inventario ordenado por precio (menor a mayor):")
    mostrar_inventario(inventario_ordenado)

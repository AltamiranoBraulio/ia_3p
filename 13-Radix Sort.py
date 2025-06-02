# ------------------------------------------
# Función que aplica el algoritmo Radix Sort a una lista de enteros (puntuaciones)
# ------------------------------------------

def radix_sort(puntuaciones):
    # Encuentra el valor máximo de la lista para saber cuántos dígitos como máximo tiene un número
    max_val = max(puntuaciones)

    # Inicializamos la variable 'exp' con 1, que representa la posición del dígito actual
    # Por ejemplo: unidades (1), decenas (10), centenas (100), etc.
    exp = 1

    # Bucle principal: repetimos mientras tengamos posiciones de dígitos que revisar
    while max_val // exp > 0:
        # Llamamos a la función auxiliar que realiza el ordenamiento por conteo
        # según el dígito actual (indicado por 'exp')
        conteo_por_digito(puntuaciones, exp)

        # Aumentamos 'exp' por un factor de 10 para pasar al siguiente dígito
        # Ejemplo: de unidades (1) pasamos a decenas (10), luego centenas (100), etc.
        exp *= 10

    # Retornamos la lista ya ordenada al finalizar
    return puntuaciones


# ------------------------------------------
# Función auxiliar para realizar ordenamiento por conteo basado en un dígito específico
# ------------------------------------------

def conteo_por_digito(puntuaciones, exp):
    # Número de elementos en la lista
    n = len(puntuaciones)

    # Lista temporal que almacenará los valores ordenados según el dígito actual
    output = [0] * n

    # Lista para contar las ocurrencias de cada dígito (0 al 9)
    # Índices representan los dígitos posibles en la posición actual
    count = [0] * 10

    # Recorremos la lista de puntuaciones
    for i in range(n):
        # Obtenemos el dígito relevante en la posición 'exp' de cada número
        # Por ejemplo, si exp = 10, extrae las decenas
        indice = (puntuaciones[i] // exp) % 10

        # Incrementamos la cuenta de ese dígito
        count[indice] += 1

    # Modificamos 'count' para que contenga posiciones reales en 'output'
    # Es decir, acumulamos los conteos
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construimos el arreglo de salida usando los conteos
    # Recorremos la lista de puntuaciones en orden inverso para mantener la estabilidad
    i = n - 1
    while i >= 0:
        # Nuevamente extraemos el dígito actual
        indice = (puntuaciones[i] // exp) % 10

        # Colocamos el valor en la posición correcta en la lista de salida
        output[count[indice] - 1] = puntuaciones[i]

        # Reducimos el conteo de ese dígito
        count[indice] -= 1

        # Pasamos al siguiente número (en orden inverso)
        i -= 1

    # Copiamos los valores ordenados desde 'output' de regreso a la lista original
    for i in range(n):
        puntuaciones[i] = output[i]


# ------------------------------------------
# Función que imprime en consola el ranking de jugadores con sus puntuaciones
# ------------------------------------------

def mostrar_ranking(jugadores, puntuaciones):
    print("🏆 Ranking de Jugadores (Mayor Puntuación):")

    # Emparejamos cada jugador con su puntuación usando zip
    for jugador, puntos in zip(jugadores, puntuaciones):
        # Mostramos el nombre y la puntuación de cada jugador
        print(f"🎮 {jugador} - {puntos} puntos")

    print()  # Línea en blanco para mejorar legibilidad


# ------------------------------------------
# Bloque principal de ejecución del programa
# ------------------------------------------

if __name__ == "__main__":
    # Diccionario que almacena jugadores como claves y sus puntuaciones como valores
    ranking_jugadores = {
        "PlayerOne": 9230,
        "NoobSlayer": 750,
        "DarkSoul": 4860,
        "MVP_Killer": 12300,
        "SniperX": 9985,
        "SpeedRunGod": 3210,
        "ZeldaFan": 11400,
        "BotDestroyer": 678,
    }

    # Extraemos solo los nombres de los jugadores (claves del diccionario)
    nombres = list(ranking_jugadores.keys())

    # Extraemos las puntuaciones (valores del diccionario)
    puntuaciones = list(ranking_jugadores.values())

    # Mostramos el ranking original antes de ordenar
    print("📋 Ranking original:")
    mostrar_ranking(nombres, puntuaciones)

    # Usamos Radix Sort para ordenar las puntuaciones (hacemos copia para no alterar la original)
    puntuaciones_ordenadas = radix_sort(puntuaciones.copy())

    # Ordenamos los pares jugador-puntuación con base en la puntuación (usamos sorted + lambda)
    jugadores_ordenados = sorted(ranking_jugadores.items(), key=lambda x: x[1])

    # Invertimos la lista para que esté en orden de mayor a menor
    jugadores_ordenados.reverse()

    # Extraemos nuevamente los nombres y puntuaciones, ya ordenados
    nombres_finales = [jugador[0] for jugador in jugadores_ordenados]
    puntos_finales = [jugador[1] for jugador in jugadores_ordenados]

    # Mostramos el ranking final, ya ordenado correctamente
    print("✅ Ranking final ordenado:")
    mostrar_ranking(nombres_finales, puntos_finales)

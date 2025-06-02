# -------------------------------------------------------
# Algoritmo Straight Merging (Merge Sort) para ranking de películas
# -------------------------------------------------------

def merge_sort(peliculas):
    """
    Esta función ordena una lista de tuplas (nombre_pelicula, puntuación)
    usando el algoritmo Merge Sort (Straight Merging).
    El orden es descendente (mejor puntuación primero).
    """

    # Paso 0: Revisamos si la lista está vacía o tiene un solo elemento
    # Esto es importante porque una lista con 0 o 1 elemento ya está ordenada por definición
    if len(peliculas) <= 1:
        # En ese caso, simplemente devolvemos la lista tal cual, sin modificar nada
        return peliculas

    # Paso 1: Dividir la lista en dos mitades para luego ordenarlas por separado
    # Calculamos el índice medio para partir la lista en dos partes casi iguales
    medio = len(peliculas) // 2

    # Creamos una sublista que contiene la primera mitad de los elementos
    izquierda = peliculas[:medio]

    # Creamos otra sublista que contiene la segunda mitad de los elementos
    derecha = peliculas[medio:]

    # Paso 2: Aplicar recursivamente el merge_sort a la sublista izquierda
    # Esto significa que seguimos dividiendo la lista izquierda hasta llegar al caso base
    izquierda_ordenada = merge_sort(izquierda)

    # Paso 2 (continuación): Aplicar recursivamente el merge_sort a la sublista derecha
    # Igual que con la izquierda, dividimos y ordenamos la derecha por separado
    derecha_ordenada = merge_sort(derecha)

    # Paso 3: Una vez que ambas mitades están ordenadas, procedemos a fusionarlas
    # La función merge combinará estas dos listas ordenadas en una sola lista ordenada
    return merge(izquierda_ordenada, derecha_ordenada)


def merge(izquierda, derecha):
    """
    Esta función toma dos listas ordenadas (izquierda y derecha)
    y las combina en una sola lista también ordenada.
    La ordenación es de mayor a menor según la puntuación de las películas.
    """

    resultado = []   # Aquí guardaremos la lista final combinada y ordenada

    i = 0            # Índice para recorrer la lista 'izquierda'
    j = 0            # Índice para recorrer la lista 'derecha'

    # Mientras no hayamos llegado al final de ninguna de las dos listas
    while i < len(izquierda) and j < len(derecha):

        # Comparamos la puntuación de la película en la posición i de la lista izquierda
        # con la puntuación de la película en la posición j de la lista derecha
        # Recordemos que la puntuación está en la posición 1 de cada tupla
        if izquierda[i][1] >= derecha[j][1]:

            # Si la puntuación en 'izquierda' es mayor o igual, agregamos esa película primero
            resultado.append(izquierda[i])

            # Avanzamos el índice i para mirar el siguiente elemento de la lista izquierda
            i += 1

        else:
            # Si la puntuación en 'derecha' es mayor, agregamos esa película primero
            resultado.append(derecha[j])

            # Avanzamos el índice j para mirar el siguiente elemento de la lista derecha
            j += 1

    # Cuando salimos del while, significa que alguna de las dos listas ya fue completamente
    # agregada a resultado, pero puede que queden elementos en la otra lista.

    # Por eso, agregamos todos los elementos restantes de la lista izquierda (si hay)
    resultado.extend(izquierda[i:])

    # También agregamos todos los elementos restantes de la lista derecha (si hay)
    resultado.extend(derecha[j:])

    # Finalmente, devolvemos la lista completa y ordenada
    return resultado


# -------------------------------------------------------
# Función para mostrar el ranking de películas
# -------------------------------------------------------

def mostrar_ranking(peliculas_ordenadas):
    """
    Esta función recibe la lista de películas ya ordenadas
    y muestra un ranking bonito y fácil de leer con índices.
    """

    print("\n🎥 Ranking de películas por puntuación:")

    # Usamos enumerate para obtener índice (empezando en 1) y datos de cada película
    for idx, (titulo, puntaje) in enumerate(peliculas_ordenadas, start=1):

        # Imprimimos la posición, título y la puntuación con una estrella para hacerlo visual
        print(f"{idx}. {titulo} - ⭐ {puntaje}/10")


# -------------------------------------------------------
# Bloque principal: aquí empieza la ejecución del programa
# -------------------------------------------------------

if __name__ == "__main__":

    # Creamos una lista con nombres de películas y sus puntuaciones promedio de críticas
    peliculas = [
        ("The Godfather", 9.2),
        ("Inception", 8.8),
        ("Interstellar", 8.6),
        ("The Dark Knight", 9.0),
        ("Pulp Fiction", 8.9),
        ("Parasite", 8.6),
        ("The Shawshank Redemption", 9.3),
        ("Fight Club", 8.8),
        ("Forrest Gump", 8.8),
        ("The Matrix", 8.7),
    ]

    # Mostramos la lista original sin ordenar, para comparar después
    print("🎬 Lista original de películas:")
    for titulo, puntaje in peliculas:
        print(f"{titulo} - ⭐ {puntaje}/10")

    # Llamamos a la función merge_sort para ordenar la lista de películas
    peliculas_ordenadas = merge_sort(peliculas)

    # Finalmente, mostramos el ranking ordenado usando la función mostrar_ranking
    mostrar_ranking(peliculas_ordenadas)

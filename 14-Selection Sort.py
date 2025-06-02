# ------------------------------------------
# Algoritmo Selection Sort aplicado a un ranking de películas
# ------------------------------------------

def selection_sort(peliculas, votos):
    """
    Esta función ordena dos listas relacionadas: 'peliculas' y 'votos'.
    Utiliza el algoritmo Selection Sort para ordenar las películas
    según la cantidad de votos, en orden ascendente.
    """

    n = len(votos)  # Obtenemos la cantidad total de elementos a ordenar (cantidad de películas)

    # Recorremos cada elemento de la lista (posición i)
    for i in range(n):
        # Suponemos que el elemento actual (en la posición i) es el menor
        indice_min = i

        # Buscamos el verdadero menor desde la posición i+1 hasta el final de la lista
        for j in range(i + 1, n):
            # Si encontramos un valor menor que el actual mínimo
            if votos[j] < votos[indice_min]:
                # Actualizamos el índice del mínimo encontrado
                indice_min = j

        # Terminamos de buscar y tenemos el índice del valor mínimo en 'indice_min'
        # Intercambiamos el valor mínimo con el valor actual en la posición i
        votos[i], votos[indice_min] = votos[indice_min], votos[i]  # Intercambiamos los votos

        # También intercambiamos las películas correspondientes para mantener la relación correcta
        peliculas[i], peliculas[indice_min] = peliculas[indice_min], peliculas[i]

    # Retornamos las listas ya ordenadas
    return peliculas, votos


# ------------------------------------------
# Función para mostrar el ranking de películas con sus votos
# ------------------------------------------

def mostrar_ranking(peliculas, votos):
    # Título del ranking
    print("\n🎥 Ranking de Películas por Votos (de menos a más votada):")

    # Recorremos todas las películas y las mostramos junto con su posición y número de votos
    for i in range(len(peliculas)):
        # Imprimimos el número de ranking, el nombre de la película y su cantidad de votos
        print(f"{i+1}. {peliculas[i]} - {votos[i]} votos")


# ------------------------------------------
# Bloque principal del programa
# ------------------------------------------

if __name__ == "__main__":
    # Creamos un diccionario donde:
    # - La clave es el nombre de una película
    # - El valor es la cantidad de votos que ha recibido
    votos_peliculas = {
        "Inception": 320,
        "Titanic": 210,
        "The Dark Knight": 450,
        "Forrest Gump": 150,
        "Interstellar": 500,
        "The Matrix": 300,
        "Avatar": 280,
    }

    # Extraemos las claves del diccionario (nombres de películas) como una lista
    peliculas = list(votos_peliculas.keys())

    # Extraemos los valores del diccionario (cantidad de votos) como una lista
    votos = list(votos_peliculas.values())

    # Mostramos en pantalla la votación original (sin ordenar)
    print("🎬 Votación original (sin ordenar):")
    for pelicula, voto in zip(peliculas, votos):  # zip() permite recorrer ambas listas al mismo tiempo
        print(f"{pelicula} - {voto} votos")  # Mostramos cada película y su respectivo número de votos

    # Llamamos a la función selection_sort para ordenar las películas por número de votos
    # Usamos .copy() para no modificar las listas originales
    peliculas_ordenadas, votos_ordenados = selection_sort(peliculas.copy(), votos.copy())

    # Mostramos el ranking final ya ordenado
    mostrar_ranking(peliculas_ordenadas, votos_ordenados)

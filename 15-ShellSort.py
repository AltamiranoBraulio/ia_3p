# ------------------------------------------
# Algoritmo Shell Sort aplicado al ranking de atletas
# ------------------------------------------

def shell_sort(nombres, tiempos):
    """
    Esta función ordena dos listas (nombres y tiempos) de acuerdo a los valores en 'tiempos',
    utilizando el algoritmo Shell Sort. Se ordenan de menor a mayor tiempo (es decir, el más rápido primero).
    """

    n = len(tiempos)            # Obtenemos cuántos elementos hay en la lista 'tiempos'
    gap = n // 2                # Inicializamos el 'gap' o salto con la mitad de la longitud de la lista

    # Mientras el valor del gap sea mayor que 0, seguimos reduciendo y ordenando
    while gap > 0:
        # Empezamos a recorrer la lista desde el índice igual al gap hasta el final
        for i in range(gap, n):
            # Guardamos el valor actual de tiempo que vamos a ordenar
            tiempo_actual = tiempos[i]
            # También guardamos el nombre correspondiente al tiempo actual
            nombre_actual = nombres[i]
            # Creamos una variable 'j' para movernos hacia atrás en la lista
            j = i

            # Mientras 'j' no se haya salido de los límites (j >= gap)
            # y el tiempo en la posición anterior (con separación de gap) sea mayor que el actual,
            # realizamos el intercambio de valores
            while j >= gap and tiempos[j - gap] > tiempo_actual:
                # Movemos el tiempo anterior (más grande) una posición hacia adelante
                tiempos[j] = tiempos[j - gap]
                # Hacemos lo mismo con el nombre, para mantener sincronizados nombre-tiempo
                nombres[j] = nombres[j - gap]
                # Retrocedemos gap posiciones para seguir comparando hacia atrás
                j -= gap

            # Una vez encontrado el lugar correcto, colocamos el tiempo actual allí
            tiempos[j] = tiempo_actual
            # También colocamos el nombre correspondiente en esa posición
            nombres[j] = nombre_actual

        # Después de una pasada completa, reducimos el gap a la mitad (forma común de reducir el salto)
        gap //= 2  # Se hace entero con división //

    # Finalmente, devolvemos ambas listas ya ordenadas (nombres y tiempos sincronizados)
    return nombres, tiempos


# ------------------------------------------
# Función para mostrar el ranking final
# ------------------------------------------

def mostrar_ranking(nombres, tiempos):
    # Imprimimos una cabecera indicando que vamos a mostrar el ranking
    print("\n🏅 Ranking de Atletas (100m - tiempo más bajo es mejor):")
    # Recorremos las listas y mostramos cada atleta con su tiempo
    for i in range(len(nombres)):
        print(f"{i+1}. {nombres[i]} - {tiempos[i]} segundos")


# ------------------------------------------
# Bloque principal del programa
# ------------------------------------------

if __name__ == "__main__":
    # Creamos un diccionario con los nombres de los atletas como claves
    # y sus respectivos tiempos (en segundos) como valores
    tiempos_atletas = {
        "Usain Bolt": 9.58,
        "Tyson Gay": 9.69,
        "Yohan Blake": 9.69,
        "Asafa Powell": 9.72,
        "Justin Gatlin": 9.74,
        "Christian Coleman": 9.76,
        "Trayvon Bromell": 9.77,
        "Fred Kerley": 9.84,
    }

    # Extraemos las claves (nombres) y los valores (tiempos) del diccionario
    # y los convertimos en listas para poder ordenarlas
    nombres = list(tiempos_atletas.keys())      # Lista de nombres de los atletas
    tiempos = list(tiempos_atletas.values())    # Lista de tiempos correspondientes

    # Mostramos los datos originales tal y como están en el diccionario
    print("🏃‍♂️ Tiempos originales (sin ordenar):")
    for nombre, tiempo in zip(nombres, tiempos):
        # zip permite recorrer ambas listas al mismo tiempo
        print(f"{nombre} - {tiempo} segundos")

    # Llamamos a la función shell_sort con copias de las listas
    # para que los originales no se modifiquen
    nombres_ordenados, tiempos_ordenados = shell_sort(nombres.copy(), tiempos.copy())

    # Finalmente mostramos el ranking ordenado usando la función auxiliar
    mostrar_ranking(nombres_ordenados, tiempos_ordenados)

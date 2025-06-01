# Importamos el módulo random para generar números aleatorios
import random

# Definición de la función principal de ordenamiento Flash Sort
def flash_sort(arr):
    # Obtenemos la longitud del arreglo
    n = len(arr)

    # Si el arreglo tiene uno o ningún elemento, ya está ordenado, se regresa tal cual
    if n <= 1:
        return arr

    # Encontramos el valor mínimo y máximo del arreglo
    min_val = min(arr)
    max_val = max(arr)

    # Si todos los elementos son iguales, no hay nada que ordenar
    if min_val == max_val:
        return arr

    # Calculamos el número de clases (bins o grupos), normalmente se recomienda 0.43 * n
    m = int(0.43 * n)

    # Creamos un arreglo de conteo (L) con m elementos inicializados en cero
    L = [0] * m

    # Calculamos un factor de clasificación (c) para distribuir los elementos
    c = (m - 1) / (max_val - min_val)

    # Contamos cuántos elementos pertenecen a cada clase
    for num in arr:
        # Calculamos el índice de la clase para cada elemento
        k = int(c * (num - min_val))
        # Incrementamos el contador de la clase correspondiente
        L[k] += 1

    # Acumulamos los conteos para convertirlos en límites superiores de cada clase
    for i in range(1, m):
        L[i] += L[i - 1]

    # Iniciamos el proceso de permutación usando el primer elemento del arreglo
    hold = arr[0]  # Guardamos el primer valor como 'temporal'
    j = 0          # Índice actual desde donde empieza el intercambio
    move = 0       # Contador de cuántos elementos ya han sido colocados correctamente

    # Continuamos hasta que todos los elementos hayan sido movidos menos uno
    while move < n - 1:
        # Calculamos la clase a la que pertenece el valor actual
        k = int(c * (hold - min_val))

        # Si el índice j ya alcanzó o superó el límite superior de su clase, avanzamos
        while j >= L[k]:
            j += 1                # Avanzamos al siguiente índice
            hold = arr[j]        # Tomamos el nuevo valor como 'hold'
            k = int(c * (hold - min_val))  # Recalculamos su clase

        # Mientras no se haya alcanzado el límite superior de la clase
        while j < L[k]:
            k = int(c * (hold - min_val))      # Calculamos la clase actual
            dest = L[k] - 1                    # Posición destino del valor actual
            arr[dest], hold = hold, arr[dest]  # Intercambiamos valores
            L[k] -= 1                          # Reducimos el límite superior de esa clase
            move += 1                          # Incrementamos el número de elementos colocados

    # Luego del reordenamiento por clases, se aplica Insertion Sort para finalizar
    for i in range(1, n):
        temp = arr[i]     # Elemento actual a insertar
        j = i - 1         # Comenzamos a comparar hacia la izquierda
        # Mientras no lleguemos al inicio y el valor sea mayor que el actual
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]  # Desplazamos el valor a la derecha
            j -= 1              # Seguimos hacia la izquierda
        arr[j + 1] = temp       # Insertamos el valor en la posición correcta

    # Devolvemos el arreglo ordenado
    return arr

# Punto de entrada del script
if __name__ == "__main__":
    # Generamos una lista de 30 números aleatorios entre 1000 y 9999
    datos = [random.randint(1000, 9999) for _ in range(30)]

    # Mostramos la lista original
    print("Lista original:")
    print(datos)

    # Ordenamos la lista usando el algoritmo Flash Sort
    ordenado = flash_sort(datos.copy())

    # Mostramos la lista ordenada
    print("\nLista ordenada con Flash Sort:")
    print(ordenado)

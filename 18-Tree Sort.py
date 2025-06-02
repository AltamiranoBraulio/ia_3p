# --------------------------------------------------------------
# Tree Sort aplicado a cargas sísmicas laterales (ingeniería civil)
# --------------------------------------------------------------

class NodoArbol:
    """
    Nodo básico para el árbol binario de búsqueda.
    Cada nodo representa una carga sísmica lateral (en kN).
    """
    def __init__(self, valor):
        self.valor = valor  # Valor de la carga (kN)
        self.izquierda = None  # Subárbol izquierdo (valores menores)
        self.derecha = None    # Subárbol derecho (valores mayores)


def insertar_en_arbol(raiz, valor):
    """
    Inserta un valor dentro del árbol BST respetando las reglas:
    izquierda < valor <= derecha
    """
    if raiz is None:
        return NodoArbol(valor)
    elif valor <= raiz.valor:
        raiz.izquierda = insertar_en_arbol(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar_en_arbol(raiz.derecha, valor)
    return raiz


def recorrido_inorden(nodo, resultado):
    """
    Recorrido inorden del árbol BST que devuelve los valores en orden ascendente.
    """
    if nodo:
        recorrido_inorden(nodo.izquierda, resultado)  # Visita subárbol izquierdo
        resultado.append(nodo.valor)                  # Visita nodo actual
        recorrido_inorden(nodo.derecha, resultado)    # Visita subárbol derecho


def tree_sort(cargas):
    """
    Realiza Tree Sort: inserta todas las cargas en el árbol y luego recorre inorden.
    """
    raiz = None
    for carga in cargas:
        raiz = insertar_en_arbol(raiz, carga)

    resultado_ordenado = []
    recorrido_inorden(raiz, resultado_ordenado)
    return resultado_ordenado


# --------------------------------------------------------------
# Simulación de análisis estructural
# --------------------------------------------------------------

import random

def simular_cargas_sismicas(n_pisos):
    """
    Simula cargas laterales en kN para cada piso de un edificio.
    """
    return [round(random.uniform(20, 200), 1) for _ in range(n_pisos)]


def mostrar_cargas(cargas, mensaje):
    print(f"\n{mensaje}")
    for i, carga in enumerate(cargas, 1):
        print(f"Piso {i}: {carga} kN")


# ------------------------
# Bloque principal
# ------------------------
if __name__ == "__main__":
    # Generamos cargas aleatorias en 10 pisos
    cargas = simular_cargas_sismicas(10)

    # Mostramos cargas originales
    mostrar_cargas(cargas, "Cargas sísmicas originales:")

    # Ordenamos con Tree Sort
    cargas_ordenadas = tree_sort(cargas)

    # Mostramos las cargas ordenadas de menor a mayor
    mostrar_cargas(cargas_ordenadas, "Cargas ordenadas (Tree Sort):")

    # Punto de análisis: cargas más altas = zonas críticas
    carga_maxima = max(cargas_ordenadas)
    print(f"\n⚠️ Carga sísmica máxima registrada: {carga_maxima} kN (¡verificar refuerzo estructural!)")

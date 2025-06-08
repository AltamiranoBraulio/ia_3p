# Importamos el módulo `heapq`, que nos permite trabajar con colas de prioridad usando montículos (heaps), 
# lo cual es útil para implementar algoritmos eficientes como Dijkstra.
import heapq

# Importamos `matplotlib.pyplot` para crear gráficos y visualizaciones, en este caso para visualizar la red de entregas.
import matplotlib.pyplot as plt

# Importamos `networkx`, que es una librería especializada en la creación, manipulación y visualización de grafos.
import networkx as nx

# Importamos `time`, aunque en este código no se usa directamente, suele utilizarse para temporizadores o pausas.
import time

# Definimos una clase llamada `DeliveryOptimizer`, que encapsula toda la lógica para optimizar entregas en una red de rutas.
class DeliveryOptimizer:
    # Método constructor: se ejecuta automáticamente cuando se crea una nueva instancia de la clase.
    def __init__(self):
        # Creamos un diccionario que representa el grafo de la red de entregas.
        # Cada nodo representa un punto (ciudad o estación), y los valores son diccionarios que indican a qué nodos se puede ir y con qué costo (distancia).
        self.delivery_network = {
            'A': {'B': 8, 'C': 5, 'D': 12},  # Desde A se puede ir a B, C y D con los costos indicados.
            'B': {'E': 10, 'A': 8},          # Desde B se puede ir a E o regresar a A.
            'C': {'D': 7, 'E': 9},           # Desde C se puede ir a D o E.
            'D': {'E': 15},                  # Desde D sólo se puede ir a E.
            'E': {}                          # Desde E no hay salidas (nodo final o destino).
        }

        # Creamos un conjunto que contendrá todos los nodos únicos del grafo.
        self.all_nodes = set(self.delivery_network.keys())  # Inicialmente agregamos las claves del diccionario (los nodos de salida).

        # Recorremos los valores del diccionario, que son los destinos alcanzables desde cada nodo.
        for neighbors in self.delivery_network.values():
            # Agregamos cada nodo destino al conjunto `all_nodes` para asegurarnos de tener todos los nodos.
            self.all_nodes.update(neighbors.keys())

    # Método que implementa el algoritmo de Dijkstra para encontrar las rutas más cortas desde un nodo origen.
    def find_optimal_route(self, start):
        # Creamos un diccionario que guardará la distancia mínima conocida desde el nodo de inicio hasta cada nodo.
        # Inicializamos todas las distancias como infinito (significa que no sabemos cómo llegar aún).
        distances = {node: float('inf') for node in self.all_nodes}

        # Diccionario que guarda el nodo anterior en la ruta más corta encontrada para cada nodo.
        previous_nodes = {node: None for node in self.all_nodes}

        # La distancia desde el nodo de inicio a sí mismo es 0.
        distances[start] = 0

        # Creamos una cola de prioridad para explorar los nodos más prometedores primero (los más cercanos).
        # Se inicia con una tupla (distancia=0, nodo=start).
        priority_queue = [(0, start)]

        # Mientras haya nodos por explorar en la cola...
        while priority_queue:
            # Sacamos el nodo con menor distancia acumulada (más prometedor).
            current_distance, current_node = heapq.heappop(priority_queue)

            # Revisamos cada vecino del nodo actual.
            for neighbor, weight in self.delivery_network.get(current_node, {}).items():
                # Calculamos la distancia total desde el nodo de inicio hasta este vecino pasando por el nodo actual.
                distance = current_distance + weight

                # Si encontramos una ruta más corta, actualizamos la distancia y el nodo anterior.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node

                    # Agregamos el vecino a la cola para seguir explorando desde allí.
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Una vez que tenemos todas las distancias y nodos anteriores, reconstruimos las rutas completas.
        return self._build_routes(start, previous_nodes, distances)

    # Método privado para reconstruir las rutas óptimas desde el nodo de inicio usando los resultados de Dijkstra.
    def _build_routes(self, start, previous_nodes, distances):
        # Diccionario para almacenar las rutas completas a cada nodo.
        routes = {}

        # Iteramos por cada nodo del grafo.
        for node in self.all_nodes:
            if node == start:
                continue  # No reconstruimos la ruta hacia el nodo de inicio.

            path = []  # Lista que representará el camino desde el inicio hasta el nodo actual.
            current_node = node

            # Mientras sepamos cuál fue el nodo anterior...
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)  # Insertamos el nodo al inicio del camino.
                current_node = previous_nodes[current_node]  # Avanzamos hacia atrás en el camino.

            # Si encontramos un camino (path no está vacío), lo almacenamos.
            if path:
                path.insert(0, start)  # Insertamos el nodo de inicio al principio.
                routes[node] = {
                    'path': path,                 # Ruta completa desde inicio hasta nodo.
                    'distance': distances[node],  # Distancia total calculada.
                    'steps': len(path) - 1        # Número de pasos o segmentos recorridos.
                }

        return routes  # Devolvemos el diccionario con todas las rutas óptimas.

    # Método que visualiza y anima las rutas en un grafo.
    def animate_routes(self, routes):
        # Creamos un grafo dirigido usando NetworkX.
        G = nx.DiGraph()

        # Añadimos todos los arcos (edges) del grafo con sus pesos (distancias).
        for origin, destinations in self.delivery_network.items():
            for dest, weight in destinations.items():
                G.add_edge(origin, dest, weight=weight)

        # Calculamos una posición para cada nodo para que el grafo sea legible.
        pos = nx.spring_layout(G, seed=42)

        # Activamos el modo interactivo de matplotlib para hacer animaciones.
        plt.ion()

        # Creamos una figura con un eje para graficar el grafo.
        fig, ax = plt.subplots(figsize=(10, 6))

        # Por cada destino calculado, animamos cómo se forma la ruta desde el inicio.
        for destination, route_data in routes.items():
            ax.clear()  # Limpiamos la gráfica anterior.

            # Dibujamos los nodos y etiquetas en azul claro.
            nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', ax=ax)
            nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)

            # Dibujamos las aristas del grafo base (en gris claro).
            nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='gray', ax=ax)

            # Dibujamos las etiquetas de los pesos de las aristas.
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

            path = route_data['path']  # Obtenemos el camino a este destino.

            # Animamos paso a paso cada segmento del camino.
            for i in range(len(path) - 1):
                edge = [(path[i], path[i + 1])]  # Arista a resaltar.

                # Dibujamos la arista actual en rojo.
                nx.draw_networkx_edges(G, pos, edgelist=edge, width=2, edge_color='red', ax=ax)

                # Resaltamos los nodos actuales en color salmón.
                nx.draw_networkx_nodes(G, pos, nodelist=[path[i], path[i + 1]], node_color='salmon', node_size=800, ax=ax)

                # Ponemos un título temporal indicando el progreso de la ruta.
                ax.set_title(f"Ruta desde A hasta {destination} - Paso {i+1}/{len(path)-1}", fontsize=14)

                # Pausamos para dar efecto de animación.
                plt.pause(1)

        # Título final para la animación completa.
        ax.set_title("Red de Entregas - Animación de Rutas", fontsize=14)

        # Desactivamos el modo interactivo y mostramos la figura final.
        plt.ioff()
        plt.show()

    # Método para imprimir las rutas óptimas encontradas de forma textual en la consola.
    def print_routes(self, routes):
        print("\nRutas Óptimas de Entrega:")
        print("-------------------------")
        for destination, data in routes.items():
            print(f"\nDestino: {destination}")
            print(f"Ruta: {' -> '.join(data['path'])}")
            print(f"Distancia total: {data['distance']} km")
            print(f"Número de segmentos: {data['steps']}")

# Función principal del programa.
def main():
    # Creamos una instancia del optimizador de entregas.
    delivery = DeliveryOptimizer()

    # Definimos el nodo de inicio.
    start_point = 'A'

    # Mostramos mensaje de inicio.
    print("\nCalculando rutas óptimas desde el punto A...")

    # Ejecutamos el algoritmo de Dijkstra para obtener las rutas desde A.
    optimal_routes = delivery.find_optimal_route(start_point)

    # Imprimimos en consola las rutas encontradas.
    delivery.print_routes(optimal_routes)

    # Mostramos visualmente y con animaciones cómo se forman las rutas.
    delivery.animate_routes(optimal_routes)

# Punto de entrada del programa: esta condición se cumple si ejecutamos este archivo directamente.
if __name__ == "__main__":
    main()

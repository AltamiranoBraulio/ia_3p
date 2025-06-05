"""
Optimizador de Rutas FedEx con Dijkstra - Versión Simplificada
------------------------------------------------------------
Este programa calcula la ruta óptima para entregas considerando:
- Distancia mínima (km)
- Minimizar vueltas/retornos
- Generación automática de gráfico de ruta
"""
import heapq
import matplotlib.pyplot as plt
import networkx as nx

class FedExDelivery:
    def __init__(self):
        # Definición fija de la red de entregas (origen, destino, distancia)
        self.delivery_network = {
            'CentroDist': {'ZonaIndustrial': 8, 'CentroCiudad': 5, 'ResidencialNorte': 12},
            'ZonaIndustrial': {'ResidencialSur': 10, 'CentroDist': 8},
            'CentroCiudad': {'ResidencialNorte': 7, 'ResidencialSur': 9},
            'ResidencialNorte': {'ResidencialSur': 15},
            'ResidencialSur': {}  # Punto final sin salidas
        }
        self.all_nodes = set(self.delivery_network.keys())
        for neighbors in self.delivery_network.values():
            self.all_nodes.update(neighbors.keys())

    def find_optimal_route(self, start):
        """Implementación Dijkstra modificada para evitar vueltas innecesarias"""
        distances = {node: float('inf') for node in self.all_nodes}
        previous_nodes = {node: None for node in self.all_nodes}
        distances[start] = 0
        
        # Usamos una cola de prioridad
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # Explorar vecinos
            for neighbor, weight in self.delivery_network.get(current_node, {}).items():
                distance = current_distance + weight
                
                # Solo actualizamos si encontramos un camino más corto
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return self._build_routes(start, previous_nodes, distances)

    def _build_routes(self, start, previous_nodes, distances):
        """Construye todas las rutas óptimas desde el origen"""
        routes = {}
        for node in self.all_nodes:
            if node == start:
                continue
                
            path = []
            current_node = node
            
            # Reconstruir ruta desde el destino hasta el inicio
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            
            if path:  # Solo agregar rutas válidas
                path.insert(0, start)
                routes[node] = {
                    'path': path,
                    'distance': distances[node],
                    'steps': len(path) - 1
                }
        
        return routes

    def plot_routes(self, routes):
        """Visualiza la red y la ruta óptima usando matplotlib"""
        G = nx.DiGraph()
        
        # Agregar nodos y aristas
        for origin, destinations in self.delivery_network.items():
            for dest, weight in destinations.items():
                G.add_edge(origin, dest, weight=weight)
        
        # Configurar gráfico
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(12, 8))
        
        # Dibujar la red completa
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='gray')
        
        # Resaltar las rutas óptimas
        for route_data in routes.values():
            path = route_data['path']
            path_edges = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(
                G, pos, edgelist=path_edges,
                width=2, alpha=0.8, edge_color='red', arrows=True
            )
            nx.draw_networkx_nodes(
                G, pos, nodelist=path,
                node_size=800, node_color='salmon'
            )
        
        # Mostrar distancias
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.title(" Red de Entregas FedEx - Rutas Óptimas", fontsize=14)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def print_routes(self, routes):
        """Muestra las rutas en la terminal"""
        print("\n📦 Rutas Óptimas de Entrega FedEx:")
        print("----------------------------------")
        for destination, data in routes.items():
            print(f"\n📍 Destino: {destination}")
            print(f"🛣️ Ruta: {' → '.join(data['path'])}")
            print(f"📏 Distancia total: {data['distance']} km")
            print(f"🛑 Paradas: {data['steps']}")

def main():
    fedex = FedExDelivery()
    start_point = 'CentroDist'  # Punto de partida fijo
    
    print("\n🚚 Calculando rutas óptimas desde el centro de distribución...")
    optimal_routes = fedex.find_optimal_route(start_point)
    
    fedex.print_routes(optimal_routes)
    fedex.plot_routes(optimal_routes)

if __name__ == "__main__":
    main()
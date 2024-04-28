import heapq

class GrafoNoDirigido:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, ambiente):
        if ambiente not in self.vertices:
            self.vertices[ambiente] = {}

    def agregar_arista(self, origen, destino, distancia):
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen][destino] = distancia
        self.vertices[destino][origen] = distancia

    def arbol_expansion_minima(self):
        arbol = GrafoNoDirigido()
        visitados = set()
        visitados.add(next(iter(self.vertices)))  # Empezar desde un vértice aleatorio
        total_cables = 0
        heap = [(0, next(iter(self.vertices)), None)]  # (distancia, vertice, padre)
        while heap and len(visitados) < len(self.vertices):
            distancia, vertice, padre = heapq.heappop(heap)
            if vertice not in visitados:
                arbol.agregar_arista(padre, vertice, distancia)
                visitados.add(vertice)
                total_cables += distancia
                for vecino, peso in self.vertices[vertice].items():
                    if vecino not in visitados:
                        heapq.heappush(heap, (peso, vecino, vertice))
        return arbol, total_cables

    def camino_mas_corto(self, origen, destino):
        distancia_minima = {vertice: float('inf') for vertice in self.vertices}
        distancia_minima[origen] = 0
        heap = [(0, origen)]  # (distancia, vertice)
        while heap:
            distancia, vertice = heapq.heappop(heap)
            if distancia > distancia_minima[vertice]:
                continue
            for vecino, peso in self.vertices[vertice].items():
                nueva_distancia = distancia + peso
                if nueva_distancia < distancia_minima[vecino]:
                    distancia_minima[vecino] = nueva_distancia
                    heapq.heappush(heap, (nueva_distancia, vecino))
        return distancia_minima[destino]


def main():
    grafo = GrafoNoDirigido()

    # Agregar vértices y aristas
    ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]
    for ambiente in ambientes:
        grafo.agregar_vertice(ambiente)

    aristas = [
        ("cocina", "comedor", 10),
        ("cocina", "sala de estar", 5),
        ("cocina", "patio", 7),
        # Agregar más aristas aquí
    ]
    for origen, destino, distancia in aristas:
        grafo.agregar_arista(origen, destino, distancia)

    # Árbol de expansión mínima
    arbol_minimo, total_cables = grafo.arbol_expansion_minima()
    print("Árbol de expansión mínima:", arbol_minimo.vertices)
    print("Total de metros de cables necesarios:", total_cables)

    # Camino más corto desde la habitación 1 hasta la sala de estar
    origen = "habitación 1"
    destino = "sala de estar"
    distancia_minima = grafo.camino_mas_corto(origen, destino)
    print(f"Camino más corto desde {origen} hasta {destino}: {distancia_minima} metros")

if __name__ == "__main__":
    main()

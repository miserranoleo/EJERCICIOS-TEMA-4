import random

class GrafoDirigido:
    def __init__(self):
        self.vertices = {}
        self.aristas = []

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append((destino, peso))
            self.aristas.append((origen, destino, peso))

    def eliminar_desconectados(self):
        nodos_conectados = set()
        for origen, destinos in self.vertices.items():
            nodos_conectados.add(origen)
            for destino, _ in destinos:
                nodos_conectados.add(destino)
        nodos_desconectados = set(self.vertices.keys()) - nodos_conectados
        for nodo in nodos_desconectados:
            del self.vertices[nodo]

    def nodo_mas_saliente(self):
        return max(self.vertices, key=lambda x: len(self.vertices[x]))

    def nodo_mas_entrante(self):
        nodos_entrantes = {nodo: 0 for nodo in self.vertices}
        for _, destinos in self.vertices.items():
            for destino, _ in destinos:
                nodos_entrantes[destino] += 1
        return max(nodos_entrantes, key=nodos_entrantes.get)

    def nodos_inaccesibles(self):
        nodos_alcanzables = set()
        for _, destinos in self.vertices.items():
            for destino, _ in destinos:
                nodos_alcanzables.add(destino)
        nodos_inaccesibles = set(self.vertices.keys()) - nodos_alcanzables
        return nodos_inaccesibles

    def contar_vertices(self):
        return len(self.vertices)

    def contar_ciclos_directos(self):
        return sum(1 for origen, destino, _ in self.aristas if origen == destino)

    def arista_mas_larga(self):
        return max(self.aristas, key=lambda x: x[2])

def generar_grafo():
    grafo = GrafoDirigido()
    for i in range(1, 16):
        grafo.agregar_vertice(i)
    for _ in range(30):
        origen = random.randint(1, 15)
        destino = random.randint(1, 15)
        peso = random.randint(1, 100)
        grafo.agregar_arista(origen, destino, peso)
    return grafo

def main():
    grafo = generar_grafo()
    grafo.eliminar_desconectados()
    print("Nodo con mayor cantidad de aristas que salen de él:", grafo.nodo_mas_saliente())
    print("Nodo con mayor cantidad de aristas que llegan a él:", grafo.nodo_mas_entrante())
    print("Vértices desde los cuales no se puede acceder a otro vértice:", grafo.nodos_inaccesibles())
    print("Cantidad de vértices en el grafo:", grafo.contar_vertices())
    print("Cantidad de vértices con ciclo directo:", grafo.contar_ciclos_directos())
    print("Arista más larga:", grafo.arista_mas_larga())

if __name__ == "__main__":
    main()

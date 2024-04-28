import math

class GrafoNoDirigido:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_vertice(self, lugar, latitud, longitud):
        self.vertices[lugar] = (latitud, longitud)

    def agregar_arista(self, lugar1, lugar2, distancia):
        if lugar1 not in self.aristas:
            self.aristas[lugar1] = {}
        self.aristas[lugar1][lugar2] = distancia

        if lugar2 not in self.aristas:
            self.aristas[lugar2] = {}
        self.aristas[lugar2][lugar1] = distancia

    def calcular_distancia(self, lugar1, lugar2):
        latitud1, longitud1 = self.vertices[lugar1]
        latitud2, longitud2 = self.vertices[lugar2]
        distancia = math.sqrt((latitud2 - latitud1)**2 + (longitud2 - longitud1)**2)
        return distancia

    def arbol_expansion_minima(self, lugar_inicial):
        arbol = GrafoNoDirigido()
        visitados = set()
        visitados.add(lugar_inicial)
        total_distancia = 0
        for lugar in self.vertices:
            if lugar != lugar_inicial:
                distancia = self.calcular_distancia(lugar_inicial, lugar)
                total_distancia += distancia
                arbol.agregar_vertice(lugar, *self.vertices[lugar])
                arbol.agregar_arista(lugar_inicial, lugar, distancia)
        return arbol, total_distancia

    def camino_mas_corto(self, origen, destino):
        distancias = {lugar: float('inf') for lugar in self.vertices}
        distancias[origen] = 0
        visitados = set()
        while visitados != set(self.vertices):
            lugar_actual = min((lugar for lugar in self.vertices if lugar not in visitados), key=lambda x: distancias[x])
            visitados.add(lugar_actual)
            for vecino in self.aristas.get(lugar_actual, {}):
                if vecino not in visitados:
                    nueva_distancia = distancias[lugar_actual] + self.aristas[lugar_actual][vecino]
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
        return distancias[destino]

def main():
    grafo = GrafoNoDirigido()

    # Agregar lugares turísticos con sus coordenadas de latitud y longitud
    lugares = {
        "Partenón": (37.9715, 23.7263),  # Atenas
        "Olimpia (Zeus)": (37.6383, 21.63),
        "Olimpia (Hera)": (37.6383, 21.63),
        "Delfos (Apolo)": (38.4827, 22.5039),
        "Sunión (Poseidón)": (37.6631, 24.0408),
        "Éfeso (Artemisa)": (37.9490, 27.3637),
        "Acrópolis (Teatro de Dionisio)": (37.9715, 23.7263)  # Atenas
    }

    for lugar, (latitud, longitud) in lugares.items():
        grafo.agregar_vertice(lugar, latitud, longitud)

    # Agregar aristas entre los lugares turísticos
    grafo.agregar_arista("Partenón", "Olimpia (Zeus)", 100)
    grafo.agregar_arista("Partenón", "Olimpia (Hera)", 200)
    grafo.agregar_arista("Partenón", "Delfos (Apolo)", 300)
    grafo.agregar_arista("Partenón", "Sunión (Poseidón)", 400)
    grafo.agregar_arista("Partenón", "Éfeso (Artemisa)", 500)
    grafo.agregar_arista("Partenón", "Acrópolis (Teatro de Dionisio)", 600)
    # Agregar más aristas aquí

    # Árbol de expansión mínima desde el templo de Atenea (Partenón) en Atenas
    arbol_minimo, total_distancia = grafo.arbol_expansion_minima("Partenón")
    print("Árbol de expansión mínima:", arbol_minimo.vertices)
    print("Distancia total del árbol de expansión mínima:", total_distancia)

    # Camino más corto desde el templo de Atenea (Partenón) en Atenas hasta el templo de Apolo en Delfos
    origen = "Partenón"
    destino = "Delfos (Apolo)"
    distancia_minima = grafo.camino_mas_corto(origen, destino)
    print(f"Camino más corto desde {origen} hasta {destino}: {distancia_minima:.2f} kilómetros")

if __name__ == "__main__":
    main()

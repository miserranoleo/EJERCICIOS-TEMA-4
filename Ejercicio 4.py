import os.path

class NodoArbolBinario:
    def __init__(self, nombre, nrr):
        self.nombre = nombre
        self.nrr = nrr
        self.izquierda = None
        self.derecha = None

class ArbolIndice:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, nrr):
        self.raiz = self._insertar_recursivo(self.raiz, nombre, nrr)

    def _insertar_recursivo(self, raiz, nombre, nrr):
        if raiz is None:
            return NodoArbolBinario(nombre, nrr)
        if nombre < raiz.nombre:
            raiz.izquierda = self._insertar_recursivo(raiz.izquierda, nombre, nrr)
        elif nombre > raiz.nombre:
            raiz.derecha = self._insertar_recursivo(raiz.derecha, nombre, nrr)
        return raiz

    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, raiz, nombre):
        if raiz is None or raiz.nombre == nombre:
            return raiz
        if nombre < raiz.nombre:
            return self._buscar_recursivo(raiz.izquierda, nombre)
        return self._buscar_recursivo(raiz.derecha, nombre)

    def modificar(self, nombre, nuevo_nrr):
        nodo = self.buscar(nombre)
        if nodo is not None:
            nodo.nrr = nuevo_nrr

    def eliminar(self, nombre):
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self, raiz, nombre):
        if raiz is None:
            return raiz
        if nombre < raiz.nombre:
            raiz.izquierda = self._eliminar_recursivo(raiz.izquierda, nombre)
        elif nombre > raiz.nombre:
            raiz.derecha = self._eliminar_recursivo(raiz.derecha, nombre)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            elif raiz.derecha is None:
                return raiz.izquierda
            raiz.nombre = self._menor_valor(raiz.derecha)
            raiz.derecha = self._eliminar_recursivo(raiz.derecha, raiz.nombre)
        return raiz

    def _menor_valor(self, raiz):
        actual = raiz
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.nombre

def cargar_personajes_desde_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.")
        return []

    personajes = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            personajes.append((partes[0], float(partes[1]), float(partes[2])))
    return personajes

def main():
    nombre_archivo = "personajes_star_wars.txt"
    personajes = cargar_personajes_desde_archivo(nombre_archivo)

    arbol_indice = ArbolIndice()

    # Insertar personajes en el árbol índice
    for i, (nombre, _, _) in enumerate(personajes):
        arbol_indice.insertar(nombre, i)

    # Mostrar información de Yoda y Boba Fett
    yoda = arbol_indice.buscar("Yoda")
    if yoda:
        print(f"Información de Yoda: Nombre: {yoda.nombre}, NRR: {yoda.nrr}")
    else:
        print("Yoda no encontrado en el árbol índice.")

    boba_fett = arbol_indice.buscar("Boba Fett")
    if boba_fett:
        print(f"Información de Boba Fett: Nombre: {boba_fett.nombre}, NRR: {boba_fett.nrr}")
    else:
        print("Boba Fett no encontrado en el árbol índice.")

    # Mostrar listado ordenado alfabéticamente de personajes que miden más de 1 metro
    print("Personajes que miden más de 1 metro:")
    for nombre, altura, _ in sorted(personajes):
        if altura > 1.0:
            print(nombre)

    # Mostrar listado ordenado alfabéticamente de personajes que pesan menos de 75 kilos
    print("Personajes que pesan menos de 75 kilos:")
    for nombre, _, peso in sorted(personajes):
        if peso < 75.0:
            print(nombre)

if __name__ == "__main__":
    main()


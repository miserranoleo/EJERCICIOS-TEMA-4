class Pedido:
    def __init__(self, general, planeta, descripcion, prioridad):
        self.general = general
        self.planeta = planeta
        self.descripcion = descripcion
        self.prioridad = prioridad  # Agregamos el campo de prioridad

class NodoColaPrioridad:
    def __init__(self, pedido):
        self.pedido = pedido
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, pedido):
        nodo_nuevo = NodoColaPrioridad(pedido)
        if self.esta_vacia() or pedido.prioridad > self.cabeza.pedido.prioridad:
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza = nodo_nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and pedido.prioridad <= actual.siguiente.pedido.prioridad:
                actual = actual.siguiente
            nodo_nuevo.siguiente = actual.siguiente
            actual.siguiente = nodo_nuevo

    def atender(self):
        if self.esta_vacia():
            return None
        pedido_atendido = self.cabeza.pedido
        self.cabeza = self.cabeza.siguiente
        return pedido_atendido

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def atender_pedidos(cola):
    bitacora = Pila()
    while not cola.esta_vacia():
        pedido = cola.atender()
        bitacora.apilar(pedido)
    return bitacora

def main():
    cola = ColaPrioridad()

    # Agregar pedidos a la cola con sus respectivas prioridades
    cola.agregar(Pedido("General Tarkin", "Alderaan", "Solicita refuerzos", 1))  # Prioridad baja
    cola.agregar(Pedido("Agente Kallus", "Lothal", "Informe sobre situación de tropas", 2))  # Prioridad media
    cola.agregar(Pedido("Gran Inquisidor", "Lothal", "Investigar actividad rebelde", 3))  # Prioridad alta
    cola.agregar(Pedido("General Veers", "Hoth", "Preparar ataque", 1))  # Prioridad baja
    cola.agregar(Pedido("General Dodonna", "Yavin IV", "Plan de defensa", 1))  # Prioridad baja
    cola.agregar(Pedido("Capitán Needa", "Destructor Estelar", "Reportar estado del escudo", 2))  # Prioridad media
    cola.agregar(Pedido("General Hera Syndulla", "Lothal", "Solicita ayuda para ataque", 3))  # Prioridad alta

    # Atender pedidos y almacenar los de alta prioridad en la bitácora
    bitacora = atender_pedidos(cola)

    # Mostrar pedidos almacenados en la bitácora
    print("Pedidos en la bitácora:")
    while not bitacora.esta_vacia():
        pedido = bitacora.desapilar()
        print(f"General: {pedido.general}, Planeta: {pedido.planeta}, Descripción: {pedido.descripcion}")

if __name__ == "__main__":
    main()

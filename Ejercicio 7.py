class GrafoNoDirigido:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, tarea):
        if tarea not in self.vertices:
            self.vertices[tarea] = {}

    def agregar_arista(self, tarea1, tarea2, tiempo, persona):
        self.agregar_vertice(tarea1)
        self.agregar_vertice(tarea2)
        self.vertices[tarea1][tarea2] = (tiempo, persona)
        self.vertices[tarea2][tarea1] = (tiempo, persona)

    def obtener_tiempo_total_minimo(self):
        tiempo_total = 0
        personas_por_tarea = {}
        for tarea, vecinos in self.vertices.items():
            for vecino, (tiempo, persona) in vecinos.items():
                tiempo_total += tiempo
                personas_por_tarea[tarea] = persona
        return tiempo_total, personas_por_tarea

    def obtener_camino_minimo(self, inicio, fin):
        visitados = set()
        cola = [(inicio, [inicio])]
        while cola:
            (vertice, camino) = cola.pop(0)
            if vertice not in visitados:
                if vertice == fin:
                    return camino
                visitados.add(vertice)
                for vecino in self.vertices[vertice]:
                    cola.append((vecino, camino + [vecino]))

    def obtener_tareas_que_puede_realizar(self, persona):
        tareas = []
        for tarea, vecinos in self.vertices.items():
            for vecino, (tiempo, asignado) in vecinos.items():
                if asignado == persona:
                    tareas.append(tarea)
                    break
        return tareas

def main():
    proyecto = GrafoNoDirigido()

    # Agregar tareas y aristas con tiempo y persona asignada
    proyecto.agregar_arista("análisis de requerimientos", "diseño de base de datos", 5, "Harry")
    proyecto.agregar_arista("análisis de requerimientos", "diseño de interfaz de usuario", 4, "John")
    proyecto.agregar_arista("diseño de base de datos", "desarrollo del backend", 8, "Harry")
    proyecto.agregar_arista("diseño de interfaz de usuario", "desarrollo del frontend", 6, "John")
    proyecto.agregar_arista("desarrollo del backend", "pruebas de integración", 7, "Harry")
    proyecto.agregar_arista("desarrollo del frontend", "pruebas de usabilidad", 6, "John")
    proyecto.agregar_arista("pruebas de integración", "presentación de mockups", 3, "Harry")
    proyecto.agregar_arista("pruebas de usabilidad", "presentación de mockups", 2, "John")

    # Determinar tiempo total mínimo del proyecto y personas que realizan cada tarea
    tiempo_total, personas_por_tarea = proyecto.obtener_tiempo_total_minimo()
    print("Tiempo total mínimo del proyecto:", tiempo_total)
    print("Personas que realizan cada tarea:", personas_por_tarea)

    # Determinar el camino mínimo desde "análisis de requerimientos" hasta "presentación de mockups"
    camino_minimo = proyecto.obtener_camino_minimo("análisis de requerimientos", "presentación de mockups")
    print("Camino mínimo:", camino_minimo)

    # Indicar todas las tareas que puede realizar la persona "Harry"
    tareas_harry = proyecto.obtener_tareas_que_puede_realizar("Harry")
    print("Tareas que puede realizar Harry:", tareas_harry)

if __name__ == "__main__":
    main()

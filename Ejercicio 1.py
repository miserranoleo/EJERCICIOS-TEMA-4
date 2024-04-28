class Jedi:
    def __init__(self, nombre, especie, anio_nacimiento, color_sable, ranking, maestros):
        self.nombre = nombre
        self.especie = especie
        self.anio_nacimiento = anio_nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestros = maestros

class NodoArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar_jedi_por_nombre(raiz, jedi):
    if raiz is None:
        return NodoArbolBinario(jedi)

    if jedi.nombre < raiz.valor.nombre:
        raiz.izquierda = insertar_jedi_por_nombre(raiz.izquierda, jedi)
    elif jedi.nombre > raiz.valor.nombre:
        raiz.derecha = insertar_jedi_por_nombre(raiz.derecha, jedi)

    return raiz

def insertar_jedi_por_ranking(raiz, jedi):
    if raiz is None:
        return NodoArbolBinario(jedi)

    if jedi.ranking < raiz.valor.ranking:
        raiz.izquierda = insertar_jedi_por_ranking(raiz.izquierda, jedi)
    elif jedi.ranking > raiz.valor.ranking:
        raiz.derecha = insertar_jedi_por_ranking(raiz.derecha, jedi)

    return raiz

def insertar_jedi_por_especie(raiz, jedi):
    if raiz is None:
        return NodoArbolBinario(jedi)

    if jedi.especie < raiz.valor.especie:
        raiz.izquierda = insertar_jedi_por_especie(raiz.izquierda, jedi)
    elif jedi.especie > raiz.valor.especie:
        raiz.derecha = insertar_jedi_por_especie(raiz.derecha, jedi)

    return raiz

def inorden(raiz):
    if raiz is None:
        return []

    return inorden(raiz.izquierda) + [raiz.valor] + inorden(raiz.derecha)

def nivel(raiz):
    if raiz is None:
        return []

    cola = [(raiz, 0)]
    niveles = []

    while cola:
        nodo, nivel_actual = cola.pop(0)
        if nivel_actual == len(niveles):
            niveles.append([])
        niveles[nivel_actual].append(nodo.valor)
        if nodo.izquierda:
            cola.append((nodo.izquierda, nivel_actual + 1))
        if nodo.derecha:
            cola.append((nodo.derecha, nivel_actual + 1))

    return niveles

def buscar_jedi_por_nombre(raiz, nombre):
    if raiz is None:
        return None

    if raiz.valor.nombre == nombre:
        return raiz.valor
    elif nombre < raiz.valor.nombre:
        return buscar_jedi_por_nombre(raiz.izquierda, nombre)
    else:
        return buscar_jedi_por_nombre(raiz.derecha, nombre)

def buscar_jedi_por_ranking(raiz, ranking):
    if raiz is None:
        return None

    if raiz.valor.ranking == ranking:
        return raiz.valor
    elif ranking < raiz.valor.ranking:
        return buscar_jedi_por_ranking(raiz.izquierda, ranking)
    else:
        return buscar_jedi_por_ranking(raiz.derecha, ranking)

def buscar_jedi_por_especie(raiz, especie):
    if raiz is None:
        return None

    if raiz.valor.especie == especie:
        return raiz.valor
    elif especie < raiz.valor.especie:
        return buscar_jedi_por_especie(raiz.izquierda, especie)
    else:
        return buscar_jedi_por_especie(raiz.derecha, especie)

def listar_jedi(jedis):
    for jedi in jedis:
        print(f"Nombre: {jedi.nombre}")
        print(f"Especie: {jedi.especie}")
        print(f"Año de nacimiento: {jedi.anio_nacimiento}")
        print(f"Color del sable de luz: {jedi.color_sable}")
        print(f"Ranking: {jedi.ranking}")
        print(f"Maestros: {', '.join(jedi.maestros)}")
        print()

# Crear árboles de acceso a los datos
arbol_nombre = None
arbol_ranking = None
arbol_especie = None

# Simulación de datos de Jedi
jedis = [
    Jedi("Yoda", "Desconocida", 896, "Verde", "Jedi Master", ["Desconocido"]),
    Jedi("Luke Skywalker", "Humano", 19, "Azul", "Jedi Knight", ["Yoda", "Obi-Wan Kenobi"]),
    Jedi("Anakin Skywalker", "Humano", 41, "Azul", "Jedi Knight", ["Obi-Wan Kenobi"]),
    Jedi("Obi-Wan Kenobi", "Humano", 57, "Azul", "Jedi Knight", ["Yoda", "Qui-Gon Jinn"]),
    Jedi("Mace Windu", "Humano", 72, "Morado", "Jedi Master", ["Desconocido"]),
    Jedi("Qui-Gon Jinn", "Humano", 92, "Verde", "Jedi Master", ["Desconocido"]),
    Jedi("Ahsoka Tano", "Togruta", 36, "Verde", "Jedi Knight", ["Anakin Skywalker", "Plo Koon"]),
    Jedi("Plo Koon", "Kel Dor", 102, "Azul", "Jedi Master", ["Desconocido"]),
    Jedi("Kit Fisto", "Nautolano", 97, "Verde", "Jedi Knight", ["Desconocido"]),
    Jedi("Shaak Ti", "Togruta", 67, "Azul", "Jedi Master", ["Desconocido"]),
]

# Insertar jedis en los árboles de acceso a los datos
for jedi in jedis:
    arbol_nombre = insertar_jedi_por_nombre(arbol_nombre, jedi)
    arbol_ranking = insertar_jedi_por_ranking(arbol_ranking, jedi)
    arbol_especie = insertar_jedi_por_especie(arbol_especie, jedi)

# Realizar barridos
print("Barrido inorden del árbol por nombre:")
print(inorden(arbol_nombre))
print()

print("Barrido inorden del árbol por ranking:")
print(inorden(arbol_ranking))
print()

print("Barrido por nivel del árbol por ranking:")
print(nivel(arbol_ranking))
print()

print("Barrido por nivel del árbol por especie:")
print(nivel(arbol_especie))
print()

# Mostrar información de Yoda y Luke Skywalker
print("Información de Yoda:")
yoda = buscar_jedi_por_nombre(arbol_nombre, "Yoda")
if yoda:
    listar_jedi([yoda])
else:
    print("Yoda no encontrado.")
print()

print("Información de Luke Skywalker:")
luke = buscar_jedi_por_nombre(arbol_nombre, "Luke Skywalker")
if luke:
    listar_jedi([luke])
else:
    print("Luke Skywalker no encontrado.")
print()

# Mostrar todos los Jedi con ranking “Jedi Master”
print("Jedi con ranking 'Jedi Master':")
jedi_master = buscar_jedi_por_ranking(arbol_ranking, "Jedi Master")
if jedi_master:
    listar_jedi([jedi_master])
else:
    print("No se encontraron Jedi con ranking 'Jedi Master'.")
print()

# Listar todos los Jedi que utilizaron sable de luz color verde
print("Jedi con sable de luz verde:")
jedi_verde = [jedi for jedi in jedis if "Verde" in jedi.color_sable]
listar_jedi(jedi_verde)
print()

# Listar todos los Jedi cuyos maestros están en el archivo
print("Jedi cuyos maestros están en el archivo:")
jedi_maestros = [jedi for jedi in jedis if any(maestro in [j.nombre for j in jedis] for maestro in jedi.maestros)]
listar_jedi(jedi_maestros)
print()

# Mostrar todos los Jedi de especie “Togruta” o “Cerean”
print("Jedi de especie 'Togruta' o 'Cerean':")
jedi_especies = [jedi for jedi in jedis if jedi.especie in ["Togruta", "Cerean"]]
listar_jedi(jedi_especies)
print()

# Listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre
print("Jedi cuyos nombres comienzan con A o contienen '-'")
jedi_a_hifen = [jedi for jedi in jedis if jedi.nombre.startswith("A") or "-" in jedi.nombre]
listar_jedi(jedi_a_hifen)

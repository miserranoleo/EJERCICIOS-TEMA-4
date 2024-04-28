class NodoArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class NodoArbolNario:
    def __init__(self, valor, es_directorio=True):
        self.valor = valor
        self.es_directorio = es_directorio
        self.hijos = []

def transformar_a_binario(arbol_nario):
    if arbol_nario is None:
        return None

    raiz_binaria = NodoArbolBinario(arbol_nario.valor)

    if arbol_nario.es_directorio:
        for hijo in arbol_nario.hijos:
            hijo_binario = transformar_a_binario(hijo)
            if raiz_binaria.izquierda is None:
                raiz_binaria.izquierda = hijo_binario
            else:
                actual = raiz_binaria.izquierda
                while actual.derecha:
                    actual = actual.derecha
                actual.derecha = hijo_binario
    else:
        raiz_binaria.izquierda = NodoArbolBinario(arbol_nario.valor)

    return raiz_binaria

def barrido_inorden(raiz):
    if raiz is None:
        return []

    return barrido_inorden(raiz.izquierda) + [raiz.valor] + barrido_inorden(raiz.derecha)

def listar_contenido_carpeta(raiz, nombre_carpeta):
    if raiz is None:
        return []

    if raiz.valor == nombre_carpeta:
        contenido = []
        actual = raiz.izquierda
        while actual:
            contenido.append(actual.valor)
            actual = actual.derecha
        return contenido
    else:
        return listar_contenido_carpeta(raiz.izquierda, nombre_carpeta) + listar_contenido_carpeta(raiz.derecha, nombre_carpeta)

def contar_archivos_por_carpeta(raiz):
    if raiz is None:
        return {}

    if raiz.izquierda is None:
        return {raiz.valor: 1}
    else:
        conteo = {}
        actual = raiz.izquierda
        while actual:
            if actual.valor in conteo:
                conteo[actual.valor] += 1
            else:
                conteo[actual.valor] = 1
            actual = actual.derecha
        return conteo

def mostrar_archivos(raiz):
    if raiz is None:
        return []

    archivos = []
    if raiz.izquierda is None:
        archivos.append(raiz.valor)
    else:
        actual = raiz.izquierda
        while actual:
            archivos.append(actual.valor)
            actual = actual.derecha

    return archivos

# Crear un árbol n-ario de ejemplo
# Esto es solo una representación simplificada del árbol n-ario del directorio
# Para un árbol n-ario más complejo, se necesitaría un proceso diferente para construirlo
# Supongamos que tenemos un árbol n-ario con una estructura similar a esta:
# / (directorio)
# ├── Documentos (directorio)
# │   ├── Tareas (directorio)
# │   │   ├── tarea1.txt (archivo)
# │   │   └── tarea2.txt (archivo)
# │   └── Notas (directorio)
# │       ├── nota1.txt (archivo)
# │       └── nota2.txt (archivo)
# └── Imágenes (directorio)
#     ├── imagen1.jpg (archivo)
#     └── imagen2.png (archivo)

arbol_nario = NodoArbolNario("/", True)
documentos = NodoArbolNario("Documentos", True)
tareas = NodoArbolNario("Tareas", True)
tarea1 = NodoArbolNario("tarea1.txt", False)
tarea2 = NodoArbolNario("tarea2.txt", False)
notas = NodoArbolNario("Notas", True)
nota1 = NodoArbolNario("nota1.txt", False)
nota2 = NodoArbolNario("nota2.txt", False)
imagenes = NodoArbolNario("Imágenes", True)
imagen1 = NodoArbolNario("imagen1.jpg", False)
imagen2 = NodoArbolNario("imagen2.png", False)

arbol_nario.hijos = [documentos, imagenes]
documentos.hijos = [tareas, notas]
tareas.hijos = [tarea1, tarea2]
notas.hijos = [nota1, nota2]
imagenes.hijos = [imagen1, imagen2]

# Transformar el árbol n-ario en un árbol binario no balanceado
arbol_binario = transformar_a_binario(arbol_nario)

# Realizar barrido inorden del árbol binario
print("Barrido inorden del árbol binario:")
print(barrido_inorden(arbol_binario))
print()

# Listar el contenido de la carpeta /Imágenes
print("Contenido de la carpeta /Imágenes:")
print(listar_contenido_carpeta(arbol_binario, "Imágenes"))
print()

# Contar cuántos archivos hay en cada carpeta
print("Cantidad de archivos por carpeta:")
print(contar_archivos_por_carpeta(arbol_binario))
print()

# Mostrar todos los archivos
print("Todos los archivos:")
print(mostrar_archivos(arbol_binario))

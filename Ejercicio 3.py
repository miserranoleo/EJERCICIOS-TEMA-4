class NodoArbolBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_nodos_nivel(raiz, nivel_deseado):
    if raiz is None:
        return 0

    if nivel_deseado == 0:
        return 1
    else:
        return contar_nodos_nivel(raiz.izquierda, nivel_deseado - 1) + contar_nodos_nivel(raiz.derecha, nivel_deseado - 1)

def nivel_completo(raiz, nivel_deseado):
    if raiz is None:
        return False

    if nivel_deseado == 0:
        return raiz.izquierda is not None and raiz.derecha is not None
    else:
        return nivel_completo(raiz.izquierda, nivel_deseado - 1) and nivel_completo(raiz.derecha, nivel_deseado - 1)

def contar_nodos_faltantes(raiz, nivel_deseado):
    if raiz is None:
        return 0

    if nivel_completo(raiz, nivel_deseado):
        return 0

    nodos_faltantes = 0
    if nivel_deseado == 0:
        if raiz.izquierda is None:
            nodos_faltantes += 1
        if raiz.derecha is None:
            nodos_faltantes += 1
    else:
        nodos_faltantes += contar_nodos_faltantes(raiz.izquierda, nivel_deseado - 1)
        nodos_faltantes += contar_nodos_faltantes(raiz.derecha, nivel_deseado - 1)

    return nodos_faltantes

# Ejemplo de árbol binario
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#  /
# 7
raiz = NodoArbolBinario(1)
raiz.izquierda = NodoArbolBinario(2)
raiz.derecha = NodoArbolBinario(3)
raiz.izquierda.izquierda = NodoArbolBinario(4)
raiz.izquierda.derecha = NodoArbolBinario(5)
raiz.derecha.derecha = NodoArbolBinario(6)
raiz.izquierda.izquierda.izquierda = NodoArbolBinario(7)

nivel = 2

# Calcular el número de nodos en el nivel dado
num_nodos_nivel = contar_nodos_nivel(raiz, nivel)
print(f"El número de nodos en el nivel {nivel} es: {num_nodos_nivel}")

# Determinar si el nivel está completo
nivel_completo_resultado = nivel_completo(raiz, nivel)
if nivel_completo_resultado:
    print(f"El nivel {nivel} está completo.")
else:
    print(f"El nivel {nivel} no está completo.")

# Contar los nodos faltantes para completar el nivel
nodos_faltantes = contar_nodos_faltantes(raiz, nivel)
print(f"Nodos faltantes para completar el nivel {nivel}: {nodos_faltantes}")

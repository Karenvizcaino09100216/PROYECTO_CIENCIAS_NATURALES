import re
from fractions import Fraction
from collections import defaultdict
import math



elementos_validos = [
"H","He","Li","Be","B","C","N","O","F","Ne",
"Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
"Fe","Cu","Zn","Ag","Au","Hg","Pb","Sn"
]



from fractions import Fraction
from collections import defaultdict
import re
import math



def mostrar_introduccion():

    print("\n--------------------------------------------------")
    print("        PROGRAMA DE ESTEQUIOMETRÍA")
    print(" Balanceador de ecuaciones químicas en Python")
    print("--------------------------------------------------\n")

    print("¿QUÉ ES LA ESTEQUIOMETRÍA?\n")

    print("La estequiometría es una rama de la química que estudia")
    print("las relaciones cuantitativas entre los reactivos y los")
    print("productos que participan en una reacción química.")
    print("\nEsto significa que permite calcular cuánta cantidad")
    print("de una sustancia reacciona con otra y qué cantidad")
    print("de producto se obtiene.\n")

    print("Para poder realizar cálculos estequiométricos es")
    print("necesario que la ecuación química esté BALANCEADA.")
    print("Una ecuación está balanceada cuando tiene el mismo")
    print("número de átomos de cada elemento en ambos lados.")
    print("\n")

    print("--------------------------------------------------")
    print("PASOS PARA UTILIZAR LA ESTEQUIOMETRÍA")
    print("--------------------------------------------------\n")

    print("1. Identificar los reactivos y los productos.")
    print("2. Reconocer los elementos químicos presentes.")
    print("3. Identificar los subíndices de cada compuesto.")
    print("4. Ajustar los coeficientes de cada sustancia.")
    print("5. Verificar que el número de átomos sea igual")
    print("   en ambos lados de la ecuación.")
    print("6. Si no coincide, se realiza el balanceo.\n")

    print("Este programa realizará automáticamente")
    print("el proceso de balanceo.\n")

    print("Ejemplo de ecuación:")
    print("Na2CO3 + HCl -> NaCl + H2O + CO2\n")



def parse_formula(formula):

    elementos = re.findall(r'([A-Z][a-z]?)(\d*)', formula)

    conteo = defaultdict(int)

    for elemento, numero in elementos:

        if numero == "":
            numero = 1
        else:
            numero = int(numero)

        conteo[elemento] += numero

    return dict(conteo)



def separar_reaccion(reaccion):

    reaccion = reaccion.replace("-->", "->")

    reactivos, productos = reaccion.split("->")

    lista_reactivos = reactivos.split("+")
    lista_productos = productos.split("+")

    lista_reactivos = [x.strip() for x in lista_reactivos]
    lista_productos = [x.strip() for x in lista_productos]

    return lista_reactivos, lista_productos



def crear_matriz(reactivos, productos):

    compuestos = reactivos + productos

    elementos = set()

    formulas = []

    for compuesto in compuestos:

        datos = parse_formula(compuesto)

        formulas.append(datos)

        for elemento in datos:
            elementos.add(elemento)

    elementos = list(elementos)

    matriz = []

    for elemento in elementos:

        fila = []

        for i, formula in enumerate(formulas):

            cantidad = formula.get(elemento, 0)

            if i < len(reactivos):
                fila.append(Fraction(cantidad))
            else:
                fila.append(Fraction(-cantidad))

        matriz.append(fila)

    return matriz, elementos



def rref(matriz):

    A = [fila[:] for fila in matriz]

    filas = len(A)
    columnas = len(A[0])

    pivotes = []

    fila = 0

    for col in range(columnas):

        if fila >= filas:
            break

        for i in range(fila, filas):
            if A[i][col] != 0:
                A[i], A[fila] = A[fila], A[i]
                break
        else:
            continue

        pivote = A[fila][col]

        A[fila] = [x / pivote for x in A[fila]]

        for i in range(filas):

            if i != fila:

                factor = A[i][col]

                A[i] = [
                    A[i][j] - factor * A[fila][j]
                    for j in range(columnas)
                ]

        pivotes.append(col)

        fila += 1

    return A, pivotes



def obtener_solucion(rref_matriz, pivotes):

    columnas = len(rref_matriz[0])

    libres = [c for c in range(columnas) if c not in pivotes]

    vector = [Fraction(0)] * columnas

    libre = libres[0]

    vector[libre] = Fraction(1)

    for i, p in enumerate(pivotes):

        total = Fraction(0)

        for l in libres:
            total += rref_matriz[i][l] * vector[l]

        vector[p] = -total

    return vector



def convertir_enteros(vector):

    denominadores = [v.denominator for v in vector]

    mcm = denominadores[0]

    for d in denominadores[1:]:
        mcm = abs(mcm * d) // math.gcd(mcm, d)

    enteros = [int(v * mcm) for v in vector]

    gcd_total = abs(enteros[0])

    for n in enteros[1:]:
        gcd_total = math.gcd(gcd_total, abs(n))

    enteros = [n // gcd_total for n in enteros]

    return enteros



def verificar_balanceo(reactivos, productos):

    conteo_izq = defaultdict(int)
    conteo_der = defaultdict(int)

    for r in reactivos:

        datos = parse_formula(r)

        for e, c in datos.items():
            conteo_izq[e] += c

    for p in productos:

        datos = parse_formula(p)

        for e, c in datos.items():
            conteo_der[e] += c

    return conteo_izq == conteo_der



def balancear(reaccion):

    reactivos, productos = separar_reaccion(reaccion)

    if verificar_balanceo(reactivos, productos):

        print("\nLa ecuación ya está balanceada.")
        print("Esto ocurre porque el número de átomos")
        print("de cada elemento es igual en ambos lados.")
        return

    matriz, elementos = crear_matriz(reactivos, productos)

    rref_matriz, pivotes = rref(matriz)

    solucion = obtener_solucion(rref_matriz, pivotes)

    coeficientes = convertir_enteros(solucion)

    coef_reactivos = coeficientes[:len(reactivos)]
    coef_productos = coeficientes[len(reactivos):]

    print("\nECUACIÓN BALANCEADA\n")

    izquierda = []

    for c, r in zip(coef_reactivos, reactivos):

        if c == 1:
            izquierda.append(r)
        else:
            izquierda.append(str(c) + " " + r)

    derecha = []

    for c, p in zip(coef_productos, productos):

        if c == 1:
            derecha.append(p)
        else:
            derecha.append(str(c) + " " + p)

    print(" + ".join(izquierda) + " -> " + " + ".join(derecha))



def main():

    mostrar_introduccion()

    reaccion = input("Ingrese la ecuación química:\n")

    balancear(reaccion)


main()
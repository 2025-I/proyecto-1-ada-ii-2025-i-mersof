from itertools import combinations

def read_file(funcion):
    file2 = "../entradas/file2.txt"

    with open(file2, "r") as f:
        lineas = [linea.strip() for linea in f.readlines() if linea.strip()]

    i = 0
    n_problems = int(lineas[i])
    i += 1

    # Recorre de acuerdo a el numero de problemas y va guardando en cada uno:
    # m -> numero de empleados
    # El grafo
    # Lista de calificaciones de cada empleado

    for n in range(n_problems):

        m = int(lineas[i])  # numero de empleados
        i += 1

        grafo = []  # Genera la matriz de las reglas de supervision
        for _ in range(m):
            grafo.append(list(map(int, lineas[i].split())))
            i += 1
        print(grafo)
        # Toma cada caracter de la linea y lo convierte en una lista de enteros separados con coma
        calificaciones = list(map(int, lineas[i].split()))

        i += 1
        arbol_reglasSupervicion(m, grafo, calificaciones, funcion)

        # Se llama la funcion pasandole los datos del problema para
        # resolver la maximizacion de las calificaciones y construir la solucion optima


def arbol_reglasSupervicion(m, grafo, calificaciones, funcion):
    # Genera un diccionario donde cada llave es un supervisor y una lista de values que son los subordinado
    reglas = {i: [] for i in range(m)}
    tiene_supervisor = [False] * m

    for supervisor, fila in enumerate(grafo):

        for supervisado, relacion in enumerate(fila):

            if relacion == 1:
                reglas[supervisor].append(supervisado)
                tiene_supervisor[supervisado] = True

    if funcion == "voraz":
        print(reglas)
        return max_sumaVoraz(m, reglas, calificaciones)
    elif funcion == "dinamica":
        # Detectar raíz (el empleado que no tiene supervisor) para el algoritmo dinamico
        raices = [i for i, tiene in enumerate(tiene_supervisor) if not tiene]
        if len(raices) != 1:
            raise ValueError("El grafo debe ser un único árbol")
        raiz = raices[0]
        return max_sumaDinamica(m, raiz, reglas, calificaciones)
    elif funcion == "bruta":
        return max_sumaFuerzaBruta(m, reglas, calificaciones)


def max_sumaVoraz(m, reglas, calificaciones):
    maxima_calificacion = max(calificaciones)  # Escogemos el valor maximo de la lista calificaciones
    index_maximo = calificaciones.index(
        maxima_calificacion)  # Obtenemos su indice del empelado con el valor maximo para saber en que posicion se ubica en invitados
    index_eliminados = set()  # Se añadiran al conjunto el supervisor y el subordinado del empleado con el valor maximo, para no invitarlos
    suma_maxima = 0  # Se iran sumando las calificaciones de los empleados de mayor calificacion
    invitados = [0] * m  # Lista del tamaño del numero de empleados, para la solucion optima

    while maxima_calificacion is not None:

        if index_maximo in reglas[index_maximo]:
            index_eliminados.add(index_maximo)
            maxima_calificacion = max((v for i, v in enumerate(calificaciones) if i not in index_eliminados),
                                      default=None)
            if maxima_calificacion is None:
                break
            index_maximo = calificaciones.index(maxima_calificacion)
            continue
        # Se va sumando las calificaciones de los empleados con mayor calificacion
        # Y se invitan

        suma_maxima += maxima_calificacion
        invitados[index_maximo] = 1

        # Verifica cuales son los subordinados del empleado con mayor calificacion
        # Y los elimina para no invitarlos

        for subordinados in reglas[index_maximo]:
            index_eliminados.add(subordinados)

        # Verifica si el empleado con mayor calificacion tiene un supervisor
        # Si si, elimina su supervisor

        for supervisor, subordinado in reglas.items():
            if index_maximo in subordinado:
                index_eliminados.add(supervisor)

        # Tambien elimina el empleado con mayor calificacion
        # Para poder escoger el siguiente empleado con mayor calificacion
        # filtrando los que estan eliminados

        index_eliminados.add(index_maximo)
        maxima_calificacion = max((v for i, v in enumerate(calificaciones) if i not in index_eliminados), default=None)

        if maxima_calificacion is not None:
            index_maximo = calificaciones.index(maxima_calificacion)
        else:
            break
    # Añadimos la suma_maxima que se obtuvo para construir y devolver la solucion optima
    invitados.append(suma_maxima)
    print(invitados)
    return invitados


# Enfoque TOP-DOWN -> Guarda resultados, para no volverlos a calcular

# Diccionario donde se guardan los resultados optimos de los subproblemas


# subprolemas:
def max_sumaDinamica(m, raiz, reglas, calificaciones):
    dp = {}
    # Utilizamos esta funcion para recorrer desde abajo hacia arriba
    # --- RECORRIDO POSTORDEN SIN RECURSIVIDAD ---
    stack = []
    visitado = [False] * m
    stack.append((raiz, False))

    while stack:
        nodo, procesado = stack.pop()

        if not procesado:
            stack.append((nodo, True))
            # Añadimos hijos en orden inverso para procesarlos en el orden correcto
            for subordinado in reversed(reglas[nodo]):
                stack.append((subordinado, False))
        else:
            no_invitado = 0
            invitado = calificaciones[nodo]

            for subordinado in reglas[nodo]:
                no_invitado += max(dp[subordinado])  # Máximo entre invitar o no al hijo
                invitado += dp[subordinado][0]  # Si invitamos al padre, no al hijo

            dp[nodo] = (no_invitado, invitado)

    # --- RECONSTRUCCIÓN DE LA SOLUCIÓN (ITERATIVA) ---
    invitados = [0] * m
    pila = [(raiz, False)]  # (nodo, tomar_supervisor)

    while pila:
        nodo, tomar_supervisor = pila.pop()

        no_invitado, invitado = dp[nodo]
        invitar = not tomar_supervisor and invitado > no_invitado
        invitados[nodo] = 1 if invitar else 0

        # Añadimos los subordinados en orden inverso para mantener el orden original
        for subordinado in reversed(reglas[nodo]):
            pila.append((subordinado, invitar))

    # --- SUMA FINAL ---
    suma_maxima = sum(calificaciones[i] for i in range(m) if invitados[i] == 1)
    invitados.append(suma_maxima)
    return invitados + [suma_maxima]


def max_sumaFuerzaBruta(m, reglas, calificaciones):
    suma_maxima = 0
    mejor_combinacion = []
    invitados = [0] * m

    def validar_combinacion(comb):

        for i in comb:
            for j in comb:
                if i != j and j in reglas.get(i, []):
                    return False
        return True

    for tamano in range(1, m + 1):
        for comb in combinations(range(m), tamano):
            if validar_combinacion(comb):
                total = sum(calificaciones[i] for i in comb)
                if total > suma_maxima:
                    suma_maxima = total
                    mejor_combinacion = comb

    for _ in mejor_combinacion:
        invitados[_] = 1

    invitados.append(suma_maxima)
    print(invitados)
    return invitados


if __name__ == "__main__":
    read_file("voraz")
    # read_file("dinamica")
    # read_file("bruta")

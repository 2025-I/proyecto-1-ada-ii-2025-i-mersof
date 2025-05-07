def read_file(funcion):
    file2 = "file2.txt"

    with open(file2, 'r') as f:
        lines = [linea.strip() for linea in f.readlines() if linea.strip()]

    i = 0
    n_problems = int(lines[i])
    i += 1

    # Recorre de acuerdo a el numero de problemas y va guardando en cada uno:
    # m -> numero de empleados
    # El grafo
    # Lista de calificaciones de cada empleado

    for n in range(n_problems):

        m = int(lines[i])  # numero de empleados
        i += 1

        grafo = []  # Genera la matriz de las reglas de supervision
        for _ in range(m):
            grafo.append(lines[i].split())
            i += 1

        # Toma cada caracter de la linea y lo convierte en una lista de enteros separados con coma
        calificaciones = list(map(int, lines[i].split()))

        i += 1

        arbol_reglasSupervicion(m, grafo, calificaciones, funcion)

        # Se llama la funcion pasandole los datos del problema para
        # resolver la maximizacion de las calificaciones y construir la solucion optima


def arbol_reglasSupervicion(m, grafo, calificaciones, funcion):
    # Genera un diccionario donde cada llave es un supervisor y una lista de values que son los subordinados
    reglas = {i: [] for i in range(m)}
    tiene_supervisor = [False] * m

    for supervisor, fila in enumerate(grafo):
        for supervisado, relacion in enumerate(fila):
            if relacion == 1:
                reglas[supervisor].append(supervisado)
                tiene_supervisor[supervisado] = True

    # Detectar raíz (el empleado que no tiene supervisor) para el algoritmo dinamico

    raiz = next(i for i, tiene in enumerate(tiene_supervisor) if not tiene)

    if funcion == "voraz":
        return max_sumaVoraz(m, reglas, calificaciones)
    elif funcion == "dinamica":
        return max_sumaDinamica(m, raiz, reglas, calificaciones)
    elif funcion == "bruta":
        return max_sumaFuerzaBruta()


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
            else:
                indice_maximo = calificaciones.index(maxima_calificacion)

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

    # Añadimos la suma_maxima que se obtuvo para construir y devolver la solucion optima
    invitados.append(suma_maxima)
    return invitados

#Enfoque TOP-DOWN -> Guarda resultados, para no volverlos a calcular

dp = {} #Diccionario donde se guardan los resultados optimos de los subproblemas
#subprolemas:
def max_sumaDinamica(m, raiz, reglas, calificaciones):

    #Utilizamos esta funcion para recorrer desde abajo hacia arriba
    def recorrido(nodo):

        no_invitado_empleado = 0

        # Se verifica si el empleado no esta en los subordinados de empleado : 0...n
        # lo que significa, que verifica si no se supervisa a si mismo
        invitado_empleado = calificaciones[nodo] if nodo not in reglas[nodo] else 0

        # recorremos todos los subordinados de cada empleado
        for subordinados in reglas[nodo]:
            recorrido(subordinados)
            no_invitado_empleado += max(dp[subordinados])
            invitado_empleado += dp[subordinados][0]

        dp[nodo] = (no_invitado_empleado, invitado_empleado)

    recorrido(raiz)
    invitados = [0] * m

    def construir_solcionOptima(nodo, tomar_supervisor):

        no_invitado, invitado = dp[nodo]

        invitar = not tomar_supervisor and invitado > no_invitado

        invitados[nodo] = 1 if invitar else 0

        for subordinado in reglas[nodo]:
            construir_solcionOptima(subordinado, invitar)

    construir_solcionOptima(raiz, False)

    suma_maxima = sum(calificaciones[i] for i in range(m) if invitados[i] == 1)

    invitados.append(suma_maxima)
    return invitados

def max_sumaFuerzaBruta(n, m, grafo, calification):
    pass


if __name__ == "__main__":
    read_file("voraz")

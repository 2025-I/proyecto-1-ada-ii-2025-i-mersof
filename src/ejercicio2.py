def read_file():
    file2 = "file2.txt"

    with open(file2, 'r') as f:

        lines = [linea.strip() for linea in f.readlines() if linea.strip()]

    i = 0
    n_problems = int(lines[i])
    i += 1

    for n in range(n_problems):

        m = int(lines[i])
        i += 1

        grafo = []
        for _ in range(m):
            grafo.append(lines[i].split())
            i += 1

        # Se añaden al grafo la reglas de supervisión

        calification = list(map(int, lines[i].split()))
        i += 1

        # en la linea de calificaciones separa y convierte cada caracter en int con la funcion map

        max_sumaVoraz(n, m, grafo, calification)

        # Se llama la funcion pasandole los datos del probloma para
        # resolver la maximizacion de las calificaciones


def max_sumaVoraz(n, m, grafo, calification):
    rules = {i: int(0) for i in range(len(grafo))}
    i = 0
    nodo_actual = 0
    while i < len(rules) - 1:
        for index, rule in enumerate(grafo[nodo_actual]):
            if rule > 0:
                employable_supervised = grafo[nodo_actual].index(rule)
                rules[nodo_actual] = employable_supervised

        nodo_actual += 1
        i += 1
    print(rules)

    maxima_calification = max(calification)
    print(maxima_calification)


def max_sumaDinamica(n, m, grafo, calification):
    pass


def max_sumaFuerzaBruta(n, m, grafo, calification):
    pass


if __name__ == "__main__":
    read_file()

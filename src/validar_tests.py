def generar_grafo(n):
    grafo = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        grafo[i][i + 1] = 1
    return grafo


def validar_restricciones(m, grafo, invitados):

    # Validar que todos los valores sean 0 o 1
    for val in invitados[:m]:
        if val not in (0, 1):
            return False

    for i in range(m):
        for j in range(m):
            if grafo[i][j] == 1:
                if invitados[i] == 1 and invitados[j] == 1:
                    return False
    return True

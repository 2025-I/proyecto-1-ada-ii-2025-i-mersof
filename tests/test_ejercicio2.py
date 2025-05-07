import unittest

from src.ejercicio2 import arbol_reglasSupervicion


class TestsFiestaCompañia(unittest.TestCase):

    def test_tamano_5(self):
        m = 5
        grafo = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        calificaciones = [10, 30, 15, 5, 8]

        resultado_dinamica = arbol_reglasSupervicion(m, grafo, calificaciones, "dinamica")
        self.assertTrue(validar_solucion(m, grafo, resultado_dinamica))

    def test_solo_un_empleado(self):
        m = 1
        grafo = [[0]]
        calificaciones = [5]

        resultado_voraz = arbol_reglasSupervicion(m, grafo, calificaciones, "voraz")
        self.assertTrue(validar_solucion(m, grafo, resultado_voraz))

    def test_tamano_10(self):
        m = 10
        grafo_10 = generar_arbol_lineal(m)
        calificaciones = list(range(m))  # Datos correctos
        print(calificaciones)

        # resultado_voraz = arbol_reglasSupervicion(m, grafo_10, calificaciones, "voraz")
        resultado_dinamica = arbol_reglasSupervicion(m, grafo_10, calificaciones, "dinamica")

        # self.assertTrue(validar_solucion(m, grafo_10, resultado_voraz))
        self.assertTrue(validar_solucion(m, grafo_10, resultado_dinamica))

    def test_tamano_100(self):
        m = 100
        grafo_100 = generar_arbol_lineal(m)
        calificaciones = list(range(m))  # Datos correctos
        print(calificaciones)

        # resultado_voraz = arbol_reglasSupervicion(m, grafo_100, calificaciones, "voraz")
        resultado_dinamica = arbol_reglasSupervicion(m, grafo_100, calificaciones, "dinamica")

        # self.assertTrue(validar_solucion(m, grafo_100, resultado_voraz))
        self.assertTrue(validar_solucion(m, grafo_100, resultado_dinamica))

    def test_tamano_1000(self):
        m = 1000
        grafo_1000 = generar_arbol_lineal(m)
        calificaciones1 = list(range(m))  # Datos correctos
        print(calificaciones1)

        resultado_voraz = arbol_reglasSupervicion(m, grafo_1000, calificaciones1, "voraz")
        # resultado_dinamica = arbol_reglasSupervicion(m, grafo_1000, calificaciones1, "dinamica")

        self.assertTrue(validar_solucion(m, grafo_1000, resultado_voraz))
        # self.assertTrue(validar_solucion(m, grafo_1000, resultado_dinamica))

    def test_tamano_10000(self):
        m = 10000
        grafo_10000 = generar_arbol_lineal(m)
        calificaciones2 = list(range(m))
        print(calificaciones2)

        # resultado_voraz = arbol_reglasSupervicion(m, grafo_10000, calificaciones2, "voraz")
        resultado_dinamica = arbol_reglasSupervicion(m, grafo_10000, calificaciones2, "dinamica")

        # self.assertTrue(validar_solucion(m, grafo_10000, resultado_voraz))
        self.assertTrue(validar_solucion(m, grafo_10000, resultado_dinamica))

    def test_tamano_50000(self):
        m = 50000
        grafo_50000 = generar_arbol_lineal(m)
        calificaciones = list(range(m))
        print(calificaciones)

        resultado_voraz = arbol_reglasSupervicion(m, grafo_50000, calificaciones, "voraz")
        # resultado_dinamica = arbol_reglasSupervicion(m, grafo_50000, calificaciones, "dinamica")

        self.assertTrue(validar_solucion(m, grafo_50000, resultado_voraz))
        # self.assertTrue(validar_solucion(m, grafo_50000, resultado_dinamica))


def generar_arbol_lineal(n):
    grafo = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        grafo[i][i + 1] = 1
    return grafo


def validar_solucion(m, grafo, invitados):
    #return: True si es válida, False si hay conflictos

    # Validar que todos los valores sean 0 o 1
    for val in invitados[:m]:
        if val not in (0, 1):
            print("Valor inválido en 'invitados': debe ser solo 0 o 1")
            return False

    # Recorrer toda la matriz de adyacencia
    for i in range(m):
        for j in range(m):
            if grafo[i][j] == 1:  # Si i supervisa a j
                if invitados[i] == 1 and invitados[j] == 1:
                    print(f"Conflicto: empleado {i} y su subordinado {j} están ambos invitados")
                    return False

    return True

if __name__ == '__main__':
    unittest.main()

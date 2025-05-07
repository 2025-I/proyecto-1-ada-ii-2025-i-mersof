import unittest

from src.ejercicio2 import arbol_reglasSupervicion
from src.validar_tests_2 import generar_grafo, validar_restricciones


class TestsFiestaCompania(unittest.TestCase):

    def test_tamano_5(self):
        m = 5
        grafo = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        calificaciones = [10, 30, 15, 5, 8]

        resultado_dinamica = arbol_reglasSupervicion(m, grafo, calificaciones, "dinamica")
        self.assertTrue(validar_restricciones(m, grafo, resultado_dinamica))

    def test_solo_un_empleado(self):
        m = 1
        grafo = [[0]]
        calificaciones = [5]

        resultado_voraz = arbol_reglasSupervicion(m, grafo, calificaciones, "voraz")
        self.assertTrue(validar_restricciones(m, grafo, resultado_voraz))

    def test_tamano_10(self):
        m = 10
        grafo_10 = generar_grafo(m)
        calificaciones = list(range(m))  # Datos correctos
        print(calificaciones)

        # resultado_voraz = arbol_reglasSupervicion(m, grafo_10, calificaciones, "voraz")
        #resultado_dinamica = arbol_reglasSupervicion(m, grafo_10, calificaciones, "dinamica")
        resultado_bruta = arbol_reglasSupervicion(m, grafo_10, calificaciones, "bruta")

        # self.assertTrue(validar_restricciones(m, grafo_10, resultado_voraz))
        #self.assertTrue(validar_restricciones(m, grafo_10, resultado_dinamica))
        self.assertTrue(validar_restricciones(m, grafo_10, resultado_bruta))


    def test_tamano_100(self):
            m = 100
            grafo_100 = generar_grafo(m)
            calificaciones = list(range(m))  # Datos correctos
            print(calificaciones)

            # resultado_voraz = arbol_reglasSupervicion(m, grafo_100, calificaciones, "voraz")
            resultado_dinamica = arbol_reglasSupervicion(m, grafo_100, calificaciones, "dinamica")

            # self.assertTrue(validar_restricciones(m, grafo_100, resultado_voraz))
            self.assertTrue(validar_restricciones(m, grafo_100, resultado_dinamica))

    def test_tamano_1000(self):
        m = 1000
        grafo_1000 = generar_grafo(m)
        calificaciones1 = list(range(m))  # Datos correctos
        print(calificaciones1)

        resultado_voraz = arbol_reglasSupervicion(m, grafo_1000, calificaciones1, "voraz")
        # resultado_dinamica = arbol_reglasSupervicion(m, grafo_1000, calificaciones1, "dinamica")

        self.assertTrue(validar_restricciones(m, grafo_1000, resultado_voraz))
        # self.assertTrue(validar_restricciones(m, grafo_1000, resultado_dinamica))

    def test_tamano_10000(self):
        m = 10000
        grafo_10000 = generar_grafo(m)
        calificaciones2 = list(range(m))
        print(calificaciones2)

        # resultado_voraz = arbol_reglasSupervicion(m, grafo_10000, calificaciones2, "voraz")
        resultado_dinamica = arbol_reglasSupervicion(m, grafo_10000, calificaciones2, "dinamica")

        # self.assertTrue(validar_restricciones(m, grafo_10000, resultado_voraz))
        self.assertTrue(validar_restricciones(m, grafo_10000, resultado_dinamica))

    def test_tamano_50000(self):
        m = 50000
        grafo_50000 = generar_grafo(m)
        calificaciones = list(range(m))
        print(calificaciones)

        resultado_voraz = arbol_reglasSupervicion(m, grafo_50000, calificaciones, "voraz")
        # resultado_dinamica = arbol_reglasSupervicion(m, grafo_50000, calificaciones, "dinamica")

        self.assertTrue(validar_restricciones(m, grafo_50000, resultado_voraz))
        # self.assertTrue(validar_restricciones(m, grafo_50000, resultado_dinamica))


if __name__ == '__main__':
    unittest.main()

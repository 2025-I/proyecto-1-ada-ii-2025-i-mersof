import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from src.ejercicio2 import arbol_reglasSupervicion
from src.validar_tests_2 import generar_grafo, validar_restricciones

def medir_tiempos():

    resultados = {
        'voraz': [],
        'dinamica': [],
    }

    for estrategia in ["voraz", "dinamica"]:
        print(f"\nEjecutando estrategia '{estrategia}'...")

        for t in [100, 200, 300, 400, 500]:

            print(f"\n{'='*60}")
            print(f"Probando con m = {t}")
            print(f"{'='*60}")

            grafo = generar_grafo(t)
            calificaciones = list(range(t))

            suma = 0
            exitosas = 0

            for _ in range(5):
                start_time = time.perf_counter()
                resultado = arbol_reglasSupervicion(t, grafo, calificaciones, estrategia)
                end_time = time.perf_counter()

                if validar_restricciones(t, grafo, resultado):
                    suma += (end_time - start_time)
                    exitosas += 1
                else:
                    print(f"Resultado inválido en {estrategia} con m={t}")
                    break

            if exitosas == 5:
                promedio = suma / 5
                resultados[estrategia].append(promedio)
            else:
                resultados[estrategia].append(None)  # o 0, o dejar vacío según prefieras

    print(resultados)
    return resultados

def graficas(resultados):
    estrategias = list(resultados.keys())
    num_estrategias = len(estrategias)
    width = 0.25  # ancho de cada barra

    tamaños = [100, 200, 300, 400, 500]
    posiciones_base = list(range(len(tamaños)))

    plt.figure(figsize=(10, 6))

    # Dibujar cada estrategia con desplazamiento en X
    for i, estrategia in enumerate(estrategias):
        desplazamiento = [x + width * i for x in posiciones_base]
        tiempos = resultados[estrategia]
        barras = plt.bar(desplazamiento, tiempos, width=width, label=estrategia.capitalize())

        # Añadir los valores encima de cada barra
        for barra in barras:
            yval = barra.get_height()
            plt.text(barra.get_x() + barra.get_width()/2, yval + 0.0005,
                     f"{yval:.3f}", ha='center', va='bottom', fontsize=8)

    # Calcular el centro de cada grupo de barras para las etiquetas
    tick_pos = [x + width * (num_estrategias - 1) / 2 for x in posiciones_base]
    plt.xticks(tick_pos, tamaños)

    # Etiquetas y detalles
    plt.xlabel("Tamaño de entrada (m)")
    plt.ylabel("Tiempo promedio (sg)")
    plt.title("Comparación de Tiempos Promedios por Estrategia")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    r = medir_tiempos()
    graficas(r)


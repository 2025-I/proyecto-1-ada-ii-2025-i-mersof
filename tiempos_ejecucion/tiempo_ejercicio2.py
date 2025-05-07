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
        'bruta': [],
    }

    for estrategia in ["voraz", "dinamica", "bruta"]:

        print(f"\nEjecutando estrategia '{estrategia}'...")

        suma = 0
        for t in [4, 8, 12, 16, 20]:

            print(f"\n{'='*60}")
            print(f"Probando con m = {t}")
            print(f"{'='*60}")

            grafo = generar_grafo(t)
            calificaciones = list(range(t))

            start_time = time.perf_counter()
            resultado = arbol_reglasSupervicion(t, grafo, calificaciones, estrategia)
            end_time = time.perf_counter()

            es_valida = validar_restricciones(t, grafo, resultado)

            if es_valida is True:
                suma += (end_time - start_time)*1000

            else: break

        tiempo_promedio = (suma/5)
        resultados[estrategia] = tiempo_promedio

    print(resultados)
    return resultados

def graficas(resultados):

    # Extraer los tiempos
    voraz_time = resultados["voraz"]
    dinamica_time = resultados["dinamica"]
    bruta_time = resultados["bruta"]


# Preparar datos para graficar
    etiquetas = ['Voraz', 'Dinámica', 'Fuerza Bruta']
    tiempos = [voraz_time, dinamica_time, bruta_time]

    # Crear gráfica de barras
    plt.figure(figsize=(8, 5))
    barras = plt.bar(etiquetas, tiempos, color=["#4E79A7", "#F28E2B", "#f71f1f"])

    # Títulos y etiquetas
    plt.xlabel("Estrategias")
    plt.ylabel("Tiempo en milisegundos")
    plt.title("Comparación de Tiempos Promedios (5 repeticiones)\n Voraz vs Dinámica vs Fuerza Bruta")
    plt.grid(True, linestyle='--', alpha=0.5)

    # Mostrar los valores encima de las barras
    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.0005,
                 f"{yval:.6f}", ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    r = medir_tiempos()
    graficas(r)


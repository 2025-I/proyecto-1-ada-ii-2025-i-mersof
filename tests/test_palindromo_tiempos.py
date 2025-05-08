
import time
import random
import string
import csv
import sys
from pathlib import Path

# Agregar la raíz del proyecto al path para importar desde src
sys.path.append(str(Path(__file__).parent.parent))

# Ahora puedes importar desde src.ejercicio1
from src.ejercicio1 import (
    normalize_text,
    find_longest_palindromic_subsequence_dp,
    find_longest_palindromic_subsequence_brute,
    find_longest_palindromic_subsequence_greedy
)

# -----------------------------
# Configuración
# -----------------------------
TAMANOS = {
    "Juguete": 10,
    "Pequeño": 100,
    "Mediano": 1000,
    "Grande": 10000,
    "Extra Grande": 50000
}

REPETICIONES = 5
RESULTADOS_CSV = "../resultados_tiempos.csv"  # Guarda en la raíz del proyecto

# -----------------------------
# Función auxiliar para generar datos aleatorios
# -----------------------------
def generar_datos(tamaño):
    def random_string(length=20):
        return ''.join(random.choices(string.ascii_lowercase + ' ', k=length))
    return [random_string() for _ in range(tamaño)]

# -----------------------------
# Programa principal
# -----------------------------
if __name__ == "__main__":
    resultados_totales = []

    for nombre_tam, tamano in TAMANOS.items():
        print(f"\n🧪 Ejecutando tests para '{nombre_tam}' ({tamano} frases)...")

        for i in range(REPETICIONES):
            print(f" Repetición {i+1}/{REPETICIONES}")
            datos = generar_datos(tamano)
            normalized = [normalize_text(frase) for frase in datos]

            start_dp = time.perf_counter()
            dp_res = find_longest_palindromic_subsequence_dp(normalized)
            end_dp = time.perf_counter()

            start_brute = time.perf_counter()
            brute_res = find_longest_palindromic_subsequence_brute(normalized)
            end_brute = time.perf_counter()

            start_greedy = time.perf_counter()
            greedy_res = find_longest_palindromic_subsequence_greedy(normalized)
            end_greedy = time.perf_counter()

            resultados_totales.append({
                "Tamaño_nombre": nombre_tam,
                "Tamaño_numero": tamano,
                "Repetición": i + 1,
                "Tiempo_DP": end_dp - start_dp,
                "Tiempo_Brute": end_brute - start_brute,
                "Tiempo_Greedy": end_greedy - start_greedy
            })

    # Guardar resultados
    with open(RESULTADOS_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Tamaño_nombre", "Tamaño_numero", "Repetición",
            "Tiempo_DP", "Tiempo_Brute", "Tiempo_Greedy"
        ])
        writer.writeheader()
        writer.writerows(resultados_totales)

    print(f"\n Resultados guardados en '{RESULTADOS_CSV}'")
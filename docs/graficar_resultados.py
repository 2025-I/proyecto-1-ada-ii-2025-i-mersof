# docs/graficar_resultados.py

import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILE = "../resultados_tiempos.csv"  #busca el CSV en la raíz
OUTPUT_DIR = "graficas"

os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    print("ERROR No se encontró el archivo CSV. Ejecuta primero los tests de tiempo.")
    exit()

df_avg = df.groupby(['Tamaño_nombre', 'Tamaño_numero']).mean().reset_index()

# Gráfica de barras
plt.figure(figsize=(10, 6))
df_avg.set_index('Tamaño_nombre')[['Tiempo_DP', 'Tiempo_Brute', 'Tiempo_Greedy']].plot(kind='bar')
plt.title("Comparativa de tiempos promedio")
plt.ylabel("Tiempo promedio (segundos)")
plt.xlabel("Tamaño de entrada")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(["Programación Dinámica", "Fuerza Bruta", "Greedy"])
plt.savefig(os.path.join(OUTPUT_DIR, "tiempos_promedio.png"))
plt.show()
import tkinter as tk 
from tkinter import filedialog
import unicodedata
import re
import time

# ==============================
# FUNCIONES AUXILIARES
# ==============================

def normalizar(cadena):
    """Normaliza la cadena: sin acentos, minúsculas, solo letras y números."""
    cadena = cadena.lower()
    cadena = ''.join(
        c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn'
    )
    cadena = re.sub(r'[^a-z0-9]', '', cadena)
    return cadena


# ==============================
# PROGRAMACIÓN DINÁMICA
# ==============================

def palindromo_mas_largo(cadena):
    n = len(cadena)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if cadena[i] == cadena[j]:
                dp[i][j] = 2 + dp[i+1][j-1] if l > 2 else 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp 

def reconstruir_palindromo(cadena, dp):
    n = len(cadena)
    memo = {}

    def helper(i, j):
        if i > j: return {""}
        if i == j: return {cadena[i]}
        if (i, j) in memo: return memo[(i, j)]

        res = set()
        if cadena[i] == cadena[j] and dp[i][j] == dp[i+1][j-1] + 2:
            for mid in helper(i+1, j-1):
                res.add(cadena[i] + mid + cadena[j])
        if dp[i+1][j] == dp[i][j]:
            res.update(helper(i+1, j))
        if dp[i][j-1] == dp[i][j]:
            res.update(helper(i, j-1))

        memo[(i, j)] = res
        return res

    posibles = helper(0, n - 1)
    max_len = max(len(p) for p in posibles)
    return min(p for p in posibles if len(p) == max_len)

 
def resolver_dinamico(lineas):
    n = int(lineas[0])
    resultados = []
    for i in range(1, n + 1):
        normal = normalizar(lineas[i])
        if not normal:
            resultados.append("")
            continue
        dp = palindromo_mas_largo(normal)
        resultados.append(reconstruir_palindromo(normal, dp))
    return resultados


# ==============================
# FUERZA BRUTA
# ==============================

def generar_palindromos(cadena):
    memo = {}

    def helper(i, j):
        if i > j: return {""}
        if i == j: return {cadena[i]}
        if (i, j) in memo: return memo[(i, j)]
        res = set()
        if cadena[i] == cadena[j]:
            for mid in helper(i+1, j-1):
                res.add(cadena[i] + mid + cadena[j])
        res.update(helper(i+1, j))
        res.update(helper(i, j-1))
        memo[(i, j)] = res
        return res

    posibles = helper(0, len(cadena) - 1)
    max_len = max((len(p) for p in posibles), default=0)
    return min((p for p in posibles if len(p) == max_len), default="")


def resolver_fuerza_bruta(lineas):
    n = int(lineas[0])
    resultados = []
    for i in range(1, n + 1):
        normal = normalizar(lineas[i])
        if not normal:
            resultados.append("")
            continue
        resultados.append(generar_palindromos(normal))
    return resultados


# ==============================
# VORAZ
# ==============================

def voraz(cadena):
    mejor = ""
    def expandir(i, j):
        while i >= 0 and j < len(cadena) and cadena[i] == cadena[j]:
            i -= 1
            j += 1
        return cadena[i+1:j]

    for i in range(len(cadena)):
        p1 = expandir(i, i)
        p2 = expandir(i, i + 1)
        mejor = max(mejor, p1, p2, key=len)

    return mejor

def resolver_voraz(lineas):
    n = int(lineas[0])
    resultados = []
    for i in range(1, n + 1):
        normal = normalizar(lineas[i])
        if not normal:
            resultados.append("")
            continue
        resultados.append(voraz(normal))
    return resultados


# ==============================
# ARCHIVOS
# ==============================

def seleccionar_archivo():
    raiz = tk.Tk()
    raiz.withdraw()
    ruta = filedialog.askopenfilename(
        title="Selecciona el archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if not ruta:
        raise FileNotFoundError("No se seleccionó archivo.")
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def guardar_resultados(resultados):
    raiz = tk.Tk()
    raiz.withdraw()
    ruta = filedialog.asksaveasfilename(
        title="Guardar resultados como...",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if not ruta:
        print("No se guardó ningún archivo.")
        return
    with open(ruta, "w", encoding="utf-8") as f:
        for r in resultados:
            f.write(r + "\n")
    print(f"Resultados guardados en: {ruta}")


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    try:
        lineas = seleccionar_archivo()
    except FileNotFoundError as e:
        print(e)
        exit()

    print("=== Selecciona el algoritmo ===")
    print("1. Programación Dinámica")
    print("2. Fuerza Bruta")
    print("3. Voraz")

    opcion = input("Opción (1/2/3): ").strip()
    if opcion == "1":
        resultados = resolver_dinamico(lineas)
    elif opcion == "2":
        resultados = resolver_fuerza_bruta(lineas)
    elif opcion == "3":
        resultados = resolver_voraz(lineas)
    else:
        print("Opción no válida.")
        exit()

    print("\n--- RESULTADOS ---")
    for r in resultados:
        print(r)

    guardar = input("\n¿Deseas guardar los resultados en un archivo? (s/n): ").strip().lower()
    if guardar == "s":
        guardar_resultados(resultados)

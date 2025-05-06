import unicodedata
import tkinter as tk
from tkinter import filedialog
import re

def normalizar(cadena):
    cadena = cadena.lower()
    cadena = ''.join(
        c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn'
    )
    cadena = re.sub(r'[^a-z0-9]', '', cadena)
    return cadena

def dp_longitud_maxima(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for longitud in range(2, n+1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            if s[i] == s[j]:
                if longitud == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp

def backtrack(s, i, j, camino, dp, resultados):
    if i > j:
        resultados.add(camino + camino[::-1])
        return
    if i == j:
        resultados.add(camino + s[i] + camino[::-1])
        return
    if s[i] == s[j] and dp[i][j] == dp[i+1][j-1] + 2:
        backtrack(s, i+1, j-1, camino + s[i], dp, resultados)
    else:

        if dp[i+1][j] >= dp[i][j-1]:
            backtrack(s, i+1, j, camino, dp, resultados)
        if dp[i][j-1] >= dp[i+1][j]:
            backtrack(s, i, j-1, camino, dp, resultados)

def resolver_problema_1(entrada):
    n = int(entrada[0])
    resultados = []

    for i in range(1, n+1):
        original = entrada[i]
        cadena = normalizar(original)
        if not cadena:
            resultados.append("")
            continue
        dp = dp_longitud_maxima(cadena)
        subconjuntos = set()
        backtrack(cadena, 0, len(cadena)-1, "", dp, subconjuntos)
        resultado = sorted(subconjuntos)[0]  # elegimos el primero alfabéticamente
        resultados.append(resultado)
    
    return resultados


# ==============================
# FILE CHOOSER
# ==============================

def seleccionar_archivo():
    raiz = tk.Tk()
    raiz.withdraw()  # Ocultar ventana principal
    
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo de entrada",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    
    if not ruta_archivo:
        raise FileNotFoundError("No se seleccionó un archivo válido.")
    
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read().splitlines()

# =============================
# MAINn 
# ==============================

if __name__ == "__main__":
    lineas_entrada = seleccionar_archivo()
    resultados = resolver_problema_1(lineas_entrada)
    print("\n".join(resultados))

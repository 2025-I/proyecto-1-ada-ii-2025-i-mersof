import re
import tkinter as tk
from tkinter import filedialog
import unicodedata

# ==============================
# NORMALIZACIÓN DE LA CADENA
# ==============================

def normalizar(cadena):
    cadena = unicodedata.normalize('NFKD', cadena).encode('ascii', 'ignore').decode('utf-8')
    return re.sub(r'[^a-z0-9]', '', cadena.lower())  # Incluye números y minúsculas

# ==============================
# PROGRAMACIÓN DINÁMICA PARA LONGITUD MÁXIMA
# ==============================

def dp_longitud_maxima(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i+1][j-1] if i+1 <= j-1 else 0)
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp

# ==============================
# TODAS LAS SUBSECUENCIAS MÁXIMAS
# ==============================

def backtrack(s, i, j, actual, dp, resultados):
    if i > j:
        resultados.add(actual)
        return
    if i == j:
        resultados.add(actual + s[i])
        return

    if s[i] == s[j]:

        nueva_actual = actual + s[i]
        backtrack(s, i+1, j-1, nueva_actual, dp, resultados)

        if i+1 > j-1:
            resultados.add(nueva_actual + s[j])  # Agregar la subsecuencia completa
    else:

        if dp[i+1][j] >= dp[i][j-1]:
            backtrack(s, i+1, j, actual, dp, resultados)
        if dp[i][j-1] >= dp[i+1][j]:
            backtrack(s, i, j-1, actual, dp, resultados)

# ==============================
# SOLUCIÓN PRINCIPAL
# ==============================

def resolver_problema_1(lineas_entrada):
    n = int(lineas_entrada[0])
    resultados = []
    
    for linea in lineas_entrada[1:n+1]:
        normalizada = normalizar(linea.strip())
        if not normalizada:
            resultados.append("")
            continue
            
        dp = dp_longitud_maxima(normalizada)
        max_len = dp[0][len(normalizada)-1]
        conjunto_resultados = set()
        backtrack(normalizada, 0, len(normalizada)-1, "", dp, conjunto_resultados)
        
        subsecuencias_maximas = [subseq for subseq in conjunto_resultados if len(subseq) == max_len]
        resultados.append(' '.join(sorted(subsecuencias_maximas)))
    
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
    
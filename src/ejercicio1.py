import re
import tkinter as tk
from tkinter import filedialog

# ==============================
# NORMALIZACIÓN DE LA CADENA
# ==============================
def normalizar(cadena):
    """Elimina caracteres no alfanuméricos y convierte a minúsculas."""
    return re.sub(r'[^a-z0-9]', '', cadena.lower())

# ==============================
# PROGRAMACIÓN DINÁMICA PARA LONGITUD MÁXIMA
# ==============================
def dp_longitud_maxima(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    
    # Llenar la matriz DP desde subcadenas cortas a largas
    for i in range(n-1, -1, -1):
        dp[i][i] = 1  # Subcadena de un solo carácter
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i+1][j-1] if i+1 <= j-1 else 0)
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp

# ==============================
# GENERAR TODAS LAS SUBSECUENCIAS MÁXIMAS
# ==============================
def backtrack(s, i, j, actual, dp, resultados):
    if i > j:
        resultados.add(actual)
        return
    if i == j:
        resultados.add(actual + s[i])
        return
    
    if s[i] == s[j]:
        # Incluir ambos caracteres y avanzar
        nueva_actual = actual + s[i]
        backtrack(s, i+1, j-1, nueva_actual, dp, resultados)
        # Caso especial: caracteres adyacentes
        if i+1 > j-1:
            resultados.add(actual + s[i] + s[j])
    else:
        # Explorar ambas ramas si hay empate en longitud
        if dp[i+1][j] >= dp[i][j-1]:
            backtrack(s, i+1, j, actual, dp, resultados)
        if dp[i][j-1] >= dp[i+1][j]:
            backtrack(s, i, j-1, actual, dp, resultados)



# ==============================
#  FILE CHOOSER
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


import re
import tkinter as tk
from tkinter import filedialog

# ==============================
# NORMALIZACIÓN DE LA CADENA
# ==============================
def normalizar(cadena):
    """Elimina caracteres no alfanuméricos y convierte a minúsculas."""
    return re.sub(r'[^a-z0-9]', '', cadena.lower())


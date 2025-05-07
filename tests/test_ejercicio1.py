import pytest
import random
import string
import time
from src.ejercicio1 import (
    generar_palindromos,
    palindromo_mas_largo,
    voraz
)

def generar_cadena_aleatoria(n):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def extraer_maximo_fuerza_bruta(lista):
    if not lista:
        return ""
    max_len = len(max(lista, key=len))
    return next(p for p in lista if len(p) == max_len)

# Tamaños normales
tamaños_prueba = [
    ("juguete", 10),
    ("pequeño", 100),
    ("mediano", 1000),
]

@pytest.mark.parametrize("nombre,tamaño", tamaños_prueba)
def test_algoritmos_subsecuencia_palindromica(nombre, tamaño):
    ejecutar_pruebas(nombre, tamaño)

# Pruebas "pesadas", marcadas como slow
tamaños_lentos = [
    ("grande", 10000),
    ("extra_grande", 50000),
]

@pytest.mark.slow
@pytest.mark.parametrize("nombre,tamaño", tamaños_lentos)
def test_algoritmos_subsecuencia_palindromica_lenta(nombre, tamaño):
    ejecutar_pruebas(nombre, tamaño)

# Función común para ejecutar pruebas comparativas
def ejecutar_pruebas(nombre, tamaño):
    cadena = generar_cadena_aleatoria(tamaño)
    repeticiones = 5

    # Fuerza bruta
    t_total_fb = 0
    for _ in range(repeticiones):
        t0 = time.time()
        resultado_fb = generar_palindromos(cadena)
        t_total_fb += time.time() - t0
    promedio_fb = t_total_fb / repeticiones
    mejor_fb = extraer_maximo_fuerza_bruta(resultado_fb)

    # Dinámica
    t_total_dp = 0
    for _ in range(repeticiones):
        t0 = time.time()
        resultado_dp = palindromo_mas_largo(cadena)
        t_total_dp += time.time() - t0
    promedio_dp = t_total_dp / repeticiones

    # Voraz
    t_total_vz = 0
    for _ in range(repeticiones):
        t0 = time.time()
        resultado_vz = voraz(cadena)
        t_total_vz += time.time() - t0
    promedio_vz = t_total_vz / repeticiones

    print(f"\n[{nombre.upper()} - {tamaño}]")
    print(f"Fuerza bruta: '{mejor_fb[:30]}...' (len={len(mejor_fb)}), {promedio_fb:.4f}s")
    print(f"Dinámica    : '{resultado_dp[:30]}...' (len={len(resultado_dp)}), {promedio_dp:.4f}s")
    print(f"Voraz       : '{resultado_vz[:30]}...' (len={len(resultado_vz)}), {promedio_vz:.4f}s")

    assert len(resultado_dp) == len(mejor_fb), "La solución dinámica no coincide con fuerza bruta"
    assert resultado_vz == resultado_vz[::-1], "La solución voraz no es un palíndromo válido"

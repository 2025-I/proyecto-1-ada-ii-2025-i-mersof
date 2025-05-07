import pytest
import time 
from src.ejercicio1 import resolver_dinamico, resolver_fuerza_bruta, resolver_voraz

# Función auxiliar para guardar resultados en un archivo
def guardar_resultados(algoritmo, tamano, tiempo, resultado):
    with open("resultados_pruebas.txt", "a") as f:
        f.write(f"Algoritmo: {algoritmo}, Tamaño: {tamano}, Tiempo: {tiempo:.6f} segundos, Resultado: {len(resultado)} caracteres\n")

# Datos de prueba (ahora más complejos y grandes)
pruebas = [
    ("Pequeña", ["abc" * i for i in range(1, 101)]),    # Entrada pequeña, cadenas con longitud de 3 a 300
    ("Mediana", ["abc" * i for i in range(1, 1001)]),   # Entrada mediana, cadenas de 3 a 3000
    ("Grande", ["abc" * i for i in range(1, 10001)]),   # Entrada grande, cadenas de 3 a 30000
    ("Extra Grande", ["abc" * i for i in range(1, 50001)]) # Entrada extra grande, cadenas de 3 a 150000
]

# Prueba para los tres algoritmos con una sola entrada
@pytest.mark.parametrize("tamano, lineas", pruebas)
def test_algoritmos_completos(tamano, lineas):
    # =======================
    # Test para Programación Dinámica
    start_time = time.time()
    resultado_dinamico = resolver_dinamico(lineas)
    tiempo_dinamico = time.time() - start_time
    guardar_resultados("Programación Dinámica", tamano, tiempo_dinamico, resultado_dinamico)
    
    # =======================
    # Test para Fuerza Bruta
    start_time = time.time()
    resultado_fuerza_bruta = resolver_fuerza_bruta(lineas)
    tiempo_fuerza_bruta = time.time() - start_time
    guardar_resultados("Fuerza Bruta", tamano, tiempo_fuerza_bruta, resultado_fuerza_bruta)
    
    # =======================
    # Test para Algoritmo Voraz
    start_time = time.time()
    resultado_voraz = resolver_voraz(lineas)
    tiempo_voraz = time.time() - start_time
    guardar_resultados("Voraz", tamano, tiempo_voraz, resultado_voraz)

    # =======================
    # Assert para verificar que todos los algoritmos devuelven un resultado
    assert len(resultado_dinamico) > 0
    assert len(resultado_fuerza_bruta) > 0
    assert len(resultado_voraz) > 0

    # Verificar que los resultados sean consistentes (aunque cada algoritmo podría tener un enfoque distinto)
    assert resultado_dinamico == resultado_fuerza_bruta == resultado_voraz, "Los resultados no coinciden"

 
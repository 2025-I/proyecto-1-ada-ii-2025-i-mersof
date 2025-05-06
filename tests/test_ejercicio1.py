import pytest
import time
from src.ejercicio1 import resolver_problema_1
from src.ejercicio1 import normalizar, dp_longitud_maxima, backtrack, resolver_problema_1

# =======================
# TESTS PARA normalizar
# =======================

def test_normalizar_con_acentos_y_simbolos():
    assert normalizar("¡Hola, señorita Álvarez! ¿Cómo está?") == "holasenoritaalvarezcomoesta"

def test_normalizar_numeros_y_mayusculas():
    assert normalizar("Número123 ABC-XYZ") == "numero123abcxyz"

def test_normalizar_cadena_vacia():
    assert normalizar("!!!???") == ""

# =======================
# TESTS PARA dp_longitud_maxima
# =======================

def test_dp_longitud_simple_palindromo():
    s = "abba"
    dp = dp_longitud_maxima(s)
    assert dp[0][3] == 4  # "abba" es palíndromo completo

def test_dp_con_letras_repetidas():
    s = "abcba"
    dp = dp_longitud_maxima(s)
    assert dp[0][4] == 5  # "abcba"

def test_dp_sin_palindromo_largo():
    s = "abc"
    dp = dp_longitud_maxima(s)
    assert dp[0][2] == 1  # Solo un carácter

# =======================
# TESTS PARA backtrack
# =======================

def test_backtrack_unica_subsecuencia_maxima():
    s = "abba"
    dp = dp_longitud_maxima(s)
    resultados = set()
    backtrack(s, 0, len(s)-1, "", dp, resultados)
    assert "abba" in resultados

def test_backtrack_multiples_subsecuencias():
    s = "aaa"
    dp = dp_longitud_maxima(s)
    resultados = set()
    backtrack(s, 0, len(s)-1, "", dp, resultados)
    assert resultados == {"aaa"}  # Puede haber múltiples si eliges otro string


def test_backtrack_palindromo_simple():
    s = "abc"
    dp = dp_longitud_maxima(s)
    resultados = set()
    backtrack(s, 0, len(s)-1, "", dp, resultados)
    assert resultados == {"a", "b", "c"}

# =======================
# TESTS PARA resolver_problema_1
# =======================

def test_resolver_una_linea_palindromo_completo():
    entrada = ["1", "Anita lava la tina"]
    salida = resolver_problema_1(entrada)
    assert salida == ["anitalavalatina"]

def test_resolver_varias_lineas():
    entrada = ["3", "an ana", "12321", "abc"]
    salida = resolver_problema_1(entrada)
    assert salida[0] == "anana"
    assert salida[1] == "12321"
    assert salida[2] in {"a", "b", "c"} 

def test_resolver_linea_vacia_y_simbolos():
    entrada = ["2", "!!!", "@@@"]
    salida = resolver_problema_1(entrada)
    assert salida == ["", ""]


# =======================
# CASOS DE TAMAÑO JUGUETE
# =======================
def test_juguete_palindromos_simples():
    entrada = ["3", "oso", "ana", "12321"]
    salida = resolver_problema_1(entrada)
    assert salida == ["oso", "ana", "12321"]

# =======================
# CASOS PEQUEÑOS (100)
# =======================
def test_pequeno_100_elementos():
    entrada = ["100"] + ["reconocer"] * 100
    salida = resolver_problema_1(entrada)
    assert len(salida) == 100
    assert all(r == "reconocer" for r in salida)

# =======================
# CASOS MEDIANOS (1000)
# =======================
def test_mediano_1000_elementos():
    entrada = ["1000"] + ["anitalavalatina"] * 1000
    t_inicio = time.time()
    salida = resolver_problema_1(entrada)
    t_fin = time.time()
    
    assert len(salida) == 1000
    assert all(r == "anitalavalatina" for r in salida)
    assert t_fin - t_inicio < 10  # tiempo razonable

# =======================
# CASOS GRANDES (10000)
# =======================
def test_grande_10000_elementos():
    entrada = ["10000"] + ["reconocer"] * 10000
    t_inicio = time.time()
    salida = resolver_problema_1(entrada)
    t_fin = time.time()

    assert len(salida) == 10000
    assert all(r == "reconocer" for r in salida)
    assert t_fin - t_inicio < 60  # depende del equipo

# =======================
# CASOS EXTRA GRANDES (50000)
# =======================
def test_extra_grande_50000_elementos():
    entrada = ["50000"] + ["oso"] * 50000
    t_inicio = time.time()
    salida = resolver_problema_1(entrada)
    t_fin = time.time()

    assert len(salida) == 50000
    assert all(r == "oso" for r in salida)
    assert t_fin - t_inicio < 180  # tolerancia para ejecución prolongada


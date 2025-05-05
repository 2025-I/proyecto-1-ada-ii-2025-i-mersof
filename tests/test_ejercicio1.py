import pytest
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
    s = "abcba"
    dp = dp_longitud_maxima(s)
    resultados = set()
    backtrack(s, 0, len(s)-1, "", dp, resultados)
    assert resultados == {"abcba", "acbca"} # Al menos una en común

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
    assert salida == ["anana", "12321", "a b c"]

def test_resolver_linea_vacia_y_simbolos():
    entrada = ["2", "!!!", "@@@"]
    salida = resolver_problema_1(entrada)
    assert salida == ["", ""]

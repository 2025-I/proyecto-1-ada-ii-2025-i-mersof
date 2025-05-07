import pytest
from src.ejercicio1 import normalize_text, find_longest_palindromic_subsequence_dp, find_longest_palindromic_subsequence_brute, find_longest_palindromic_subsequence_greedy

def test_cadenas_con_numeros():
    entradas = ["abc123321cba"]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "abc123321cba"
    assert resultado_voraz[0] == "abc123321cba"
    assert resultado_fuerza_bruta[0] == "abc123321cba"


def test_con_acentos_y_mayusculas():
    entradas = ["Ana"]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "ana"
    assert resultado_voraz[0] == "ana"
    assert resultado_fuerza_bruta[0] == "ana"


def test_frases():
    entradas = ["Daba leer arroz a la zorra, la zorra a leer daba."]
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_voraz[0] == "dabalearrozalazorraelabad"
    assert resultado_fuerza_bruta[0] == "dabalearrozalazorraelabad"


def test_palabras_comunes():
    entradas = ["Reconocer"]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "reconocer"
    assert resultado_voraz[0] == "reconocer"
    assert resultado_fuerza_bruta[0] == "reconocer"


def test_frase_con_puntuacion_compleja():
    entradas = ["¡Anita lava la tina! La tina la lava Anita!"]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "anitavalatina"
    assert resultado_voraz[0] == "anitavalatina"
    assert resultado_fuerza_bruta[0] == "anitavalatina"


def test_palindromo_largo_con_mayusculas_y_acentos():
    entradas = ["Reina consorte de España, amada, sana, España de consorte reina."]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "reinaconsortedespanaamadasanaespanadesorentr"
    assert resultado_voraz[0] == "reinaconsortedespanaamadasanaespanadesorentr"
    assert resultado_fuerza_bruta[0] == "reinaconsortedespanaamadasanaespanadesorentr"


def test_frase_con_caracteres_especiales():
    entradas = ["Eva, ¿sabes qué te pasa? No te atrevas a pasarte."]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "evasabesteapasanoteatrevasapasarte"
    assert resultado_voraz[0] == "evasabesteapasanoteatrevasapasarte"
    assert resultado_fuerza_bruta[0] == "evasabesteapasanoteatrevasapasarte"


def test_frase_con_palabras_intercaladas():
    entradas = ["La red de redes está conectada a través de la red."]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "laredederedessconectadaatrevedelared"
    assert resultado_voraz[0] == "laredederedessconectadaatrevedelared"
    assert resultado_fuerza_bruta[0] == "laredederedessconectadaatrevedelared"


def test_frase_con_subcadenas_palindromicas():
    entradas = ["Yo dono el que dona hoy."]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "yodonelquedonahoy"
    assert resultado_voraz[0] == "yodonelquedonahoy"
    assert resultado_fuerza_bruta[0] == "yodonelquedonahoy"
 

def test_palindromo_muy_largo():
    entradas = ["Anita atina la palindromicidad de los datos. ¿Por qué la respuesta no es rápida?"]
    resultado_dinamico = find_longest_palindromic_subsequence_dp([str(len(entradas))] + entradas)
    resultado_voraz = find_longest_palindromic_subsequence_greedy([str(len(entradas))] + entradas)
    resultado_fuerza_bruta = find_longest_palindromic_subsequence_brute([str(len(entradas))] + entradas)

    assert resultado_dinamico[0] == "anitaatinalapalindromicidaddelosdatosporkuelarespuestanoresrapida"
    assert resultado_voraz[0] == "anitaatinalapalindromicidaddelosdatosporkuelarespuestanoresrapida"
    assert resultado_fuerza_bruta[0] == "anitaatinalapalindromicidaddelosdatosporkuelarespuestanoresrapida"

import unittest
from src.ejercicio1 import (
    normalize_text,
    find_longest_palindromic_subsequence_dp,
    find_longest_palindromic_subsequence_brute,
    find_longest_palindromic_subsequence_greedy
)

def is_palindrome(text):
    return text == text[::-1]

class TestPalindromo(unittest.TestCase):

    def test_a_juguete(self):
        """Test a) Juguete (10 frases): Verifica que la solución funcione"""
        frases = [
            "Anita lava la tina",
            "Sometamos o matemos",
            "La ruta nos aportó otro paso natural",
            "Dábale arroz a la zorra el abad",
            "A man a plan a canal Panama",
            "racecar",
            "abcde",
            "abaccad",
            "xyzzyx",
            "Eva can I see bees in a cave"
            
        ]
        normalized = [normalize_text(frase) for frase in frases]
        
        dp_results = find_longest_palindromic_subsequence_dp(normalized)
        brute_results = find_longest_palindromic_subsequence_brute(normalized)
        greedy_results = find_longest_palindromic_subsequence_greedy(normalized)

        for i, res in enumerate(dp_results):
            with self.subTest(indice=i):
                self.assertTrue(is_palindrome(res), f"DP falló en '{frases[i]}': {res} no es palíndromo")
                self.assertEqual(res, brute_results[i], f"DP y Brute no coinciden en '{frases[i]}'")

        for i, res in enumerate(greedy_results):
            with self.subTest(indice=i):
                self.assertTrue(is_palindrome(res), f"Greedy falló en '{frases[i]}'")

    def test_b_pequeno(self):
        """Test b) Pequeño (100 frases): Validación general"""
        from random import choices, randint
        import string

        def random_string(length=20):
            return ''.join(choices(string.ascii_lowercase + ' ', k=length))

        # Mezcla de frases base y aleatorias
        frases = ["abcde", "abaccad", "racecar", "xyzzyx", "level"] * 20
        frases += [random_string() for _ in range(80)]
        normalized = [normalize_text(f) for f in frases]

        resultados = find_longest_palindromic_subsequence_greedy(normalized)

        for i, res in enumerate(resultados):
            if i % 10 == 0:
                print(f"Evaluando resultado {i}...")
            self.assertTrue(is_palindrome(res), f"Greedy falló en frase {i}: '{res}'")

    def test_c_mediano(self):
        """Test c) Mediano (1000 frases): Escalabilidad básica"""
        from random import choices
        import string

        def random_string(length=20):
            return ''.join(choices(string.ascii_lowercase + ' ', k=length))

        frases = [random_string() for _ in range(1000)]
        normalized = [normalize_text(f) for f in frases]
        resultados = find_longest_palindromic_subsequence_dp(normalized)

        for i, res in enumerate(resultados):
            if i % 100 == 0:
                print(f"Evaluando resultado {i}...")
            self.assertTrue(is_palindrome(res), f"DP falló en frase {i}. Resultado: '{res}'")

    def test_d_grande(self):
        """Test d) Grande (10000 frases): Alto volumen"""
        from random import choices
        import string

        def random_string(length=20):
            return ''.join(choices(string.ascii_lowercase + ' ', k=length))

        frases = [random_string() for _ in range(10000)]
        normalized = [normalize_text(f) for f in frases]
        resultados = find_longest_palindromic_subsequence_dp(normalized)

        for i, res in enumerate(resultados):
            if i % 1000 == 0:
                print(f"Evaluando resultado {i}...")
            self.assertTrue(is_palindrome(res), f"DP falló en frase {i}. Resultado: '{res}'")

    def test_e_extra_grande(self):
        """Test e) Extra grande (50000 frases): Muy lento pero válido"""
        from random import choices
        import string

        def random_string(length=20):
            return ''.join(choices(string.ascii_lowercase + ' ', k=length))

        frases = [random_string() for _ in range(50000)]
        normalized = [normalize_text(f) for f in frases]
        resultados = find_longest_palindromic_subsequence_dp(normalized)

        for i, res in enumerate(resultados[:10]):  # Validar solo las primeras 10 por rendimiento
            print(f"Evaluando muestra {i}: '{res}'")
            self.assertTrue(is_palindrome(res), f"DP falló en frase {i}. Resultado: '{res}'")

    # -----------------------------
    # Tests adicionales no basados en tamaño
    # -----------------------------

    def test_caso_vacio(self):
        """Valida comportamiento con frases vacías"""
        frases = ["", "   ", "\t\n\r"]
        resultados = find_longest_palindromic_subsequence_brute(frases)

        for i, res in enumerate(resultados):
            with self.subTest(indice=i):
                self.assertEqual(res, "")
                self.assertTrue(is_palindrome(res))

    def test_un_solo_caracter(self):
        """Test con frases de un solo carácter"""
        frases = ["a", "b", "c", "d", "e"]
        resultados = find_longest_palindromic_subsequence_greedy(frases)

        for i, res in enumerate(resultados):
            with self.subTest(indice=i):
                self.assertEqual(res, frases[i])
                self.assertTrue(is_palindrome(res))

    def test_palindromo_completo(self):
        """Frase completa es un palíndromo"""
        frases = ["racecar", "madam", "radar", "level", "deed"]
        resultados = find_longest_palindromic_subsequence_brute(frases)

        for i, res in enumerate(resultados):
            with self.subTest(frase=frases[i]):
                self.assertEqual(res, frases[i])
                self.assertTrue(is_palindrome(res))

    def test_sin_palindromo_claro(self):
        """Frases sin palíndromo obvio"""
        frases = ["abcdefgh", "lmnopqrst", "xyz", "world", "hello"]
        resultados = find_longest_palindromic_subsequence_greedy(frases)

        for i, res in enumerate(resultados):
            with self.subTest(frase=frases[i]):
                self.assertLessEqual(len(res), 2, f"Resultado muy largo: '{res}'")
                self.assertTrue(is_palindrome(res))

    def test_palindromo_interno(self):
        """Palíndromo dentro de texto aleatorio"""
        frases = [
            "abcxyzracecarxyzcba",
            "holaanitalavalatinachao",
            "abcdefggfedcba",
            "xxxyyyzzzyyyxxx",
            "aabbcbbadd"
        ]
        expected = [
            "racecar",
            "anitalavalatina",
            "abcdefggfedcba",
            "yyyzzzyyy",
            "abbcbba"
        ]

        normalized = [normalize_text(f) for f in frases]
        resultados_dp = find_longest_palindromic_subsequence_dp(normalized)
        resultados_brute = find_longest_palindromic_subsequence_brute(normalized)
        resultados_greedy = find_longest_palindromic_subsequence_greedy(normalized)

        for i, (dp, brute, greedy, exp) in enumerate(zip(resultados_dp, resultados_brute, resultados_greedy, expected)):
            with self.subTest(indice=i):
                self.assertIn(dp, brute)
                self.assertTrue(is_palindrome(dp))
                self.assertTrue(is_palindrome(brute))
                self.assertTrue(is_palindrome(greedy))

if __name__ == '__main__':
    unittest.main()
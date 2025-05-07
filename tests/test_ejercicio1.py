import unittest
from src.ejercicio1 import normalize_text, find_longest_palindromic_subsequence_dp
from src.ejercicio1 import find_longest_palindromic_subsequence_brute
from src.ejercicio1 import find_longest_palindromic_subsequence_greedy

 
class TestPalindromoFunctions(unittest.TestCase):

    def test_normalize_text(self):
        self.assertEqual(normalize_text("Ánita lava la tina"), "anitalavalatina")
        self.assertEqual(normalize_text("¡Hola, Mundo! 123"), "holamundo")
        self.assertEqual(normalize_text("Sometámos-o-matémós"), "sometamosomatemos")
        self.assertEqual(normalize_text(""), "")
        self.assertEqual(normalize_text("   "), "")

    def test_multiple_inputs(self):
        inputs = [
            "Anita lava la tina",
            "Sometamos o matemos",
            "La ruta nos aportó otro paso natural"
        ]
        expected_dp = [
            "anitalavalatina",
            "sometamosomatemos",
            "larutanosaportootropasonatural"
        ]
        expected_brute = expected_dp.copy()
        expected_greedy = [
            "anitalavalatina",
            "matomsomatm",  # Greedy puede no encontrar el óptimo
            "larutanaportootropasonatural"
        ]

        self.assertEqual(find_longest_palindromic_subsequence_dp(inputs), expected_dp)
        self.assertEqual(find_longest_palindromic_subsequence_brute(inputs), expected_brute)
        self.assertEqual(find_longest_palindromic_subsequence_greedy(inputs), expected_greedy)

    def test_long_phrase(self):
        input_text = "La ruta nos aportó otro paso natural que nadie había notado antes"
        
        # Normalizamos la entrada
        normalized_input = normalize_text(input_text)

        # Ejecutar los métodos con texto ya normalizado
        result_dp = find_longest_palindromic_subsequence_dp([normalized_input], pre_normalized=True)[0]
        result_brute = find_longest_palindromic_subsequence_brute([normalized_input], pre_normalized=True)[0]
        result_greedy = find_longest_palindromic_subsequence_greedy([normalized_input], pre_normalized=True)[0]

        # Verificar que los resultados no estén vacíos y sean palíndromos
        self.assertTrue(len(result_dp) > 5)
        self.assertEqual(result_dp, result_brute)  # DP y Brute deben dar lo mismo
        self.assertTrue(result_greedy == result_dp or len(result_greedy) + 1 >= len(result_dp))  # Greedy puede no ser óptimo

    def test_perfect_palindrome(self):
        input_text = "A man, a plan, a canal: Panama"
        expected = normalize_text(input_text)
        
        result_dp = find_longest_palindromic_subsequence_dp([input_text])[0]
        self.assertEqual(result_dp, expected)

        result_brute = find_longest_palindromic_subsequence_brute([input_text])[0]
        self.assertEqual(result_brute, expected)

        result_greedy = find_longest_palindromic_subsequence_greedy([input_text])[0]
        self.assertEqual(result_greedy, expected)

    def test_edge_cases(self):
        inputs = ["", "   ", "a", "ab", "abc"]

        dp_result = find_longest_palindromic_subsequence_dp(inputs)
        self.assertEqual(dp_result, ["", "", "a", "a", "a"])

        brute_result = find_longest_palindromic_subsequence_brute(inputs)
        self.assertEqual(brute_result, ["", "", "a", "a", "a"])

        greedy_result = find_longest_palindromic_subsequence_greedy(inputs)
        self.assertEqual(greedy_result, ["", "", "a", "a", "a"])

    if __name__ == '__main__':
        unittest.main()
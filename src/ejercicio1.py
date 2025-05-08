import re
import tkinter as tk
from tkinter import filedialog
import unicodedata


# Normalizar la cadena: eliminar caracteres no alfabéticos y convertir a minúsculas

def normalize_text(text: str) -> str:

    # Normalización Unicode para quitar acentos

    text = unicodedata.normalize('NFD', text)  # Descompone los caracteres con acentos
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')  # Elimina los caracteres de acento

    # Eliminar todo lo que no sea alfabético y convertir a minúsculas

    return re.sub(r'[^a-zA-Z]', '', text).lower()


# Función de programación dinámica (LPS)
def find_longest_palindromic_subsequence_dp(input_lines: list[str], pre_normalized=False) -> list[str]:
    result = []
    for phrase in input_lines:
        normalized_phrase = phrase if pre_normalized else normalize_text(phrase)
        n = len(normalized_phrase)
        if n == 0:
            result.append("")
            continue

        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if normalized_phrase[i] == normalized_phrase[i + 1]:
                dp[i][i + 1] = True
                start, max_len = i, 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if normalized_phrase[i] == normalized_phrase[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        start, max_len = i, length

        result.append(normalized_phrase[start:start + max_len])
    return result


# Función fuerza bruta para encontrar la subsecuencia palíndroma más larga
def find_longest_palindromic_subsequence_brute(input_lines: list[str], pre_normalized=False) -> list[str]:
    def is_palindrome(s):
        return s == s[::-1]

    result = []
    for phrase in input_lines:
        normalized = phrase if pre_normalized else normalize_text(phrase)
        best = ""
        n = len(normalized)
        for i in range(n):
            for j in range(i, n):
                sub = normalized[i:j + 1]
                if is_palindrome(sub) and len(sub) > len(best):
                    best = sub
        result.append(best)
    return result


# Función voraz para encontrar la subsecuencia palíndroma más larga
def find_longest_palindromic_subsequence_greedy(input_lines: list[str], pre_normalized=False) -> list[str]:
    def expand(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    result = []
    for phrase in input_lines:
        normalized = phrase if pre_normalized else normalize_text(phrase)
        best = ""
        for i in range(len(normalized)):
            p1 = expand(normalized, i, i)
            p2 = expand(normalized, i, i + 1)
            best = max(best, p1, p2, key=len)
        result.append(best)
    return result


# Función para seleccionar un archivo
def choose_file():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(title="Selecciona un archivo .txt", filetypes=[("Text files", "*.txt")])
    return file_path


# Función principal para leer la entrada desde un archivo y ejecutar las técnicas
def main():
    file_path = choose_file()
    if not file_path:
        print("No se seleccionó ningún archivo.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

    try:
        n = int(lines[0])
        phrases = lines[1:n + 1]
    except (ValueError, IndexError):
        print("Formato incorrecto: primera línea debe ser un número.")
        return

    # Ejecutar métodos
    dp_result = find_longest_palindromic_subsequence_dp(phrases)
    brute_result = find_longest_palindromic_subsequence_brute(phrases)
    greedy_result = find_longest_palindromic_subsequence_greedy(phrases)

    # Mostrar resultados
    print("\nResultados:")
    for i, phrase in enumerate(phrases):
        print(f"\nFrase original: {phrase}")
        print(f"  DP     : {dp_result[i]}")
        print(f"  Fuerza Bruta: {brute_result[i]}")
        print(f"  Greedy : {greedy_result[i]}")


# Ejecutar el programa
if __name__ == "__main__":
    main()

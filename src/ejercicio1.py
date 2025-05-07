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
def find_longest_palindromic_subsequence_dp(input_lines: list[str]) -> list[str]:
    try:
        num_lines = int(input_lines[0])
        phrases = input_lines[1 : 1 + num_lines]
    except ValueError:
        phrases = input_lines

    result = []
    for phrase in phrases:
        normalized_phrase = normalize_text(phrase)
        length = len(normalized_phrase)
        if length == 0:
            result.append("")
            continue
 
        # P[i][j] = True si normalized_phrase[i..j] es palíndromo
        dp_table = [[False] * length for _ in range(length)]
        start_index, max_length = 0, 1

        # Longitud 1
        for i in range(length):
            dp_table[i][i] = True

        # Longitud 2
        for i in range(length - 1):
            if normalized_phrase[i] == normalized_phrase[i + 1]:
                dp_table[i][i + 1] = True
                start_index, max_length = i, 2

        # Longitud ≥ 3
        for sub_length in range(3, length + 1):
            for i in range(0, length - sub_length + 1):
                j = i + sub_length - 1
                if normalized_phrase[i] == normalized_phrase[j] and dp_table[i + 1][j - 1]:
                    dp_table[i][j] = True
                    if sub_length > max_length:
                        start_index, max_length = i, sub_length

        # Extraer la subcadena óptima
        result.append(normalized_phrase[start_index : start_index + max_length])

    return result

# Función fuerza bruta para encontrar la subsecuencia palíndroma más larga
def find_longest_palindromic_subsequence_brute(input_lines: list[str]) -> list[str]:
    def is_palindrome(substring: str) -> bool:
        return substring == substring[::-1]

    try:
        num_lines = int(input_lines[0])
        phrases = input_lines[1 : 1 + num_lines]
    except ValueError:
        phrases = input_lines

    result = []
    for phrase in phrases:
        normalized_phrase = normalize_text(phrase)
        best_palindrome = ""
        length = len(normalized_phrase)
        # Genera todos los pares (i,j)
        for i in range(length):
            for j in range(i, length):
                substring = normalized_phrase[i : j + 1]
                if is_palindrome(substring) and len(substring) > len(best_palindrome):
                    best_palindrome = substring
        result.append(best_palindrome)
    return result

# Función voraz para encontrar la subsecuencia palíndroma más larga
def find_longest_palindromic_subsequence_greedy(input_lines: list[str]) -> list[str]:
    try:
        num_lines = int(input_lines[0])
        phrases = input_lines[1 : 1 + num_lines]
    except ValueError:
        phrases = input_lines

    def expand_palindrome(text, left, right):
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        # al salir, [left+1:right] es palíndromo
        return text[left + 1 : right]

    result = []
    for phrase in phrases:
        normalized_phrase = normalize_text(phrase)
        best_palindrome = ""
        for i in range(len(normalized_phrase)):
            # impar
            p1 = expand_palindrome(normalized_phrase, i, i)
            if len(p1) > len(best_palindrome):
                best_palindrome = p1
            # par
            p2 = expand_palindrome(normalized_phrase, i, i + 1)
            if len(p2) > len(best_palindrome):
                best_palindrome = p2
        result.append(best_palindrome)
    return result

# Función para seleccionar un archivo
def choose_file():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(title="Selecciona un archivo .txt", filetypes=[("Text files", "*.txt")])
    return file_path

# Función principal para leer la entrada desde un archivo y ejecutar las técnicas
def main():
    # Selección del archivo
    file_path = choose_file()
    if not file_path:
        print("No se seleccionó ningún archivo.")
        return
    
    # Lectura del archivo
    with open(file_path, 'r', encoding='utf-8') as file:
        input_lines = file.readlines()

    # Asegurarse de que la primera línea contenga un número válido
    try:
        num_lines = int(input_lines[0].strip())  # Número de cadenas a procesar
    except ValueError:
        print("El archivo no tiene el formato correcto.")
        return

    # Llamar a las funciones para cada técnica
    result_dp = find_longest_palindromic_subsequence_dp([str(num_lines)] + input_lines[1:])
    result_brute = find_longest_palindromic_subsequence_brute([str(num_lines)] + input_lines[1:])
    result_greedy = find_longest_palindromic_subsequence_greedy([str(num_lines)] + input_lines[1:])

    # Imprimir los resultados
    print("Resultados con programación dinámica:")
    for res in result_dp:
        print(res)

    print("\nResultados con fuerza bruta:")
    for res in result_brute:
        print(res)

    print("\nResultados con enfoque voraz:")
    for res in result_greedy:
        print(res)

# Ejecutar el programa
if __name__ == "__main__":
    main()

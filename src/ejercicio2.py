
def fiesta_compania():

    n = 0                           # Numero de problemas
    m = 0                           # Numero de empleados
    matriz = []                     # Grafo (reglas de supervición)
    calificacion_empleados = []     # Lista de la calififacion de convivencia de cada empleado

    archivo = "../entradas/file2.txt"
    with open(archivo, 'r') as f:
        for index, line in enumerate(f):
            line = line.strip()
            if line:
                print(f"Línea {index}: {line}")



if __name__ == "__main__":
    fiesta_compania()
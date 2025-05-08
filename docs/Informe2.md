# Problema 2: Planeando una fiesta de la companía
Dada una estructura jerárquica empresarial representada comó arbol, maximizar la suma de calificaciones de convivencia 
de los empleados invitados a una fiesta, con la restricción de que ningún invitado puede ser supervisor directo de otro.

## Funciones Generales

**1. Función read_file():**

Función que leera el `archivo de texto` desde le file chooser con el proposito de recopilar los datos necesarios para 
generar la solución optima en cada algoritmo utilizado.

datos recopilados:

        n -> numero de problemas a resolver
        m -> tamaño de la entrada (tamaño de la matriz)
        grafo -> matriz de adyacencia m*m
        calificaciones -> lista de las calificaicones de cada empleado

**2. Función arbol_reglasSupervision()**
    
Función que genera un diccionario que contendra las reglas de supervisión.

con el formato:
        
    reglas = { 0: [1], 1:[2] } 
    
Donde las **`keys`** representan los supervisores y los **`values`** una lista de subordinados
    
    
## Algoritmo Fuerza Bruta 
    
### Complejidad Teorica (computacional)


## Algoritmo Dinamico
## Algoritmo Voraz
###

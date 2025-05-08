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

**2. Función arbol_reglasSupervision():**
    
Función que genera un diccionario que contendra las reglas de supervisión.
con el formato: donde las **`keys`** representan los supervisores y los **`values`** una lista de subordinados.
        
    reglas = { 0:[1], 1:[2], ... n:[n] }
    
## Algoritmo Fuerza Bruta 

En este algoritmo se implementó teniendo la idea de generar el mayor numero posible de combinaciones de empleados
validando si cumplen con las restricciones descritas en el problema y asi generar la solución optima invitando a 
la combinacion que tenga la maxima suma de califiaciones de convivencia.

### Complejidad Teorica (computacional)
    
Este algoritmo cuenta con una complejidad computacional de O(2<sup>m</sup> * m <sup>2</sup>)
    
    - Numero de combinaciones: O(2<sup>m</sup>)
    - Suma y validación de cada combinacion: O(m<sup>2</sup>)

### Complejidad Experimental 
    
Aunque no es un algoritmo muy eficiente con tamaños de entradas muy grandes, al hacer todas las combinaciones entre 
empleados garantiza tarde o temprano llegar a una solución optima a diferencia del algoritmo voraz que tiene un tiempo 
de ejecucion menor. En este caso en concreto, al tener una una entrada **`m > 20`** es inviable calcular una complejidad 
experimental o sus tiempos de ejecucion puesto que el algoritmo tarda mucho en construirla.

    Caso de Ejemplo: m = 10
    El algoritmo tendria que hacer 2<sup>100</sup> combinaciones,
    en total 1,267,650,600,228,229,401,496,703,205,376

## Algoritmo Dinamico
## Algoritmo Voraz
###

# Problema 2: Planeando una fiesta de la companía

Dada una estructura jerárquica empresarial representada como árbol, maximizar la suma de calificaciones de convivencia
de los empleados invitados a una fiesta, con la restricción de que ningún invitado puede ser supervisor directo de otro.
    
    Entrada:

         1               -> n: numero de problemas
         5               -> m: numero de empleado
         0 1 0 0 0
         0 0 1 0 0       -> matriz reglas de supervisión 
         0 0 0 1 0           1 = supervisor directo del empleado
         0 0 0 0 1           0 = no es supervisor del empleado
         1 0 0 0 0       
         10 30 15 5 8    -> calificaciones de cada empleado
    
    salida:
         
        0 1 0 0 1 38        -> 1 = invitado, 0 = no invitado  y al final suma de los empleados invitados

## 1. Funciones Generales

**a. Función read_file():**

FFunción que leerá el `archivo de texto` desde el file chooser con el propósito de recopilar los datos necesarios para
generar la solución óptima en cada algoritmo utilizado.

Datos recopilados:

        n -> Número de problemas a resolver
        m -> Tamaño de la entrada (tamaño de la matriz)
        grafo -> Matriz de adyacencia m*m
        calificaciones -> Lista de las calificaciones de cada empleado

**b. Función arbol_reglasSupervision():**

Función que genera un diccionario que contendrá las reglas de supervisión
con el formato: las **`keys`** representan los supervisores y los **`values`** una lista de subordinados.

    reglas = { 0:[1], 1:[2], ... n:[n] }

## 2. Algoritmo Fuerza Bruta

Este algoritmo se implementó teniendo la idea de generar el mayor número posible de combinaciones de empleados
validando si cumplen con las restricciones descritas en el problema y así generar la solución óptima invitando a.
la combinación que tenga la máxima suma de calificaciones de convivencia.

### a. Complejidad Teórica (computacional)

Este algoritmo cuenta con una complejidad computacional de O(2<sup>m</sup> * m <sup>2</sup>)

    - Número de combinaciones: O(2<sup>m</sup>)
    - Suma y validación de cada combinación: O(m<sup>2</sup>)

### b. Complejidad Experimental

Aunque no es un algoritmo muy eficiente, con tamaños de entradas muy grandes, al hacer todas las combinaciones entre
Los empleados garantizan tarde o temprano llegar a una solución óptima a diferencia del algoritmo voraz que tiene un tiempo
de ejecución menor. En este caso en concreto, al tener una entrada **`m > 20`** es inviable calcular una complejidad
experimental o sus tiempos de ejecución, puesto que el algoritmo tarda mucho en construirla.

    Ejemplo: m = 10
    El algoritmo tendría que hacer 2<sup>100</sup> combinaciones.
    En total  1,267,650,600,228,229,401,496, 703,205,376

## 3. Algoritmo dinámico

El algoritmo dinámico utiliza un enfoque Button-up (iterativo), mediante un recorrido postorden, va resolviendo los
subproblemas de forma ascendente, lo que asegura que este algoritmo sea el mejor en cuanto a encontrar una
La solución óptima y al mismo tiempo tener el mejor tiempo de ejecución es que guarda los resultados para no volverlos a calcular, actúa como una especie de memoria.

Para garantizar un recorrido postorden hacemos uso de `stack` pila que se le pasa a los empleados que ya fueron
calculados. Los resultados óptimos de los subproblemas se guardan en `dp` para construir la solución óptima.

    ¿Por qué no se usa recursividad?
    Como primera implementación, se tenía un algoritmo dinámico recursivo, pero dado que puede recibir tamaños de 
    entradas muy grandes generan un árbol muy grande y Python al tener una recursión limitada, no 
    generaba una solución óptima. Por ende, se optó por un enfoque iterativo.  

### a. Complejidad Teórica (computacional)

Tiene una complejidad computacional lineal **`O(m)`** dado que el tamaño de la entrada es proporcional
al tiempo de ejecución. Como se menciona anteriormente, al ser una complejidad lineal en el peor de los casos
lo convierte en el mejor algoritmo para buscar una solución óptima al problema de la fiesta de compañía.

### b. Complejidad Experimental

Siempre garantizará llegar a la solución, el guardar los resultados  lo convierte en un algoritmo eficiente con
Grandes tamaños de **`m`**. Se puede calcular con valores **`m < 50000`**.

## Algoritmo Voraz

En el algoritmo Voraz se utilizó una estrategia que, aunque no es inteligente y no considera todas las opciones
como otros algoritmos, puede llegar a una solución óptima en un mejor tiempo que el de fuerza bruta. En este caso,
la estrategia que se utiliza es encontrar el máximo valor de calificación de un empleado en cada iteración,
eliminando a su supervisor y subordinado de la lista de invitados, también se elimina el empleado que ya fue calculado
para garantizar que tome otro valor máximo.

### a. Complejidad Teórica (computacional)

Cuenta con una complejidad computacional de O(m<sup>2</sup>).

    Donde:
    m: recorre cada empleado
    m: busca a su supervisor y subordinado para eliminar

### b. Complejidad Experimental

Aunque es un algoritmo que no siempre garantiza una solución óptima, puede recibir tamaños de entrada más grandes
que el de fuerza bruta, por ende se pueden calcular sus tiempos de ejecución efectivamente.

## 4. Tiempos de Ejecución (vs.)

Se graficaron los tiempos de ejecución de los algoritmos Voraz y dinámico, donde cada barra representa un promedio
de la suma de tiempos que le tomó al algoritmo calcular cada tamaño 5 veces.


![grafica tiempos de ejecución](/docs/images/Figure_1.png)

    numero de repiticiones : 5
    tamaños de entrada : 100, 200, 300, 400, 500

### ¿Por qué no se muestran los tiempos de ejecución del algoritmo de fuerza bruta?

No se grafica este algoritmo porque, al ser unos tamaños de entrada muy grandes, le es imposible o
tarda mucho en construir la solución.

## 5. Tamaños de Entrada

### a. Prueba de Juguete ( m = 10)}

| Algoritmo    | Tiempo ejecución Test |
|--------------|-----------------------|
| Fuerza Bruta | 0.06 s                |
| Dinámico     | 0.05 s                |
| Voraz        | 0.07 s                |

### b. Prueba de Pequeño ( m = 100)

| Algoritmo    | Tiempo ejecución Test |
|--------------|-----------------------|
| Fuerza Bruta | inviable              |
| Dinámico     | 0.16 s                |
| Voraz        | 0.18 s                |

### c. Prueba de Mediano ( m = 1000)

| Algoritmo    | Tiempo ejecución Test |
|--------------|-----------------------|
| Fuerza Bruta | inviable              |
| Dinámico     | 0.23 s                |
| Voraz        | 0.22 s                |

### d. Prueba de Grande ( m = 10000)

| Algoritmo    | Tiempo ejecución Test |
|--------------|-----------------------|
| Fuerza Bruta | inviable              |
| Dinámico     | 12.68 s               |
| Voraz        | 19.96 s               |

### E. Prueba de ExtraGrande ( m = 50000)

| Algoritmo    | Tiempo ejecución Test  |
|--------------|------------------------|
| Fuerza Bruta | inviable               |
| Dinámico     | memoryError / inviable |
| Voraz        | memoryError / inviable |

# 6. Tabla de Comparación complejidad temporal

| Algoritmo    | O( )                              | observaciones                                                   |
|--------------|-----------------------------------|-----------------------------------------------------------------|
| Fuerza Bruta | O(m)                              | ineficiente con m < 20, pero garantiza solución optima          |
| Dinámico     | O(2<sup>m</sup> * m <sup>2</sup>) | eficiente con m > 20, pero no siempre garantiza solucion optima |
| Voraz        | O(m <sup>2</sup>)                 | eficiente con m > 20, siempre garantiza solución optima         |

# 7. Conclusionesq  1A  




# Problema 2: Planeando una fiesta de la companía
Dada una estructura jerárquica empresarial representada comó arbol, maximizar la suma de calificaciones de convivencia 
de los empleados invitados a una fiesta, con la restricción de que ningún invitado puede ser supervisor directo de otro.

## 1. Funciones Generales

**a. Función read_file():**

Función que leera el `archivo de texto` desde le file chooser con el proposito de recopilar los datos necesarios para 
generar la solución optima en cada algoritmo utilizado.

datos recopilados:

        n -> numero de problemas a resolver
        m -> tamaño de la entrada (tamaño de la matriz)
        grafo -> matriz de adyacencia m*m
        calificaciones -> lista de las calificaicones de cada empleado

**b. Función arbol_reglasSupervision():**
    
Función que genera un diccionario que contendra las reglas de supervisión
con el formato: las **`keys`** representan los supervisores y los **`values`** una lista de subordinados.
        
    reglas = { 0:[1], 1:[2], ... n:[n] }
    
## 2. Algoritmo Fuerza Bruta 

Este algoritmo se implementó teniendo la idea de generar el mayor numero posible de combinaciones de empleados
validando si cumplen con las restricciones descritas en el problema y asi generar la solución optima invitando a 
la combinacion que tenga la maxima suma de califiaciones de convivencia.

### a.Complejidad Teorica (computacional)
    
Este algoritmo cuenta con una complejidad computacional de O(2<sup>m</sup> * m <sup>2</sup>)
    
    - Numero de combinaciones: O(2<sup>m</sup>)
    - Suma y validación de cada combinacion: O(m<sup>2</sup>)

### b.Complejidad Experimental 
    
Aunque no es un algoritmo muy eficiente con tamaños de entradas muy grandes, al hacer todas las combinaciones entre 
empleados garantiza tarde o temprano llegar a una solución optima a diferencia del algoritmo voraz que tiene un tiempo 
de ejecucion menor. En este caso en concreto, al tener una una entrada **`m > 20`** es inviable calcular una complejidad 
experimental o sus tiempos de ejecucion puesto que el algoritmo tarda mucho en construirla.

    Ejemplo: m = 10
    El algoritmo tendria que hacer 2<sup>100</sup> combinaciones,
    en total 1,267,650,600,228,229,401,496,703,205,376

## 3. Algoritmo Dinamico

El algoritmo dinamico utiliza un enfoque buttom-up (iterativo), mediante un recorrido post-orden, va resolviendo los 
subproblemas de forma ascendente, lo que asegura que este algoritmo sea el mejor en cuanto a encontrar una
solucion optima y al mismo tiempo tener el mejor tiempo de ejecucion es que guarda los resultados para no volverlos a 
calcular, actua como una especie de memoria.

Para garantizar un recorrido post-orden hacemos uso de `stack` pila que se le pasa los empleados que ya fueron 
calculados. Los resultados optimos de los subproblemas se guardan en `dp` para construir la solucion optima.

    ¿ Porque no se usa recursividad ?
    Como primera implementación, se tenia un algoritmo dinamico recursivo pero dado que puede recibir tamaños de 
    entradas muy grandes, genera un arbol muy grande y python al tener una recursion es limitada, no 
    generaba una solucion optima. Por ende, se opto por un enfoque iterativo. 

### a. Complejidad Teorica (computacional)

Tiene una complejidad computacional lineal **`O(m)`** dado que el tamaño de la entrada es proporcional 
al tiempo de ejeución. Como se menciona anteriormente, al ser una complejidad lineal en el peor de los casos 
lo convierte en el mejor algoritmo para buscar una solucion optima a el problema de la fiesta de compañia.
    
### b. Complejidad Experimental

Siempre garantizará llegar a la solución, el guardar los resultados  lo convierte en un algoritmo eficiente con 
grandes tamaños de **`m`**. Se puede calcular con valores **`m < 50000`**. 

## Algoritmo Voraz

En el algoritmo voraz se utilizo una estrategia que aunque no es inteligente y no considera todas las opciones 
como otros algoritmos, puede llegar a una solucion optima en un mejor tiempo que el de fuerza bruta. En este caso, 
la estrategia que se utiliza es encontrar el maximo valor de calificación de un empleado en cada iteracion, 
eliminando a su supervisor y subordinado de la lista de invitados, tambien se elimina el empleado que ya fue calculado 
para garantizar que tome otro valor maximo.  

### a. Complejidad Teorica (computacional)

Cuenta con una complejidad computacional de O(m<sup>2</sup>).
    
    donde:
    m: recorre cada empleado
    m: busca su supervisor y subordinado para eliminar


### b. Complejidad Experimental

Aunque es un algoritmo que no siempre garantiza una solución optima, puede recibir tamaños de entrada mas grandes 
que el de fuerza bruta, por ende se puede calcular sus tiempos de ejecución efectivamente.

## 4. Tiempos de Ejecución (vs)

Se graficarón los tiempos de ejecucion de los algoritmos Voraz y Dinamico, donde cada barra representa un promedio 
de la suma de tiempos que le tomo al algoritmo calcular cada tamaño 5 veces. 


![grafica tiempos de ejecución](/docs/images/Figure_1.png)

    numero de repiticiones : 5
    tamaños de entrada : 100, 200, 300, 400, 500

### ¿Por que no se muestran los tiempos de ejecución del algirmto de fuerza bruta?

No se grafica este algortimo porque al ser unos tamaño de entrada muy grandes, a el algoritmo le es imposible o 
tarda mucho en construir la solucion.

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

# 7. Conclusiones




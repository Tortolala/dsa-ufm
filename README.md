### Estructuras de Datos y Algoritmos (2026)
Código base para el curso Estructuras de Datos y Algoritmos en Universidad Francisco Marroquín.

## Index

* [Arrays](https://github.com/Tortolala/dsa-ufm/tree/master/01_arrays)
* [Stacks](https://github.com/Tortolala/dsa-ufm/tree/master/02_stacks)
* [Queues](https://github.com/Tortolala/dsa-ufm/tree/master/03_queues)
* [Profiling](https://github.com/Tortolala/dsa-ufm/tree/master/04_profiling)
* [Linked Lists](https://github.com/Tortolala/dsa-ufm/tree/master/05_linked_list)

## Actividad no. 10: Algoritmos de Búsqueda

**Entrega:** 29 de abril, 11:30am.

**Instrucciones:** 

1. En parejas (asignadas), trabajar un repositorio colaborativamente. Se les será asignado un rol de `dev_1` y `dev_2` a considerar en las instrucciones. Deberán trabajar utilizando branches de forma ordenada.

2. **Repositorio [`dev_1`]:** crear un repositorio público con el nombre `search_algorithms`, agregar a `dev_2` al proyecto. Este repositorio y los commits realizados entre 10 y 11:20am serán su entregable final. 

3. **Unit testing [`dev_1`]:** realizar por separado un unit test para los algoritmos:
    - Búsqueda lineal
    - Búsqueda binaria

    Cada test unitario debe considerar como mínimo 5 escenarios. Committear, en este commit solo deben existir los unit tests, no los algoritmos implementados.

4. **Unit testing [`dev_2`]:** implementar los algoritmos:
    - Búsqueda lineal
    - Búsqueda binaria

    Ambas implementaciones deben encontrarse en un módulo llamado `searching.py`. Committear.

5. **Unit testing [`dev_1` y `dev_2`]:** en modalidad *pair programming*, realizar benchmarking de ambos algoritmos utilizando pytest. Deberán evaluar un escenario en el cual recorren una lista de 100K elementos y el target no es encontrado. Utilizar el modo `pedantic` configurando por lo menos 5 rounds de 5 iteraciones cada uno.


6. **Documentación [`dev_1` y `dev_2`]:** en modalidad *pair programming*, documentar en el README del repositorio los necesario para:
    - Clonar el repositorio
    - Ejecutar el unit testing de cada algoritmo
    - Ejecutar el benchmarking

   Adjuntar al final una sección de *Anexos* que muestre capturas de pantalla del resultado de ambos unit tests y el benchmark. 

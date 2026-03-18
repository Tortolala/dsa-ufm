### Estructuras de Datos y Algoritmos (2026)
Código base para el curso Estructuras de Datos y Algoritmos en Universidad Francisco Marroquín.

## Index

* [Arrays](https://github.com/Tortolala/dsa-ufm/tree/master/01_arrays)
* [Stacks](https://github.com/Tortolala/dsa-ufm/tree/master/02_stacks)
* [Queues](https://github.com/Tortolala/dsa-ufm/tree/master/03_queues)
* [Profiling](https://github.com/Tortolala/dsa-ufm/tree/master/04_profiling)
* [Linked Lists](https://github.com/Tortolala/dsa-ufm/tree/master/05_linked_list)

## Actividad - Simulacro de Parcial

**Entrega:** 18 de marzo, 11:30am.

**Instrucciones:** 

1. **Entregable:** crear un repositorio nuevo con el nombre `dsa_pre_midterm`. Este repositorio y los commits realizados entre 10 y 11:20am serán su entregable final. 

2. **Clases base:** utilizando este repositorio como base, crear una nueva versión de la clase *LinkedList* que cumpla con lo siguiente:
    - Estar en un archivo únicamente de definición (clase *Node* y *LinkedList*)
    - Estilo consistente con la base de código del curso
    - Cumplimiento de formato con PEP8
    - No deben existir docstrings en esta clase (por el momento)
    - Utilizar type hinting
    - El código debe verse depurado, no como *AI slop*.
    - No deben manejar aún excepciones

    Al finalizar estos cambios y tener una clase *LinkedList* acorde a lo específicado, committear.

3. **Mejoras a clases:** agregar las siguientes mejoras a las clases *LinkedList* y *Node*:
    - Convertir la LL en una lista doblemente encadenada.
    - Agregar a la clase *Node* un diccionario que contenga los siguientes atributos:
        - Nombre de canción
        - Artista
        - Álbum
    
    Committear sus cambios.

4. **Data:** las clases trabajadas hasta el momento, se utilizarán para implementar una playlist de música. Para esto, crear un archivo exclusivamente para el demo de la playlist. 

    Llenar de datos dicha playlist, por lo cual implica diseñar un mecanismo que permita obtener la información de 50 canciones de su elección y agregarlas a la lista linkeada.

    Committear progreso.

5. **Interfaz:** implementar una interfaz en consola, la cual debe permitir iniciar la playlist de 50 canciones, cumpliendo con lo siguiente:
    - Iniciar con la primera canción y "reproducirla"
    - Avanzar a la siguiente canción
    - Regresar a la canción anterior
    - El inicio y el final de la playlist deben ser límites, la lista linkeada no debe ser circular
    
    El diseño de la interfaz y sus controles queda a su criterio. Debe ser una interfaz en consola, no con un motor gráfico. 

    Committear la implementación de la playlist. 

6. **Documentación:** documentar en el README del repositorio los necesario para:
    - Clonar y correr existosamente su programa
    - Navegar la playlist según los controles definidos

    Committear update del README.

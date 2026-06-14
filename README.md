# Trabajo Práctico Integrador - Gestión de Datos de Países

## ¿De qué trata el programa?
Es una aplicación de consola hecha en **Python 3.x** que sirve para leer, ordenar, filtrar y sacar estadísticas de un conjunto de datos de países. Toda la información inicial la toma directamente de un archivo CSV (`paises.csv`), cargando en memoria el nombre de cada país, su población, los km2 de superficie y el continente.

Para armar el código nos enfocamos en la **modularización**. Esto significa que el programa está dividido en funciones específicas donde cada una se encarga de una sola tarea (cargar el archivo, filtrar, ordenar, etc.). Además, le sumamos validaciones a cada ingreso de datos por consola para que el programa no se rompa si ponés una opción inválida, una letra en vez de un número, o si dejás campos vacíos.
---
## Estructura de archivos
├── tp_INT.py              # El código fuente principal de la aplicación
├── paises.csv           # El archivo con los datos base de los países
└── README.md            # Estas instrucciones de uso

#¿Como usar el programa?
Requisitos:
•	Tener instalado Python 3.x
•	Dejar el archivo países.csv en la misma carpeta que TP_int.py

Como manejarse en el menú:
Cuando el programa arranca te muestra un menú interactivo en la consola, Solo hay que escribir el numero de la opción que queremos usar y a apretar ENTER:
1.	Carga inicial de países: Lee el archivo CSV y pasa todos los datos a listas y diccionarios dentro del programa
2.	Agregar nuevo país: Pide los datos para sumar un país a la lista. Controla que el país no se repita.
3.	Actualizar datos de un país: Busca un país por nombre y te permite cambiar los datos de forma selectiva
4.	Buscar un país: Escribis el nombre del país, o partes de el, y los busca sin importar mayúsculas, minúsculas o tildes-
5.	Filtrar países: Permite achicar la lista para ver solo los países de un continente especifico, o los que están dentro de un rango de población o superficie 
6.	Ordenar países: Podes reordenar la lista de forma ascendente o descendente gracias al algoritmo de reordenamiento Bubble Sort.
7.	Estadisticas y salir: Muestra en pantalla el resumen  de los datos y cierra el programa de forma segura

Ejemplo de entradas y salidas 

Opcion 2.
 
Entradas:
•	Nombre del país: Corea Del Norte
•	Continente de Corea Del Norte: Asia
•	Población de Corea Del Norte: 26633691
•	Superficie en km² de Corea Del Norte: 120540
             Salidas: 
•	'Corea Del Norte' fue agregado correctamente.
            
Opcion 4:
Entrada:
•	Ingrese texto a buscar: arg
               Salida:
•	Resultados para 'arg':

___________________________________________________________________________
NOMBRE DEL PAÍS        | POBLACIÓN      | SUPERFICIE KM²   | CONTINENTE  
___________________________________________________________________________
Argentina              | 46,000,000     | 2,780,400        | America Del sur


Participantes;
Valdez Luciana
Etura sofia

Link al video: 

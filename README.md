# Trabajo Práctico Integrador - Sistema de Gestión de Datos de Países

1) Descripción del programa:

Este programa es una aplicación de consola diseñada para la administración, análisis y persistencia de 
datos geográficos y demográficosde países. 
La aplicación permite gestionar un dataset que incluye el nombre del país, su volumen de población, 
su superficie en km2 y el continente al que pertenece.
El software se destaca por dos pilares técnicos:
- Diseño Modular: El código fuente está estructurado de manera limpia mediante funciones independientes y especializadas,
  lo que facilita el mantenimiento, la escalabilidad y la legibilidad del sistema.
- Robustez y Validación:** Cuenta con un estricto control de flujos apoyado en bloques 'try-except'
- para capturar excepciones de tipo numérico ('ValueError') y de claves ('KeyError').
- El sistema valida activamente que no se ingresen campos vacíos, datos con formatos inválidos o registros de países ya existentes
- (duplicados), impidiendo que la aplicación colapse ante errores del operador.


2) Instrucciones de uso:

Requisitos del sistema:
* Tener instalado Python
* El archivo de datos origen 'paises.cs' debe estar guardado en la misma que el script principal 'tp_INT.py'.
Operación del menú interactivo:
Al ejecutar el script ('python tp_INT.py'), se desplegará una interfaz de consola con 7 opciones.
Para interactuar, el usuario debe ingresar el número correspondiente a la acción y presionar enter:
1. Carga inicial de países:   
   Abre de manera segura el archivo plano '"paises.csv"' usando codificación UTF-8 y mapea las columnas mediante la librería nativa
   'csv.DictReader' para cargarlas en la memoria activa del programa.
2. Agregar nuevo país: Permite dar de alta un país en la lista. Valida que el nombre no esté repetido, que los campos de texto
   contengan caracteres alfabéticos y que los datos numéricos (población y superficie) sean enteros mayores a cero.
3. Actualizar datos de un país: Permite la modificación selectiva de un país existente. Cuenta con una función de búsqueda
   insensible a mayúsculas/minúsculas y tildes, y permite presionar ENTER para conservar los valores anteriores sin alterarlos.
4. Buscar país: Realiza una búsqueda flexible por coincidencias parciales de caracteres. Utiliza técnicas de normalización para
   limpiar cadenas de texto eliminando tildes y forzando minúsculas.
5. Filtrar países: Divide el dataset en subtablas según tres criterios: por coincidencia exacta de continente, o por rangos
   numéricos configurables mediante límites mínimos y máximos de población o superficie.
6. Ordenar países: Reordena los datos de forma ascendente o descendente según el criterio elegido (nombre, población o superficie).
   Para cumplir con los requerimientos de la cátedra, **no utiliza funciones automáticas de Python**; implementa de forma manual
   el algoritmo clásico de ordenamiento **Bubble Sort** (ordenamiento por burbuja).
7. Estadísticas avanzadas y Salir: Realiza cálculos analíticos sobre los datos en memoria antes de finalizar.
   Muestra totales acumulados, promedios demográficos y de superficie, identifica los países en los extremos máximos y mínimos
   de población, y genera un conteo dinámico de países por continente antes de cerrar el bucle principal.

3) Ejemplos de Entradas y Salidas:


- EJEMPLO A: Control de Errores en Alta de País (Opción 2)
Si el usuario intenta ingresar un tipo de dato incorrecto (letras en campos numéricos) o dejar vacíos los campos, 
el programa responde de forma controlada:

AGREGAR NUEVO PAÍS
Ingrese 'x' para cancelar.

Nombre del país: 
El nombre no puede estar vacío. Intente nuevamente.
Nombre del país: Italia
Continente de Italia: Europa
Población de Italia: cincuenta millones
Dato inválido. Intente nuevamente.
Población de Italia: 58800000
Superficie en km² de Italia: 301340

- EJEMPLO B: Actualización Comparativa de Datos (Opción 3)
Al modificar un registro, el sistema normaliza la búsqueda del nombre e imprime un cuadro comparativo con el estado
de los datos (antes y después):

ACTUALIZAR DATOS DE UN PAÍS
Ingrese 'x' para cancelar y volver al menú principal

Ingrese el nombre del país a modificar: ÍTALIA

País seleccionado: Italia
(Presione ENTER para conservar el valor actual sin cambios)

Nuevo continente: Europa del Sur
Nueva población: [ENTER]
Nueva superficie en km²: [ENTER]

Los datos de 'Italia' fueron actualizados.
———————————————————————————————————————————————————————————————————————————
DATOS ANTERIORES || Continente: Europa | Población: 58,800,000 | Superficie: 301,340 km²
DATOS NUEVOS     || Continente: Europa del Sur | Población: 58,800,000 | Superficie: 301,340 km²
———————————————————————————————————————————————————————————————————————————



- EJEMPLO C: Ordenamiento Algorítmico Bubble Sort (Opción 6)
Al solicitar el ordenamiento por población de manera descendente (mayor a menor):

Lista ordenada por POBLACION:
___________________________________________________________________________
NOMBRE DEL PAÍS        | POBLACIÓN      | SUPERFICIE KM²   | CONTINENTE  
___________________________________________________________________________
Italia                 | 58,800,000     | 301,340          | Europa del Sur
Argentina              | 46,044,701     | 2,780,400        | America     
Armenia                | 2,777,970      | 29,743           | Asia        
___________________________________________________________________________

4. Participación de los Integrantes
El desarrollo de este proyecto integrador se distribuyó equitativamente entre las dos integrantes del equipo,
asumiendo las siguientes responsabilidades de programación y diseño técnico.






'Italia' fue agregado correctamente.


# Tarea_1_Taller_Software_DS
Contexto:
Se realizó una encuesta a un grupo de estudiantes universitarios para conocer sus hábitos alimenticios y de actividad física. La encuesta consistió en varias preguntas, incluyendo información demográfica, frecuencia de consumo de diferentes grupos de alimentos, frecuencia y duración de actividad física, y opiniones sobre la disponibilidad de opciones saludables en el campus.
Objetivo:
Aplicar los conceptos de programación en Python aprendidos en la unidad 1, como la declaración de variables, importación de módulos, sentencias condicionales (if), ciclos (for, while) y manejo de estructuras de datos (diccionarios, listas, strings), para analizar los datos de la encuesta y generar informes sobre los hábitos alimenticios y de actividad física de los estudiantes universitarios.
Para simular la toma de la encuesta debe crear un programa generador_encuesta.py el cual generara un archivo CSV con los resultados de la encuesta. El segundo programa que debe crear llamado procesador_encuesta.py es quien se encarga de leer el archivo CSV para luego calcular y mostrar las estadísticas de la encuesta. A continuación, se explican los requerimientos para cada uno de los programas solicitados.

Requerimientos Programa 1 ("generador_encuesta.py"):
1. Debe generar un archivo CSV llamado "encuesta_habitos.csv" con al menos 50 (el valor debe ser leído desde teclado) filas de datos.
2. La primera fila del archivo contiene las etiquetas: Sexo, Edad y Respuesta. Estas etiquetas deben estar separadas por un espacio en blanco.
3. Las siguientes filas del archivo (las al menos 50 filas) deben tener tres valores ordenados de acuerdo al orden establecido por las etiquetas de la primera fila. Primero, Sexo, el cual puede tomar solo los strings “Femenino” o “Masculino”, luego Edad, que puede ser un valor entero entre 18 y 45 y Respuesta, que puede tomar solo los strings “Sí”, “No” o “Tal vez”. Los valores están separados por un espacio en blanco.
4. Utilice el módulo 'random' para generar los datos aleatorios para las tres categorías estudiadas en la encuesta. Por tanto, el archivo de salida debería lucir como:
   
    Sexo Edad Respuesta
    Femenino 20 Tal vez
    Femenino 22 Si
    Masculino 27 No
    Femenino 24 Tal vez
    Masculino 32 Si

Requerimientos Programa 2 ("procesador_encuesta.py")
1. Debe solicitar al usuario el nombre del archivo de datos CSV al inicio.
2. Importar los módulos necesarios para leer el archivo CSV y realizar análisis de datos
básicos.
3. Almacenar los datos en un diccionario de listas, donde cada clave representa una
columna del archivo CSV (Sexo, Edad, Respuesta) y cada lista contiene los valores
correspondientes.
4. Realiza un preprocesamiento de datos para transformar las respuestas (e.g., convertir
respuestas de texto a números).
5. Utilice ciclos y sentencias condicionales para calcular estadísticas descriptivas (e.g.,
promedio, mediana, moda) para la columna Edad.
6. Utilice ciclos y sentencias condicionales para contar la frecuencia de cada tipo de
respuesta (Sí/No/Tal vez).
7. Implemente un menú interactivo usando ciclos while con las siguientes opciones:
  a. Leer archivo de datos
  b. Mostrar estadísticas generales (media, mediana, conteo de respuestas por tipo)
  c. Filtrar datos por sexo y mostrar estadísticas
  d. Filtrar datos por rango de edad y mostrar estadísticas
  e. Guardar resultados en un archivo (todos aquellos generados)
  f. Salir
Para las opciones de filtrado (7.c y 7.d), permita al usuario especificar el sexo o el rango de edad y muestre las estadísticas. Si es sexo, conteo de respuestas por sexo, conteo de respuestas por tipo y por sexo. De manera equivalente al aplicar rango de edad.
Para la opción de guardado (7.e), genere un archivo de texto que contenga las estadísticas generales y los resultados de los filtros aplicados.

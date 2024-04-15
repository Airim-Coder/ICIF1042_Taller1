#Autor: Maria Paz Cisternas Pardo
#Version: 23.04.14
#Contenido:
# 1- Debe generar un archivo CSV llamado "encuesta_habitos.csv" con al menos 50 (el valor debe ser leído desde teclado) filas de datos.
# 2- La primera fila del archivo contiene las etiquetas: Sexo, Edad y Respuesta. Estas etiquetas deben estar separadas por un espacio en blanco.
# 3- Las siguientes filas del archivo (las al menos 50 filas) deben tener tres valores ordenados de acuerdo al orden establecido por las etiquetas
#   de la primera fila. Primero, Sexo, el cual puede tomar solo los strings “Femenino” o “Masculino”, luego Edad, que puede ser un valor entero entre
#   18 y 45 y Respuesta, que puede tomar solo los strings “Sí”, “No” o “Tal vez”. Los valores están separados por un espacio en blanco
# 4- Utilice el módulo 'random' para generar los datos aleatorios para las tres categorías estudiadas en la encuesta.

def Generador_Encuesta():
    import os, random, csv

    # Declaracion de variables
    sexo_list=['Femenino','Masculino']
    edad_list=range(18,46)
    respuesta_list=['Sí','No','Tal vez']    

    # Entrada de usuario
    print("GENERADOR DE ENCUESTAS DE HABITOS\nCuantas filas tendra esta encuesta?")
    filas = int(input("Considere a lo menos 50 filas: "))
    while(True):
        if filas < 50 :
            print("El numero de filas debe ser mayor o igual a 50")
            filas = int(input("Numero de filas de datos (minimo 50):"))
        else:
            
            # Genera Lista de datos aleatorios para la encuesta
            datos = [['Sexo','Edad','Respuesta']]
            for i in range(filas):
                sexo= random.choice(sexo_list)
                edad= random.choice(edad_list)
                respuesta= random.choice(respuesta_list)
                datos.append([sexo,edad,respuesta])

            # Verifica si existe archivo CSV y lo elimina
            if os.path.exists("encuesta_habitos.csv"):
                os.remove("encuesta_habitos.csv")

            # Genera un nuevo archivo CSV con datos
            with open("encuesta_habitos.csv", mode='w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv,delimiter=' ')
                for fila in datos:
                    escritor_csv.writerow(fila)

                print("Archivo CSV generado con exito")
            # Cierra el archivo CSV
            archivo_csv.close()
            break   
            # Cierra el programa

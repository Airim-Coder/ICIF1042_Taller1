'''
#Autor: Maria Paz Cisternas Pardo
#Version: 23.04.19
#Contenido:
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
'''

import csv, os
import pandas as pd
import numpy as np

CACHE=[] #almacenar datos procesados en memoria temporal
def ProcesadorEncuesta(): 
    print("PROCESADOR DE ENCUESTAS\nQue desea hacer?")
    print("a. Leer archivo de datos" 
        + "\nb. Mostrar estadísticas generales (media, mediana, conteo de respuestas por tipo)" 
        + "\nc. Filtrar datos por sexo y mostrar estadísticas" 
        + "\nd. Filtrar datos por rango de edad y mostrar estadísticas" 
        + "\ne. Guardar resultados en un archivo (todos aquellos generados)" 
        + "\nf. Salir")
    opcion = str(input("Ingrese su opcion: "))
    while(True):
        if opcion == "a":
            #archivo = input("Ingrese el nombre del archivo a procesar: ") #pide el nombre del archivo
            archivo = "encuesta_habitos.csv" #Solo para depuracion
            CACHE.append(f"lectura de archivo: {archivo}")
            datos_archivo = LeerEncuesta(archivo)
            print("Archivo importado con exito")
            opcion = str(input("Que desea hacer ahora?\nIngrese su opcion: "))
            
        elif opcion == "b":
            CACHE.append("\nESTADISTICAS GENERALES")
            estadistica = CalculosEstadisticos(datos_archivo)
            PrintDatos(estadistica)
            opcion = str(input("Ingrese su opcion: "))
            
        elif opcion == "c":
            resp = int(input("Por cual valor le gustaria filtrar?"
                             +"\n1. Femenino"
                             +"\n2. Masculino"
                             +"\nIngrese su opcion: "))
            #region validacion
            contador = 0
            while(contador<3):
                if(resp==1):
                    resp = "Femenino"
                    break
                elif(resp==2):
                    resp = "Masculino"
                    break
                else:
                    contador += 1
                    print("El valor indicado no se encuentra entre las opciones")
                    resp = int(input("Ingrese su opcion: "))
            #endregion
            CACHE.append("\nESTADISTICAS GENERALES FILTRADO POR "+ str(resp))
            filtro_sexo=FileFilter(datos_archivo,'Sexo',resp,'')
            estadistica = CalculosEstadisticos(filtro_sexo)
            PrintDatos(estadistica)
            opcion = str(input("Ingrese su opcion: "))
            
        elif opcion == "d":
            resp1 = int(input("Indique desde que edad: "))
            resp2 = int(input("hasta que edad: "))
            #region validacion
            contador = 0
            while(contador<3):
                if resp1>resp2:
                    contador += 1
                    print("El valor minimo no puede ser mayor al maximo")
                elif resp1<18:
                    contador += 1
                    print("El valor minimo no puede ser menor a 18")
                elif resp2<19:
                    contador += 1
                    print("El valor minimo no puede ser menor a 19")
                elif resp1>44:
                    contador += 1
                    print("El valor maximo no puede ser mayor a 45")
                elif resp2>45:
                    contador += 1
                    print("El valor maximo no puede ser mayor a 46")
                else:
                    break
            #endregion
            CACHE.append("ESTADISTICAS GENERALES FILTRADO POR EDADES:"+str(resp1)+"-"+str(resp2))
            filtro_edad=FileFilter(datos_archivo,'Edad',resp1,resp2)
            estadistica = CalculosEstadisticos(filtro_edad)
            PrintDatos(estadistica)
            
            opcion = str(input("Ingrese su opcion: "))
            
        elif opcion == "e":
            GuardarEnArchivo()
            opcion = str(input("Ingrese su opcion: "))
            
        elif opcion == "f":
            print("Gracias por usar el procesador de encuestas")
            break
        else:
            print("Opcion no valida")
            opcion = str(input("Ingrese su opcion: "))
            
#region Funciones Principales
def LeerEncuesta(archivo):  #funcion para leer el archivo csv
    try:
        with open(archivo, 'r') as csv_archivo: #abre el archivo
            csv_reader = csv.reader(csv_archivo, delimiter=" ") #separa las columnas
            datos={} #diccionario para almacenar los datos
            cabeceras = next(csv_reader) #obtiene las cabeceras
            for cabecera in cabeceras: #recorre las cabeceras
                datos[cabecera] = [] #crea una lista por cada cabecera

            for fila in csv_reader: #recorre las columnas
                for i, valor in enumerate(fila): #recorre las columnas
                    datos[cabeceras[i]].append(valor) # almacena cada fila en el diccionario por cabecera
        return datos

    except FileNotFoundError: #control de error si el archivo no existe
        print(f"Error: Archivo '{archivo}' no encontrado.")
def CalculosEstadisticos(archivo): #funcion para calcular los estadisticos con archivo entregado
    try:
        estadistica=[]
    #region validaciones
        for data in archivo.values():
            if isinstance(data, list):
                edades = archivo["Edad"] #obtiene las edades
                sexo = archivo["Sexo"] #obtiene los sexos
                respuesta = archivo["Respuesta"] #obtiene las respuestas
                break
            elif isinstance(data, dict):
                edades = list(archivo["Edad"].values()) #obtiene las edades
                sexo = list(archivo["Sexo"].values()) #obtiene los sexos
                respuesta = list(archivo["Respuesta"].values()) #obtiene las respuestas
                break
        #endregion
        #EDAD
        media_edad = MediaCal(edades)
        moda_edad = ModaCal(edades)
        mediana_edad = MedianaCal(edades)
        #SEXO
        moda_sexo = ModaCal(sexo)
        frecuencia_sexo = FrecuenciaCal(archivo,"Sexo")
        #RESPUESTA
        moda_respuesta = ModaCal(respuesta)
        frecuencia_respuesta = FrecuenciaCal(archivo,"Respuesta")
        
        #region ALMACENAR DATOS
        estadistica.append("EDAD:")
        estadistica.append(f"Media: {media_edad}")  
        estadistica.append(f"Moda: {moda_edad}")  
        estadistica.append(f"Mediana: {mediana_edad}")  
        
        estadistica.append("\nSEXO:")
        estadistica.append(f"Moda: {moda_sexo}")  
        estadistica.append("Frecuencia:")
        for key, value in frecuencia_sexo.items():
            estadistica.append(f"{key}: {value}")

        estadistica.append("\nRESPUESTA:")
        estadistica.append(f"Moda: {moda_respuesta}")  
        estadistica.append("Frecuencia:")
        for key, value in frecuencia_respuesta.items():
            estadistica.append(f"{key}: {value}")
        CACHE.append(estadistica)#Agregar a la cache
        #endregion
        return estadistica
    except:
        print("No se pudo realizar los calculos")
def GuardarEnArchivo(): #funcion para guardar datos procesados y almacenados en CACHE en un txt
    try:
        if os.path.exists("Calculado.txt"):# Elimina archivo CSV si existe en el directorio
                os.remove("Calculado.txt")
        with open("Calculado.txt", "w") as f:
                for fila in CACHE:
                    if isinstance(fila, str):
                        f.write(str(fila) + "\n")
                    elif isinstance(fila, list):
                        for i in fila:
                            f.write(str(i) + "\n")
        print("Archivo generado con exito")
    except:
        print("Ha surgido un error mientras se escribia el archivo")
#endregion
#region Miscelaneos
def ListParseToInt(lista): #convierte una lista de strings a enteros
    try:
        lista_int = []
        for i in lista:
            lista_int.append(int(i))
        return lista_int
    except:
        print("No hay enteros para convertir")
def FileFilter(archivo, columna, filtro1, filtro2): #filtra los datos de un archivo csv por columna segun los valores entregados
    df = pd.DataFrame(archivo)
    try:
        if columna == "Sexo":
            filtro = df[df[columna]==filtro1]
        elif columna == "Edad":
            df['Edad'] = df['Edad'].astype(int)
            filtro = df.query('@filtro1 <= Edad <= @filtro2')
        return filtro.to_dict()
    except Exception as e:
        print("Algo salio mal:"+str(e))
def DictParseToList(archivo,columna): #convierte un diccionario a una lista
    try:
        for data in archivo.values():
            if isinstance(data, list):
                datos = archivo[columna]
                break
            elif isinstance(data, dict):
                datos = list(archivo[columna].values()) #obtiene las edades
                break
        return datos
    except:
        print("No ha sido posible convertir el diccionario entragado a Lista")
def PrintDatos(lista): #imprime los datos de una lista
    try:
        for fila in lista:
                if isinstance(fila, str):
                    print(str(fila))
                elif isinstance(fila, list):
                    for i in fila:
                        print(str(i))
    except:
        print("Ha surgido un error")
#endregion
#region Estadistica
def MediaCal(lista): #calcula la media de una lista de enteros
    try:
        lista_int = ListParseToInt(lista)
        suma = sum(lista_int)
        media = round(suma/len(lista_int),2)
        return media
    except:
        print("No es posible calcular la media con los datos entregados")
def ModaCal(lista): #calcula moda de una lista de enteros
    try:
        contador = {}
        for obj in lista:
            contador.setdefault(obj, 0)  # Inicializar el conteo para la edad si no existe
            contador[obj] += 1
        moda= max(contador, key=contador.get) 
        return moda
    except:
        print("No es posible calcular la Moda con los datos entregados")
def MedianaCal(lista):  #calcula la mediana de una lista de enteros
    try:
        lista_int = ListParseToInt(lista)
        largo_lista = len(sorted(lista_int))
        mitad_indice = largo_lista//2
        if largo_lista % 2 == 0:
            mediana = (sorted(lista_int)[mitad_indice - 1] + sorted(lista_int)[mitad_indice]) / 2
        else:
            mediana = sorted(lista_int)[mitad_indice]
        return mediana
    except:
        print("No es posible calcular la Mediana con los datos entregados")
def FrecuenciaCal(archivo, columna): #calcula la frecuencia de una columna de un archivo
    try:
        datos = DictParseToList(archivo,columna)
        contador={}
        if columna == "Respuesta":
            contador = {"Sí": 0, "No": 0, "Tal vez": 0}
            for obj in datos:
                if obj == "Sí":
                    contador["Sí"] += 1
                elif obj == "No":
                    contador["No"] += 1
                elif obj == "Tal vez":
                    contador["Tal vez"] += 1
                else:
                    print(f"Se encontró una respuesta desconocida: {obj}")
        elif columna =="Sexo":
            contador = {"Masculino": 0, "Femenino": 0}
            for obj in datos:
                if obj == "Masculino":
                    contador["Masculino"] += 1
                elif obj == "Femenino":
                    contador["Femenino"] += 1
                else:
                    print(f"Se encontró un sexo desconocido: {obj}")
        return contador
    except:
        print("No se reconocio variable Cualitativa")
#endregion

def main():#Solo para depuracion
    ProcesadorEncuesta()

if __name__ == "__main__":
    main()
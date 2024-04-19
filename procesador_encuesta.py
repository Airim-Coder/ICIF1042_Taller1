# 1. Debe solicitar al usuario el nombre del archivo de datos CSV al inicio.
# 2. Importar los módulos necesarios para leer el archivo CSV y realizar análisis de datos
# básicos.
# 3. Almacenar los datos en un diccionario de listas, donde cada clave representa una
# columna del archivo CSV (Sexo, Edad, Respuesta) y cada lista contiene los valores
# correspondientes.
# 4. Realiza un preprocesamiento de datos para transformar las respuestas (e.g., convertir
# respuestas de texto a números).
# 5. Utilice ciclos y sentencias condicionales para calcular estadísticas descriptivas (e.g.,
# promedio, mediana, moda) para la columna Edad.
# 6. Utilice ciclos y sentencias condicionales para contar la frecuencia de cada tipo de
# respuesta (Sí/No/Tal vez).
# 7. Implemente un menú interactivo usando ciclos while con las siguientes opciones:
#   a. Leer archivo de datos
#   b. Mostrar estadísticas generales (media, mediana, conteo de respuestas por tipo)
#   c. Filtrar datos por sexo y mostrar estadísticas
#   d. Filtrar datos por rango de edad y mostrar estadísticas
#   e. Guardar resultados en un archivo (todos aquellos generados)
#   f. Salir
import csv, os

CACHE=[]
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
            archivo = input("Ingrese el nombre del archivo a procesar: ") #pide el nombre del archivo
            #archivo = "encuesta_habitos.csv" #Solo para depuracion
            CACHE.append(f"lectura de archivo: {archivo}")
            datos_archivo = LeerEncuesta(archivo)
            print("Archivo importado con exito")
            opcion = str(input("Que desea hacer ahora?\nIngrese su opcion: "))
        elif opcion == "b":
            CACHE.append("Estadistica General del Archivo:")
            CalcularEstadisticas(datos_archivo)
            opcion = str(input("Ingrese su opcion: ")) 
        elif opcion == "c":
            #resp = str(input("Indique un Sexo(Femenino/Masculino): "))
            #CACHE.append("Estadistica filtrada por Sexo ({resp}):")
            #filtro_sexo=EstadisticaSexoxFiltro(datos_archivo,resp)
            print("No implementado aun")
            opcion = str(input("Ingrese su opcion: "))
        elif opcion == "d":
            #resp1 = int(input("Indique desde que edad: "))
            #resp2 = int(input("hasta que edad: "))
            #CACHE.append("Estadistica filtrada por Rango de Edad ({resp1}-{resp2}):")
            print("No implementado aun")
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

#region Calculos Estadisticos
def int_list_format(lista):
    lista_int = []
    for i in lista:
        lista_int.append(int(i))
    return lista_int
def CalcularMedia(lista):#funcion para calcular media
    lista_int = int_list_format(lista)
    suma = sum(lista_int)
    media = suma/len(lista_int)
    return media
def CalcularModa(lista):#funcion para calcular moda
    contador = {}
    for obj in lista:
        contador.setdefault(obj, 0)  # Inicializar el conteo para la edad si no existe
        contador[obj] += 1
    moda= max(contador, key=contador.get) 
    return moda
def CalcularMediana(lista):#funcion para calcular mediana
    lista_int = int_list_format(lista)
    largo_lista = len(sorted(lista_int))
    mitad_indice = largo_lista//2
    if largo_lista % 2 == 0:
        mediana = (sorted(lista_int)[mitad_indice - 1] + sorted(lista_int)[mitad_indice]) / 2
    else:
        mediana = sorted(lista_int)[mitad_indice]
    return mediana
def CalculoFrecuencia(archivo,columna):#funcion para calcular frecuencia
    datos=archivo[columna]
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
    else:
        print(f"No se reconocio variable Cualitativa")
    return contador

''' NO FUNCIONA
def EstadisticaSexoxFiltro(archivo, valor):#funcion para obtener la estadistica de sexo por filtro
    filtered = {'units': []}
    if valor in archivo['Sexo']:
        filtered['units'] = [elem for elem in data['units'] if elem['age'] == age]
    return filtered
     #CalcularEstadisticas(filtro)
'''
#endregion


def LeerEncuesta(archivo): #funcion para leer el archivo
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

def CalcularEstadisticas(datos_archivo):
    edades = datos_archivo["Edad"] #obtiene las edades
    sexo = datos_archivo["Sexo"] #obtiene los sexos
    respuesta = datos_archivo["Respuesta"] #obtiene las respuestas

    estadistica=[]


    media_edad = CalcularMedia(edades)
    estadistica.append(f"Media para edad: {media_edad}")

    moda_edad = CalcularModa(edades)
    estadistica.append(f"Moda para edad: {moda_edad}")

    mediana_edad = CalcularMediana(edades)
    estadistica.append(f"Mediana para edad: {mediana_edad}")
    
    moda_sexo = CalcularModa(sexo)
    estadistica.append(f"Moda para sexo: {moda_sexo}")

    frecuencia_sexo = CalculoFrecuencia(datos_archivo,"Sexo")
    estadistica.append(f"Frecuencia:")
    for key, value in frecuencia_sexo.items():
        estadistica.append(f"{key}: {value}")

    moda_respuesta = CalcularModa(respuesta)
    estadistica.append(f"Moda para respuesta: {moda_respuesta}")
    frecuencia_respuesta = CalculoFrecuencia(datos_archivo,"Respuesta")
    estadistica.append(f"Frecuencia:")
    for key, value in frecuencia_respuesta.items():
        estadistica.append(f"{key}: {value}")

    CACHE.append(estadistica)#Agregar a la cache
    
    
    #Imprimir resultados
    print("\nESTADISTICAS GENERALES")
    print("EDAD:")
    print(f"Media: {media_edad}")  
    print(f"Moda: {moda_edad}")  
    print(f"Mediana: {mediana_edad}")  
    
    print("\nSEXO:")
    print(f"Moda: {moda_sexo}")  
    print("Frecuencia:")
    for key, value in frecuencia_sexo.items():
        print(f"{key}: {value}")

    print("\nRESPUESTA:")
    print(f"Moda: {moda_respuesta}")  
    print("Frecuencia:")
    for key, value in frecuencia_respuesta.items():
        print(f"{key}: {value}")

def GuardarEnArchivo():
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


def main():#Solo para depuracion
    ProcesadorEncuesta()

if __name__ == "__main__":
    main()
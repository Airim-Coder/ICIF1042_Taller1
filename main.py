import generador_encuesta as ge #importar la clase generador_encuesta
import procesador_encuesta as pe #importar la clase procesador_encuesta

#menu principal

print("Bienvenido al taller nro 1 de SF para DS\nQue le gustaria hacer a continuacion?")
print("1. Generar una encuesta" 
     + "\n2. Procesar Datos de Una Encuesta" 
     + "\n3. Salir")
entrada = int(input("Ingrese su opcion: ")) #menu principal

while(True):
    if entrada == 1:
        ge.Generador_Encuesta() #llamar a la clase generador_encuesta
        print("\nQue le gustaria hacer ahora?\n1. Generar una encuesta\n2. Procesar Datos de Una Encuesta\n3. Salir")
        entrada = int(input("Ingrese su opcion: "))
    elif entrada == 2:
        pe.ProcesadorEncuesta() #llamar a la clase procesador_encuesta
        print("\nQue le gustaria hacer ahora?\n1. Generar una encuesta\n2. Procesar Datos de Una Encuesta\n3. Salir")
        entrada = int(input("Ingrese su opcion: "))
    elif entrada == 3:
        print("Gracias por usar esta mini app de consola\nHasta Pronto!")
        break #salir del programa
    else:
        print("Opcion no valida")
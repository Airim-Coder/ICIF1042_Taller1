import generador_encuesta as ge

print("Bienvenido al taller nro 1 de SF para DS\nQue le gustaria hacer a continuacion?")
print("1. Generar una encuesta\n2. Procesar Datos de Una Encuesta\n3. Salir")
entrada = int(input("Ingrese su opcion: "))

while(True):
    if entrada == 1:
        ge.Generador_Encuesta()
        print("\nQue le gustaria hacer ahora?\n1. Generar una encuesta\n2. Procesar Datos de Una Encuesta\n3. Salir")
        entrada = int(input("Ingrese su opcion: "))
    elif entrada == 2:
        print("Bajpo construccion")  # TODO: Crear la clase Procesador_Encuesta
        print("\nQue le gustaria hacer ahora?\n1. Generar una encuesta\n2. Procesar Datos de Una Encuesta\n3. Salir")
        entrada = int(input("Ingrese su opcion: "))
    elif entrada == 3:
        print("Gracias por usar esta mini app de consola\nHasta Pronto!")
        break
    else:
        print("Opcion no valida")
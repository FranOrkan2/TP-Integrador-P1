import csv
#Crea la lista de 0 con datos de algunos paises
def crear_archivo():
    with open("datos_paises.csv", "w", newline="", encoding="utf-8") as archivo:
        lista= ["nombre,poblacion,superficie,continente\n",  
                "Argentina,45376763,2780400,América\n",  
                "Japón,125800000,377975,Asia\n",  
                "Brasil,213993437,8515767,América\n", 
                "Alemania,83149300,357022,Europa\n"]
        
        archivo.writelines(lista)
        print("Lista creada")
        
#Agrega un pais en la ultima linea
def agregar_pais():
    try:
        with open("datos_paises.csv", "a", newline="", encoding="utf-8") as archivo:
            nombre = input("Ingrese el nombre del pais: ").title()
            continente= input("Ingrese el contintente al que pertenece: ").title()
            
            if nombre.isalpha() != True or continente.isalpha() != True: raise ValueError("Caracter invalido")
            
            poblacion= int(input("Ingrese la cantidad de habitantes: "))
            supeficie= int(input("Ingrese la superficie en m²: "))

            linea= f"{nombre},{poblacion},{supeficie},{continente}\n"
            archivo.write(linea)

    except ValueError as e:
        print(f"Error: {e}")

#Actualiza los datos de poblacion y superficie  
def actualizar_datos():
    
    try:
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            columnas= lector.fieldnames
            filas=list(lector)
        
        nombre_actualizar= input("Ingrese el pais: ").title()
        encontrado=False        

        for fila in filas:
            if nombre_actualizar == fila["nombre"]:
                    
                poblacio_actualizar= int(input("Ingrese la poblacion: "))
                superficie_actualizar=int(input("Ingrese la superficie: "))
                if poblacio_actualizar <=0 or superficie_actualizar <=0: raise ValueError("Ingrese valores enteros positivos")
                
                fila["poblacion"] = poblacio_actualizar
                fila["superficie"] = superficie_actualizar
                encontrado=True
                break
        
        if encontrado == True:
            with open("datos_paises.csv", "w", newline="", encoding="utf-8") as archivo:
                escritor=csv.DictWriter(archivo, fieldnames=columnas)
                escritor.writeheader()
                escritor.writerows(filas)
        
    except FileNotFoundError: print("Error: El archivo no existe")        
    except ValueError as e: print(f"Error: {e}")

#Buscar paies por nombre completo o parcial
def buscar_pais():
    try:
        nombre= input("Ingrese el pais: ").title()
        if nombre.isalpha()!= True:raise ValueError("Caracter invalido")
        encontrado=False
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
        
            for lista in lector:
                if nombre in lista["nombre"]:
                    print(f"Nombre: {lista["nombre"]} - Poblacion: {lista["poblacion"]} - Superficie: {lista["superficie"]} - Continente: {lista["continente"]}")
                    encontrado=True
                    break
            if not encontrado: print(f"{nombre} no existe")
    except FileNotFoundError:print("Error: El archivo no existe")
    except ValueError as e: print(f"Error: {e}")

opcion=0
while opcion != 7:

    #Menu Principal
    print("=" *170)
    print("1) Crear Lista   2) Agregar un Pais   3) Actualizar Datos   4)Buscar    5)Filtrar    6)Estadisticas    7)Salir")
    print("="*170)
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion<=0 or opcion >7: raise ValueError("Valor fuera de rango")
        if opcion==1: crear_archivo()
        elif opcion==2: agregar_pais()
        elif opcion==3: actualizar_datos()
        elif opcion==4: buscar_pais()
    except ValueError as e:
        print(f"Error: {e}")

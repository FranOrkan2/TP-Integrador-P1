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
                    print(f"Nombre: {lista["nombre"]} | Poblacion: {lista["poblacion"]} | Superficie: {lista["superficie"]} | Continente: {lista["continente"]}")
                    encontrado=True
                    break
            if not encontrado: print(f"{nombre} no existe")
    except FileNotFoundError:print("Error: El archivo no existe")
    except ValueError as e: print(f"Error: {e}")

#Filtra por nombre, poblacion y superficie (ascendente y descendente)
def filtrar():
    try:
        print("Filtrar")
        print("1)Por Nombre")
        print("2)Por Poblacion")
        print("3)Por Superficie")
        
        filtro= int(input("Opcion: "))
        if filtro <1 or filtro >3: raise ValueError("Valor fuera de rango")
        paises=[]
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            
            for lista in lector:
                datos ={"nombre": lista["nombre"], "poblacion": int(lista["poblacion"]), "superficie": int(lista["superficie"]), "continente": lista["continente"]}
                paises.append(datos)

            def obtener_nombre(pais):
                return pais["nombre"]
            
            def obtener_poblacion(pais):
                return pais["poblacion"]
            
            def obtener_superficie(pais):
                return pais["superficie"]
            
            if filtro==1:
                paises.sort(key=obtener_nombre)
                for pais in paises:
                    print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais["continente"]}")
            elif filtro==2:
                paises.sort(key=obtener_poblacion)
                for pais in paises:
                    print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais["continente"]}")
            elif filtro==3:
                print("1) Ascendente  2) Descendente")
                opciones= int(input("Opcion: "))
                if opciones <1 or opciones>2: raise ValueError("Valor fuera de rango")
                if opciones== 1:
                    paises.sort(key=obtener_superficie)
                    for pais in paises:
                        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais["continente"]}")
                elif opciones==2:
                    paises.sort(key=obtener_superficie, reverse=True)
                    for pais in paises:
                        print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais["continente"]}")
    
    except FileNotFoundError: print("Error: El archivo no existe")    
    except ValueError as e:
        print(f"Error: {e}")

def estadistica():
    
    try:
        paises=[]
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            for lista in lector:
                for lista in lector:
                    datos ={"nombre": lista["nombre"], "poblacion": int(lista["poblacion"]), "superficie": int(lista["superficie"]), "continente": lista["continente"]}
                    paises.append(datos)
            
            menor=8300000000
            mayor = 0
            nombre_menor, nombre_mayor=""

            for pais in paises:
                poblacion = pais["poblacion"]
                
                if poblacion < menor:
                    menor = poblacion
                    nombre_menor = pais["nombre"]
                
                if poblacion> mayor:
                    mayor = poblacion
                    nombre_mayor = pais["nombre"]

            



    except FileNotFoundError: print("Error: El archivo no existe")         
    
    print("")
    print("Pais con mayor poblacion")
    print("")


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
        elif opcion==5: filtrar()
    except ValueError as e:
        print(f"Error: {e}")

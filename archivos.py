import csv
from validaciones import pedir_texto, pedir_entero
def crear_archivo():
    """
    Crea el archivo datos_paises.csv con los datos iniciales de los países.
 
    Escribe el encabezado (nombre, poblacion, superficie, continente) y
    cuatro países predefinidos usando writelines(), que escribe toda la
    lista de líneas en una sola llamada.
 
    Parámetros: ninguno
    Retorna: ninguno
    """
    with open("datos_paises.csv", "w", newline="", encoding="utf-8") as archivo:
        lista= ["nombre,poblacion,superficie,continente\n",  
                "Argentina,45376763,2780400,América\n",  
                "Japón,125800000,377975,Asia\n",  
                "Brasil,213993437,8515767,América\n", 
                "Alemania,83149300,357022,Europa\n"]
        
        archivo.writelines(lista)
        print("\nLista creada\n")

def agregar_pais(continentes):
    """
    Solicita al usuario los datos de un nuevo país y lo agrega al archivo CSV.
 
    Validaciones aplicadas:
      - nombre y continente: solo letras (se aceptan espacios entre palabras,
        por ejemplo 'Estados Unidos' o 'América del Norte').
      - poblacion y superficie: deben ser enteros positivos.
 
    Usa modo append ('a') para no sobreescribir los datos ya guardados.
 
    Parámetros: ninguno
    Retorna: ninguno
    """
    try:
        with open("datos_paises.csv", "a", newline="", encoding="utf-8") as archivo:
            #nombre = input("Ingrese el nombre del pais: ").title()
            nombre = pedir_texto("Ingrese el nombre del pais: ")
            menu_continentes = "\nSeleccione el continente al que pertenece:\n1) América\n2) Asia\n3) Europa\n4) África\n5) Oceanía\nOpción: "
            opcion_continente = int(input(menu_continentes))
            
            continente = list(continentes.keys())[opcion_continente - 1]  # Obtiene el nombre del continente según la opción seleccionada
            
            # Valida que cada palabra del nombre contenga solo letras
            #if not all(palabra.isalpha() for palabra in nombre.split()): 
                #raise ValueError("Caracter invalido en el nombre")
            # Valida que cada palabra del continente contenga solo letras
            if continente not in continentes:
                raise ValueError("Continente no reconocido. Ingrese uno de los siguientes: América, Asia, Europa, África, Oceanía.")
                      
            
            poblacion= pedir_entero("Ingrese la cantidad de habitantes: ")
            superficie= pedir_entero("Ingrese la superficie en KM²: ")

            #if poblacion <= 0 or superficie <= 0:
                #raise ValueError("La población y la superficie deben ser enteros positivos")
            
            linea= f"{nombre},{poblacion},{superficie},{continente}\n"
            archivo.write(linea)
    except FileNotFoundError:
        print("Error: El archivo no existe")
    except ValueError as e:
        print(f"Error: {e}")

#Actualiza los datos de poblacion y superficie. No se puede actualizar el nombre ni el continente.
def actualizar_datos():
    '''Permite actualizar la población y superficie de un país existente en el archivo CSV.
    - Lee todo el archivo en memoria usando csv.DictReader para facilitar la actualización.
    - Solicita el nombre del país a actualizar y valida que exista.
    - Si el país existe, solicita los nuevos valores de población y superficie, validando que sean enteros positivos.
    - Escribe de nuevo todo el archivo con los datos actualizados usando csv.DictWriter.
    Parámetros: ninguno
    Retorna: ninguno
    '''
    
    try:
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            columnas= lector.fieldnames
            filas=list(lector)
        
        nombre_actualizar= pedir_texto("Ingrese el pais: ")
        encontrado=False        

        for fila in filas:
            
            if nombre_actualizar == fila["nombre"]:
                
                poblacio_actualizar= pedir_entero("Ingrese la poblacion: ")
                superficie_actualizar=pedir_entero("Ingrese la superficie en KM²: ")

                #if poblacio_actualizar <=0 or superficie_actualizar <=0: 
                    #raise ValueError("Ingrese valores enteros positivos")
                    
                # Actualiza solo los campos permitidos; nombre y continente no se modifican
                fila["poblacion"] = poblacio_actualizar
                fila["superficie"] = superficie_actualizar
                encontrado=True
                break
        
        if encontrado == True:
            # Reescribe el archivo completo con los datos actualizados
            with open("datos_paises.csv", "w", newline="", encoding="utf-8") as archivo:
                escritor=csv.DictWriter(archivo, fieldnames=columnas)
                escritor.writeheader() # escribe la línea de encabezado
                escritor.writerows(filas)# escribe todas las filas (incluida la modificada)
        else:
            print("No se ha encontrado el pais para actualizar...")
    except FileNotFoundError: print("Error: El archivo no existe")        
    except ValueError as e: print(f"Error: {e}")
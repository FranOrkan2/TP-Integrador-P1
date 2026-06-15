import csv
from validaciones import pedir_texto, pedir_entero

def crear_archivo():
    """
    Crea el archivo datos_paises.csv con los datos iniciales de los países.
 
    Escribe el encabezado (nombre, poblacion, superficie, continente)
    usando writelines(), que escribe toda la
    lista de líneas en una sola llamada.
 
    Parámetros: ninguno
    Retorna: ninguno
    """
    try:
        with open("datos_paises.csv", "x", newline="", encoding="utf-8") as archivo:
        
            lista= ["nombre,poblacion,superficie,continente\n"] 
        
            archivo.writelines(lista)
            print("\nLista creada\n")
    except FileExistsError:
        print("\nError: El archivo ya existe, no se puede crear nuevamente.")

def agregar_pais(continentes):
    """
    Solicita al usuario los datos de un nuevo país y lo agrega al archivo CSV.
 
    Validaciones aplicadas:
      - nombre: solo letras (se aceptan espacios entre palabras, por ejemplo 'Estados Unidos').
      - poblacion y superficie: deben ser enteros positivos.
 
    Usa modo append ('a') para no sobreescribir los datos ya guardados.

    """
    try:
        with open("datos_paises.csv","r") as f:
            f.read()
        with open("datos_paises.csv", "a", newline="", encoding="utf-8") as archivo:
            
            nombre = pedir_texto("Ingrese el nombre del pais: ")
            menu_continentes = "\nSeleccione el continente al que pertenece:\n1) América\n2) Asia\n3) Europa\n4) África\n5) Oceanía\nOpción: "
            opcion_continente = int(input(menu_continentes))
            
            continente = list(continentes.keys())[opcion_continente - 1]  # Obtiene el nombre del continente según la opción seleccionada
            
            poblacion= pedir_entero("Ingrese la cantidad de habitantes: ")
            superficie= pedir_entero("Ingrese la superficie en KM²: ")
 
            linea= f"{nombre},{poblacion},{superficie},{continente}\n"
            archivo.write(linea)
            print(f"\n{nombre} agregado exitosamente.\n")
    except FileNotFoundError:
        print("\nError: El archivo no existe, POR FAVOR, primero cree el archivo. Opción 1 del menú.")
    except Exception as e:
        print(f"Error inesperado: {e}, comuníquese con el desarrollador para resolverlo.")
    
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
            print(f"\n{nombre_actualizar} actualizado exitosamente.\n")
        else:
            print("No se ha encontrado el pais para actualizar...")
    except FileNotFoundError: 
        print("Error: El archivo no existe, POR FAVOR, primero cree el archivo. Opción 1 del menú.")
    except Exception as e:
        print(f"Error inesperado: {e}, comuníquese con el desarrollador para resolverlo.")
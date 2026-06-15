import csv
from validaciones import pedir_texto
#Buscar paies por nombre completo o parcial
def buscar_pais():
    """
    Busca un país por nombre completo o parcial en el archivo CSV.
 
    Formatea la entrada con title() para mejorar la coincidencia
    (por ejemplo 'argentina' → 'Argentina').
    La búsqueda es parcial: 'Arg' encuentra 'Argentina'.
    Muestra el primer resultado encontrado y detiene la búsqueda.
 
    Parámetros: ninguno
    Retorna: ninguno
    """
    try:
        
        nombre= pedir_texto("Ingrese el pais: ")
        
        encontrado=False
        
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            #Búsqueda parcial: verifica si el nombre ingresado está contenido en el campo
            for lista in lector:
                if nombre in lista["nombre"]:
                    print(f"Nombre: {lista["nombre"]} | Poblacion: {lista["poblacion"]} | Superficie: {lista["superficie"]} | Continente: {lista["continente"]}")
                    
                    encontrado=True

                    break
            if not encontrado: print(f"{nombre} no existe en el archivo")

    except FileNotFoundError:print("Error: El archivo no existe")

#Filtra por nombre, poblacion y superficie (ascendente y descendente)
def filtrar():
    """
    Filtra y ordena los países por nombre, población o superficie.
 
    Submenú principal:
      1) Por nombre      → orden alfabético ascendente
      2) Por población   → orden numérico ascendente
      3) Por superficie  → el usuario elige ascendente o descendente
 
    Usa list.sort() con el parámetro key para ordenar sin crear
    una lista nueva. Las funciones auxiliares se definen fuera del
    bloque 'with' para mantener el código organizado.
 
    Parámetros: ninguno
    Retorna: ninguno
    """
    def obtener_nombre(pais):
        return pais["nombre"]
    
    def obtener_poblacion(pais):
        return pais["poblacion"]
    
    def obtener_superficie(pais):
        return pais["superficie"]
    
    """Imprime todos los países de la lista en el formato estándar."""
    def mostrar_paises(paises):
        for pais in paises:
            print(f"Nombre: {pais['nombre']} | Poblacion: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
    
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
                datos ={"nombre": lista["nombre"], 
                        "poblacion": int(lista["poblacion"]), 
                        "superficie": int(lista["superficie"]), 
                        "continente": lista["continente"]
                        }
                
                paises.append(datos)

            if filtro == 1:
                paises.sort(key=obtener_nombre)
                mostrar_paises(paises)

            elif filtro == 2:
                paises.sort(key=obtener_poblacion)
                mostrar_paises(paises)

            elif filtro == 3:
                print("1) Ascendente  2) Descendente")
                opciones= int(input("Opcion: "))
                if opciones < 1 or opciones > 2: 
                    raise ValueError("Valor fuera de rango (1 o 2)")
                
                if opciones == 1:
                    paises.sort(key=obtener_superficie)
                    mostrar_paises(paises)

                # reverse=False → de menor a mayor | reverse=True → de mayor a menor
                elif opciones == 2:
                    paises.sort(key=obtener_superficie, reverse=(opciones == 2))
                    mostrar_paises(paises)

    except FileNotFoundError: print("Error: El archivo no existe")    
    except ValueError as e:
        print(f"Error: {e}")
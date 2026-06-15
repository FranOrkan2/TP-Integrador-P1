import csv

def estadistica(continentes):
    '''Permite mostrar estadísticas sobre los países en el archivo CSV, como el país con mayor y menor población. Los promedios de superficie y población, y la cantidad de países por continente
    - Define funciones auxiliares para contar países por continente y mostrar el conteo, manteniendo el código organizado.
    - Lee el archivo CSV usando csv.DictReader y almacena los datos en una lista de diccionarios para facilitar el análisis.
    - Inicializa variables para almacenar la población menor y mayor, así como los nombres de los países correspondientes.
    - Recorre la lista de países y compara la población de cada país con las variables de menor y mayor población, actualizando estas variables según sea necesario.
    - Al finalizar el recorrido, muestra el nombre del país con mayor población y el nombre del país con menor población.
    Parámetros: ninguno
    Retorna: ninguno
    '''
    def contar_por_continente(paises):
        for pais in paises:
            continente = pais["continente"]
            if continente in continentes:
                continentes[continente] += 1
            
        return continentes
     
    def mostrar_conteo(conteo):
        print("\n" + "=" * 50)
        print("Cantidad de países por continente")
        print("=" * 50)
        
        for continente, cantidad in conteo.items():
            print(f"\t{continente:<10}: {cantidad} {'país' if cantidad == 1 else 'países'}")
        print("=" * 50)

    # Inicializa el conteo de países por continente con 0 para cada continente conocido        
    try:
        paises=[]
        with open("datos_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            for lista in lector:
                datos ={"nombre": lista["nombre"], "poblacion": int(lista["poblacion"]), "superficie": int(lista["superficie"]), "continente": lista["continente"]}
                paises.append(datos)

            conteo = contar_por_continente(paises)
            mostrar_conteo(conteo)

            if not paises:
                print("El archivo no contiene países.")
                return
            
            # Se inicializa con el primer país para no depender de valores arbitrarios
            menor = paises[0]["poblacion"]
            mayor = paises[0]["poblacion"]
            nombre_menor = paises[0]["nombre"]
            nombre_mayor = paises[0]["nombre"]
            suma_poblacion, suma_superficie = paises[0]["poblacion"], paises[0]["superficie"]
            poblacion, superficie = 0, 0
            contador_poblacion, contador_superficie = 1, 1
            

            for pais in paises[1:]: # Se empieza desde el segundo país porque el primero ya esta cargado.
                poblacion = pais["poblacion"]
                superficie = pais["superficie"]
                suma_poblacion += poblacion
                suma_superficie += superficie
                contador_poblacion += 1
                contador_superficie += 1

                if poblacion < menor:
                    menor = poblacion
                    nombre_menor = pais["nombre"]
                
                if poblacion> mayor:
                    mayor = poblacion
                    nombre_mayor = pais["nombre"] 
            
            print("Estadísticas generales:")
            print("=" * 50)
            print(f"\nPaís con mayor población: {nombre_mayor} ({mayor:,} hab.)")
            print(f"País con menor población: {nombre_menor} ({menor:,} hab.)")
            print(f"El promedio de población es: {suma_poblacion // contador_poblacion:,} hab.")
            print(f"El promedio de superficie es: {suma_superficie // contador_superficie:,} km²")
            print("=" * 50)

    except FileNotFoundError:
        print("Error: El archivo no existe. Primero cree la lista (opción 1).")
    except ValueError as e:
        print(f"Error: {e}")
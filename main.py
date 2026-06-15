
from archivos import crear_archivo, agregar_pais, actualizar_datos
from consultas import buscar_pais, filtrar
from estadisticas import estadistica

# =============================================================
# GESTIÓN DE PAÍSES - datos_paises.csv
# =============================================================
# Nota general sobre el manejo de archivos CSV en este programa:
#   - encoding="utf-8" → soporta caracteres especiales como tildes y ñ
#   - newline=""       → evita líneas en blanco extra en Windows
# Estas opciones se aplican en todas las funciones que abren archivos.
# =============================================================

       
    
# =============================================================
# MENÚ PRINCIPAL
# =============================================================

opcion=0
while opcion != 7:

    continentes = {"América": 0, "Asia": 0, "Europa": 0, "África": 0, "Oceanía": 0}
    
    print("=" * 10 + "| Menú Principal | " + "=" * 10)
    print("1) Crear Lista\n2) Agregar un País\n3) Actualizar Datos\n4) Buscar\n5) Filtrar\n6) Estadísticas\n7) Salir")
    print("="*39)
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion<=0 or opcion >7: raise ValueError("Valor fuera de rango")
        if opcion==1: crear_archivo()
        elif opcion==2: agregar_pais(continentes=continentes)
        elif opcion==3: actualizar_datos()
        elif opcion==4: buscar_pais()
        elif opcion==5: filtrar()
        elif opcion==6: estadistica(continentes=continentes)
        elif opcion==7: 
            input("\nPrograma finalizado... presione Enter para Finalizar")
            break
        if opcion != 7:
            input("\nPresione Enter para continuar...\n")

    except ValueError as e:
        print(f"Error: {e}")


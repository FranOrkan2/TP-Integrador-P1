💻 Programación 1 Tecnicatura Universitaria en Programación

📍 UNIVERSIDAD TECNOLOGICA NACIONAL

🌎 Gestión de Países

💻 Trabajo Práctico Integrador — Programación I

✨ Integrantes Grupo 162:
            Fernandez, Jorge Nahuel              Comisión: M26 C1-14
            Rodriguez Abálos, Francisco Felix    Comisión: M26 C1-14

🖊️ Descripción

Sistema de gestión de países desarrollado en Python como Trabajo Práctico Integrador de la materia Programación I. Permite administrar un archivo CSV con datos de países (nombre, población, superficie y continente) desde la terminal, ofreciendo operaciones de creación, consulta, modificación y análisis estadísticos.

✳️Funcionalidades implementadas

✅ Crear archivo CSV con datos iniciales
✅ Agregar un nuevo país con validación de datos
✅ Actualizar población y superficie de un país existente
✅ Buscar país por nombre completo o parcial
✅ Filtrar y ordenar países por nombre, población o superficie (ascendente/descendente)
✅ Estadísticas: país con mayor/menor población, promedios y cantidad de países por continente

▶️ Cómo ejecutar el programa


1) Descargar o clonar el repositorio
2) Abrir una terminal en la carpeta del proyecto
3) Ejecutar el siguiente comando:
                    python main.py
4) Al iniciar por primera vez, seleccionar la opción "1) Crear Lista" para generar el archivo CSV con los datos iniciales.

✔️ Ejemplo de uso

'''
==================== | Menu Principal | ====================
1) Crear Lista
2) Agregar un País
3) Actualizar Datos
4) Buscar
5) Filtrar
6) Estadísticas
7) Salir
=======================================================
Ingrese una opción: 6

==================================================
Cantidad de países por continente
==================================================
        América   : 2 países
        Asia      : 1 país
        Europa    : 1 país
        África    : 0 países
        Oceanía   : 0 países
==================================================
Estadísticas generales:
==================================================

País con mayor población: Brasil (213,993,437 hab.)
País con menor población: Alemania (83,149,300 hab.)
El promedio de población es: 117,079,875 hab.
El promedio de superficie es: 3,007,541 km²
==================================================
'''

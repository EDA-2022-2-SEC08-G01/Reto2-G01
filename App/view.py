"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printTiempo_Memoria(tiempo, memoria): 
    mensaje = "****  Tiempo [ms]: {0} | Memoria [kb]: {1}  ****".format(round(tiempo,2), round(memoria,2))
    print(mensaje)

def printAmazon(catalog):
    size_plataforma = lt.size(catalog["model"]["amazon_prime"]) 
    movie = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        movie = lt.getElement(catalog["model"]["amazon_prime"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 canciones cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 canciones cargadas son...    >>>')
        print(
            "      Nombre: " + 
            movie["title"] + 
            " , Tipo: " + 
            str(movie["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(movie["release_year"])))

def printHulu(catalog):
    size_plataforma = lt.size(catalog["model"]["hulu"]) 
    movie = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        movie = lt.getElement(catalog["model"]["hulu"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 canciones cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 canciones cargadas son...    >>>')
        print(
            "      Nombre: " + 
            movie["title"] + 
            " , Tipo: " + 
            str(movie["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(movie["release_year"])))

def printNetflix(catalog):
    size_plataforma = lt.size(catalog["model"]["netflix"]) 
    movie = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        movie = lt.getElement(catalog["model"]["netflix"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 canciones cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 canciones cargadas son...    >>>')
        print(
            "      Nombre: " + 
            movie["title"] + 
            " , Tipo: " + 
            str(movie["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(movie["release_year"])))

def printDisney(catalog):
    size_plataforma = lt.size(catalog["model"]["disney_plus"]) 
    movie = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        movie = lt.getElement(catalog["model"]["disney_plus"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 canciones cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 canciones cargadas son...    >>>')
        print(
            "      Nombre: " + 
            movie["title"] + 
            " , Tipo: " + 
            str(movie["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(movie["release_year"])))


def printMenu():
    
    print("====="*15)
    print("          >>               Bienvenido                    <<     ")
    print("  [R0]   q- Cargar información en el catálogo.")
    print("  [R1]   1- Examinar los álbumes en un año de interés.")
    print("  [R2]   2- Encontrar los artistas por popularidad.")
    print("  [R3]   3- Encontrar las canciones por popularidad.")
    print("  [R4]   4- Encontrar la canción más popular de un artista.")
    print("  [R5]   5- Encontrar la discografía de un artista.")
    print("  [R6]   6- Clasificar las canciones de artistas con mayor distribución.")
    print("         0- Salir")
    print("====="*15)

catalog = controller.newController()
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('>> Seleccione una opción para continuar: ')
    if inputs == "q":
        print("Cargando información de los archivos ....")
        Amazon, Hulu, Netflix, Disney, tiempo, memoria = controller.loadData(catalog)
        TotalPeliculas = int(Amazon) + int(Hulu) + int(Netflix) + int(Disney)
        print("=="*40)
        print("      Número de peliculas en amazon: {0}".format(Amazon))
        print("      Número de peliculas en netflix: {0}".format(Netflix))
        print("      Número de peliculas en hulu: {0}".format(Hulu))
        print("      Número de peliculas en diney: {0}".format(Disney))
        print("      Número de peliculas cargadas: {0}".format(TotalPeliculas))


        print("=="*70)
        printAmazon(catalog)
        print("=="*70)
        printNetflix(catalog)
        print("=="*70)
        printHulu(catalog)
        print("=="*70)
        printDisney(catalog)

        printTiempo_Memoria(tiempo, memoria)

    else:
        sys.exit(0)
sys.exit(0)

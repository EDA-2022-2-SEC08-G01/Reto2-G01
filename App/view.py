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
    size_platform = lt.size(catalog["model"]["amazon_prime"]) 
    film = "" 
    pos = [0, 1, 2, size_platform-3, size_platform-2, size_platform-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["amazon_prime"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 peliculas cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 peliculas cargadas son...    >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))

def printHulu(catalog):
    size_platform = lt.size(catalog["model"]["hulu"]) 
    film = "" 
    pos = [0, 1, 2, size_platform-3, size_platform-2, size_platform-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["hulu"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 peliculas cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 peliculas cargadas son...    >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))

def printNetflix(catalog):
    size_platform = lt.size(catalog["model"]["netflix"]) 
    film = "" 
    pos = [0, 1, 2, size_platform-3, size_platform-2, size_platform-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["netflix"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 peliculas cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 peliculas cargadas son...    >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))

def printDisney(catalog):
    size_platform = lt.size(catalog["model"]["disney_plus"]) 
    film = "" 
    pos = [0, 1, 2, size_platform-3, size_platform-2, size_platform-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["disney_plus"], pos[i])
        if   i == 0:
            print('>>>   Primeras 3 peliculas cargadas son...   >>>')
        elif i == 3:
            print('>>>   Últimas 3 peliculas cargadas son...    >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))


#=^..^=   [Funciones de impresión]  =^..^=    =^..^=    =^..^=    =^..^=

#-------------------[Requerimiento 1]-------------------------------------------------------------

def printR1(films, num_films, estrenos_anio):

    print("=="*35)
    print('            Para el año {0}, se encontaron {1} peliculas'.format(estrenos_anio, num_films))
    print("=="*35)
    print('>>>>>>   Las primeras 3 películas en {0} son...   >>>>>>'.format(estrenos_anio))
    for i in range(6):
        film = lt.getElement(films, i+1)

        print(
            "Nombre: " + 
            str(film["title"]) + 
            ",\n    Fecha de lanzamiento: " + 
            str(film["release_year"] ) + 
            ",\n    Tipo: " + 
            str(film["type"]) + "\n"
        )
        if i+1 == 3:
            
            print('>>>>>>   Las últimas 3 películas en {0} son...   >>>>>>'.format(estrenos_anio))

#--------------------------[Requerimiento 2]-----------------------------------------------------------
def printR2(films, num_films, date):

    print("=="*35)
    print('            Para la fecha {0}, se encontaron {1} películas'.format(date, num_films))
    print("=="*35)
    print('>>>>>>   Los primeros 3 Tv Shows en {0} son...   >>>>>>'.format(date))
    for i in range(6):
        film = lt.getElement(films, i+1)

        print(
            "Nombre: " + 
            str(film["title"]) + 
            ",\n    Fecha de lanzamiento: " + 
            str(film["release_year"] ) + 
            ",\n    Tipo: " + 
            str(film["type"]) + "\n"
        )
        if i+1 == 3:
            
            print('>>>>>>   Los últimos 3  en {0} son...   >>>>>>'.format(date))
        
#--------------------------[Requerimiento 3]-----------------------------------------------------------
def printR5(film_types, resp_films, Actor_Name):
    films, TvShows, total = film_types
    print("=="*35)
    print("         {0} tiene: {1} films, {2} Tv Shows.".format(Actor_Name, films, TvShows))
    print("         Constituyendo un total de {0} proyectos.".format(total))
    
    print("\n>>>>>>    Los 3 primeros contenidos de {0} son: ".format(Actor_Name))

    for i in range(6):
        film = lt.getElement(resp_films, i +1)
        
        print(
            "Fecha de publicacion: " + 
            str(film["release_year"]) + 
            ",\n      Nombre del álbum: " + 
            str(film["title"]) + 
            ",\n      peliculas en el film: " + 
            str(film["director"]) + 
            ",\n      Tipo de film: " +
            str(film["type"]) + 
            ",\n      Nombre del artista: " +  
            str(Actor_Name) + 
            "\n"
        )
        if i +1 == 3:
            
            print(">>>>>>    Los 3 últimos contenidos de {0} son: ".format(Actor_Name))




def printMenu():
    
    print("====="*15)
    print("          >>               Bienvenido                    <<     ")
    print("  [R0]   c- Cargar información en el catálogo.")
    print("  [R1]   1- Examinar las pelicuas estrenadas en un año de interés.")
    print("  [R2]   2- Examinar los programas de televisión agregados en un año.")
    print("  [R3]   3- Encontrar el contenido donde participa un actor")
    print("  [R4]   4- Encontrar el contenido por un genero particular.")
    print("  [R5]   5- Encontrar el contenido producido en un país.")
    print("  [R6]   6- Encontrar el contenido con un director involucrado.")
    print("  [R7]   7- Listar el TOP(N) de los géneros con más contenido.")
    print("         0- Salir")
    print("====="*15)

catalog = controller.newController()
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('>> Seleccione una opción para continuar: ')
    if inputs == "c":
        print("Cargando información de los archivos ....")
        Amazon, Hulu, Netflix, Disney, General, tiempo, memoria = controller.loadData(catalog)
        print("=="*40)
        print("      Número de peliculas en amazon: {0}".format(Amazon))
        print("      Número de peliculas en netflix: {0}".format(Netflix))
        print("      Número de peliculas en hulu: {0}".format(Hulu))
        print("      Número de peliculas en diney: {0}".format(Disney))
        print("      Número de peliculas cargadas: {0}".format(General))


        print("=="*70)
        printAmazon(catalog)
        print("=="*70)
        printNetflix(catalog)
        print("=="*70)
        printHulu(catalog)
        print("=="*70)
        printDisney(catalog)

        printTiempo_Memoria(tiempo, memoria)

    elif int(inputs) == 1:
        estrenos_anio = input("> Ingrese el año que desea examinar: ")
        films, num_films, tiempo, memoria = controller.filmsbyYear(catalog, estrenos_anio)

        if tiempo == None:
            print('     No se halló este año')
        else:
            printR1(films,num_films, estrenos_anio)
            printTiempo_Memoria(tiempo, memoria)

    elif int(inputs) == 2:
        date = input("> Ingrese la fecha que desea examinar: ")
        films, num_films, tiempo, memoria = controller.TvShowsAdded(catalog, date)

        if tiempo == None:
            print('     No se halló nada en esta fecha')
        else:
            printR2(films,num_films,date)
            printTiempo_Memoria(tiempo,memoria)

    elif int(inputs) == 3:
        Actor_Name = input("Ingrese el nombre del actor que desea buscar: ")
        film_types, resp_films, time, memory,= controller.filmsActor(catalog, Actor_Name)
        
        if time == None:
            print("     No se encontró el contenido de ese artist")
        else:
            printR5(film_types, resp_films)
            printTiempo_Memoria(time, memory)




    else:
        sys.exit(0)
sys.exit(0)

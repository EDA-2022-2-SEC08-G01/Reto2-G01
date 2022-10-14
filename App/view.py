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
import pandas as pd 
from tabulate import tabulate as tb
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printTime_Memoria(Time, memoria): 
    mensaje = "****  Time [ms]: {0} | Memoria [kb]: {1}  ****".format(round(Time,2), round(memoria,2))
    print(mensaje)

def printAmazon(catalog):
    size_plataforma = lt.size(catalog["model"]["amazon_prime"]) 
    film = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["amazon_prime"], pos[i])
        if   i == 0:
            print('>>>   los 3 primeros contenidos cargados de Amazon Prime son...   >>>')
        elif i == 3:
            print('>>>   los 3 ultimos contenidos cargados de Amazon Prime son...   >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))

def printHulu(catalog):
    size_plataforma = lt.size(catalog["model"]["hulu"]) 
    film = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["hulu"], pos[i])
        if   i == 0:
            print('>>>   Los 3 primeros contenidos cargados de Hulu son...   >>>')
        elif i == 3:
            print('>>>   Los 3 últimos contenidos cargados de Hulu son...    >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))

def printNetflix(catalog):
    size_plataforma = lt.size(catalog["model"]["netflix"]) 
    film = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["netflix"], pos[i])
        if   i == 0:
            print('>>>   Los 3 primeros contenidos cargados de Netflix son...   >>>')
        elif i == 3:
            print('>>>   Los 3 últimos contenidos cargados de Netflix son...    >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))

def printDisney(catalog):
    size_plataforma = lt.size(catalog["model"]["disney_plus"]) 
    film = "" 
    pos = [0, 1, 2, size_plataforma-3, size_plataforma-2, size_plataforma-1]

    for i in range(6):
        film = lt.getElement(catalog["model"]["disney_plus"], pos[i])
        if   i == 0:
            print('>>>   Los 3 primeros contenidos cargados de Disney son...    >>>')
        elif i == 3:
            print('>>>   Los 3 últimos contenidos cargados de Disney son...     >>>')
        print(
            "      Nombre: " + 
            film["title"] + 
            " , Tipo: " + 
            str(film["type"] ) + 
            " , Año lanzamiento: " + 
            str(int(film["release_year"])))


#=^..^[Funciones de impresión]  =^..^=    =^..^=    =^..^= 

#-------------------[Requerimiento 1]-------------------------------------------------------------

def printR1(films, num_films, estrenos_anio):

    print("=="*35)
    print('            Para el año {0}, se encontaron {1} peliculas'.format(estrenos_anio, num_films))
    print("=="*35)
    print('>>>>>>   Las primeras 3 películas en {0} son...   >>>>>>'.format(estrenos_anio))
    #print(films)
    if lt.size(films) >= 6: 
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
    if lt.size(films) < 6: 
        for film in lt.iterator(films):
            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n"
            )

        

#--------------------------[Requerimiento 2]-----------------------------------------------------------
def printR2(films, num_films, date):

    print("=="*35)
    print('            Para el año {0}, se encontaron {1} creaciones (Movies y TvShows)'.format(date, num_films))
    print("=="*35)
    print('>>>>>>   Los primeros 3 contenidos encontrados en {0} son...   >>>>>>'.format(date))
    if lt.size(films) > 6: 
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
                
                print('>>>>>>   Los últimos 3 contenidos encontrados en {0} son...   >>>>>>'.format(date))
    else: 
        for film in lt.iterator(films):

            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n"
            )
        
#--------------------------[Requerimiento 3]-----------------------------------------------------------
def printR3(resp_films, types, Actor_Name):
    films, TvShows, Total = types
    print("=="*35)
    print("         {0} tiene: {1} Peliculas, {2} Tv Shows.".format(Actor_Name, films, TvShows))
    print("         Constituyendo un total de {0} creaciones.".format(Total))
    
    print("\n>>>>>>    Los 3 primeros albumes en la discografia de {0} son: ".format(Actor_Name))
    if lt.size(resp_films) > 6: 
        for i in range(6):
            film = lt.getElement(resp_films, i+1)
        
        print(
            "Fecha de publicacion: " + 
            str(film["release_year"]) + 
            ",\n      Nombre del álbum: " + 
            str(film["title"]) + 
            ",\n      Canciones en el film: " + 
            str(film["director"]) + 
            ",\n      Tipo de film: " +
            str(film["type"]) + 
            ",\n      Nombre del artista: " +  
            str(Actor_Name) + 
            "\n"
        )
        if i +1 == 3:
            
            print(">>>>>>    Las últimas 3 películas de {0} son: ".format(Actor_Name))
    else: 
        for film in lt.iterator(resp_films):

            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n"
            )

#--------------------------[Requerimiento 4]-----------------------------------------------------------
def printR4(resp_films, types, genre):
    films, TvShows, Total = types
    print("=="*35)
    print("         {0} tiene: {1} Peliculas, {2} TV Shows.".format(genre, films, TvShows))
    print("         Constituyendo un total de {0} Creaciones (contenido).".format(Total))
    
    print("\n>>>>>>    Las 3 primeras películas de {0} son: ".format(genre))

    if lt.size(resp_films) > 6: 
        for i in range(6):
            film = lt.getElement(resp_films, i+1)

            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n"
            )
            if i+1 == 3:
                
                print('>>>>>>   Las últimas 3 películas en {0} son...   >>>>>>'.format(genre))
    else: 
        for film in lt.iterator(resp_films):

            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n")

#--------------------------[Requerimiento 5]-----------------------------------------------------------

def printR5(resp_films, types, country):
    films, TvShows, Total = types
    print("=="*35)
    print("         {0} tiene: {1} Peliculas, {2} Creaciones.".format(country, films, TvShows))
    print("         Constituyendo un total de {0} Creaciones (contenido).".format(Total))
    
    print("\n>>>>>>    Las 3 primeras películas de {0} son: ".format(country))

    if lt.size(resp_films) > 6: 
        for i in range(6):
            film = lt.getElement(resp_films, i+1)

            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n"
            )
            if i+1 == 3:
                
                print('>>>>>>   Las últimas 3 películas  en {0} son...   >>>>>>'.format(country))
    else: 
        for film in lt.iterator(resp_films):

            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n")

#--------------------------[Requerimiento 6]-----------------------------------------------------------



def printR6(ans, director):

    # Indice de ans: cantidad_total_DIC, types, list_genre, cont_total, contenidopordic

    print("=="*35)
    print(f" {director} tiene un total de  {str(ans[0])} contenido de los cuales {str(ans[1][0])} son peliculas, y {str(ans[1][1])} son series.")
    print("=="*35)
    print(f"El total por plataforma de streaming es  {ans[5]}")
    print("=="*35)
    print(f"los generos listados son {ans[2]}")
    print("=="*35)
    print('>>>>>>   Las primeras 3 películas en {0} son...   >>>>>>'.format(director))
    #print(films)
    if lt.size(ans[4]) >= 6: 
        for i in range(6):
            film = lt.getElement(ans[4], i+1)

            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n"
            )
            if i+1 == 3:
                
                print('>>>>>>   Las últimas 3 películas en {0} son...   >>>>>>'.format(director))
    if lt.size(ans[4]) < 6: 
        for film in lt.iterator(ans[4]):
            print(
                "Nombre: " + 
                str(film["title"]) + 
                ",\n    Fecha de lanzamiento: " + 
                str(film["release_year"] ) + 
                ",\n    Tipo: " + 
                str(film["type"]) + "\n"
            )

#--------------------------[Requerimiento 7]-----------------------------------------------------------
def printR7(topGen, top):
    gen=lt.newList('ARRAY_LIST')

    rank= topGen['first']

    while rank:
        i=rank['info']
        count= i['num_movies']+i['num_shows']
        lt.addLast(gen,(i['genre'],count))

        rank=rank['next']
    
    gen2=lt.newList('ARRAY_LIST')

    rank= topGen['first']
    while rank:
        i=rank['info']
        count= i['num_movies']+i['num_shows']
        lt.addLast(gen2,(i['genre'],count,('count type // movie: '+str(i['num_movies'])+' // TV shows: '+str(i['num_shows'])),('count stream service // amazon: '+str(i['amazon'])+ ' // netflix: '+ str(i['netflix'])+' // hulu: '+str(i['hulu'])+' // disney: '+str(i['disney']))))
        rank=rank['next']

    print('----- TOP ' + top + 'LISTED_IN -----')
    print(gen['elements'])
    print('----- TOP Listed_in detalles -----')
    tabla2=tb(gen2['elements'], headers=['listed_in','count','type','stream_service'],tablefmt='grid')
    print(tabla2)

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
    print("  [R8]   8- Listar el TOP(N) de los actores más populares para un género en específico.")
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
        Amazon, Hulu, Netflix, Disney, General, Time, memoria = controller.loadData(catalog)
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

        printTime_Memoria(Time, memoria)

    elif int(inputs) == 1:
        estrenos_anio = input("> Ingrese el año que desea examinar: ")
        films, num_films, Time, memoria = controller.FilmsByYear(catalog, estrenos_anio)

        if Time == None:
            print('     No se halló este año')
        else:
            printR1(films,num_films, estrenos_anio)
            printTime_Memoria(Time, memoria)

    elif int(inputs) == 2:
        date = input("> Ingrese la fecha que desea examinar: ")
        films, num_films, Time, memoria = controller.TvShowsAdded(catalog, date)

        if Time == None:
            print('     No se halló nada en esta fecha')
        else:
            printR2(films,num_films,date)
            printTime_Memoria(Time,memoria)

    elif int(inputs) == 3:
        Actor_Name = input("Ingrese el nombre del actor que desea buscar: ").title()
        resp_films, types, time, memory,= controller.FilmsByActor(catalog, Actor_Name)
        
        if time == None:
            print("     No se encontró contenido en el que participe este actor")
        else:
            printR3(resp_films, types, Actor_Name)
            printTime_Memoria(time, memory)
    
    elif int(inputs) == 4:
        Genere_Name = input("Ingrese el genero que desea buscar: ")
        resp_films, types, time, memory,= controller.FilmsByGenre(catalog, Genere_Name)
        
        if time == None:
            print("     No se encontró contenido relacionado con este género.")
        else:
            printR4(resp_films, types, Genere_Name)
            printTime_Memoria(time, memory)

    elif int(inputs) == 5:
        country = input("Ingrese el pais que desea buscar: ").title()
        resp_films, types, time, memory,= controller.FilmsByCountry(catalog, country)
        
        if time == None:
            print("     No se encontró contenido relacionado con este país.")
        else:
            printR5(resp_films, types, country)
            printTime_Memoria(time, memory)
    
    elif int(inputs) == 6:
        director = input("Ingrese el nombre del director que desea buscar ").title()
        respuesta, time, memory, = controller.FilmsbyDirector(catalog,director)
        if time == None:
            print("     No se encontró contenido relacionado con este director.")
        else:
            printR6(respuesta, director)
            printTime_Memoria(time, memory)

    elif int(inputs) == 7:
        top=input("Ingrese el TOP N que desea buscar: ")
        resp,time,memory=controller.topGenres(catalog,top)

        printR7(resp,top)
        printTime_Memoria(time,memory)





    else:
        sys.exit(0)
sys.exit(0)

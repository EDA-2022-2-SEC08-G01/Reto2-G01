"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from platform import architecture
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mgs
assert cf
from datetime import datetime as dt


# Construccion de modelos
def newCatalog():
    catalog = {
        "amazon_prime" : None,
        "hulu" : None, 
        "netflix": None,
        "disney_plus": None,
        "general": None,
        #================[lab7]================
        "genres":  None,
        #================[id]==================
        "id_amazon": None,
        "id_hulu": None,
        "id_netflix": None,
        "id_disney": None,
        "id_films": None,
        #=================[R1]=================
        "films_per_year": None,
        #=================[R2]=================
        'film_per_actor' : None,
        #=================[R3]=================
        "film_per_genres": None,
        #=================[R4]=================
        'film_per_country': None,
        #=================[R5]=================
        "film_per_director": None
    }
    catalog["amazon_prime"] = lt.newList("ARRAY_LIST")
    catalog["hulu"] = lt.newList("ARRAY_LIST")
    catalog["netflix"] = lt.newList("ARRAY_LIST")
    catalog["disney_plus"] = lt.newList("ARRAY_LIST")
    catalog["general"] = lt.newList("ARRAY_LIST")
    #================[ids]=====================
    
    catalog['id_films'] = mp.newMap(numelements = 46000,
                        maptype= 'PROBING',
                        loadfactor = 0.4
                        )
    catalog['id_amazon'] = mp.newMap(numelements = 46000,
                        maptype= 'PROBING',
                        loadfactor = 0.4
                        )
    catalog['id_hulu'] = mp.newMap(numelements = 46000,
                        maptype= 'PROBING',
                        loadfactor = 0.4
                        )
    catalog['id_netflix'] = mp.newMap(numelements = 46000,
                        maptype= 'PROBING',
                        loadfactor = 0.4
                        )
    catalog['id_disney'] = mp.newMap(numelements = 46000,
                        maptype= 'PROBING',
                        loadfactor = 0.4
                        )
    
    
    #=================[R1]=================
    catalog["films_per_year"] = mp.newMap(numelements= 250, 
                        maptype="PROBING",
                        loadfactor=0.4
                        )
    
    #=================[R2]=================
    catalog["films_per_date"] = mp.newMap(numelements= 46000, 
                        maptype="PROBING",
                        loadfactor=0.4
                        )
    #=================[R3]=================
    catalog['film_per_actor'] = mp.newMap(numelements= 40000,
                        maptype='PROBING',
                        loadfactor= 0.4
                        )
                        
    #=================[R4 & R7]=================
    catalog["film_per_genres"] = mp.newMap(numelements = 200,
                        maptype='PROBING',
                        loadfactor= 0.4
                        )

    #=================[R5]=================
    catalog['film_per_country'] = mp.newMap(numelements = 400, 
                        maptype= 'PROBING',
                        loadfactor = 0.4
                        )

    #================[R6]===================
    catalog["film_per_director"] = mp.newMap(numelements = 40000, 
                        maptype= 'PROBING',
                        loadfactor = 0.4
                        )

    #================[Adicionales]===================
    catalog["films_per_type"] = mp.newMap(numelements= 250, 
                        maptype="PROBING",
                        loadfactor=0.4
                        )
    return catalog

# Funciones para agregar informacion al catalogo
def addAmazon(catalog, film):
    
    lt.addLast(catalog["amazon_prime"], film)
    #=================[Id]====================
    mp.put(catalog['id_amazon'], film['show_id'], film)

def addHulu(catalog, film):
    
    lt.addLast(catalog["hulu"], film)
    #=================[Id]====================
    mp.put(catalog['id_hulu'], film['show_id'], film)

def addNetflix(catalog, film):
    
    lt.addLast(catalog["netflix"], film)
    #=================[Id]====================
    mp.put(catalog['id_netflix'], film['show_id'], film)

def addDisney(catalog, film):
    
    lt.addLast(catalog["disney_plus"], film)
    #=================[Id]====================
    mp.put(catalog['id_disney'], film['show_id'], film)


def addGeneral(catalog, film):
    
    lt.addLast(catalog["general"], film)
    #=================[Id]====================
    mp.put(catalog['id_films'], film['show_id'], film)
    actors = film['cast'].split(",")  # Se obtienen los actores
    for actor in actors:
        addMapActor(catalog, actor.strip(), film)
    genres = film['listed_in'].split(",")  # Se obtienen los generos
    for gen in genres:
        addMapGenres(catalog, gen.strip(), film)
    countrys = film['country'].split(",")  # Se obtienen los paises
    for country in countrys:
        addMapCountry(catalog, country.strip(), film)
    addMapYears(catalog, film)
    addMapDate(catalog, film)
    #=================[Requerimiento 1]=================
def addMapYears(catalog, film):
    if film["type"] == "Movie":

        anio_film = str(film["release_year"])
        exists_year = mp.get(catalog["films_per_year"], anio_film)

        if exists_year:
            insertElementHashR1(exists_year["value"], film, lo=1,hi=None)

        else:
            mp.put(catalog["films_per_year"], anio_film, lt.newList("ARRAY_LIST"))
            exists_year = mp.get(catalog["films_per_year"], anio_film)
            lt.addLast(exists_year["value"], film)
    
    #==================[Requerimiento 2]===================
def addMapDate(catalog, film):
    if film["type"] == "TV Show":
        date_add = str(film["date_added"])
        exists_date = mp.get(catalog["films_per_date"], date_add)

        if exists_date:
            insertElementHashR2(exists_date["value"], film, lo=1,hi=None)

        else:
            mp.put(catalog["films_per_date"], date_add, lt.newList("ARRAY_LIST"))
            exists_date = mp.get(catalog["films_per_date"], date_add)
            lt.addLast(exists_date["value"], film)

    #=================[Requerimiento 3]=================
def addMapActor(catalog, actor_name, film):
    actors = catalog['film_per_actor']
    existactor = mp.contains(actors, actor_name)
    if existactor:
        entry = mp.get(actors, actor_name)
        actor = me.getValue(entry)
    else:
        lista = lt.newList()
        mp.put(actors,actor_name,lista)
        entry = mp.get(actors, actor_name)
        actor = me.getValue(entry)
    lt.addLast(actor, film)

    #=================[Requerimiento 4]=================
def addMapGenres(catalog, genre, film):
    genres = catalog['film_per_genres']
    existgenre = mp.contains(genres, genre)
    if existgenre:
        entry = mp.get(genres, genre)
        gen = me.getValue(entry)
        lt.addLast(gen, film)
    else:
        lista = lt.newList()
        mp.put(genres,genre,lista)
        entry = mp.get(genres, genre)
        gen = me.getValue(entry)
    lt.addLast(gen, film)

    #=================[Requerimiento 5]=================
def addMapCountry(catalog, country, film):
    countrys = catalog['film_per_country']
    existcountry = mp.contains(countrys, country)
    if existcountry:
        entry = mp.get(countrys, country)
        nation = me.getValue(entry)
    else:
        lista = lt.newList()
        mp.put(countrys,country,lista)
        entry = mp.get(countrys, country)
        nation = me.getValue(entry)
    lt.addLast(nation, film)


#=^..^= [Funciones por requerimiento]  =^..^=    =^..^=    =^..^=    =^..^=

#=================[Requerimiento 1]=================

def insertElementHashR1(lista, film, lo=1, hi=None):
    if hi is None:
        hi = lt.size(lista) + 1
    while lo < hi:
        mid = (lo+hi)//2
        if film["release_year"] < lt.getElement(lista, mid)["release_year"]: 
            hi = mid
        
        else:
             lo = mid+1
    lt.insertElement(lista, film, lo)

def FilmsByYear(catalog, estrenos_anio):
    """
    Función principal del requerimiento 1
    """
    lista_anio = mp.get(catalog["model"]["films_per_year"], estrenos_anio)

    
    if lista_anio == None:
        return None, None

    lista_anio = mp.get(catalog["model"]["films_per_year"], estrenos_anio)["value"]
    num_films = mp.size(lista_anio)
    lista_anio_ord = mgs.sort(lista_anio, cmpRequerimiento1)
    films = FirstAndLast(lista_anio_ord)


    return films, num_films


#=====================[Requerimiento 2]================================
def insertElementHashR2(lista, film, lo=1, hi=None):
    if hi is None:
        hi = lt.size(lista) + 1
    while lo < hi:
        mid = (lo+hi)//2
        if film["date_added"] < lt.getElement(lista, mid)["date_added"]: 
            hi = mid
        
        else:
             lo = mid+1
    lt.insertElement(lista, film, lo)

def TvShowsAdded(catalog, date):
    """
    Función principal del requerimiento 2
    """
    lista_dates = mp.get(catalog["model"]["films_per_date"], date)
    
    if lista_dates == None:
        return None, None
    lista_dates = mp.get(catalog["model"]["films_per_date"], date)["value"]
    num_films = mp.size(lista_dates)
    lista_dates_ord = mgs.sort(lista_dates, cmpRequerimiento2)
    films = FirstAndLast(lista_dates_ord)


    return films, num_films

#=====================[Requerimiento 3]================================

 
def ContentByActor(catalog, Actor_Name):
    resp_films = None 
    exist_films = mp.get(catalog["film_per_actor"], Actor_Name)
    if exist_films:
        resp_films = me.getValue(exist_films)
        types = CountContentbyTypeR3(resp_films)
        resp_films = mgs.sort(resp_films,cmpRequerimiento3)

    return resp_films, types

#=====================[Requerimiento 4]================================

def ContentByGenre(catalog, genre):
    resp_films = None 
    exist_films = mp.get(catalog["film_per_genres"], genre)
    if exist_films:
        resp_films = me.getValue(exist_films)
        types = CountContentbyTypeR4(resp_films, genre)
        resp_films = mgs.sort(resp_films,cmpRequerimiento4)

    return resp_films, types

#=====================[Requerimiento 5]================================

 
def ContentCountry(catalog, country):
    resp_films = None 
    exist_films = mp.get(catalog["film_per_country"], country)
    if exist_films:
        resp_films = me.getValue(exist_films)
        types = CountContentbyTypeR5(resp_films, country)
        resp_films = mgs.sort(resp_films,cmpRequerimiento5)

    return resp_films, types



#=^..^[Funciones de comparación para comparar elementos de una lista]  =^..^=    =^..^=    =^..^=  

#cmp por requerimiento

def cmpRequerimiento1(content1, content2):
    Default = False 

    duration1 = content1["duration"].split() 
    duration2 = content2["duration"].split()

    
    if (content1['title']) < (content2['title']):
            Default = True 
    elif  (content1['title']) == (content2['title']):
        if len(duration1) > 0 and len(duration2) > 0:
            if (int(duration1[0]) < int(duration2[0])):
                Default = True
    
    return Default

def cmpRequerimiento2(content1, content2):
    Default = False 

    duration1 = content1["duration"].split() 
    duration2 = content2["duration"].split()

    
    if (content1['title']) < (content2['title']):
            Default = True 
    elif  (content1['title']) == (content2['title']):
        if len(duration1) > 0 and len(duration2) > 0:
            if (int(duration1[0]) < int(duration2[0])):
                Default = True
    
    return Default



def cmpRequerimiento3(film1, film2):

    Default = False 

    duration1 = film1["duration"].split()
    duration2 = film2["duration"].split()

    if (int(film1['release_year']) < int(film2['release_year'])):
            Default = True
    elif  (int(film1['release_year']) == int(film2['release_year'])):
        if (film1['title']) < (film2['title']):
            Default = True 
        elif  (film1['title']) == (film2['title']):
            if len(duration1) > 0 and len(duration2) > 0:
                if (int(duration1[0]) < int(duration2[0])):
                    Default = True
    return Default


def cmpRequerimiento4(film1, film2):

    Default = False 

    duration1 = film1["duration"].split()
    duration2 = film2["duration"].split()

    if (int(film1['release_year']) < int(film2['release_year'])):
            Default = True
    elif  (int(film1['release_year']) == int(film2['release_year'])):
        if (film1['title']) < (film2['title']):
            Default = True 
        elif  (film1['title']) == (film2['title']):
            if len(duration1) > 0 and len(duration2) > 0:
                if (int(duration1[0]) < int(duration2[0])):
                    Default = True
    return Default

def cmpRequerimiento5(film1, film2):

    Default = False 

    duration1 = film1["duration"].split()
    duration2 = film2["duration"].split()

    if (int(film1['release_year']) < int(film2['release_year'])):
            Default = True
    elif  (int(film1['release_year']) == int(film2['release_year'])):
        if (film1['title']) < (film2['title']):
            Default = True 
        elif  (film1['title']) == (film2['title']):
            if len(duration1) > 0 and len(duration2) > 0:
                if (int(duration1[0]) < int(duration2[0])):
                    Default = True
    return Default



#=^..^[Funciones para contar tipos de contenido]  =^..^=    =^..^=    =^..^= 

def CountContentbyTypeR3(lista):
    films = 0
    TvShows = 0
    total = lt.size(lista) 

    for film in lt.iterator(lista):
        if film["type"] == "Movie":
            films += 1
        elif film["type"] == "TV Show":
            TvShows += 1

    return (films, TvShows, total)

def CountContentbyTypeR4(lista, genre):
    films = 0
    TvShows = 0
    total = lt.size(lista) 

    for film in lt.iterator(lista):
        if film["type"] == "Movie":
            if genre in film["listed_in"]:
                films += 1
        elif film["type"] == "TV Show":
            if genre in film["listed_in"]:
                TvShows += 1

    return (films, TvShows, total)

def CountContentbyTypeR5(lista,country):
    films = 0 
    TvShows = 0 
    total = lt.size(lista)

    for film in lt.iterator(lista):
        if film["type"] == "Movie":
            if country in film["country"]:
                films += 1
        elif film["type"] == "TV Show":
            if country in film["country"]:
                TvShows += 1

    return (films, TvShows, total)

#=^..^[Funciones adicionales]  =^..^=    =^..^=    =^..^=  

def FirstAndLast(lista):
    sizelista = lt.size(lista)
    if sizelista <=6:
        df = (lista)
        return df
    first_3 = lt.subList(lista,1, 3)
    last_3 = lt.subList(lista,sizelista-3, 3)
    listafinal =[]
    for i in lt.iterator(first_3):
        listafinal.append(i) 
    for a in lt.iterator(last_3):
        listafinal.append(a)
    df=(listafinal)
    return df



    
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
    #=================[R1]=================
    anio_film = str(film["release_year"])
    exists_year = mp.get(catalog["films_per_year"], anio_film)

    if exists_year:
        insertElementHashr1(exists_year["value"], film, lo=1,hi=None)

    else:
        mp.put(catalog["films_per_year"], anio_film, lt.newList("ARRAY_LIST"))
        exists_year = mp.get(catalog["films_per_year"], anio_film)
        lt.addLast(exists_year["value"], film)

    #==================[R2]===================
    date_add = str(film["date_added"])
    exists_date = mp.get(catalog["films_per_date"], date_add)

    if exists_date:
        insertElementHashr2(exists_date["value"], film, lo=1,hi=None)

    else:
        mp.put(catalog["films_per_date"], date_add, lt.newList("ARRAY_LIST"))
        exists_date = mp.get(catalog["films_per_date"], date_add)
        lt.addLast(exists_date["value"], film)

    #=================[R3]=================
    cast = str(film["cast"])
    actor_name_key = mp.get(catalog["id_films"], cast)
            
    if actor_name_key != None:
                actor_name_key = actor_name_key["value"]["title"]
            
    if actor_name_key == None:
        pass
    else:
        list_actor_films = mp.get(catalog["film_per_actor"], actor_name_key)

        if list_actor_films:
            insertElementHashr2(list_actor_films["value"],film, lo=1,hi=None)
                
        else:

            mp.put(catalog["film_per_actor"], actor_name_key, lt.newList("ARRAY_LIST"))
            list_artist_albums = mp.get(catalog["film_per_actor"], actor_name_key)
            lt.addLast(list_actor_films["value"], film)


#=^..^=   =^..^=   =^..^=   [Funciones por requerimiento]  =^..^=    =^..^=    =^..^=    =^..^=

#=================[R1]=================

def insertElementHashr1(lista, film, lo=1, hi=None):
    if hi is None:
        hi = lt.size(lista) + 1
    while lo < hi:
        mid = (lo+hi)//2
        if film["release_year"] < lt.getElement(lista, mid)["release_year"]: 
            hi = mid
        
        else:
             lo = mid+1
    lt.insertElement(lista, film, lo)

def filmsbyYear(catalog, estrenos_anio):
    """
    Función principal del requerimiento 1
    """
    list_year = mp.get(catalog["model"]["films_per_year"], estrenos_anio)

    
    if list_year == None:
        return None, None

    list_year = mp.get(catalog["model"]["films_per_year"], estrenos_anio)["value"]
    num_films = mp.size(list_year)
    list_year_ord = mgs.sort(list_year, cmpReq1)
    films = FirstAndLast(list_year_ord)


    return films, num_films

#=====================[R2]================================
def insertElementHashr2(lista, film, lo=1, hi=None):
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
    list_dates = mp.get(catalog["model"]["films_per_date"], date)
    
    if list_dates == None:
        return None, None
    list_dates = mp.get(catalog["model"]["films_per_date"], date)["value"]
    num_films = mp.size(list_dates)
    list_dates_ord = mgs.sort(list_dates, cmpReq2)
    films = FirstAndLast(list_dates_ord)


    return films, num_films

#=====================[R3]================================
def insertElementHashr3(lista, film, lo=1, hi=None):
    if hi is None:
        hi = lt.size(lista) + 1
    while lo < hi:
        mid = (lo+hi)//2
        if film["release_year"] > lt.getElement(lista, mid)["release_year"]: 
            hi = mid
        
        else:
             lo = mid+1
    lt.insertElement(lista, film, lo)

def countfilmsbyType(list_films):
    films = 0 
    TvShows = 0 
    total = lt.size(list_films)

    for film in lt.iterator(list_films):
        if film["type"] == "films":
            films += 1
        elif film["type"] == "Tv Show":
            TvShows += 1

    return (films, TvShows, total)
 

def ContentActor(catalog, Actor_Name):
    service = catalog["model"]["general"]
    for content in lt.iterator(service):
        if Actor_Name.lower() in content["cast"]:


            list_films = mp.get(catalog["model"]["film_per_actor"], Actor_Name)

    if list_films == None:
        return None, None
            
    list_films = list_films["value"]
    film_types = countfilmsbyType(list_films)
    list_films_ord = mgs.sort(list_films ,cmpReq3)
    resp_films = FirstAndLast(list_films_ord)

                

    return film_types, resp_films




#=^..^=  =^..^=  [Funciones de comparación para comparar elementos de una lista]  =^..^=    =^..^=    =^..^=  

def cmpReq1(content1, content2):
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

def cmpReq2(content1, content2):
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



def cmpReq3(film1, film2):

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

# Funciones de ordenamiento

#=^..^=  =^..^=  [Funciones adicionales]  =^..^=    =^..^=    =^..^=  

def FirstAndLast(lista):
    size = lt.size(lista)
    if size >= 3:
        first_last = lt.newList('ARRAY_LIST')
        first = lt.getElement(lista,1)
        second = lt.getElement(lista,2)
        third = lt.getElement(lista,3)
        antepenultimo = lt.getElement(lista,lt.size(lista)-2)
        penultim = lt.getElement(lista,lt.size(lista)-1)
        last = lt.getElement(lista,lt.size(lista))
        
        lt.addLast(first_last, first)
        lt.addLast(first_last, second)
        lt.addLast(first_last, third)
        lt.addLast(first_last, antepenultimo)
        lt.addLast(first_last, penultim)
        lt.addLast(first_last, last)
    elif size == 1:
        first_last = lt.newList('ARRAY_LIST')
        first = lt.getElement(lista, 1)
        
        lt.addLast(first_last, first)
    elif size == 2:
        first_last = lt.newList('ARRAY_LIST')
        first = lt.getElement(lista, 1)
        second = lt.getElement(lista,2)

        lt.addLast(first_last, first)
        lt.addLast(first_last, second)

    return first_last
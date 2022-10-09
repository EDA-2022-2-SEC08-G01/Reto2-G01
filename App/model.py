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
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
from datetime import datetime as dt


# Construccion de modelos
def newCatalog():
    catalog = {
        "amazon_prime" : None,
        "hulu" : None, 
        "netflix": None,
        "disney_plus": None,
        #================[lab7]================
        "genres":  None,
        #================[id]==================
        "id_amazon": None,
        "id_hulu": None,
        "id_netflix": None,
        "id_disney": None,
        #=================[R1]=================
        "amazon_per_year": None,
        "hulu_per_year": None,
        "netflix_per_year": None,
        "disney_per_year": None,
        #=================[R2]=================
        'movie_per_actor' : None,
        #=================[R3]=================
        "movie_per_genres": None,
        #=================[R4]=================
        'movie_per_country': None,
        #=================[R5]=================
        "movie_per_director": None
    }
    catalog["amazon_prime"] = lt.newList("ARRAY_LIST")
    catalog["hulu"] = lt.newList("ARRAY_LIST")
    catalog["netflix"] = lt.newList("ARRAY_LIST")
    catalog["disney_plus"] = lt.newList("ARRAY_LIST")
    #================[ids]=====================
    
    catalog['id_amazon'] = mp.newMap(numelements = 46000,
                        maptype= 'PROBING',
                        loadfactor = 0.4,
                        )

    catalog['id_hulu'] = mp.newMap(numelements = 46000, 
                        maptype= 'PROBING',
                        loadfactor = 0.4,
                        )

    catalog['id_netflix'] = mp.newMap(numelements = 46000, 
                        maptype= 'PROBING',
                        loadfactor = 0.4,
                        )

    catalog['id_disney'] = mp.newMap(numelements = 46000,                        
                        maptype= 'PROBING',
                        loadfactor = 0.4,
                        )
    
    
    #=================[R1]=================
    catalog["amazon_per_year"] = mp.newMap(numelements= 250, 
                        maptype="PROBING",
                        loadfactor=0.4,
                        )
    catalog["hulu_per_year"] = mp.newMap(numelements= 250, 
                        maptype="PROBING",
                        loadfactor=0.4,
                        )
    catalog["netflix_per_year"] = mp.newMap(numelements= 250, 
                        maptype="PROBING",
                        loadfactor=0.4,
                        )
    catalog["disney_per_year"] = mp.newMap(numelements= 250, 
                        maptype="PROBING",
                        loadfactor=0.4,
                        )

    #=================[R2]=================
    catalog['movie_per_actor'] = mp.newMap(numelements= 40000,
                        maptype='PROBING',
                        loadfactor= 0.4,
                        )
                        
    #=================[R3 & R6]=================
    catalog["movie_per_genres"] = mp.newMap(numelements = 200,
                        maptype='PROBING',
                        loadfactor= 0.4,
                        )

    #=================[R4]=================
    catalog['movie_per_country'] = mp.newMap(numelements = 400, 
                        maptype= 'PROBING',
                        loadfactor = 0.4,
                        )

    #================[R5]===================
    catalog["movie_per_director"] = mp.newMap(numelements = 40000, 
                        maptype= 'PROBING',
                        loadfactor = 0.4,
                        )
    return catalog

# Funciones para agregar informacion al catalogo
def addAmazon(catalog, movie):
    
    lt.addLast(catalog["amazon_prime"], movie)
    #=================[Id]====================
    mp.put(catalog['id_amazon'], movie['show_id'], movie)

def addHulu(catalog, movie):
    
    lt.addLast(catalog["hulu"], movie)
    #=================[Id]====================
    mp.put(catalog['id_hulu'], movie['show_id'], movie)

def addNetflix(catalog, movie):
    
    lt.addLast(catalog["netflix"], movie)
    #=================[Id]====================
    mp.put(catalog['id_netflix'], movie['show_id'], movie)

def addDisney(catalog, movie):
    
    lt.addLast(catalog["disney_plus"], movie)
    #=================[Id]====================
    mp.put(catalog['id_disney'], movie['show_id'], movie)


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
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

# Funciones de ordenamiento

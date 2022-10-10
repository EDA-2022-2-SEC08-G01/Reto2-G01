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
 """

import config as cf
import model
import csv
import time
import tracemalloc
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
size = "small"

# Inicialización del Catálogo de libros
def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control

# Funciones para la carga de datos

def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    
    tracemalloc.start()

    start_time = getTime()
    start_memory = getMemory()

    Amazon = loadAmazon(catalog)
    Hulu = loadHulu(catalog)
    Netflix = loadNetflix(catalog)
    Disney = loadDisney(catalog)
    General = loadGeneral(catalog)


    stop_memory = getMemory()
    stop_time = getTime()
  
    tracemalloc.stop()

    time = deltaTime(stop_time, start_time)
    memory = deltaMemory(stop_memory, start_memory)
    return Amazon, Hulu, Netflix, Disney, General, time, memory

def loadAmazon(catalog):
    """
    Carga todas las peliculas del archivo de Amazon y las agrega a la lista de peliculas. 
    """
    amazonfile = cf.data_dir + 'Streaming/amazon_prime_titles-utf8-{0}.csv'.format(size)
    input_file = csv.DictReader(open(amazonfile, encoding='utf-8'))
    for film in input_file:
        model.addAmazon(catalog, film)
    return lt.size(catalog["amazon_prime"])

def loadNetflix(catalog):
    """
    Carga todas las peliculas del archivo de Netflix y las agrega a la lista de peliculas.
    """
    netflixfile = cf.data_dir + 'Streaming/netflix_titles-utf8-{0}.csv'.format(size)
    input_file = csv.DictReader(open(netflixfile, encoding='utf-8'))
    for film in input_file:
        model.addNetflix(catalog, film)
    return lt.size(catalog["netflix"])

def loadHulu(catalog):
    """
    Carga todas las peliculas del archivo de Hulu y las agrega a la lista de peliculas.
    """
    hulufile = cf.data_dir + 'Streaming/hulu_titles-utf8-{0}.csv'.format(size)
    input_file = csv.DictReader(open(hulufile, encoding='utf-8'))
    for film in input_file:
        model.addHulu(catalog, film)
    return lt.size(catalog["hulu"])

def loadDisney(catalog):
    """
    Carga todas las peliculas del archivo de Disney y las agrega a la lista de peliculas.
    """
    disneyfile = cf.data_dir + 'Streaming/disney_plus_titles-utf8-{0}.csv'.format(size)
    input_file = csv.DictReader(open(disneyfile, encoding='utf-8'))
    for film in input_file:
        model.addDisney(catalog, film)
    return lt.size(catalog["disney_plus"])

def loadGeneral(catalog):
    """
    Carga todas las peliculas del archivo (todas las plataformas) y las agrega a la lista de peliculas.
    """
    disneyfile = cf.data_dir + 'Streaming/disney_plus_titles-utf8-{0}.csv'.format(size)
    input_file_1 = csv.DictReader(open(disneyfile, encoding='utf-8'))
    hulufile = cf.data_dir + 'Streaming/hulu_titles-utf8-{0}.csv'.format(size)
    input_file_2 = csv.DictReader(open(hulufile, encoding='utf-8'))
    netflixfile = cf.data_dir + 'Streaming/netflix_titles-utf8-{0}.csv'.format(size)
    input_file_3 = csv.DictReader(open(netflixfile, encoding='utf-8'))
    amazonfile = cf.data_dir + 'Streaming/amazon_prime_titles-utf8-{0}.csv'.format(size)
    input_file_4 = csv.DictReader(open(amazonfile, encoding='utf-8'))
    for film in input_file_1:
        model.addGeneral(catalog, film)
    for film in input_file_2:
        model.addGeneral(catalog, film)
    for film in input_file_3:
        model.addGeneral(catalog, film)
    for film in input_file_4:
        model.addGeneral(catalog, film)
    return lt.size(catalog["general"])


#=====================[Requerimiento 1]=======================================
def filmsbyYear(catalog, estrenos_anio):

    tracemalloc.start()

    start_time = getTime()
    start_memory = getMemory()

    films, num_films = model.filmsbyYear(catalog, estrenos_anio)

    stop_memory = getMemory()
    stop_time = getTime()
    
    tracemalloc.stop()

    time = deltaTime(stop_time, start_time)
    memory = deltaMemory(stop_memory, start_memory)

    if films == None:
        return None, None, None, None

    return films, num_films, time, memory

#=====================[Requerimiento 2]=======================================
def TvShowsAdded(catalog, date):

    tracemalloc.start()

    start_time = getTime()
    start_memory = getMemory()

    films, num_films = model.TvShowsAdded(catalog, date)

    stop_memory = getMemory()
    stop_time = getTime()
    
    tracemalloc.stop()

    time = deltaTime(stop_time, start_time)
    memory = deltaMemory(stop_memory, start_memory)

    if films == None:
        return None, None, None, None

    return films, num_films, time, memory

#=====================[Requerimiento 3]=======================================
def filmsActor(catalog, Actor_Name):

    tracemalloc.start()

    start_time = getTime()
    start_memory = getMemory()

    film_types, resp_films = model.ContentActor(catalog, Actor_Name)

    stop_memory = getMemory()
    stop_time = getTime()
    
    tracemalloc.stop()

    time = deltaTime(stop_time, start_time)
    memory = deltaMemory(stop_memory, start_memory)

    if resp_films == None:
        return None, None, None, None

    return film_types, resp_films, time, memory



# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

#=^..^=   =^..^=   =^..^=    =^..^=  [Funciones de Tiempo]  =^..^=    =^..^=    =^..^=    =^..^=
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


#=^..^=   =^..^=   =^..^=    =^..^=  [Funciones para medir memoria]  =^..^=    =^..^=    =^..^=    =^..^=

def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

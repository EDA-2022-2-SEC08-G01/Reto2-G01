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
tam = "large"

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

def loadData(control, memflag=True):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    
    #tracemalloc.start()

    start_time = getTime()
    #start_memory = getMemory()

    Amazon = loadAmazon(catalog)
    Hulu = loadHulu(catalog)
    Netflix = loadNetflix(catalog)
    Disney = loadDisney(catalog)


    #stop_memory = getMemory()
    stop_time = getTime()
  
    #tracemalloc.stop()

    time = deltaTime(stop_time, start_time)
    #memory = deltaMemory(stop_memory, start_memory)
    return Amazon, Hulu, Netflix, Disney, time

def loadAmazon(catalog):
    """
    Carga todas las canciones del archivo y las agrega a la lista de tracks. 
    """
    amazonfile = cf.data_dir + 'Streaming/amazon_prime_titles-utf8-{0}.csv'.format(tam)
    input_file = csv.DictReader(open(amazonfile, encoding='utf-8'))
    for movie in input_file:
        model.addAmazon(catalog, movie)
    return lt.size(catalog["amazon_prime"])

def loadNetflix(catalog):
    """
    Carga todos los albums del archivo y los agrega a la lista de albums.
    """
    netflixfile = cf.data_dir + 'Streaming/netflix_titles-utf8-{0}.csv'.format(tam)
    input_file = csv.DictReader(open(netflixfile, encoding='utf-8'))
    for movie in input_file:
        model.addNetflix(catalog, movie)
    return lt.size(catalog["netflix"])

def loadHulu(catalog):
    """
    Carga todas los artistas del archivo y las agrega a la lista de artists.
    """
    hulufile = cf.data_dir + 'Streaming/hulu_titles-utf8-{0}.csv'.format(tam)
    input_file = csv.DictReader(open(hulufile, encoding='utf-8'))
    for movie in input_file:
        model.addHulu(catalog, movie)
    return lt.size(catalog["hulu"])

def loadDisney(catalog):
    """
    Carga todas los artistas del archivo y las agrega a la lista de artists.
    """
    disneyfile = cf.data_dir + 'Streaming/disney_plus_titles-utf8-{0}.csv'.format(tam)
    input_file = csv.DictReader(open(disneyfile, encoding='utf-8'))
    for movie in input_file:
        model.addDisney(catalog, movie)
    return lt.size(catalog["disney_plus"])

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo












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


# Funciones para medir la memoria utilizada


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

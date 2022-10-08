﻿"""
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

from atexit import register
from operator import mod
from model import cmpMoviesByReleaseYear
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qs
import config as cf
import model
import csv
import pandas as pd
#import tabulate

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def newController(structure):
    control = {'model': None}
    control["model"] = model.newCatalog(structure)
    return control
 



# Funciones para la carga de datos

def loadTitles(catalog, sampleSize):
    sample = str(sampleSize) + "pct"
    if sampleSize == 100:
        sample = "large"
    register = 0
    all_registers={}
    uuid= 0
    count = 0
    for service in catalog: #service toma el valor de amazon, hulu, etc
        
        if service != "general":
            individual_register = 0    
            platform = catalog[service]
            file = cf.data_dir + "Streaming/" + service + "_titles-utf8-" + sample + ".csv"
            input_file = csv.DictReader(open(file, encoding='utf-8'))
            for content in input_file: #content toma el valor de cada diccionario "cada línea del archivo"
                model.addContent(platform, content, service, uuid)
                model.addContent(catalog["general"], content, service, uuid)
                uuid += 1
                count += 1
                if count % 50 == 0:
                    ins.sort(platform, cmpMoviesByReleaseYear)
                    ins.sort(catalog["general"], cmpMoviesByReleaseYear)
            register += model.platformSize(platform)
            individual_register += model.platformSize(platform)
            all_registers[service] = individual_register
    
    return register, all_registers

control = newController("ARRAY_LIST")

def loadData(control, sampleSize):
    catalog = control["model"]
    register, all_registers = loadTitles(catalog, sampleSize)
    
    return register, all_registers


# Funciones de ordenamiento
def choosingSorts(control, orderType):
    return model.choosingSorts(control["model"], orderType)




def sortCatalog(control, order):
    catalog = control["model"]
    return model.sortCatalog(catalog, order)
# Funciones de consulta sobre el catálogo
def firstAndLast(catalog):
    return model.firstAndLast(catalog)

def findContentByGenre(control, genre):
    return model.findContentByGenre(control["model"], genre)


def findContentByCountry(control, country):
    return model.findContentByCountry(control["model"], country)


def findContentByActor(control, nameAutor):
    return model.findContentByActor(control["model"], nameAutor)

def moviesInYears(control, initial_year, final_year):
    return model.moviesInYears(control["model"], initial_year, final_year)

def TvShowsInPeriod(control, initialDate, finalDate):
    return model.TvShowsInPeriod(control["model"], initialDate, finalDate)

def directorInvolved(control, director):
    return model.directorInvolved(control["model"], director)

def topGenders(control, top):
    return model.topGenders(control["model"], top)
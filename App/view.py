﻿"""
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

from atexit import register
from pyexpat import model
#from turtle import pd
from wsgiref import headers
import config as cf
import sys
import controller as controller
from DISClib.ADT import list as lt
assert cf
from tabulate import tabulate
import pandas as pd
default_limit = 1000
sys.setrecursionlimit(default_limit*100)

# revisar cambios hechos del 8 al 11 de septiembre, hemos hecho más commits después de esa fecha gracias :)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController(structure):
    control = controller.newController(structure)
    return control

def chooseStructure():
    structure = int(input("Seleccione una estructura para organizar los datos (0 para SINGLE_LINKED o 1 para ARRAY_LIST): "))
    if structure == 0:
        return "SINGLE_LINKED"
    elif structure == 1:
        return "ARRAY_LIST"

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar películas estrenadas en un periodo de tiempo")
    print("3- Listar programas de televisión agregados en un periodo de tiempo")
    print("4- Consultar contenido donde participa un actor")
    print("5- Consultar contenido por un género específico")
    print("6- Consultar contenido producido en un país")
    print("7- Consultar1 contenido con un director involucrado")
    print("8- Listar el TOP x de los géneros con más contenido")
    print("9- Seleccionar tipo de lista, ordenamiento y muestra")
    print("0- Salir")


def countPlatformTable(ar):
    values = list(ar.values())
    keys = list(ar.keys())
    platforms = [[keys[0],str(values[0])],[keys[1],str(values[1])],[keys[2],str(values[2])],[keys[3],str(values[3])]]
    print(tabulate((platforms), headers= ["Service Name", "count"], tablefmt = "fancy_grid"))
    print("\n")

#def firstAndLastTable():
    
#catalog = None

def loadData(control, sampleSize):
    register = controller.loadData(control, sampleSize)
    return register

def loadDataDefault(control):
    register = controller.loadDataDefault(control)
    return register



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        structure = input("Selecciones una estructura de datos ('ARRAY_LIST', 'SINGLE_LINKED', 'CHAINING' o 'PROBING'): ").upper()
        if structure != "ARRAY_LIST" and structure != "SINGLE_LINKED" and structure != "CHAINING"and structure != "PROBING":
            structure = input("Por favor, elija una opcion válida: ")
        
        control = newController(structure)
        sampleSize = int(input("Ingrese el porcentaje de la muestra ('5', '10', '20', '30', '50', '80', '100'): "))
        print("Cargando información de los archivos ....")
        register, ar = loadData(control, sampleSize)
        print(register)
        print('Títulos cargados: ' + str(register))
        print("-"*100)

        print(countPlatformTable(ar))

        
        firstAndLast = controller.firstAndLast(control["model"])
        consulta = (list(firstAndLast.values())[0])
        lista=[]
        for pelicula in consulta:
            elemento= list(pelicula.values())
            lista.append(elemento)
        #print(tabulate((lista), headers= ['show_id', 'streaming_service', 'type', 'release_year', 
        #    'title', 'director', 'cast', 'country', 'date_adeed', 'rating', 'duration', 'listed_in', 'description'], tablefmt='grid', stralign= 'left'))
        print(lista)
    elif int(inputs[0]) == 2:
        initial_year = int(input("Ingrese el año inicial del periodo: "))
        final_year = int(input("Ingrese el año final del periodo: "))
        sub, ar , delt= controller.moviesInYears(control, initial_year, final_year)
        delta_time = delt
        print("Hay " + str(ar) +" películas estrenadas entre " + str(initial_year) + " y " + str(final_year))
        print("Los tres primeros, tres ultimos encontrados de acuerdo a sus parámetros son: ")
        print(sub)
        print("\nPara este requerimiento, delta tiempo:", str(delta_time))
    
    elif int(inputs[0]) == 3:
        initialDate = input("Ingrese la fecha inicial del periodo: ")
        finalDate = input("Ingrese la fecha final del periodo: ")
        sub, ar, delt = controller.TvShowsInPeriod(control, initialDate, finalDate)
        delta_time = delt
        print("Hay " + str(ar) +" series estrenadas entre " + str(initialDate) + " y " + str(finalDate))
        print("Los tres primeros, tres ultimos encontrados de acuerdo a los parámetros son: ")
        print(sub)
        print("\n Para este requerimiento, delta tiempo:", str(delta_time))


    
    elif int(inputs[0]) == 4:
        nameAutor = input("\nIngrese el nombre del actor que desea buscar: ")
        register, contentByAutor, delt = controller.findContentByActor(control, nameAutor)
        delta_time = delt
        df = contentByAutor
        print(nameAutor.title(), "tiene un total de", register["TV Shows"], "TV Shows y " , register["Movies"], "Movies.")
        print("Los tres primeros, tres ultimos encontrados y su informacion son: ")
        print(df)
        print("\n Para este requerimiento, delta tiempo:", str(delta_time))

    elif int(inputs[0]) == 5:
        genre = input("Ingrese el nombre del género de pelicula o serie que desea buscar: ")
        ans, delt = controller.findContentByGenre(control, genre)
        delta_time = delt
        print(f"Hay un total de {str(ans[1])} series y {str(ans[2])}  peliculas del género -{genre}-")
        df = ans[0]
        print("Los tres primeros, tres ultimos encontrados de acuerdo a sus parámetros son: ")
        print(df)
        #print(tabulate(df,headers='keys',tablefmt='fancy_grid'))
        print("\n Para este requerimiento, delta tiempo:", str(delta_time))
        



    elif int(inputs[0]) == 6:
        country = input("Ingrese el país que desea buscar: ")
        register, contentByCountry, delt = controller.findContentByCountry(control, country)
        delta_time = delt
        print(country.title(), "tiene un total de", register["TV Shows"], "TV Shows y " , register["Movies"], "Movies.")
        print("Los tres primeros, tres ultimos encontrados de acuerdo a sus parametros son: ")
        print(contentByCountry)
        print("\n Para este requerimiento, delta tiem   po:", str(delta_time))
    
    elif int(inputs[0]) == 7:
        director = input("Ingrese el director que desea buscar: ")
        tr, sr, gr, sub,delta_time = controller.directorInvolved(control, director)
        print(tr, sr, gr, sub)
        print("\n Para este requerimiento, delta tiempo:", str(delta_time))

    elif int(inputs[0]) == 8:
        top = int(input("Ingrese el TOP N que desea conocer: "))
        ag = controller.topGenders(control, top)
        print(ag)
        


    elif int(inputs[0]) == 9:
        orderType = input("Ingrese el ordenamiento a usar ('shell', 'insertion', 'selection', 'merge', 'quick'): ").lower()
        sorted_list, delta = controller.choosingSorts(control, orderType)
        print(delta)
        print("-"*100)
        #print(sorted_list)
        
        
    else:
        sys.exit(0)
sys.exit(0)

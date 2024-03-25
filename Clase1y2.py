#Clase 1

import numpy as np
def pertenece(x,lista)-> bool:
    if x in lista:
        return True
    else:
        return False

def mas_larga(l1,l2)-> list:
    if len(l1) < len(l2):
        return l2
    else:
        return l1
    
def mezclar(c1:str,c2:str)-> str:
    mezcla = " "
    if len(c1) >= len(c2):
        for i in range(len(c2)):
            mezcla += c1[i] + c2[i]
        mezcla += c1[len(c2):]
        return mezcla
    else:
        for i in range(len(c1)):
            mezcla += c1[i] + c2[i]
        mezcla += c2[len(c1):]
        return mezcla
        
    
def monto_total()-> float:
    monto = 0
    saldo = 500000
    while saldo > 0:
       saldo += (0.05/12) * saldo - (2684.11)
       monto += (2684.11) 
    return monto
       
def monto_adelanta()-> float:
    monto = 0 
    saldo = 500000
    meses = 0
    while saldo > 0: 
        while meses < 12: 
            saldo += (0.05/12) * saldo - (3684.11)
            monto += (3684.11) 
            meses += 1
        saldo += (0.05/12) * saldo - (2684.11)
        monto += (2684.11) 
        meses += 1 
    print(f"Tarda {meses} meses")
    print (f"El monto total es de {monto}")
        
def monto_adelanta2()-> float:
    monto = 0 
    saldo = 500000
    meses = 0
    while saldo > 0:
        while 60 < meses < 108: 
            saldo += (0.05/12) * saldo - (3684.11)
            monto += (3684.11) 
            meses += 1
        saldo += (0.05/12) * saldo - (2684.11)
        monto += (2684.11) 
        meses += 1 
    print(f"Tarda {meses} meses")
    print (f"El monto total es de {monto}")
    
    
    
def geringoso(lista)-> dict:
    dict = {}
    for elem in lista:
        dict[elem] = [geringoso_aux(elem)]
    return dict

def geringoso_aux(x:str)-> str:
    palabra = ""
    lista = ["a","A","e","E","i","I","o","O","u","U"]
    for i in range(len(x)):
        if x[i] in lista:
            palabra += x[i] + "p" + x[i]
        else:
            palabra += x[i]
    return palabra

def tabla_multiplicar(x):
    for multiplicador in range(1,10):
        resultado = 0
        for i in range(multiplicador): 
            resultado += x
        print(f"{x} x {multiplicador} = {resultado}")
    

for i in range(1,10):
    tabla_multiplicar(i)
    print()
    
# Clase 2
import csv 

def leer_parque(nombre_archivo,parque):
    lista_parque = []
    with open(nombre_archivo,"rt",encoding="utf-8") as archivo:
        filas = csv.reader(archivo)
        encabezado = next(filas)
        for fila in filas:
            if fila[10] == parque:
                arbol = fila[6]
                if arbol: 
                    arboles = dict(zip(encabezado, fila))
                    lista_parque.append(arboles)
    return lista_parque
            

def especies(lista_parque):
    conjunto_de_especies = set()
    for dict in lista_parque:
        conjunto_de_especies.add(dict["nombre_com"])
    return conjunto_de_especies

def contar_ejemplares(lista_parque):
    diccionario = {}
    for dict in lista_parque:
        if dict["nombre_com"] in diccionario:
            diccionario[dict["nombre_com"]]  += 1
        else:
            diccionario[dict["nombre_com"]] = 1
    return diccionario 

def obtener_alturas(lista_parque, especie):
    alturas = []
    for dict in lista_parque:
        if dict["nombre_com"] == especie:
            alturas.append(float(dict["altura_tot"]))
        else:
            alturas = alturas
    return alturas

def obtener_inclinaciones(lista_parque, especie):
    inclinaciones = []
    for dict in lista_parque:
        if dict["nombre_com"] == especie:
            inclinaciones.append(float(dict["inclinacio"]))
        else:
            inclinaciones = inclinaciones
    return inclinaciones

def especimen_mas_inclinado(lista_parque):
    especies = []
    inclinaciones = []
    max_inclinaciones = []
    for dictionary in lista_parque:
        especies.append(dictionary["nombre_com"])
    for especie in especies:
       inclinaciones = obtener_inclinaciones(lista_parque,especie)
       max_inclinaciones.append(max(inclinaciones))
       incli = max(max_inclinaciones)
    for i in range(len(max_inclinaciones)):
        if max_inclinaciones[i] == incli:
            arbol = especies[i]
        else:
            i += 1
    print (f" el arbol {arbol} tiene una inclinación de {max(max_inclinaciones)}")
            
def especie_promedio_mas_inclinada(lista_parque):
    especies = []
    promedios = []
    for dictionary in lista_parque:
        especies.append(dictionary["nombre_com"])
    for especie in especies:
        obtener_inclinaciones(lista_parque, especie)
        promedios.append(sum(obtener_inclinaciones(lista_parque, especie))/len(obtener_inclinaciones(lista_parque, especie)))
    for i in range(len(promedios)):
        if promedios[i] == max(promedios):
            arbol = especies[i]
        else:
            i += 1
    print (f"el arbol con mayor inclinacion es el {arbol} y tiene una inclinación promedio de {max(promedios)}")
        
           


    
    
   
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
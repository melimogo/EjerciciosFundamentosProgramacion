# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:13:27 2018

@author: USUARIO
"""

import numpy as np


M = np.array([[500,200,300],[100,100,300],[300,400,900]])

VectorAcciones = ["Ecopetrol", "Argos", "bancolombia"]
#print(Vector_Acciones[2])

print(M)

# PUNTO 1
# Promedio por cada accion
def promedioAcciones(Vector):
    suma = 0
    for j in range(len(Vector)):
            suma = suma + Vector[j]
    return suma/len(Vector)

for i in range(len(M.T)):
    promedioAccionesPorFilas = promedioAcciones(M[i][:])
    print('El promedio para la acción {} es: {}'.format(VectorAcciones[i],promedioAccionesPorFilas))
    
# PUNTO 2
# Dia del mes en el que argos tuvo menor valor
def menorValorDelMesArgos(Vector):
    Menor = Vector[0]
    diaMenor = 0    
    for j in range(len(Vector)):
        if Menor > Vector[j]:
            Menor = Vector[j]
            diaMenor = j
    return diaMenor

def buscarArgos(Vector):
    itemArgos = 0
    for i in range(len(Vector)):
        if Vector[i] == "Argos":
            itemArgos = i
    return itemArgos

posicionArgos = buscarArgos(VectorAcciones)
menorValorArgos = menorValorDelMesArgos(M[posicionArgos][:])
print('El dia en el cual se presentó la acción mas baja fue: {}'.format(menorValorArgos+1))

#PUNTO 3
# Accion con mayor valor de cierre.
def mayorValorCierre(Vector):
    Mayor = Vector[0]
    diaMayor = 0    
    for j in range(len(Vector)):
        if Mayor < Vector[j]:
            Mayor = Vector[j]
            diaMayor = j
    return diaMayor

M = M.T
#print(M)
for i in range(len(M)):
    mayorAccionPorDia = mayorValorCierre(M[i][:])
    print('La acción al final del día {} mayor fue: {}'.format(i+1,VectorAcciones[mayorAccionPorDia]))
    
#PUNTO 4
# Comparar el dia 1 con el ultimo dia y decir si se valorizó o se devaluo
def valorizacionMatriz(Vector):
    diferencia = abs(Vector[0] - Vector[len(Vector)-1])
    if Vector[0] > Vector[len(Vector)-1]:
        mensaje = 'DEVALUADA'
    elif Vector[0] < Vector[len(Vector)-1]:
        mensaje = 'VALORIZADA'
    else:
        mensaje = 'ESTABLE'
    return mensaje,diferencia
    
M = M.T
print(M)
for i in range(len(M)):
    valorizacion,cambioValor = valorizacionMatriz(M[i][:])
    print('Segun su comportamiento en el mes, la accion {} está: {}, con un valor de: {}'.format(VectorAcciones[i],valorizacion,cambioValor))
    
    

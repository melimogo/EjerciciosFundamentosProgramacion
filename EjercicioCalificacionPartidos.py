# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:50:35 2018

@author: USUARIO
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:57:12 2018

@author: USUARIO
"""

import numpy as np

n = int(input('Ingrese el numero de partidos y regiones'))
print(n+n)

M = np.zeros((n,n))

#Punto A
def llenar_Matriz(Matriz):
    n = len(Matriz)
    for i in range(n):
        for j in range(n):
            Matriz[i][j] = input('Para la region {} y el partido {}, ingrese el número de votos '.format(i,j))
    
    return Matriz
    

print('\n PUNTO a \n')

M = llenar_Matriz(M)
print('La nueva matriz es:')
print(M)

#Punto B

def Votos_de_cada_partido(vector):
    n = len(vector)
    suma = 0
    for i in range(n):
        suma = suma + vector[i]
    mensaje = 'El total de votos del partido {} es: {}'.format(j,suma)
    return mensaje        

print('\n PUNTO b \n')
M = M.T
for j in range(n):
    
    Mensaje_votos = Votos_de_cada_partido(M[:][j])
    
    print(Mensaje_votos)



# Punto C
def Votos_de_cada_region(vector):
    n = len(vector)
    suma = 0
    for j in range(n):
        suma = suma + vector[j]
    mensaje = 'El total de votos por región {} es: {}'.format(i,suma)
    return mensaje

M = M.T
print('\n PUNTO C \n')
for i in range(n):
    Mensaje_region = Votos_de_cada_region(M[:][i])
    print(Mensaje_region)



# Punto D
def partido_con_mayor_cantidad_de_votos_de_cada_region(vector):
    n = len(vector)
    Partido = 0
    Mayor = vector[0]
    for j in range(n):
        if Mayor < vector[j]:
            Mayor = vector[j]
            Partido = j
    mensaje = 'El partido con mayor cantidad de votos de la región {} es: {}'.format(i,Partido)
    return mensaje

print('\n PUNTO D \n')
for i in range(n):
    Mensaje_mayor = partido_con_mayor_cantidad_de_votos_de_cada_region(M[i][:])
    print(Mensaje_mayor)


# Punto e
def promedios_de_votos_de_cada_region(vector):
    n = len(vector)
    suma = 0
    for j in range(n):
        suma = suma + vector[j]
    mensaje = 'El promedio de votos por la región {} es: {}'.format(i,suma/n)
    return mensaje

print('\n PUNTO e \n')
for i in range(n):
    Mensaje_votos_region = promedios_de_votos_de_cada_region(M[i][:])
    print(Mensaje_votos_region)



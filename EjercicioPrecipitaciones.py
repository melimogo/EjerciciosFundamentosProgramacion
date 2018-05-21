# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:14:21 2018

@author: USUARIO
"""

import numpy as np
#import math

mediciones= np.array([[4.6,5.0,3.2,1.3,1.7,0.7,0.0,1.1,0.4,2.8],
    [3.0,5.1,3.3,2.3,1.7,0.8,0.0,2.0,0.5,2.9], 
    [0.0,4.2,3.4,1.5,2.7,0.9,1.0,1.4,0.6,2.1],
    [0.0,3.3,3.5,5.3,1.9,1.0,0.0,3.0,0.7,2.7], 
    [0.0,5.4,3.6,1.2,1.7,0.9,2.1,2.7,0.8,2.5], 
    [2.7,0.0,1.1,4.4,0.0,5.4,3.5,1.3,1.9,0.0],
    [1.8,0.8,0.0,2.0,0.5,1.2,1.7,1.3,2.1,1.2], 
    [0.4,1.2,0.0,1.1,0.4,0.0,5.6,5.3,3.5,1.3]])


dias = len(mediciones)
mediciones = mediciones.T
ciudades = len(mediciones)

#print(mediciones)

# PUNTO 1
def mayor_precipitacion(vector):
    longitud = len(vector)
    mayor = vector[1]
    VectorMayorPre = np.zeros(longitud)
    pos = 0
    for i in range(longitud):
        if vector[i] > mayor:
            mayor = vector[i]  
    for i in range(longitud):
        if mayor == vector[i]:
            VectorMayorPre[pos] = i
            pos = pos + 1
            
    return VectorMayorPre       
              
for i in range (0,8):
    VectorMayorPre = mayor_precipitacion(mediciones[:][i])
    print('los dias de mayor precipitación de la ciudad {} son: '.format(i))
    print(VectorMayorPre)

    
# PUNTO 2
def promedio_precipitacion(matriz,dias,ciudades):
    medio_prec = 0
    vector_precipitaciones_promedio = np.zeros(ciudades)
    for i in range(ciudades):
        suma = 0
        for j in range(dias):
            suma = suma + matriz[i][j]
        medio_prec = suma / j
        print('Las precipitaciones de la ciudad {} es: {} '.format(i,medio_prec))
        vector_precipitaciones_promedio[i] = medio_prec
    return vector_precipitaciones_promedio
        
    
print('\nPUNTO 2 \n')
vector_precipitaciones_promedio = promedio_precipitacion(mediciones,dias, ciudades)



#PUNTO 3
def dias_y_ciudades_mayores_promedio(matriz,dias,ciudades,vector_precipitaciones_promedio):
    promedio = promedio_general(vector_precipitaciones_promedio)
    for i in range(ciudades):
        for j in range(dias):
            if matriz[i][j] > promedio:
                print('El dia {}, en la ciudad {} las precipitaciones fueron: {}/{:.2f}'.format(j,i,matriz[i][j],promedio))
    
def promedio_general(vector):
    suma_promedios = 0
    for i in range(len(vector)):
        suma_promedios = suma_promedios + vector[i]
    return suma_promedios/i

print('\n \n PUNTO 3 \n')
dias_y_ciudades_mayores_promedio(mediciones,dias,ciudades,vector_precipitaciones_promedio)

# PUNTO 4
def ciudades_de_menores_precipitacion_por_dia(vector):

    longitud = len(vector)
    menor = vector[1]
    pos = 0
    menor_precipitacion = np.zeros(longitud)
    for i in range(longitud):
        if vector[i] < menor:
            menor = vector[i]
    for i in range(longitud):
        if vector[i] == menor:
            menor_precipitacion[pos] = i
            pos = pos + 1
            
    return menor_precipitacion

print('\n \n PUNTO 4 \n')
for i in range (0,8):
    mediciones = mediciones.T
    menor_precipitacion = ciudades_de_menores_precipitacion_por_dia(mediciones[i][:])
    print('las ciudades de menor precipitación el día {} son {} '.format(i,menor_precipitacion))
                
    







    


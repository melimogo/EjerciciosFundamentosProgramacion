# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:27:28 2018

@author: USUARIO
"""
import numpy as np

M = np.array([[123,3123412,234234,346000,123400,123412,34850],  
    [456,2523450,56346,346534,65200,75400,22560],
    [879,1254500,223000,12500,54000,78000,27845],
    [645,1875000,15200,178000,97500,263000,59000]])
#M = np.array([[500,200,300,180,220],[100,100,300,150,600],[300,400,900,550,804]])
 
Nombres = ['ID', 'Gastos', 'Rubia', 'Negra', 'Roja', 'Verde', 'Azul']
print(Nombres)
print(M)
fila = len(M)
Columna = len(M.T)


# Punto 1
def totalIngresosVentas(Matriz,fila,Columna):
    suma = 0
    for i in range(fila):
        for j in range(2,Columna):
            suma = suma + Matriz[i][j]
    return suma

totalIngresos = totalIngresosVentas(M,fila,Columna)
print('El total de ingresos del negocio es: {}'.format(totalIngresos))

# Punto 2
def totalGananciasPuntoVenta(Matriz,fila,Columna):
    ganacias = np.zeros(fila)
    for i in range(fila):
        suma = 0
        for j in range(2,Columna):
            suma = suma + Matriz[i][j]
        
        ganacias[i] = suma - Matriz[i][1]
    return ganacias

ganaciastotales = totalGananciasPuntoVenta(M,fila,Columna)
for i in range(len(M)):
    print('El total de ganancias para el punto de venta {} fueron de: {}'.format(M[i][0],ganaciastotales[i]))

# Punto 3
def cervezaMasVendida(Matriz,fila,Columna):
        mayor = 0
        cerveza = 0
        for i in range(2,Columna):
            suma = 0
            for j in range(fila):
                suma = suma + Matriz[i][j]
            
            if suma > mayor:
                mayor = suma
                cerveza = j
                
        return cerveza 
M = M.T
MayorCerveza = cervezaMasVendida(M,fila,Columna)
print('La cerveza mas vendida es: ',MayorCerveza)

# Punto 4
def MayoresPromedio(Matriz,fila,Columna):
    puntos = np.zeros(fila)
    suma = 0
    for i in range(fila):
        suma = suma + Matriz[i][1]
    promedio = suma/fila
    cont = 0
    for i in range(fila):
        if Matriz[i][1] > promedio:
            puntos[cont] = Matriz[i][0]
            cont = cont + 1
            
    return puntos
M = M.T
puntosVentas = MayoresPromedio(M,fila,Columna)
print('Los puntos en los cuales los gaston estan por encima del promedio son: ')
print(puntosVentas)



            
            
            
            
            
            
            
            
            
    
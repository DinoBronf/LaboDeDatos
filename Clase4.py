#Clase 4 Procesamiento de datos
import numpy as np
 #empleado_01 = np.array([[20222333,33456235,45432345],[45,40,41],[2,0,1],[20000,25000,10000]])
empleado_01 = np.array([[20222333,45,2,20000],[33456235,40,0,25000],[45432345,41,1,10000]])
#Actividad 1
def supSalarioAct1(empleado_01,x:int):
    matriz_nueva = []
    for filas in empleado_01:
            if filas[3] > x:
                matriz_nueva.append(filas)
            else:
                matriz_nueva = matriz_nueva
    return np.array(matriz_nueva)

#Actividad 2
empleado_02 = np.array([[20222333,45,2,20000],[33456235,40,0,25000],[45432345,41,1,10000],[43967304,37,0,12000],[42236276,36,0,18000]])
#Actividad 3
empleado_03 = np.array([[20222333,20000,45,2],[33456235,25000,40,0],[45432345,10000,41,1],[43967304,12000,37,0],[42236276,18000,36,0]])
def supSalarioAct3(empleado_03,x:int):
    matriz_nueva = []
    for filas in empleado_03:
            if filas[1] > x:
                fila_original = [filas[0],filas[2],filas[3],filas[1]]
                matriz_nueva.append(fila_original)
            else:
                matriz_nueva = matriz_nueva
    return np.array(matriz_nueva)
#Actividad 4
empleado_04 = np.array([[20222333,33456235,45432345,43967304,42236276],[20000,25000,10000,12000,18000],[45,40,41,37,36],[2,0,1,0,0]])
def supSalarioAct4(empleado_04,x:int):
    matriz_nueva = []
    for i in range(len(empleado_04[1])):
        if empleado_04[1][i] > x:
            fila_original = [columna[i] for columna in empleado_04]
            fila_original2 = [fila_original[0],fila_original[2],fila_original[3],fila_original[1]]
            matriz_nueva.append(fila_original2)
        else:
                matriz_nueva = matriz_nueva
    return np.array(matriz_nueva)

#Actividad 5
"""
1
a) el codigo no cambio
b) hubo que ajustar el indice del codigo
2
ajustar todo el codigo
3
no hay que ir cambiando el codigo todo el tiempo
"""




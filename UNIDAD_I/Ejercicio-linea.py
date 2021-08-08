import numpy as np
import matplotlib.pyplot as plt

N = 50 #Número de filas y columnas de la matriz (cuadrada)
matriz_linea = np.zeros((N,N))#creamos la matriz con ceros en todas las celdas
linea = [] #Lista en donde se insertarán las coordenadas de los pixeles a pintar con la siguiente forma [x,y] para la línea

def Bresenham_line(x0,y0,x1,y1):
    matriz_new = []
    dx = x1 -x0
    dy = y1-y0
    dos_dy = dy*2
    dos_dy_dif_dos_dx = dos_dy- (dx*2)
    p_0 = dos_dy-dx 
    x = x0
    y = y0
    matriz_new.append(x)
    matriz_new.append(y)
    linea.append(matriz_new)
    
    i = 0
    while (i<dx):
        if p_0 < 0 :
            matriz_new = []
            x+=1
            p_0+=dos_dy
        else:
            matriz_new = []
            x+=1
            y+=1
            p_0 += dos_dy_dif_dos_dx
        i+=1
        matriz_new.append(x)
        matriz_new.append(y)
        linea.append(matriz_new)
        
def imprimir_linea():
    for c in linea:
        matriz_linea[c[0],c[1]] = 1

    print(linea)
    plt.imshow(matriz_linea)
    plt.colorbar()
    plt.title("ALGORITMO")
    plt.show()

if __name__ == "__main__":
    #  datos de entrada
    Bresenham_line(2,3,15,2)
    imprimir_linea()

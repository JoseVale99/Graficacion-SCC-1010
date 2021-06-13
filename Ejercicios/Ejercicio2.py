import numpy as np
import matplotlib.pyplot as plt

N = 50 #Número de filas y columnas de la matriz (cuadrada)
matriz_circunferencia = np.zeros((N,N))#creamos la matriz con ceros en todas las celdas
circunferencia = [] #Lista en donde se insertarán las coordenadas de los pixeles a pintar con la siguiente forma [x,y] para la circunferencia
matriz_new = []

def Bresenham_circle(xc, yc,r):
	x = 0
	y = r
	p = 5/4-r

	while (x<=y):
		# Funcion para insertar los puntos
		dibujarPixel(x,y)
		# dibujarPixel(-x,y) 
		# dibujarPixel(x,-y)            
		# dibujarPixel( -x,-y) 			
		dibujarPixel(y,x)            
		# dibujarPixel( -y,x)    
		# dibujarPixel( y,-x)            
		# dibujarPixel( -y,-x) 
		
		if p<0:
			p += 2*(x+1)+1
			x+=1
		else:
			p += 2*(x+1)+1 - 2*(y-1)
			x +=1
			y -=1
		
def dibujarPixel(x,y):
	matriz_new = []
	matriz_new.append(x)
	matriz_new.append(y)
	circunferencia.append(matriz_new)  

def imprimir_circunferencia():
	print(circunferencia)
	for c in circunferencia:
		matriz_circunferencia[c[0],c[1]] = 1

	# Mostrar plot
	plt.imshow(matriz_circunferencia)
	plt.title("Algoritmo  de Bresenham para Circunferencias")
	plt.colorbar()
	plt.show()

if __name__ == "__main__":
    #  Bloque Principal
    Bresenham_circle(0,0,10)
    imprimir_circunferencia()
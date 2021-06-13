import numpy as np 
import matplotlib.pyplot as plt

x = []
y = []

#  Crear poligono 
def create_Polygon(n_lados,r):
    auxliar = (n_lados-2)/n_lados
    angulos = 0 
    theta = 180-(auxliar*180)
    radio = r
    
    angulos = theta
    i = 0
    while (i<n_lados):
        lado_x = radio*np.cos(np.radians(angulos))
        lado_y = radio*np.sin(np.radians(angulos))
        angulos+=theta
        i+=1
        if n_lados != 4:
            n1,n2 = rotate(lado_x,lado_y,90)
        else:
            n1,n2 = rotate(lado_x,lado_y,45)
        x.append(n1)
        y.append(n2)

def rotate(x,y,tetha):
    angulo = np.radians(tetha)
    return ( round(0 + (x - 0) * np.cos(angulo) - (y - 0) * np.sin(angulo)),
    round(0 + (y - 0) * np.cos(angulo) + (x - 0) * np.sin(angulo)))


#  Traslación
t_x = []
t_y = []
def get_Traslacion(x1,y1,x2,y2):
    px = x1 + x2
    py = y1 + y2
    t_x.append(px)
    t_y.append(py)
    return (px,py)

# ESCALADO
Escalado_x = []
Escalado_y = []

def getEscalado(x0,y0,x1,y1,ix,iy):
    px = x0 * x1 + (1 - x1) * (ix)
    py = y0 * y1 + (1 - y1) * (iy)
    Escalado_x.append(px)
    Escalado_y.append(py)
    return (px,py)

#   Rotacion 

rotacion_x = []
rotacion_y = []

def getRotacion(x,y,tetha, rx, ry):
    ang = np.radians(tetha)
    nx = round(rx + (x - rx) * np.cos(ang) - (y - ry) * np.sin(ang))
    ny = round(ry + (y - ry) * np.cos(ang) + (x - rx) * np.sin(ang))
    rotacion_x.append(nx)
    rotacion_y.append(ny)
    return nx,ny


def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    print ("1.  Crear poligono ")
    print ("2.  Traslacion ")
    print ("3.  Escalado ")
    print ("4.  Rotacion ")
    print ("5.  Salir ")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        n = int(input("Introduce lado del poligono: "))
        radio = int(input("Introduce el radio de la figura :"))
        create_Polygon(n,radio)
    elif opcion == 2:
        c_x,c_y= input("Introduce la coordenada de traslación en x,y").split(',')
        for t1,t2 in zip(x, y):
            get_Traslacion(t1,t2,int(c_x),int(c_y))
        plt.fill(t_x,t_y,color="blue")
    
    elif opcion == 3:
        x1,y1 = input("Introduce el vector de escalación x,y ").split('')
        x2,y2 = input("Introduce los puntos arbitrarios x,y").split('')
        
        for v1,v2 in zip(x,y):
            getEscalado(v1,v2,int(x1),int(y1), int(x2),int(y2))
        
        plt.fill(Escalado_x, Escalado_y, color='yellow', alpha=0.1)

        
    elif opcion == 4:
        grado = int(input("Introduce el angulo de rotación: "))
        px,py = input("Introduce los puntos arbitrarios x,y ").split(',')
        for v1,v2 in zip(x,y):
            nx,ny=getRotacion(v1,v2,grado, int(px),int(py))
        plt.fill(rotacion_x, rotacion_y, color='yellow', alpha=0.1)
    
    elif opcion ==5:
        salir = True
    
    else:
        print ("Introduce un numero entre 1 y 4")
    
    plt.fill(x,y,color="red") 
    plt.xlim(-80,80)
    plt.ylim(-80,80)
    plt.show()

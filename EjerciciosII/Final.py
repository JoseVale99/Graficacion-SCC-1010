import numpy as np 
import matplotlib.pyplot as plt

x = []
y = []

#  Crear poligono 
def create_Polygon(n_lados):
    auxliar = (n_lados-2)/n_lados
    angulos = 0 
    theta = 180-(auxliar*180)
    radio = 10
    
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

def View():
    # plt.style.use('dark_background')
    # FIGURA ORIGINAL
    plt.fill(x,y,color="red") 
    
    # FIGURA TRASLADADA

    # for t1,t2 in zip(x, y):
    #     get_Traslacion(t1,t2,10,14)
    # plt.fill(t_x,t_y,color="green")
   
    # FIGURA ESCALADA
    # for v1,v2 in zip(x,y):
    #     getEscalado(v1,v2,3,4, 0, 4)
    
    # plt.fill(Escalado_x, Escalado_y, color='purple', alpha=0.1)
    
    # Rotacion 
    for v1,v2 in zip(x,y):
        nx,ny=getRotacion(v1,v2,90, 10, 20)

    plt.fill(rotacion_x, rotacion_y, color='purple', alpha=0.1)




    
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    pkt.cla()
    plt.show()

if __name__ == "__main__":
    lados =  int(input("Introduce los lados: "))
    create_Polygon(lados)
    View()

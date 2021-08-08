import numpy as np 
import matplotlib.pyplot as plt

x = []
y = []

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

def show_Polygon():
    print("VALORES PARA X")
    print(x)
    print("VALORES Y")
    print(y)

    plt.style.use('dark_background')
    plt.fill(x,y,color="green")
    plt.xlim(-20,20)
    plt.ylim(-20,20)
    plt.show()

if __name__ == "__main__":
    # BLOQUE PRINCIPAL 
    print('POLIGONO ')
    lados =  int(input("Introduce los lados: "))
    create_Polygon(lados)
    show_Polygon()


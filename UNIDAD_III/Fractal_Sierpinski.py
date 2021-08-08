import matplotlib.pyplot as plt

# Función recursiva
def Sierpinski(coordenadas=[(0,0),(0.5,1),(1,0)],n=None):
    
    # detener la recursividad
    if n == 0:
        return
    
    # Las coordenadas tienen que seguir el orden de izquierda, media, derecha
    izq   = coordenadas [0]
    medio   = coordenadas [1]
    der = coordenadas [2]
    
    # Calculamos el punto medio  
    izq_nueva = ((medio[0]-izq[0])/2+izq[0],(medio[1]-izq[1])/2+izq[1])
    medio_new = ((der[0]-izq[0])/2+izq[0],(der[1]-izq[1])/2+izq[1])
    der_nueva = ((der[0]-medio[0])/2+medio[0],(medio[1]-der[1])/2+der[1])
     
    # Se realiza el plot 
    imprimir(coordenadas)

    # Los sub-triángulos de trama recursiva
    Sierpinski([izq,izq_nueva,medio_new],n-1)
    Sierpinski([izq_nueva,medio,der_nueva],n-1)
    Sierpinski([medio_new,der_nueva,der],n-1)

def imprimir(coordinates): # Función de impresión del resultado
    x = [] #Array para almacenar los valores en x de los elementos calculados
    y = [] #Array para almacenar los valores en y de los elementos calculados
    plt.style.use('dark_background')
    for i in coordinates:
        for j in coordinates:
            if i!=j:
                x.append([i[0],j[0]])   
                y.append([i[1],j[1]])
                plt.plot(x,y,'-',color='w')

if __name__ == "__main__": 
    n = int(input("Introduce el valor de  n: "))   
    Sierpinski(n=n)
    plt.show()
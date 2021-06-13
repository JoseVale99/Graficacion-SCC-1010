import matplotlib.pylab as plt

x = []
y = []

def Move(x1,y1,x2,y2):
    px = x1 + x2
    py = y1 + y2
    x.append(px)
    y.append(py)
    
    return (x1 + (x2),y1 + (y2))

def Show_Move(x1,y1, tx, ty):
    print('PUNTO DE TRASLACIÓN',tx,ty)
    for t1,t2 in zip(x1, y1):
        print(f'La traslación de las coordenadas: ({t1,t2}) es: {Move(t1,t2,tx,ty)}')
        plt.style.use('dark_background')
    plt.xlim(-50,50)
    plt.ylim(-50,50)   
    plt.fill(x1,y1,'#7FC080')
    plt.fill(x,y, '#FFF')
    plt.show()

if __name__ == "__main__":
    # BLOQUE PRINCIPAL
    

    Show_Move([-11, -11, 0, 11, 11, 0],[7, -6, -13, -7, 7, 13], 20, 10)





from matplotlib.pyplot import (plot,
show,style)


class DDA:
    
    def __init__(self):
        self.lista_x = []
        self.lista_y = []
    
    def Draw_line(self,x0, y0, x1, y1):
        dx = x1 - x0  
        dy = y1 - y0 

        if abs(dx) > abs(dy):
            n = abs(dx)
        else:
            n = abs(dy)
    
        incrementar_x = dx/n
        incrementar_y = dy/n
        x = x0
        y = y0
        print(dx,dy)
        i=0
        while i< int(n):
            x += incrementar_x
            y += incrementar_y
            self.lista_x.append(x)
            self.lista_y.append(y)
            i+=1
    
    def Show_graphic(self):
        # mostramos los puntos en consola para X y Y
        print("PUNTOS PARA X: ")
        print(self.lista_x)
        print("PUNTOS PARA Y: ")
        print(self.lista_y)
        
        style.use('dark_background')
        plot(self.lista_x,self.lista_y)
        show()

if __name__ == "__main__":
    line = DDA()
    line.Draw_line(1, 1, 7, 3)
    line.Show_graphic()
    
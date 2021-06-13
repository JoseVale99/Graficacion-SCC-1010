
from matplotlib.pyplot import plot, show, style,ylim,xlim


class BresenhamCircle:

    def __init__(self):
        self.list_x = []
        self.list_y = []
        self.list_p = []
    def DrawCircle(self,xc, yc,r):
        x = 0
        y = r 
        p = 5/4-r

        
        self.list_p.append(p)
        while (x<=y):
            print(f"{p}    ")
            self.dibujarPixel(x,y)            
            self.dibujarPixel(-x,y) 
            self.dibujarPixel(x,-y)            
            self.dibujarPixel( -x,-y) 			
            self.dibujarPixel(y,x)            
            self.dibujarPixel( -y,x)    
            self.dibujarPixel( y,-x)            
            self.dibujarPixel( -y,-x)   
            if p<0:
                p += 2*(x+1)+1
                x+=1 
                
            else:
                p += 2*(x+1)+1 - 2*(y-1)
                x +=1
                y = y-1
            self.list_p.append(p)

    def dibujarPixel(self, x,y):
        self.list_x.append(x)
        self.list_y.append(y)

    def show_plot(self):
        print("PUNTOS PARA X:")
        print(self.list_x)
        print("PUNTOS PARA Y:")
        print(self.list_y)

        style.use('dark_background')
        plot(self.list_x, self.list_y, '-o',
        #  self.list_p,self.list_p
        )
        show()   


if __name__ == "__main__":
    bresenham = BresenhamCircle()
    bresenham.DrawCircle(0,0,10)
    bresenham.show_plot()

"""
[0, 1, 2, 3, 4, 5, 6]
PUNTOS PARA Y:
[8, 8, 8, 7, 7, 6, 6]
"""
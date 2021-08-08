
from matplotlib.pyplot import plot, show, style 



class Bresenham:

    def __init__(self):
        self.list_x = []
        self.list_y = []
    
    def Draw_line(self, x0, y0,x1,y1):
        dx = x1 -x0
        dy = y1-y0
        dos_dy = dy*2
        dos_dy_dif_dos_dx = dos_dy- (dx*2)
        p_0 = dos_dy-dx 
        x = x0
        y = y0

        self.list_x.append(x)
        self.list_y.append(y)
        i = 0
        while (i<dx):
            if p_0 <0 :
                x+=1
                p_0+=dos_dy
            else:
                x+=1
                y+=1
                p_0 += dos_dy_dif_dos_dx
            i+=1
            self.list_x.append(x)
            self.list_y.append(y)
             

    def show_plot(self):
        print("PUNTOS PARA X:")
        print(self.list_x)
        print("PUNTOS PARA Y:")
        print(self.list_y) 

        style.use('dark_background')
        plot(self.list_x,self.list_y)
        show()   


if __name__ == "__main__":
    bresenham = Bresenham()
    bresenham.Draw_line(3,5,18,3)
    bresenham.show_plot()


"""
PUNTOS PARA X:
[0, 1, 2, 3, 4, 5, 6, 7, 8]
PUNTOS PARA Y:
[10, 10, 10, 10, 9, 9, 8, 8, 7]
"""
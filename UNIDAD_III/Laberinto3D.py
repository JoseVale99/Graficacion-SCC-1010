from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Laberinto:
    
    def __init__(self,x,y,cubo_tam=None, 
            cam_pos=None,
        mapa=None):
        self.x = x
        self.y = y
        self.cubo_tam = 2 #Tamaño del cubo para cada segmento de pared.
        self.cam_pos = [-30.0, -10.0, -90.0] # Posición inicial de la cámara después de dibujar el mapa.
        self.mapa =[  # Matriz de referencia para pintar el lab.
                [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1],
                [1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1],
                [1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1],
                [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1],
                [1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1],
                [1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1],
                [1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1],
                [1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1],
                [1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1],
                [1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1],
                [1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0],
                [1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1],
                [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
                [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ]

    def InitGL(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(30, float(self.x)/float(self.y), 1.1, 100.0)
        gluLookAt(-1, 10, 1,
                -1, 9, -1,
                0, 1, 0)
        glMatrixMode(GL_MODELVIEW)

    def getCubo(self):
        ''' DIBUJAR CUBO '''
        glBegin(GL_QUADS)
        
        glColor3f(0.0, 0.0, 0.5) # blue
        glVertex3f(-1.0, -1.0,  1.0)
        glVertex3f( 1.0, -1.0,  1.0)
        glVertex3f( 1.0,  1.0,  1.0)
        glVertex3f(-1.0,  1.0,  1.0)

        glColor4f(1.0, 0.5, 0.0, 0.0)#orange/brown           
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0,  1.0, -1.0)
        glVertex3f( 1.0,  1.0, -1.0)
        glVertex3f( 1.0, -1.0, -1.0)
                    
        glColor3f(0.0, 0.5, 1.0)#baby Blue
        glVertex3f(-1.0,  1.0, -1.0)
        glVertex3f(-1.0,  1.0,  1.0)
        glVertex3f( 1.0,  1.0,  1.0)
        glVertex3f( 1.0,  1.0, -1.0)
                    
        glColor3f(0.0, 0.0, 0.5) # blue
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f( 1.0, -1.0, -1.0)
        glVertex3f( 1.0, -1.0,  1.0)
        glVertex3f(-1.0, -1.0,  1.0)
                    
        
        glVertex3f( 1.0, -1.0, -1.0)
        glVertex3f( 1.0,  1.0, -1.0)
        glVertex3f( 1.0,  1.0,  1.0)
        glVertex3f( 1.0, -1.0,  1.0)
                    
        
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0,  1.0)
        glVertex3f(-1.0,  1.0,  1.0)
        glVertex3f(-1.0,  1.0, -1.0)
        glEnd()
                   
    def Draw_cubo(self): 
        '''Dibujamos el laberinto'''
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(11.0, -20.0, 0.0)
        glTranslatef(self.cam_pos[0],
                    self.cam_pos[1],
                    self.cam_pos[2])

        contador_colum = 0        
        for i in self.mapa:
            for j in i:
                if (j == 1):
                    self.getCubo()
                 # Mover de izq a der el tamaño de cubo.
                glTranslatef(self.cubo_tam, 0.0, 0.0)
                contador_colum += 1

            # Restablecer la posición antes de comenzar la siguiente fila 
            # mientras trasladamos cada cubo hacia la cámara.
            glTranslatef(((self.cubo_tam * contador_colum) * -1), 0.0, self.cubo_tam)
            # Restablecer el contador, para ser una nueva fila.
            contador_colum = 0

        glutSwapBuffers()

# BLOQUE PRINCIPAL
if __name__ == "__main__":
    laberinto = Laberinto(740,580)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(740,580)
    glutInitWindowPosition(200,200)
    window = glutCreateWindow('LABERINTO 3D')
    glutDisplayFunc(laberinto.Draw_cubo)
    glutIdleFunc(laberinto.Draw_cubo)
    laberinto.InitGL()
    glutMainLoop()

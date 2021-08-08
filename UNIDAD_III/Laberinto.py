from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


mapa = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # Matriz de referencia para pintar el lab.
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
              [0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0],
              [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
              [0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0],
              [0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0],
              [0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0],
              [0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0],
              [0,1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0],
              [0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,1,0],
              [0,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0],
              [0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0],
              [0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0],
              [0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0],
              [0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0],
              [0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0],
              [0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0],
              [0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0],
              [0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0],
              [0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() 
    gluPerspective(20, float(400)/float(400), 0.0, 100.0)
    gluLookAt(1, 2, 7,
                1, 1, -1,
                0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

def getSquare(x,y):
    glBegin(GL_QUADS)
    glVertex2f(x, y) 
    glVertex2f((x+0.1), y)
    glVertex2f((x+0.1), (y+0.1)) 
    glVertex2f(x, (y+0.1))
    glEnd() 


def drawSquare():
    x , y = 0.0 , 0.0
    glClear(GL_COLOR_BUFFER_BIT)
    
    for row in mapa:
        for col in row:
            if col == 1:
                getSquare(x,y)
                
            x +=0.1 
        x = 0.0
        y +=0.1
    glFlush()
        
  
  
# Inicializa OpenGL con exceso
glutInit()
# Modo de visualización: GLUT_SINGLE visualización directa sin búferGLUT_RGBA usa RGB (A no alfa)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# Posición de ventana y tamaño generado
glutInitWindowPosition(0, 0)
glutInitWindowSize(400, 400)
glutCreateWindow("Laberinto")
# Llama a la función para dibujar la imagen
glutDisplayFunc(drawSquare)
glutIdleFunc(drawSquare)
InitGL()
# Bucle principal
glutMainLoop()
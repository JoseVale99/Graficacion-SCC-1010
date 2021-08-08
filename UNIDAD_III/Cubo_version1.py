from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
 
DIRECTION = 4
def InitGL(Width, Height): 
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)   
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def cubo():     
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0) 
 
    glColor3f(1.0,0.0,0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0) 
 
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
 
    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)
 
    glColor3f(0.0,0.0,1.0)
    glVertex3f(-1.0, 1.0, 1.0) 
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0) 
    glVertex3f(-1.0,-1.0, 1.0) 
 
    glColor3f(1.0,0.0,1.0)
    glVertex3f( 1.0, 1.0,-1.0) 
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glEnd()

def showScreen(): 
    global X_AXIS,Y_AXIS,Z_AXIS
    global DIRECTION
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)
    
    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)
    cubo()
    
    X_AXIS = X_AXIS - 0.30
    Z_AXIS = Z_AXIS - 0.30
 
    glutSwapBuffers()
    
def main():
    glutInit() # Iniciamos la instancia de glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) # Asignamos el modelo de color que usaremos   
    glutInitWindowSize(640, 480)   # Damos el tamaño de la ventana que se mostrará  
    glutInitWindowPosition(200,200)   # Coordenadas en donde aparecerá la venta en la pantalla   
    wind = glutCreateWindow("Test OpenGL") # Damos un titulo para la ventana
    glutDisplayFunc(showScreen)  # Designamos la función que contiene los elemntos que serán mostrados en la escena 
    glutIdleFunc(showScreen)  
    InitGL(640, 480)   
    glutMainLoop()  # Iniciamos el loop principal

if __name__ == "__main__":
    main()
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Keyboard commands.
KEY_ESCAPE = b'\x1b'
KEY_FORWARD = b'w'
KEY_LEFT = b'a'
KEY_RIGHT = b'd'

window = 0

# Distance the camera moves during each step.
stepdistance = 0.5
# Size of cubes used to create wall segments.
cubesize = 2
# Initial camera position after map is drawn.
# camerapos = [-8.0, 0.0, -38.0]
camerapos = [-30.0, -10.0, -90.0] # coordenadas para la posicion de la camara
# Initial camera rotation.
camerarot = 0.0

# Loaded textures.
ceilingtexture = None
floortexture = None
walltexture = None

def initGL(Width, Height):

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(30.0, float(Width) / float(Height), 1.1, 100.0)
        gluLookAt(1, 10, 1,
                1, 9, -1,
                0, 1, 0)
        glMatrixMode(GL_MODELVIEW)

def drawScene():

        # Represents a top-down view of the maze.
        # 1 = wall
        # 0 = path
        # This could be built procedurally; hard-coded for now.
        map = [
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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()

        # Set up the current maze view.
        # Reset position to zero, rotate around y-axis, restore position.
        glTranslatef(12.0, -18.0, 5.0)
        #glTranslatef(10.0, -10.0, 0.0)
        # glRotatef(camerarot, -70.0, 70.0,1.0)
        glTranslatef(camerapos[0], camerapos[1], camerapos[2])

     
        

        # Build the maze like a printer; back to front, left to right.
        columncount = 0

        for i in map:
            for j in i:
                if (j == 1):
                    glBegin(GL_QUADS)
                    glColor3f(1.0,1.0,1.0)  # blanco
                    glVertex3f(-1.0, -1.0,  1.0);
                    glVertex3f( 1.0, -1.0,  1.0);
                    glVertex3f( 1.0,  1.0,  1.0);
                    glVertex3f(-1.0,  1.0,  1.0);

                    glColor4f(1.0,1.0,0.0,0.0)  # amarillo    
                    glVertex3f(-1.0, -1.0, -1.0);
                    glVertex3f(-1.0,  1.0, -1.0);
                    glVertex3f( 1.0,  1.0, -1.0);
                    glVertex3f( 1.0, -1.0, -1.0);
                    
                    glColor3f(0.0,0.0,1.0)  # azul
                    glVertex3f(-1.0,  1.0, -1.0);
                    glVertex3f(-1.0,  1.0,  1.0);
                    glVertex3f( 1.0,  1.0,  1.0);
                    glVertex3f( 1.0,  1.0, -1.0);

                    glVertex3f(-1.0, -1.0, -1.0);
                    glVertex3f( 1.0, -1.0, -1.0);
                    glVertex3f( 1.0, -1.0,  1.0);
                    glVertex3f(-1.0, -1.0,  1.0);
                    
                    glColor4f(1.0,0.0,0.0,0.0) # rojo
                    glVertex3f( 1.0, -1.0, -1.0);
                    glVertex3f( 1.0,  1.0, -1.0);
                    glVertex3f( 1.0,  1.0,  1.0);
                    glVertex3f( 1.0, -1.0,  1.0);
                    
                    
                    glVertex3f(-1.0, -1.0, -1.0);
                    glVertex3f(-1.0, -1.0,  1.0);
                    glVertex3f(-1.0,  1.0,  1.0);
                    glVertex3f(-1.0,  1.0, -1.0);
                    glEnd()

                # Move from left to right one cube size.
                glTranslatef(cubesize, 0.0, 0.0)

                columncount += 1

            # Reset position before starting next row, while moving
            # one cube size towards the camera.
            glTranslatef(((cubesize * columncount) * -1), 0.0, cubesize)
            # Reset the column count; this is a new row.
            columncount = 0

        glutSwapBuffers()

def handleKeypress(*args):

    global camerapos, camerarot

    if args[0] == KEY_ESCAPE:
        sys.exit()

    # Move forward relative to camera rotation.
    if args[0] == KEY_FORWARD:

        if (camerarot == 90):
            camerapos[0] -= stepdistance

        elif (camerarot == 180):
            camerapos[2] -= stepdistance

        elif (camerarot == 270):
            camerapos[0] += stepdistance

        else:
            camerapos[2] += stepdistance

    if args[0] == KEY_LEFT:
        camerarot -= 90.0

    if args[0] == KEY_RIGHT:
        camerarot += 90.0

    # Enforce minimum and maximum rotation.
    if (camerarot < 0):
        camerarot = 270

    if (camerarot > 270):
        camerarot = 0

def main():

        global window, ceilingtexture, floortexture, walltexture

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(200, 200)

        window = glutCreateWindow('Laberinto 3D')


        glutKeyboardFunc(handleKeypress)

        glutDisplayFunc(drawScene)
        glutIdleFunc(drawScene)
        initGL(640, 480)
        glutMainLoop()

if __name__ == "__main__":


        main()

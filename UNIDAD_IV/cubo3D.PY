from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

 
class Cubo():
	#  constructor
	def __init__(self, x,y,eje_x,eje_y,eje_z):
		self.x = x
		self.y = y
		self.eje_x = eje_x
		self.eje_y = eje_y
		self.eje_z = eje_z

	def InitGL(self):
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0) 
		glDepthFunc(GL_LESS)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_SMOOTH)   
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(60, float(self.x)/float(self.y), 0.1, 120.0)
		glMatrixMode(GL_MODELVIEW)

	def getCubo(self):
		''' DIBUJAR CUBO '''
		glBegin(GL_QUADS)
		
		glColor3f(0.0,1.0,0.0) #Green
		glVertex3f( 1.0, 1.0,-1.0)
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f( 1.0, 1.0, 1.0) 
		
		glColor4f(1.0, 0.0, 0.0, 0.0)#red
		glVertex3f( 1.0,-1.0, 1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f( 1.0,-1.0,-1.0) 
		
		glColor4f(1.0, 1.0, 0.0, 0.0)#yellow
		glVertex3f( 1.0, 1.0, 1.0)
		glVertex3f(-1.0, 1.0, 1.0)
		glVertex3f(-1.0,-1.0, 1.0)
		glVertex3f( 1.0,-1.0, 1.0)
		
		glColor3f(0.5,1.0,1.0)#cyan
		glVertex3f( 1.0,-1.0,-1.0)
		glVertex3f(-1.0,-1.0,-1.0)
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f( 1.0, 1.0,-1.0)
		
		glColor4f(1.0, 0.5, 0.0, 0.0)#orange/brown  
		glVertex3f(-1.0, 1.0, 1.0) 
		glVertex3f(-1.0, 1.0,-1.0)
		glVertex3f(-1.0,-1.0,-1.0) 
		glVertex3f(-1.0,-1.0, 1.0) 
		
		glColor3f(1.0,1.0, 1.0)#white
		glVertex3f( 1.0, 1.0,-1.0) 
		glVertex3f( 1.0, 1.0, 1.0)
		glVertex3f( 1.0,-1.0, 1.0)
		glVertex3f( 1.0,-1.0,-1.0)
		
		glEnd()

	def Draw_cubo(self):		
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glTranslatef(0.0,0.0,-6.0)
		glRotatef(self.eje_x,1.0,0.0,0.0)
		glRotatef(self.eje_y,0.0,1.0,0.0)
		glRotatef(self.eje_z,0.0,0.0,1.0)
		
		# Dibujar Cubo
		self.getCubo()
		
		self.eje_x += - 0.30
		self.eje_z += - 0.30
		glutSwapBuffers()

# BLOQUE PRINCIPAL
if __name__ == "__main__":
	cubo  = Cubo(740,580,0.0,0.0,0.0)
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(740,580)
	glutInitWindowPosition(200,200)
	window = glutCreateWindow('CUBO 3D')
	glutDisplayFunc(cubo.Draw_cubo)
	glutIdleFunc(cubo.Draw_cubo)
	cubo.InitGL()
	glutMainLoop()
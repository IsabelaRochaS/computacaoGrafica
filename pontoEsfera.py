from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos,sin,pi

raio=1
detalhamento = 40
pontos=[]

for i in range(0,detalhamento+1):
    theta = (i * pi / detalhamento)-(pi/2)
    for j in range(0,detalhamento+1):
        phi = (j * 2 * pi / detalhamento)
        pontos+=[[raio*cos(theta)*cos(phi),raio*sin(theta),raio*cos(theta)*sin(phi)]]
    

#cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def PontoEsfera():

    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    for ponto in pontos:
        glVertex3fv(ponto)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,0.9)
    for ponto in pontos:
        glVertex3fv(ponto)
    glEnd()

def Esfera():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,1,0)
    PontoEsfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(20,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera de pontos")
glutDisplayFunc(Esfera)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-6)
glRotatef(0,1,1,1)
glutTimerFunc(8,timer,1)
glutMainLoop()

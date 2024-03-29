from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0

texture = []

def LoadTextures():
    global texture
    texture = glGenTextures(2)

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='paperHouse.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,-0.7,-3.0)            

    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, texture[0])

    glBegin(GL_QUADS)              
    
    # Front Face 
    glTexCoord2f(0.2258, 1.0); glVertex3f(-1.0, 0.0,  0.5)    
    glTexCoord2f(0.7770, 1.0);  glVertex3f( 1.0, 0.0,  0.5)   
    glTexCoord2f(0.7770, 0.677); glVertex3f( 1.0,  1.0,  0.5)   
    glTexCoord2f(0.2258, 0.677); glVertex3f(-1.0,  1.0,  0.5)  
    
    # Right face
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0, 0.0, -0.5)    
    glTexCoord2f(1.0, 0.677); glVertex3f( 1.0,  1.0, -0.5)   
    glTexCoord2f(0.778, 0.677); glVertex3f( 1.0,  1.0,  0.5)     
    glTexCoord2f(0.778, 1.0); glVertex3f( 1.0, 0.0,  0.5)  

     # Left Face
    glTexCoord2f(0.003, 1.0); glVertex3f(-1.0, 0.0, -0.5)  
    glTexCoord2f(0.226, 0.995); glVertex3f(-1.0, 0.0,  0.5)    
    glTexCoord2f(0.226, 0.677); glVertex3f(-1.0,  1.0,  0.5)   
    glTexCoord2f(0.003, 0.677); glVertex3f(-1.0,  1.0, -0.5)
    
    # Back Face
    glTexCoord2f(0.230, 0.0); glVertex3f(-1.0, 0.0, -0.5)    
    glTexCoord2f(0.230, 0.320); glVertex3f(-1.0,  1.0, -0.5)   
    glTexCoord2f(0.7723, 0.320); glVertex3f( 1.0,  1.0, -0.5)    
    glTexCoord2f(0.7723, 0.0 ); glVertex3f( 1.0, 0.0, -0.5)
    
    # Telhado Frente
    glTexCoord2f(0.2296, 0.499); glVertex3f(-1.0,  1.5,  0.0)   
    glTexCoord2f(0.2296, 0.677); glVertex3f(-1.0,  1.0,  0.5)    
    glTexCoord2f(0.7703, 0.677); glVertex3f( 1.0,  1.0,  0.5)    
    glTexCoord2f(0.7703, 0.499); glVertex3f( 1.0,  1.5,  0.0) 
    
    # Telhado Outro
    glTexCoord2f(0.2296, 0.499); glVertex3f(-1.0,  1.5,  0.0)   
    glTexCoord2f(0.2296, 0.677); glVertex3f(-1.0,  1.0,  -0.5)    
    glTexCoord2f(0.7703, 0.677); glVertex3f( 1.0,  1.0,  -0.5)    
    glTexCoord2f(0.7703, 0.499); glVertex3f( 1.0,  1.5,  0.0) 

    glEnd()   
    
    glBegin( GL_TRIANGLES );

    glTexCoord2f( 0.0000, 0.677); glVertex3f( -1.0,  1.0,  0.5 );
    glTexCoord2f( 0.1168, 0.524); glVertex3f( -1.0, 1.5, 0.0 );
    glTexCoord2f( 0.2214, 0.677); glVertex3f( -1.0, 1.0, -0.5);
    
    glTexCoord2f( 0.0000, 0.677); glVertex3f( 1.0,  1.0,  0.5 );
    glTexCoord2f( 0.1168, 0.524); glVertex3f( 1.0, 1.5, 0.0 );
    glTexCoord2f( 0.2214, 0.677); glVertex3f( 1.0, 1.0, -0.5);


    glEnd() 
    
    xrot  = xrot + 0.0                # X rotation
    yrot = yrot + 0.2                 # Y rotation
    zrot = zrot + 0.0                 # Z rotation

    glutSwapBuffers()

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    # print "Hit ESC key to quit."
    main()

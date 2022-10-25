from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w,h= 500,500

xPosition = 0
yPosition = 0
xScale = 1
yScale = 1
rotate = 0

def bacgroun(num_segment):
    glColor(0, 165, 0)
    glBegin(GL_POLYGON)
    # glColor()
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 150 * math.cos(theta)
        y = 150 * math.sin(theta)
        glVertex2f(x + 0, y + 0)
    glEnd()
    #lingkaran ke2 warna putih
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = 125 * math.cos(theta)
        y = 125 * math.sin(theta)
        glVertex2f(x + 0, y + 0)
    glEnd()
    # circle tengah ke3 warna hijau
    glBegin(GL_POLYGON)
    glColor(0, 165, 0)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = 80 * math.cos(theta)
        y = 80 * math.sin(theta)
        glVertex2f(x + 0, y + 0)
    glEnd()
    # balok pemotong 
    glBegin(GL_QUADS)
    glColor(255, 255, 255)
    # glColor(0,170,1)
    glVertex2f(-35, -150)#kiri bawah
    glVertex2f(35, -150)#kana bawah
    glVertex2f(35, -120)#kiri atas
    glVertex2f(-35, -120)#kanan atas
    glEnd()
    # circle_a
    glBegin(GL_POLYGON)
    glColor(0,167,0)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = 12.5 * math.cos(theta)
        y = 12.5 * math.sin(theta)
        glVertex2f(x + -35, y + -133)
    glEnd()
    # circle b 
    glBegin(GL_POLYGON)
    glColor(0,167,0)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = 12.5 * math.cos(theta)
        y = 12.5 * math.sin(theta)
        glVertex2f(x + 35, y + -133 )
    glEnd()

def mySpecialKeyboard(key,x,y):
    
    global xPosition
    global yPosition
    global xScale
    global yScale
    if key == GLUT_KEY_LEFT:
        xPosition -= 100
    elif key == GLUT_KEY_RIGHT:
        xPosition += 100
    elif key == GLUT_KEY_UP:
        yPosition += 100
    elif key == GLUT_KEY_DOWN:
        yPosition -= 100
    elif key == GLUT_KEY_PAGE_UP:
        xScale += .1
        yScale += .1
    elif key == GLUT_KEY_PAGE_DOWN:
        if xScale < 0.2 and yScale < 0.2:
            xScale -= 0
            yScale -= 0
        else:
            xScale -= .1
            yScale -= .1

def myKeyboard(key, x, y):
    global rotate
    if key == b'.':
        rotate -= 10
    elif key == b',':
        rotate += 10

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    # glScale(100,100,1)
    glTranslate(100,100,0)
    # glRotatef(90,200,200,1)
    bacgroun(360)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(mySpecialKeyboard)
glutKeyboardFunc(myKeyboard)
glutMainLoop()
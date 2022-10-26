from tkinter import CENTER
from turtle import color
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w,h= 350,350

xPosition = 0
yPosition = 0
xScale = 1
yScale = 1
rotate = 0

def background():
    #membuat awan
    pass

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
    glViewport(0, 0, 300, 300)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300, 300, -300, 300, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    # GL_POSITION(CENTER)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0,167,1.0,1)
    # glback(0,167,0)
    glLoadIdentity()
    iterate()
    # glScale(100,100,1)
    # glTranslate(100,100,0)
    # glRotatef(90,200,200,1)
    # background()
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
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1360,1000

def arena_labirin():
    glBegin(GL_QUADS)#atas
    glVertex2f(150, 600)#kiri atas, kiri bawah
    glVertex2f(820, 600)#<=kanan bawah, kanan atas
    glVertex2f(820, 570)#<=kanan atas, kanan bawah
    glVertex2f(150, 570)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri1
    glVertex2f(180, 70)#kiri atas, kiri bawah
    glVertex2f(150, 70)#<=kanan bawah, kanan atas
    glVertex2f(150, 600)#<=kanan atas, kanan bawah
    glVertex2f(180, 600)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri2
    glVertex2f(270, 370)#kiri atas, kiri bawah
    glVertex2f(300, 370)#<=kanan bawah, kanan atas
    glVertex2f(300, 600)#<=kanan atas, kanan bawah
    glVertex2f(270, 600)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah_kiri2
    glVertex2f(150, 300)#kiri atas, kiri bawah
    glVertex2f(470, 300)#<=kanan bawah, kanan atas
    glVertex2f(470, 270)#<=kanan atas, kanan bawah
    glVertex2f(150, 270)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah_bawah_kiri2
    glVertex2f(150, 190)#kiri atas, kiri bawah
    glVertex2f(470, 190)#<=kanan bawah, kanan atas
    glVertex2f(470, 160)#<=kanan atas, kanan bawah
    glVertex2f(150, 160)#kiri bawah, kiri atas
    glEnd()

    # glBegin(GL_QUADS)#bawah_bawah_kiri2
    # glVertex2f(150, 300)#kiri atas, kiri bawah
    # glVertex2f(470, 300)#<=kanan bawah, kanan atas
    # glVertex2f(470, 270)#<=kanan atas, kanan bawah
    # glVertex2f(150, 270)#kiri bawah, kiri atas

def iterate():
    glViewport(0, 0, 1360, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1360, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glClearColor(255,255,255,0)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 0.0)
    arena_labirin()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1360, 695)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("LABMATH (LABIRIN MATHEMATIC)")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

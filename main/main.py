from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1360,1000

def arena_labirin():
    glBegin(GL_QUADS)#atas
    glVertex2f(150, 1600)#kiri atas, kiri bawah
    glVertex2f(1600, 1600)#<=kanan bawah, kanan atas
    glVertex2f(1600, 1570)#<=kanan atas, kanan bawah
    glVertex2f(150, 1570)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri1
    glVertex2f(180, 1600)#kiri atas, kiri bawah
    glVertex2f(150, 1600)#<=kanan bawah, kanan atas
    glVertex2f(150, 710)#<=kanan atas, kanan bawah
    glVertex2f(180, 710)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri2
    glVertex2f(270, 1600)#kiri atas, kiri bawah
    glVertex2f(300, 1600)#<=kanan bawah, kanan atas
    glVertex2f(300, 1150)#<=kanan atas, kanan bawah
    glVertex2f(270, 1150)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah_kiri2
    glVertex2f(150, 1060)#kiri atas, kiri bawah
    glVertex2f(500, 1060)#<=kanan bawah, kanan atas
    glVertex2f(500, 1030)#<=kanan atas, kanan bawah
    glVertex2f(150, 1030)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah_bawah_kiri2
    glVertex2f(150, 900)#kiri atas, kiri bawah
    glVertex2f(400, 900)#<=kanan bawah, kanan atas
    glVertex2f(400, 870)#<=kanan atas, kanan bawah
    glVertex2f(150, 870)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah_bawah_bawah_kiri2
    glVertex2f(150, 740)#kiri atas, kiri bawah
    glVertex2f(580, 740)#<=kanan bawah, kanan atas
    glVertex2f(580, 710)#<=kanan atas, kanan bawah
    glVertex2f(150, 710)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri3
    glVertex2f(580, 710)#kiri atas, kiri bawah
    glVertex2f(550, 710)#<=kanan bawah, kanan atas
    glVertex2f(550, 500)#<=kanan atas, kanan bawah
    glVertex2f(580, 500)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutan bawah_bawah_kiri2
    glVertex2f(550, 500)#kiri atas, kiri bawah
    glVertex2f(800, 500)#<=kanan bawah, kanan atas
    glVertex2f(800, 470)#<=kanan atas, kanan bawah
    glVertex2f(550, 470)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutan2 bawah_bawah_kiri2
    glVertex2f(550, 330)#kiri atas, kiri bawah
    glVertex2f(800, 330)#<=kanan bawah, kanan atas
    glVertex2f(800, 300)#<=kanan atas, kanan bawah
    glVertex2f(550, 300)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri4
    glVertex2f(550, 330)#kiri atas, kiri bawah
    glVertex2f(580, 330)#<=kanan bawah, kanan atas
    glVertex2f(580, 150)#<=kanan atas, kanan bawah
    glVertex2f(550, 150)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutan2 bawah_bawah_kiri2
    glVertex2f(550, 180)#kiri atas, kiri bawah
    glVertex2f(1500, 180)#<=kanan bawah, kanan atas
    glVertex2f(1500, 150)#<=kanan atas, kanan bawah
    glVertex2f(550, 150)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#atastengah
    glVertex2f(800, 1600)#kiri atas, kiri bawah
    glVertex2f(770, 1600)#<=kanan bawah, kanan atas
    glVertex2f(770, 1420)#<=kanan atas, kanan bawah
    glVertex2f(800, 1420)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutatastengah
    glVertex2f(550, 1420)#kiri atas, kiri bawah
    glVertex2f(800, 1420)#<=kanan bawah, kanan atas
    glVertex2f(800, 1390)#<=kanan atas, kanan bawah
    glVertex2f(550, 1390)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutatastengah2
    glVertex2f(550, 1260)#kiri atas, kiri bawah
    glVertex2f(800, 1260)#<=kanan bawah, kanan atas
    glVertex2f(800, 1230)#<=kanan atas, kanan bawah
    glVertex2f(550, 1230)#kiri bawah, kiri atas
    glEnd()

def iterate():
    glViewport(0, 0, 1360, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 2550, 0.0, 2300, 0.0, 1.0)
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
glutInitWindowSize(1360, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("LABMATH (LABIRIN MATHEMATIC)")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

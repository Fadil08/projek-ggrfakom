from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1360,1000

def arena_labirin():
    glBegin(GL_QUADS)#atas
    glVertex2f(150, 1660)#kiri atas, kiri bawah
    glVertex2f(1600, 1660)#<=kanan bawah, kanan atas
    glVertex2f(1600, 1630)#<=kanan atas, kanan bawah
    glVertex2f(150, 1630)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri1
    glVertex2f(180, 1660)#kiri atas, kiri bawah
    glVertex2f(150, 1660)#<=kanan bawah, kanan atas
    glVertex2f(150, 630)#<=kanan atas, kanan bawah
    glVertex2f(180, 630)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri2
    glVertex2f(330, 1660)#kiri atas, kiri bawah
    glVertex2f(360, 1660)#<=kanan bawah, kanan atas
    glVertex2f(360, 1142)#<=kanan atas, kanan bawah
    glVertex2f(330, 1142)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah1
    glVertex2f(150, 1000)#kiri atas, kiri bawah
    glVertex2f(560, 1000)#<=kanan bawah, kanan atas
    glVertex2f(560, 970)#<=kanan atas, kanan bawah
    glVertex2f(150, 970)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah2
    glVertex2f(150, 830)#kiri atas, kiri bawah
    glVertex2f(400, 830)#<=kanan bawah, kanan atas
    glVertex2f(400, 800)#<=kanan atas, kanan bawah
    glVertex2f(150, 800)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah3
    glVertex2f(150, 660)#kiri atas, kiri bawah
    glVertex2f(580, 660)#<=kanan bawah, kanan atas
    glVertex2f(580, 630)#<=kanan atas, kanan bawah
    glVertex2f(150, 630)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri3
    glVertex2f(580, 650)#kiri atas, kiri bawah
    glVertex2f(550, 650)#<=kanan bawah, kanan atas
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
    glVertex2f(700, 330)#<=kanan bawah, kanan atas
    glVertex2f(700, 300)#<=kanan atas, kanan bawah
    glVertex2f(550, 300)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri4
    glVertex2f(550, 330)#kiri atas, kiri bawah
    glVertex2f(580, 330)#<=kanan bawah, kanan atas
    glVertex2f(580, 150)#<=kanan atas, kanan bawah
    glVertex2f(550, 150)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah sendiri
    glVertex2f(550, 180)#kiri atas, kiri bawah
    glVertex2f(1500, 180)#<=kanan bawah, kanan atas
    glVertex2f(1500, 150)#<=kanan atas, kanan bawah
    glVertex2f(550, 150)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#atastengah
    glVertex2f(800, 1660)#kiri atas, kiri bawah
    glVertex2f(770, 1660)#<=kanan bawah, kanan atas
    glVertex2f(770, 1470)#<=kanan atas, kanan bawah
    glVertex2f(800, 1470)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutatastengah
    glVertex2f(485, 1500)#kiri atas, kiri bawah
    glVertex2f(800, 1500)#<=kanan bawah, kanan atas
    glVertex2f(800, 1470)#<=kanan atas, kanan bawah
    glVertex2f(485, 1470)#kiri bawah, kiri atas
    glEnd()


    glBegin(GL_QUADS)#lanjutan bawah1
    glVertex2f(550, 1000)#kiri atas, kiri bawah
    glVertex2f(580, 1000)#<=kanan bawah, kanan atas
    glVertex2f(580, 800)#<=kanan atas, kanan bawah
    glVertex2f(550, 800)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#atas ke 2
    glVertex2f(515, 1332)#kiri atas, kiri bawah
    glVertex2f(800, 1332)#<=kanan bawah, kanan atas
    glVertex2f(800, 1302)#<=kanan atas, kanan bawah
    glVertex2f(515, 1302)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#penghubung 2,3
    glVertex2f(485, 1332)#kiri atas, kiri bawah
    glVertex2f(515, 1332)#<=kanan bawah, kanan atas
    glVertex2f(515, 1142)#<=kanan atas, kanan bawah
    glVertex2f(485, 1142)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#atas ke 3
    glVertex2f(515, 1172)#kiri atas, kiri bawah
    glVertex2f(930, 1172)#<=kanan bawah, kanan atas
    glVertex2f(930, 1142)#<=kanan atas, kanan bawah
    glVertex2f(515, 1142)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#Tengah1
    glVertex2f(720, 1000)#kiri atas, kiri bawah
    glVertex2f(1250, 1000)#<=kanan bawah, kanan atas
    glVertex2f(1250, 970)#<=kanan atas, kanan bawah
    glVertex2f(720, 970)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutan atas ke 3
    glVertex2f(930, 1172)#kiri atas, kiri bawah
    glVertex2f(960, 1172)#<=kanan bawah, kanan atas
    glVertex2f(960, 970)#<=kanan atas, kanan bawah
    glVertex2f(930, 970)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanannya penghubung 2,3
    glVertex2f(1080, 1332)#kiri atas, kiri bawah
    glVertex2f(1110, 1332)#<=kanan bawah, kanan atas
    glVertex2f(1110, 1142)#<=kanan atas, kanan bawah
    glVertex2f(1080, 1142)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanannya atas ke 2
    glVertex2f(930, 1332)#kiri atas, kiri bawah
    glVertex2f(1110, 1332)#<=kanan bawah, kanan atas
    glVertex2f(1110, 1302)#<=kanan atas, kanan bawah
    glVertex2f(930, 1302)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#atasnya tengah 1
    glVertex2f(930, 1500)#kiri atas, kiri bawah
    glVertex2f(1110, 1500)#<=kanan bawah, kanan atas
    glVertex2f(1110, 1470)#<=kanan atas, kanan bawah
    glVertex2f(930, 1470)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawah tengah 1
    glVertex2f(1080, 1000)#kiri atas, kiri bawah
    glVertex2f(1110, 1000)#<=kanan bawah, kanan atas
    glVertex2f(1110, 315)#<=kanan atas, kanan bawah
    glVertex2f(1080, 315)#kiri bawah, kiri atas
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

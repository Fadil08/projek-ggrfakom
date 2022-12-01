from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1360,1000

def arena_labirin():
    glBegin(GL_QUADS)#atas
    glVertex2f(150, 1660)#kiri atas, kiri bawah
    glVertex2f(1570, 1660)#<=kanan bawah, kanan atas
    glVertex2f(1570, 1630)#<=kanan atas, kanan bawah
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

    glBegin(GL_QUADS)#atasnya lagi bawah sendiri
    glVertex2f(550, 500)#kiri atas, kiri bawah
    glVertex2f(950, 500)#<=kanan bawah, kanan atas
    glVertex2f(950, 470)#<=kanan atas, kanan bawah
    glVertex2f(550, 470)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#atasnya bawah sendiri kiri
    glVertex2f(550, 330)#kiri atas, kiri bawah
    glVertex2f(750, 330)#<=kanan bawah, kanan atas
    glVertex2f(750, 300)#<=kanan atas, kanan bawah
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
    glVertex2f(1810, 180)#<=kanan bawah, kanan atas
    glVertex2f(1810, 150)#<=kanan atas, kanan bawah
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
    glVertex2f(1110, 310)#<=kanan atas, kanan bawah
    glVertex2f(1080, 310)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kiri5
    glVertex2f(720, 840)#kiri atas, kiri bawah
    glVertex2f(750, 840)#<=kanan bawah, kanan atas
    glVertex2f(750, 630)#<=kanan atas, kanan bawah
    glVertex2f(720, 630)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutan kiri 5
    glVertex2f(720, 860)#kiri atas, kiri bawah
    glVertex2f(950, 860)#<=kanan bawah, kanan atas
    glVertex2f(950, 830)#<=kanan atas, kanan bawah
    glVertex2f(720, 830)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#mirror kiri 5
    glVertex2f(920, 730)#kiri atas, kiri bawah
    glVertex2f(950, 730)#<=kanan bawah, kanan atas
    glVertex2f(950, 630)#<=kanan atas, kanan bawah
    glVertex2f(920, 630)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)# bawah mirror kiri 5
    glVertex2f(920, 500)#kiri atas, kiri bawah
    glVertex2f(950, 500)#<=kanan bawah, kanan atas
    glVertex2f(950, 310)#<=kanan atas, kanan bawah
    glVertex2f(920, 310)#kiri bawah, kiri atas
    glEnd()
    
    glBegin(GL_QUADS)#tengah2
    glVertex2f(1270, 1337)#kiri atas, kiri bawah
    glVertex2f(1240, 1337)#<=kanan bawah, kanan atas
    glVertex2f(1240, 835)#<=kanan atas, kanan bawah
    glVertex2f(1270, 835)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#ataskanan
    glVertex2f(1270, 1660)#kiri atas, kiri bawah
    glVertex2f(1240, 1660)#<=kanan bawah, kanan atas
    glVertex2f(1240, 1470)#<=kanan atas, kanan bawah
    glVertex2f(1270, 1470)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutataskanan
    glVertex2f(1240, 1500)#kiri atas, kiri bawah
    glVertex2f(1430, 1500)#<=kanan bawah, kanan atas
    glVertex2f(1430, 1470)#<=kanan atas, kanan bawah
    glVertex2f(1240, 1470)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#lanjutataskanan2
    glVertex2f(1430, 1490)#kiri atas, kiri bawah
    glVertex2f(1400, 1490)#<=kanan bawah, kanan atas
    glVertex2f(1400, 475)#<=kanan atas, kanan bawah
    glVertex2f(1430, 475)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawahtengah2
    glVertex2f(1240, 720)#kiri atas, kiri bawah
    glVertex2f(1430, 720)#<=kanan bawah, kanan atas
    glVertex2f(1430, 690)#<=kanan atas, kanan bawah
    glVertex2f(1240, 690)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawahtengah3
    glVertex2f(1240, 590)#kiri atas, kiri bawah
    glVertex2f(1430, 590)#<=kanan bawah, kanan atas
    glVertex2f(1430, 560)#<=kanan atas, kanan bawah
    glVertex2f(1240, 560)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawahtengah4
    glVertex2f(1090, 430)#kiri atas, kiri bawah
    glVertex2f(1270, 430)#<=kanan bawah, kanan atas
    glVertex2f(1270, 400)#<=kanan atas, kanan bawah
    glVertex2f(1090, 400)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#atas bawah sendiri kanan
    glVertex2f(1270, 340)#kiri atas, kiri bawah
    glVertex2f(1830, 340)#<=kanan bawah, kanan atas
    glVertex2f(1830, 310)#<=kanan atas, kanan bawah
    glVertex2f(1270, 310)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawahtengah6
    glVertex2f(1270, 430)#kiri atas, kiri bawah
    glVertex2f(1240, 430)#<=kanan bawah, kanan atas
    glVertex2f(1240, 310)#<=kanan atas, kanan bawah
    glVertex2f(1270, 310)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawahtengah7
    glVertex2f(1400, 490)#kiri atas, kiri bawah
    glVertex2f(1570, 490)#<=kanan bawah, kanan atas
    glVertex2f(1570, 460)#<=kanan atas, kanan bawah
    glVertex2f(1400, 460)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#bawahtengah8
    glVertex2f(1570, 585)#kiri atas, kiri bawah
    glVertex2f(1540, 585)#<=kanan bawah, kanan atas
    glVertex2f(1540, 470)#<=kanan atas, kanan bawah
    glVertex2f(1570, 470)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanan3
    glVertex2f(1570, 1660)#kiri atas, kiri bawah
    glVertex2f(1540, 1660)#<=kanan bawah, kanan atas
    glVertex2f(1540, 1150)#<=kanan atas, kanan bawah
    glVertex2f(1570, 1150)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanantengah1
    glVertex2f(1570, 1000)#kiri atas, kiri bawah
    glVertex2f(1540, 1000)#<=kanan bawah, kanan atas
    glVertex2f(1540, 835)#<=kanan atas, kanan bawah
    glVertex2f(1570, 835)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanantengah2
    glVertex2f(1540, 1000)#kiri atas, kiri bawah
    glVertex2f(1700, 1000)#<=kanan bawah, kanan atas
    glVertex2f(1700, 970)#<=kanan atas, kanan bawah
    glVertex2f(1540, 970)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanantengah3
    glVertex2f(1540, 870)#kiri atas, kiri bawah
    glVertex2f(1700, 870)#<=kanan bawah, kanan atas
    glVertex2f(1700, 835)#<=kanan atas, kanan bawah
    glVertex2f(1540, 835)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanantengah4
    glVertex2f(1540, 720)#kiri atas, kiri bawah
    glVertex2f(1670, 720)#<=kanan bawah, kanan atas
    glVertex2f(1670, 690)#<=kanan atas, kanan bawah
    glVertex2f(1540, 690)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#mirrorbawahtengahkanan
    glVertex2f(1700, 720)#kiri atas, kiri bawah
    glVertex2f(1670, 720)#<=kanan bawah, kanan atas
    glVertex2f(1670, 460)#<=kanan atas, kanan bawah
    glVertex2f(1700, 460)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#mirrorkeatasbawahtengahkanan
    glVertex2f(1700, 1340)#kiri atas, kiri bawah
    glVertex2f(1670, 1340)#<=kanan bawah, kanan atas
    glVertex2f(1670, 970)#<=kanan atas, kanan bawah
    glVertex2f(1700, 970)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#palingkananatas
    glVertex2f(1670, 1360)#kiri atas, kiri bawah
    glVertex2f(1820, 1360)#<=kanan bawah, kanan atas
    glVertex2f(1820, 1330)#<=kanan atas, kanan bawah
    glVertex2f(1670, 1330)#kiri bawah, kiri atas
    glEnd()

    glBegin(GL_QUADS)#kanan pass
    glVertex2f(1830, 1360)#kiri atas, kiri bawah
    glVertex2f(1800, 1360)#<=kanan bawah, kanan atas
    glVertex2f(1800, 150)#<=kanan atas, kanan bawah
    glVertex2f(1830, 150)#kiri bawah, kiri atas
    glEnd()

def tamiya(x,y):
    glColor3ub(150, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(8+x, 38+y)
    glVertex2f(6+x, 38+y)
    glVertex2f(8+x, 40+y)
    glVertex2f(10+x, 42+y)
    glVertex2f(20+x, 42+y)
    glVertex2f(22+x, 40+y)
    glVertex2f(24+x, 38+y)
    glVertex2f(22+x, 38+y)
    glEnd()

    glColor3ub(145, 142, 142)
    glBegin(GL_POLYGON)
    glVertex2f(8+x, 38+y)
    glVertex2f(22+x, 38+y)
    glVertex2f(20+x, 36+y)
    glVertex2f(10+x, 36+y)
    glEnd()

    glColor3ub(145, 142, 142)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 36+y)
    glVertex2f(20+x, 36+y)
    glVertex2f(20+x, 30+y)
    glVertex2f(10+x, 30+y)
    glEnd()

    glColor3ub(145, 142, 142)
    glBegin(GL_POLYGON)
    glVertex2f(20+x, 30+y)
    glVertex2f(10+x, 30+y)
    glVertex2f(10+x, 20+y)
    glVertex2f(20+x, 20+y)
    glEnd()

    glColor3ub(0, 30, 180)
    glBegin(GL_POLYGON)
    glVertex2f(20+x, 20+y)
    glVertex2f(24+x, 16+y)
    glVertex2f(24+x, 10+y)
    glVertex2f(22+x, 10+y)
    glVertex2f(22+x, 16+y)
    glVertex2f(20+x, 18+y)
    glEnd()

    glColor3ub(0, 30, 180)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 20+y)
    glVertex2f(6+x, 16+y)
    glVertex2f(6+x, 10+y)
    glVertex2f(8+x, 10+y)
    glVertex2f(8+x, 16+y)
    glVertex2f(10+x, 18+y)
    glEnd()

    glColor3ub(218,165,32)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 20+y)
    glVertex2f(10+x, 18+y)
    glVertex2f(10+x, 12+y)
    glVertex2f(12+x, 14+y)
    glVertex2f(12+x, 18+y)
    glEnd()

    glColor3ub(218,165,32)
    glBegin(GL_POLYGON)
    glVertex2f(10+x, 20+y)
    glVertex2f(12+x, 18+y)
    glVertex2f(18+x, 18+y)
    glVertex2f(20+x, 20+y)
    glEnd()

    glColor3ub(218,165,32)
    glBegin(GL_POLYGON)
    glVertex2f(20+x, 20+y)
    glVertex2f(20+x, 18+y)
    glVertex2f(20+x, 12+y)
    glVertex2f(18+x, 14+y)
    glVertex2f(18+x, 18+y)
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
    tamiya(100,150)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1360, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("LABMATH (LABIRIN MATHEMATIC)")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

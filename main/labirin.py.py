from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w,h= 1200,600
play = False
x= 510
y=250


def halaman():
    # glColor3f(0,1,1)
    glBegin(GL_QUADS)
    glColor3ub(207, 63, 10)
    glVertex2f(0,0)
    glVertex2f(1500,0)
    glVertex2f(1500,50)
    glVertex2f(0, 50)
    glEnd()

    glBegin(GL_QUADS)
    glColor(0,167,0)
    glVertex2f(0,50)
    glVertex2f(1200,50)
    glVertex2f(1200,75)
    glVertex2f(0,75)
    glEnd()


def backgroun_splash():
    glBegin(GL_POLYGON)
    glColor3ub(105, 200, 255)
    glVertex2f(0,0)
    glVertex2f(1200,0)
    glVertex2f(1200,600)
    glVertex2f(0,600)
    glEnd()

    # awan kiri
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 150, y + 400 )
    glEnd()
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 175, y + 400 )
    glEnd()

    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 200, y + 400 )
    glEnd()

    # awan tengah
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 500, y + 450 )
    glEnd()

    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 525, y + 450 )
    glEnd()

    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 550, y + 450 )
    glEnd()
    # awan kanan
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 850, y + 400 )
    glEnd()
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 875, y + 400 )
    glEnd()
    glBegin(GL_POLYGON)
    glColor(255,255,255)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 25 * math.cos(theta)
        y = 25 * math.sin(theta)
        glVertex2f(x + 900, y + 400 )
    glEnd()
def rumah():

    glBegin(GL_QUADS)
    # glColor3f(0.5, 0.5, 0.5)
    glColor3ub(47,79,79)
    glVertex2f(350,80)
    glVertex2f(700,80)
    glVertex2f(700,100)
    glVertex2f(350, 100)
    glEnd()

    # bagan ceronon asap 
    glBegin(GL_QUADS)
    glColor(0,0,0)
    glVertex2f(440,290)
    glVertex2f(460,307)
    glVertex2f(460,325)
    glVertex2f(440, 325)
    glEnd()

    # atap cerobong
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(430,325)
    glVertex2f(470,325)
    glVertex2f(470,330)
    glVertex2f(430, 330)
    glEnd()
    

    #bagan rumah
    glBegin(GL_POLYGON)
    glColor(0,0,1)
    glVertex2f(525, 350)
    glVertex2f(400, 250)
    glVertex2f(400,100)
    glVertex2f(650,100)
    glVertex2f(650,250)
    glEnd()

    #atap kiri 
    glBegin(GL_QUADS)
    glColor3ub(207, 63, 10)
    glVertex2f(390,250)
    glVertex2f(400,250)
    glVertex2f(525,350)
    glVertex2f(525, 360)
    glEnd()


    #atap kanan 
    glBegin(GL_QUADS)
    glColor3ub(207, 63, 10)
    glVertex2f(660,250)
    glVertex2f(650,250)
    glVertex2f(525,350)
    glVertex2f(525, 360)
    glEnd()

    #tangga1
    glBegin(GL_QUADS)
    glColor(255,255,255)
    glVertex2f(540,100)
    glVertex2f(620,100)
    glVertex2f(620,110)
    glVertex2f(540, 110)
    glEnd()

    #lantai2
    glBegin(GL_QUADS)
    glColor(0,0,0)
    glVertex2f(550, 110)
    glVertex2f(610,110)
    glVertex2f(610,120)
    glVertex2f(550,120)
    glEnd()
    #pintu
    glBegin(GL_QUADS)
    glColor3ub(238,118,0)
    glVertex2f(555,120)
    glVertex2f(605,120)
    glVertex2f(605,210)
    glVertex2f(555, 210)
    glEnd()
    # pegangan pintu
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 5 * math.cos(theta)
        y = 5 * math.sin(theta)
        glVertex2f(x + 560, y + 165 )
    glEnd()
    # membuat jendela
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.10)
    glVertex2f(430,180)
    glVertex2f(480,180)
    glVertex2f(480,230)
    glVertex2f(430,230)
    glEnd()


    # line atap rumah
    glBegin(GL_LINE_STRIP)
    glColor(0,0,0)
    glVertex2f(400,250)
    glVertex2f(390,250)
    glVertex2f(525, 360)
    glVertex2f(660,250)
    glVertex2f(650,250)
    glEnd()
    # line jendela
    glBegin(GL_LINE_STRIP)
    glColor(255,255,255)
    glVertex2f(480,180)
    glVertex2f(480,230)
    glVertex2f(430,230)
    glVertex2f(430,180)
    glVertex2f(480,180)
    glVertex2f(455,180)
    glVertex2f(455,230)
    glVertex2f(455,210)
    glVertex2f(480,210)
    glEnd()
def labirin():
    # background
    glBegin(GL_QUADS)
    glColor3f(1,1,0.5)
    glVertex2f(0,0)
    glVertex2f(1200,0)
    glVertex2f(1200,600)
    glVertex2f(0,600)
    glEnd()
    # line melingkar kiri
    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glColor3ub(0,0,1)
    glVertex2f(450,200)
    glVertex2f(300,200)
    glVertex2f(300,300)
    glVertex2f(200,300)
    glVertex2f(200,550)
    glVertex2f(700,550)
    glVertex2f(700,450)
    glEnd()

    # line melingkar kanan
    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(750,350)
    glVertex2f(700,350)
    glVertex2f(700,400)
    glVertex2f(750,400)
    glVertex2f(750,500)
    glVertex2f(800,500)
    glVertex2f(800,50)
    glVertex2f(300,50)
    glVertex2f(300,150)
    glVertex2f(400,150)
    glEnd()

    # cabang1
    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(200,400)
    glVertex2f(300,400)
    glVertex2f(300,350)
    glEnd()

    # cabang2 dari kiri
    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(200,350)
    glVertex2f(250,350)
    glEnd()

    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(250,550)
    glVertex2f(250,450)
    glEnd()

    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(450,550)
    glVertex2f(450,500)
    glVertex2f(350,500)
    glEnd()

    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(550,500)
    glVertex2f(500,500)
    glEnd()

    # titik mulai v1
    glLineWidth(10.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(600,550)
    glVertex2f(600,500)
    glVertex2f(650,500)
    glVertex2f(650,300)
    glVertex2f(600,300)
    glVertex2f(650,300)
    glVertex2f(650,250)
    glVertex2f(600,250)
    glVertex2f(650,250)
    glVertex2f(650,200)
    glVertex2f(700,200)
    glVertex2f(700,250)
    glEnd()

    # glLineWidth(10.0)
    # titik mulai j1
    glBegin(GL_LINE_STRIP)
    glVertex2f(800,200)
    glVertex2f(750,200)
    glVertex2f(750,300)
    glVertex2f(700,300)
    glEnd()
    
    # titik mulai g1 
    glBegin(GL_LINE_STRIP)
    glVertex2f(800,100)
    glVertex2f(650,100)
    glEnd()
    # titik mulai i1 
    glBegin(GL_LINE_STRIP)
    glVertex2f(800,150)
    glVertex2f(600,150)
    glVertex2f(600,100)
    glVertex2f(500,100)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(600,150)
    glVertex2f(550,150)
    glVertex2f(550,200)
    glVertex2f(500,200)
    glVertex2f(500,150)
    glVertex2f(500,350)
    glVertex2f(450,350)
    glVertex2f(600,350)
    glVertex2f(600,450)
    glEnd()
    # mulai titik p2 
    glBegin(GL_LINE_STRIP)
    glVertex2f(500,350)
    glVertex2f(500,400)
    glVertex2f(350,400)
    glVertex2f(350,450)
    glVertex2f(450,450)
    glEnd()
    # mulai titik n2 
    glBegin(GL_LINE_STRIP)
    glVertex2f(550,400)
    glVertex2f(550,450)
    glVertex2f(500,450)
    glEnd()
    # mulai titik n
    glBegin(GL_LINE_STRIP)
    glVertex2f(450,150)
    glVertex2f(450,100)
    glVertex2f(400,100)
    glEnd()
    # mulai titik h3
    glBegin(GL_LINE_STRIP)
    glVertex2f(400,250)
    glVertex2f(400,300)
    glEnd()
    # mulai titik f3
    glBegin(GL_LINE_STRIP)
    glVertex2f(350,250)
    glVertex2f(350,350)
    glVertex2f(400,350)
    glEnd()
def drawBitmapText(string,x,y,z) :
    glRasterPos3f(x,y,z)
    for c in string :
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(c))
def drawBitmapTextstart(string,x,y,z) :
    glRasterPos3f(x,y,z)
    for c in string :
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(c))

def drawText():
    glColor3f(1,1,1)
    drawBitmapText("welcome labmath player",400,375,0)
    drawBitmapTextstart("Start",497,240,0)
def btnstart():
    glBegin(GL_QUADS)
    glColor3ub(0,255,0)
    glVertex2f(490,230)
    glVertex2f(490,260)
    glVertex2f(560,260)
    glVertex2f(560,230)
    glEnd()
    # kanan
    # glBegin(GL_POLYGON)
    # glColor3ub(0,255,0)
    # for i in range(360):
    #     theta= 2 *3.1415926*i/360
    #     x = 16 * math.cos(theta)
    #     y = 16 * math.sin(theta)
    #     glVertex2f(x + 553, y + 245.5 )
    # glEnd()
    # # kiri 
    # glBegin(GL_POLYGON)
    # glColor3ub(0,255,0)
    # for i in range(360):
    #     theta= 2 *3.1415926*i/360
    #     x = 16 * math.cos(theta)
    #     y = 16 * math.sin(theta)
    #     glVertex2f(x + 500, y + 245.5 )
    # glEnd()
def btnklik(button, state, x,y):
    global play
    if button == GLUT_LEFT_BUTTON:
        if (x >= 500 and x <=560) and (y >= 230 and y <= 260):
            play =True
def splaspage():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    backgroun_splash()
    halaman()
    rumah()
    btnstart()
    drawText()
    # btnklik()
    glLoadIdentity()
    glutSwapBuffers()
def iterate():
    glViewport(0, 0, 1200, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1200, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if play == False:
        splaspage()
    else:
        labirin()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("LabMath")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMouseFunc(btnklik)
    glutMainLoop()
main()
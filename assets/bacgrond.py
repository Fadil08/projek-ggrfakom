from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

w,h= 1200,600
play = False


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
    glVertex2f(500,260)
    glVertex2f(500,230)
    glVertex2f(560,230)
    glVertex2f(560,260)
    glEnd()
    # kanan
    glBegin(GL_POLYGON)
    glColor3ub(0,255,0)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 16 * math.cos(theta)
        y = 16 * math.sin(theta)
        glVertex2f(x + 553, y + 245.5 )
    glEnd()
    # kiri 
    glBegin(GL_POLYGON)
    glColor3ub(0,255,0)
    for i in range(360):
        theta= 2 *3.1415926*i/360
        x = 16 * math.cos(theta)
        y = 16 * math.sin(theta)
        glVertex2f(x + 500, y + 245.5 )
    glEnd()
# def btnklik(button, x,y,state):
#     global play
#     if button == GLUT_LEFT_BUTTON:
#         if (x >= 495 and x <=560) and (y >= 245 and y <= 260):
#             play =True
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
        pass
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("LabMath")
    glutDisplayFunc(splaspage)
    glutIdleFunc(splaspage)
    glutMainLoop()
main()

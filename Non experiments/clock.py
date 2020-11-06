from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time


def ROUND(a):
	return int(a+0.4)

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def setPixel(xcoordinate,ycoordinate):
	glColor3f(0.2,0.0,1.5)
	glPointSize(5.0)
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()

def circle():
    r = 130
    x = r
    y = 0
    x_centre = 0
    y_centre = 0
    setPixel(x+x_centre,-y+y_centre)
    setPixel(y+x_centre,x+y_centre)
    setPixel(y+x_centre,x+y_centre)
    setPixel(-y+x_centre,x+y_centre)
    while x >= y:
        x -= 0.01
        y = math.sqrt(r*r - x*x)
        setPixel(ROUND(x_centre + x), ROUND(y_centre + y))
        setPixel(ROUND(x_centre + y), ROUND(y_centre + x))
        setPixel(ROUND(x_centre + y), ROUND(y_centre - x))
        setPixel(ROUND(x_centre + x), ROUND(y_centre - y))
        setPixel(ROUND(x_centre - x), ROUND(y_centre - y))
        setPixel(ROUND(x_centre - y), ROUND(y_centre - x))
        setPixel(ROUND(x_centre - y), ROUND(y_centre + x))
        setPixel(ROUND(x_centre - x), ROUND(y_centre + y))


def setLines(x,y):
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x, y)
    glEnd()
    glFlush()
    glutSwapBuffers()

def hourHand():
    rhour = 116
    hour = time.strftime("%H")
    angleperhour = math.pi/2 - int(hour)*math.pi/12
    x=(rhour*math.cos(angleperhour))
    y=(rhour*math.sin(angleperhour))
    setLines(x,y)

def secHand():
    rsec = 124
    sec = time.strftime("%S")
    anglepersec = math.pi/2 - int(sec)*math.pi/30
    x=(rsec*math.cos(anglepersec))
    y=(rsec*math.sin(anglepersec))
    setLines(x,y)

def minHand():
    rmin = 100
    min  = time.strftime("%M")
    anglepermin = math.pi/2 - int(min)*math.pi/30
    x=(rmin*math.cos(anglepermin))
    y=(rmin*math.sin(anglepermin))
    setLines(x,y)

def display():
    circle()
    glColor3f(1.0,0.0,0.0)
    secHand()
    glColor3f(1.0,1.0,0.0)
    minHand()
    glColor3f(1.0,1.0,1.0)
    hourHand()
    glClear(GL_COLOR_BUFFER_BIT)

def timer(value):
    glutTimerFunc(33, timer, 0)
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow('clock')
    glutDisplayFunc(display)
    init()
    timer(0)
    glutMainLoop()
    #time.sleep(1)

main()
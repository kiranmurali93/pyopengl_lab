from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100,100,-100,100)

def setPixel(xcoordinate,ycoordinate):
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    x1=float(input('x1 coordinate: '))
    y1=float(input('y1 coordinate: '))
    x2=float(input('x2 coordinate: '))
    y2=float(input('y2 coordinate: '))
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if x2>x1:
        x,y,xend = x1,y1,x2
    else:
        x,y,xend = x2,y2,x1
    setPixel(x,y)
    p=2*dy-dx
    while x<xend:
        x+=1
        if p<0:
            p=p+2*dy
        else:
            y+=1
            p=p+2*dy-2*dx
        setPixel(x,y)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Line using Bresenham")
    glutDisplayFunc(Display)
    init()
    glutMainLoop()
main()
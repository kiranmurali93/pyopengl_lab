# Program for Mid-Point Line Drawing algorithm
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# For rounding pixels
def round(a):
    return int(a+0.5)

#Midpont Function
def midpoint():
    x1 = int(input('Enter the x1 point: '))
    y1 = int(input('Enter the y1 point: '))
    x2 = int(input('Enter the x2 point: '))
    y2 = int(input('Enter the y2 point: '))

    ## to find the midpoint
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    mid = dy - (dx/2)
    print('The plotted co-ordinates are: ')
    print("(",x,",",y,")")
    while(x < x2):
        x = x + 1
        if(mid < 0):
            mid = mid + dy
            print("(",x,y,")")
            plot(x,y)
        else:
            mid = mid + (dy - dx)
            y = y + 1
            plot(x,y)
            print("(",x,",",y,")")

#Plot function
def plot(x,y):
    glBegin(GL_POINTS)
    glVertex2f(round(x),round(y))
    glEnd()
    glFlush()


def main():
    #opengl
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Line using Midpoint Algorithm")
    glutDisplayFunc(midpoint)
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100,100,-100,100)
    glutMainLoop()

main()
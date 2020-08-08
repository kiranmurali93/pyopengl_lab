from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
print('package Import Successful')

w, h = 500, 500

def float_range(start,stop,step=0.1):
    x=start
    while x<=stop:
        yield x
        x=x+step

def showScreenHorizontal():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    rf=float_range(x1Value,x2Value)
    for i in rf:
        glVertex2f(i,yValue)
    glVertex2f(x1Value, yValue)
    glEnd()
    glFlush()

def showScreenVertical():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    rf=float_range(y1Value,y2Value)
    for i in rf:
        glVertex2f(xValue,i)
    glVertex2f(xValue, y1Value)
    glEnd()
    glutSwapBuffers()

def showScreenDiagonal():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    rf=float_range(Value1,Value2)
    for i in rf:
        glVertex2f(i,i)
    glEnd()
    glutSwapBuffers()

option = int(input('Enter 1 for horizontal line and 2 for verticle line and 3 for diagonal line : '))
if option == 1:
    print('selected for horizontal line')
    x1Value = float(input('Enter x1 value : '))/100
    x2Value = float(input('Enter x2 value : '))/100
    yValue = float(input('Enter y value : '))/100
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(100,100)
    glutCreateWindow('Horizontal line')
    glutDisplayFunc(showScreenHorizontal)
    glutIdleFunc(showScreenHorizontal)
    glutMainLoop()

if option == 2:
    print('selected for verticle line')
    xValue = float(input('Enter x value : '))/100
    y1Value = float(input('Enter y1 value : '))/100
    y2Value = float(input('Enter y2 value : '))/100
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(100,100)
    glutCreateWindow('Vertical line')
    glutDisplayFunc(showScreenVertical)
    glutIdleFunc(showScreenVertical)
    glutMainLoop()

if option == 3:
    print('selected for diagonal line line')
    Value1 = float(input('Enter value1 : '))/100
    Value2 = float(input('Enter value2 : '))/100
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(100,100)
    glutCreateWindow('Diagonal line')
    glutDisplayFunc(showScreenDiagonal)
    glutIdleFunc(showScreenDiagonal)
    glutMainLoop()

else:
    print('Invalid option')



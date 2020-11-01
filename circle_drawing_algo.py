# program for circle drawing algos
# 1.Mid point circle drawing algorithm
# 2.Polar circle generation algorithm
# 3.Non - Polar circle generation algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Round off
def ROUND(a):
	return int(a+0.4)

def init():
	glClearColor(0.0,0.0,0.0,1.)
	gluOrtho2D(-100,100.0,-100.0,100.0)

# Setting pixel
def setPixel(xcoordinate,ycoordinate):
	glColor3f(1.0,0.0,1.0) 
	glPointSize(4.0)
	glBegin(GL_LINES)
	glVertex2f(-500,0)
	glVertex2f(500,0)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(0,-500)
	glVertex2f(0,500)
	glEnd() 
	glColor3f(0.2,0.0,1.5)
	glPointSize(5.0)
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

#Reading user inputs
def userinput():
    global option,x_centre,y_centre,r
    print('Select 1 for Mid point circle drawing algorithm,')
    print('2 for Polar circle generation algorithm,')
    option = int(input('3 for Non - Polar circle generation algorithm: '))
    print("Enter the Coordinates for center")
    x_centre=int(input('x coordinate :'))
    y_centre=int(input('y coordinate :'))
    r=int(input('Radius: '))

#Mid point circle drawing algorithm
def midPointCircle(x_center, y_center, r):
    x = r 
    y = 0
    # the initial point 
    setPixel(x+x_centre,y+y_centre)
    
    if (r > 0) : 
        setPixel(x+x_centre,-y+y_centre)
        setPixel(y+x_centre,x+y_centre)
        setPixel(y+x_centre,x+y_centre)
        setPixel(-y+x_centre,x+y_centre)

    # Initialising the value of P  
    P = 1 - r  

    while x > y: 
        y += 1
        if P <= 0:  
            P = P + 2 * y + 1
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if (x < y): 
            break
        setPixel(x+x_centre,y+y_centre)  
        setPixel(-x+x_centre,y+y_centre)  
        setPixel(x+x_centre,-y+y_centre)  
        setPixel(-x+x_centre,-y+y_centre)  
        if x != y: 
            setPixel(y+x_centre,x+y_centre)  
            setPixel(-y+x_centre,x+y_centre)  
            setPixel(y+x_centre,-x+y_centre)  
            setPixel(-y+x_centre,-x+y_centre)

#Polar circle generation algorithm
def polarCircle(x_centre, y_centre, r):
    x=0
    y=r
    angle = 0
    end_angle=(22/7)/4
    while angle <= end_angle:
        setPixel(ROUND(x_centre + x), ROUND(y_centre + y))
        setPixel(ROUND(x_centre + y), ROUND(y_centre + x))
        setPixel(ROUND(x_centre + y), ROUND(y_centre - x))
        setPixel(ROUND(x_centre + x), ROUND(y_centre - y))
        setPixel(ROUND(x_centre - x), ROUND(y_centre - y))
        setPixel(ROUND(x_centre - y), ROUND(y_centre - x))
        setPixel(ROUND(x_centre - y), ROUND(y_centre + x))
        setPixel(ROUND(x_centre - x), ROUND(y_centre + y))
        angle+=0.001
        x=(r*math.cos(angle))
        y=(r*math.sin(angle))

# Non - Polar circle generation algorithm
def nonPolar(x_centre, y_centre, r):
    x = r
    y = 0
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


#Display Function
def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    if option == 1:
        midPointCircle(x_centre, y_centre, r)
    elif option == 2:
        polarCircle(x_centre, y_centre, r)
    elif option == 3:
        nonPolar(x_centre, y_centre, r)
    else:
        print('Invalid input')
        exit()


def main():
    userinput()
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("circle")
    glutDisplayFunc(Display)
    init()
    glutMainLoop()


main()

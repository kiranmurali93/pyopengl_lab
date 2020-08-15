# dda algo
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Function for round off the pixel value
def ROUND(a):
	return int(a+0.5)

# init function
def init():
	glClearColor(0.0,0.0,0.0,1.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-100,100,-100,100)

#Display function
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	x1=int(input('x1 coordinate: '))
	y1=int(input ('y1 coordinate: '))
	x2=int(input('x2 coordinate: '))
	y2=int(input('y2 coordinate: '))
	lineDDA(x1,y1,x2,y2)	

# for setting pixel co-ordinates
def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

# DDA function
def lineDDA(x1,y1,x2,y2):
	dx=abs(x2-x1)
	dy=abs(y2-y1)
	x,y=x1,y1
	steps=dx if dx>dy else dy
	xincrement=dx/float(steps)
	yincrement=dy/float(steps)
	setPixel(ROUND(x),ROUND(y))	
	for i in range (steps):
		x+=xincrement
		y+=yincrement
		setPixel(ROUND(x),ROUND(y))


# main function
def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Line using DDA")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()


main()
from turtle import *
def triangle(side):
	for i in range(3):
		fd(side)
		lt(120)
def sierpinski_triangle(side):
	if side <20:
		return 0
	triangle(side)
	sierpinski_triangle(side/2)
	fd(side)
	triangle(side)
	sierpinski_triangle(side/2)
	bk(side)
	lt(60)
	fd(side)
	rt(60)
	triangle(side)
	sierpinski_triangle(side/2)
	lt(60)
	bk(side)
	rt(60)
pu()
goto(-400,-400)
pd()
tracer(0,1)
sierpinski_triangle(500)

input()


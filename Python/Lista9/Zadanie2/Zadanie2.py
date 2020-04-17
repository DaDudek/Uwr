from turtle import *
from math import *
def kwadrat(side,color):
	fillcolor(color)
	begin_fill()
	for i in range(4):
		fd(side)
		rt(90)
	end_fill()

def kwadratw(side):
	#fillcolor(color)
	#begin_fill()
	for i in range(4):
		fd(side)
		rt(90)
	#end_fill()
def carpet2(side):
	if side<20: 
		for k in range(3):
			for j in range(3):
				kwadratw(side)
				fd(side)
			bk(3*side)
			rt(90)
			fd(side)
			lt(90)
		lt(90)
		fd(3*side)
		rt(90)
		fd(3*side)
		return 0
	for i in range(3):
		for k in range(3):
			if i==1 and k==1:
				fd(side)
				continue
			else:
				kwadratw(side)
				pu()
				fd(side/3)
				rt(90)
				fd(side/3)
				lt(90)
				pd()
				kwadrat(side/3,"blue")
				pu()
				bk(side/3)
				lt(90)
				fd(side/3)
				rt(90)
				pd()
				carpet2(side/3)
		pu()
		bk(3*side)
		rt(90)
		fd(side)
		lt(90)
		pd()
	pu()
	lt(90)
	fd(3*side)
	rt(90)
	fd(3*side)
	pd()
def pelny_dywan(side):
	pu()
	goto(-450+side,450-side)
	pd()
	kwadrat(side,"blue")
	pu()
	bk(side)
	lt(90)
	fd(side)
	rt(90)
	goto(-450,450)
	pd()
	carpet2(side)			
tracer(0,1)
pelny_dywan(300)

input()

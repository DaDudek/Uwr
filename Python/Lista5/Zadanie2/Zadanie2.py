from turtle import fd, bk, lt, rt,ht,  speed
from random import randint
min=10
for i in range(40):
	x=randint(min,min+6)
	min=x
	fd(10)
	lt(90)
	fd(x)
	lt(90)
	fd(10)
	lt(90)
	fd(x)
	lt(90)
	fd(10)
input()

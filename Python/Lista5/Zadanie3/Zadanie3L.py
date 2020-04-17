from duze_cyfry import daj_cyfre
from random import*
from turtle import *
speed(10)
def kwadrat(n,kolor):
	fillcolor(kolor)
	begin_fill()
	for i in range(5):
		fd(n)
		rt(90)
	end_fill()
	lt(90)
def pusty_kwadrat(n):
	pu()
	for i in range(5):
		fd(n)
		rt(90)
	lt(90)
	pd()
def drukuj_cyfre(n):
    tmp =str(n)
    for i in range(len(tmp)):
        x=int(tmp[i])
        for r in daj_cyfre(x):
            print(r)
def przygotuj_drukuj_cyfre_ladniej(n):
    List=[]
    tmp = str(n)
    for i in range(len(tmp)):
        x=int(tmp[i])
        List.append(daj_cyfre(x) )

    return List
def drukuj_cyfre_ladniej(n,bok):
	kolory= ['red', 'green', 'blue', 'yellow', 'pink','orange']
	kolorki=[]
	tracer(0,1)
	pu()	
	lt(180)
	fd(800)
	lt(180)
	pd()
	List=przygotuj_drukuj_cyfre_ladniej(n)
	tmp = str(n)
	lgh=0
	lastNum =int(tmp[len(tmp)-1])
	for i in range(5):
		row = ""
		for j in range(lastNum):
			row += List[j][i]
			row +=" "
		print(row)
		counter=0
		tmps=-1
		for k in range(len(row)):
			kolorek=choice(kolory)
			kolorki.append(kolorek)
			if ((counter%6)==0):
				tmps=tmps+1
			if(row[k]=="#"):
				kwadrat(bok,kolorki[tmps])
			else:
				pusty_kwadrat(bok)
			counter=counter+1
		pu()
		rt(90)
		fd(bok)
		rt(90)
		fd(bok*len(row))
		pd()
		rt(180)
		lgh=len(row)
	fd(bok*(lgh+2))
	lt(90)
	fd(5*bok)
	lt(90)
	fd(bok*(lgh+2))
	lt(90)
	fd(5*bok)

#kwadrat(20)
drukuj_cyfre_ladniej(123456789,20)
input()

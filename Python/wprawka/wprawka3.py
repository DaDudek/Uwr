from turtle import *
def rysuj_jeden(bok):
	rt(90)
	fd(bok)
	lt(90)
	pu()
	fd(int(bok/2))
	lt(90)
	fd(bok)
	rt(90)
	pd()
def rysuj_zero(bok):
	for i in range(4):
		fd(bok)
		rt(90)
		fd(bok)
		rt(90)
	fd(bok)
	pu()
	fd(int(bok/2))
	pd()

def rysuj_liczbe(n,bok):
	liczba=bin(n)
	liczba=liczba[2:]
	for i in range(len(liczba)):
		print(liczba[i])
		if(int(liczba[i])==0):
			rysuj_zero(bok)
		else:
			rysuj_jeden(bok)

rysuj_liczbe(1024 + 256 + 128 + 8 + 2,30)
input()


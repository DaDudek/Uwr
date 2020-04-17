from random import *
from turtle import *
pu()
lt(90)
fd(300)
rt(90)
pd()
def kwadrat(kolor): #malowanie pikseli
	fillcolor(kolor)
	begin_fill()
	for i in range(4):
		fd(5)
		rt(90)
	fd(5)
	end_fill()
def przejscie_do_nowej_linii():
	pu()
	rt(90)
	fd(5)
	rt(90)
	fd(5*100)
	rt(180)
	pd()
def stworz_teren():
	siatka_terenu=[]
	for i in range(100):
		wiersz_terenu=[]
		for j in range(100):
			wiersz_terenu.append(0)
		siatka_terenu.append(wiersz_terenu)
	return siatka_terenu
def stworz_wzgorze(siatka_terenu):
	for k in range(15):
		wiersz_startowy=randint(0,90)
		wiersz_koncowy=wiersz_startowy+randint(0,10)
		pole_startowe=randint(0,70)
		pole_koncowe=pole_startowe+randint(0,30)
		for i in range(wiersz_startowy,wiersz_koncowy+1):
			for j in range(pole_startowe,pole_koncowe):
				siatka_terenu[i][j]=21

#funkcje pomocnicze do usrednienia wynikow
def pierwszy_wiersz(siatka_terenu,x,y):
	if y==0:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y+1]+siatka_terenu[x+1][y]+siatka_terenu[x+1][y+1])/4
		siatka_terenu[x][y]=tmp
	if y==99:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y-1]+siatka_terenu[x+1][y]+siatka_terenu[x+1][y-1])/4
		siatka_terenu[x][y]=tmp
	else:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y-1]+siatka_terenu[x][y+1]+siatka_terenu[x+1][y-1]+siatka_terenu[x+1][y]+siatka_terenu[x+1][y+1])/6
		siatka_terenu[x][y]=tmp
def ostatni_wiersz(siatka_terenu,x,y):
	if y==0:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y+1]+siatka_terenu[x-1][y]+siatka_terenu[x-1][y+1])/4
		siatka_terenu[x][y]=tmp
	if y==99:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y-1]+siatka_terenu[x-1][y]+siatka_terenu[x-1][y-1])/4
		siatka_terenu[x][y]=tmp
	else:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y-1]+siatka_terenu[x][y+1]+siatka_terenu[x-1][y-1]+siatka_terenu[x-1][y]+siatka_terenu[x-1][y+1])/6
		siatka_terenu[x][y]=tmp
def pozostale_wiersze(siatka_terenu,x,y):
	if y==0:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y+1]+siatka_terenu[x-1][y]+siatka_terenu[x-1][y+1]+siatka_terenu[x+1][y]+siatka_terenu[x+1][y+1])/6
		siatka_terenu[x][y]=tmp
	if y==99:
		tmp=(siatka_terenu[x][y]+siatka_terenu[x][y-1]+siatka_terenu[x-1][y]+siatka_terenu[x-1][y-1]+siatka_terenu[x+1][y]+siatka_terenu[x+1][y-1])/6
		siatka_terenu[x][y]=tmp
	else:
		tmp=(siatka_terenu[x][y-1]+siatka_terenu[x][y]+siatka_terenu[x][y+1])
		tmp=tmp+(siatka_terenu[x-1][y-1]+siatka_terenu[x-1][y]+siatka_terenu[x-1][y+1])
		tmp=tmp+(siatka_terenu[x+1][y-1]+siatka_terenu[x+1][y]+siatka_terenu[x+1][y+1])
		tmp=tmp/9
		siatka_terenu[x][y]=tmp
#koniec funkcji pomocniczych
def policz_srednia_wazona(siatka_terenu,x,y):
	if(x==0):
		pierwszy_wiersz(siatka_terenu,x,y)
	if x==99:
		ostatni_wiersz(siatka_terenu,x,y)
	else:
		pozostale_wiersze(siatka_terenu,x,y)
def usrednij_wynik(siatka_terenu):
	for i in range(1000000):
		x=randint(0,99)#wiersze
		y=randint(0,99)#pola
		policz_srednia_wazona(siatka_terenu,x,y)
def wartosci_skalowania(siatka_terenu):
	maximum=0
	minimum=17
	srednia=0
	for i in range(100):
		for j in range(100):
			if siatka_terenu[i][j]>maximum:
				maximum=siatka_terenu[i][j]
			if siatka_terenu[i][j]<minimum:
				minimum=siatka_terenu[i][j]
			srednia=srednia+siatka_terenu[i][j]
	srednia=srednia/10000
	Lista_do_skalowania=[maximum,minimum,srednia]
	return Lista_do_skalowania
def rysowanie_mapy(siatka_terenu,lista_do_skalowania):
	Lista_kolorow=["green", (0.5, 1, 0) , "yellow", "orange", "red", (0.5, 0,0)]
	print(1)
	for i in range(100):
		for j in range(100):
			if(siatka_terenu[i][j]>lista_do_skalowania[2]):
				tmp=(lista_do_skalowania[0]+lista_do_skalowania[2])/2
				if(siatka_terenu[i][j]>tmp):
					if(siatka_terenu[i][j]>lista_do_skalowania[0]*0.8):
						kwadrat([0.5, 0,0])
					else:
						kwadrat("red")
				else:
					kwadrat("orange")
			else:
				tmp=(lista_do_skalowania[1]+lista_do_skalowania[2])/2
				if(siatka_terenu[i][j]>tmp):
					kwadrat("yellow")
				else:
					if(siatka_terenu[i][j]<(tmp/3.5)):
						kwadrat([0.5, 1, 0])
					else:
						kwadrat("green")
		przejscie_do_nowej_linii()
	
def Zadanie4():
	siatka_terenu=stworz_teren()
	stworz_wzgorze(siatka_terenu)
	usrednij_wynik(siatka_terenu)
	rysowanie_mapy(siatka_terenu,wartosci_skalowania(siatka_terenu))
tracer(0,1)
Zadanie4()
input()

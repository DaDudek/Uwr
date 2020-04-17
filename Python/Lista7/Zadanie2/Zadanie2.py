from turtle import *
from random import *
plik=open("niespodzianka.txt")
tracer(0,1)
X=0
Y=400
lista_lokalizacji_pikseli=list()
def rysuj_kwadrat(Lista_kolorow):
	kolor_kwadratu=list()
	kolor_kwadratu.append(int(Lista_kolorow[0])/255)
	kolor_kwadratu.append(int(Lista_kolorow[1])/255)
	kolor_kwadratu.append(int(Lista_kolorow[2])/255)
	fillcolor(kolor_kwadratu)
	begin_fill()
	for i in range(5):
		fd(10)
		rt(90)
	end_fill()
	lt(90)
for wiersz in plik:
	wiersz_pikseli=wiersz.split()
	X=0
	for i in range(len(wiersz_pikseli)):
		piksel=wiersz_pikseli[i][1:-1]
		X=X+10
		lista_tmp=[X,Y,piksel]
		lista_lokalizacji_pikseli.append(lista_tmp)
	Y=Y-10
tmp=len(lista_lokalizacji_pikseli)
while(tmp>0):
	losowy_piksel=choice(lista_lokalizacji_pikseli)
	pu()
	goto(losowy_piksel[0],losowy_piksel[1])
	pd()
	rysuj_kwadrat(losowy_piksel[2].split(","))
	lista_lokalizacji_pikseli.remove(losowy_piksel)
	tmp=len(lista_lokalizacji_pikseli)
	if((tmp%10)==0):
		update()

input()


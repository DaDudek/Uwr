from kwadrat import kwadrat
from turtle import update, clear
from random import *


txt = """
..kkkkkkkkkkk.....ppp.
.........nnnk.........
...kk.................
..nnnn...pp...kkk.....
..nnkn....p...kkk.....
..n...................
....kk............ppp.
.........kkkkkk.......
..kk.......ppppp......
....p.................
...pppppp......nnn....
.................kkkk.
"""



tab=txt.split()
for i in range(len(tab)):
	tmp=list()
	for j in range(len(tab[i])):
		if tab[i][j] == "k" or tab[i][j]=="p" or tab[i][j]== "n":
			tmp.append([tab[i][j],randint(1,5)])
		else:
			tmp.append([tab[i][j],0])
	tab[i]=tmp
tab.reverse()

MY = len(tab)
MX = len(tab[0])
print(MY,MX)
def rysuj_plansze(tab):
	clear()
	for y in range(MY):
		for x in range(MX):
			if tab[y][x][0] == '.':
				kolor = 'green'
			if tab[y][x][0] == "k": #kamien czerwony
				kolor = "red"
			if tab[y][x][0] == "n": #nożyce niebieskie
				kolor = "blue"  
			if tab[y][x][0]=="p":
				kolor = 'yellow' #papier żółty   
			kwadrat(x, y, kolor)
	update()   
def pusta_plansza():
	return [MX * ['.'] for i in range(MY)]
def walcz(tab,y,x,ys,xs):
	if tab[y][x][1]>1 and tab[ys][xs][0]==".": #cos vs pusty
		tab[ys][xs]=[tab[y][x][0],tab[y][x][1]-1]

	if tab[y][x][0]=="k" and tab[ys][xs][0]=="p": #kamien vs papier
		if tab[y][x][1]==1:
			tab[y][x]=[".",0]
		if tab[y][x][1]>1:
			sila_przegranego=tab[y][x][1]
			tab[y][x]=["k",sila_przegranego-1]
		if tab[ys][xs][1]<5:
				sila_wygranego=tab[ys][xs][1]
				tab[ys][xs]=["p",sila_wygranego+1]
		

	if tab[y][x][0]=="k" and tab[ys][xs][0]=="n": #kamien vs nozyce
		if tab[ys][xs]==1:
			tab[ys][xs]=[".",0]
		if tab[ys][xs][1]>1:
			tmp=tab[ys][xs][1]
			tab[ys][xs]=["n",tmp-1]
		if tab[y][x][1]<5:
				sila_wygranego=tab[y][x][1]
				tab[y][x]=["k",sila_wygranego+1]

	if tab[y][x][0]=="p" and tab[ys][xs][0]=="k": #papier vs kamien
		if tab[ys][xs]==1:
			tab[ys][xs]=[".",0]
		if tab[ys][xs][1]>1:
			tmp=tab[ys][xs][1]
			tab[ys][xs]=["k",tmp-1]
		if tab[y][x][1]<5:
				sila_wygranego=tab[y][x][1]
				tab[y][x]=["p",sila_wygranego+1]

	if tab[y][x][0]=="p" and tab[ys][xs][0]=="n": #papier vs nozyce 
		if tab[y][x]==1:
			tab[y][x]=[".",0]
		if tab[y][x][1]>1:
			tmp=tab[y][x][1]
			tab[y][x]=["p",tmp-1]
		if tab[ys][xs][1]<5:
			sila_wygranego=tab[ys][xs][1]
			tab[ys][xs]=["n",sila_wygranego+1]
			

	if tab[y][x][0]=="n" and tab[ys][xs][0]=="p":#nozyce vs papier
		if tab[ys][xs][1]==1:
			tab[ys][xs]=[".",0]
		if tab[ys][xs][1]>1:
			tmp=tab[ys][xs][1]
			tab[ys][xs]=["p",tmp-1]
		if tab[y][x][1]<5:
			sila_wygranego=tab[y][x][1]
			tab[y][x]=["n",sila_wygranego+1]
			

	if tab[y][x][0]=="n" and tab[ys][xs][0]=="k":#nozyce vs kamien
		if tab[y][x][1]==1:
			tab[y][x]=[".",0]
		if tab[y][x][1]>1:
			tmp=tab[y][x][1]
			tab[y][x]=["n",tmp-1]
		if tab[ys][xs][1]<5:
			sila_wygranego=tab[ys][xs][1]
			tab[ys][xs]=["k",sila_wygranego+1]

def walcz_z_losowym_sasiadem(tab,y,x): #losuje sasiada - zwraca wspolrzedne 
	if y==0:
		if x==0:
			tmp=[[y,x+1],[y+1,x]]
		if x==MX-1:
			tmp=[[y,x-1],[y+1,x]]
		if x!=MX-1 and x!=0:
			tmp=[[y,x-1],[y,x+1],[y+1,x]]
	if y==MY-1:
		if x==0:
			tmp=[[y,1],[y-1,0]]
		if x==MX-1:
			tmp=[[y,x-1],[y-1,x]]
		if x!=MX-1 and x!=0:
			tmp=[[y,x-1],[y,x+1],[y-1,x]]
	if y!=MY-1 and y!=0:
		if x==0:
			tmp=[[y,x+1],[y-1,x],[y+1,x]]
		if x==MX-1:
			tmp=[[y,x-1],[y-1,x],[y+1,x]]
		if x!=MX-1 and x!=0:
			tmp=[[y,x-1],[y,x+1],[y-1,x],[y+1,x]]
	losowy_sasiad=choice(tmp)
	#print(losowy_sasiad)
	walcz(tab,y,x,losowy_sasiad[0],losowy_sasiad[1])
# reguły gry w życie:
# Mamy cztery rodzaje pól:  pola puste oraz pola zawierające komórkę typu papier, nożyce lub kamień.

# Pola niepuste dodatkowo mają zapisaną siłę (liczbę od 1 do 5)

# Jeżeli sąsiadem jest pole puste, a nasza siła jest co najmniej 2, to „zasiedlamy” je z siłą o 1 mniejszą (czyli na przykład papier z siłą 4 spowoduje wpisanie na puste miejsce papieru z siłą 3)

# Jeżeli sąsiadem jest pole naszego koloru to nic się nie dzieje.

# Jeżeli sąsiadem jest pole innego rodzaju, to następuje pojedynek w wyniku którego przegrany traci jeden punkt siły,  a zwycięzca zyskuje 1 (chyba że już ma maksymalną siłę).Pojedynek rozstrzygany jest zgodnie z zasadami oryginalnej gry:  papier pokonuje kamień,kamień nożyce, a te papier (siła nie ma znaczenia)

#Jeżeli w wyniku pojedynku siła pola zmaleje do zera, pole staje się puste.

while True:
	rysuj_plansze(tab)
	for y in range(MY):
		for x in range(MX):
			if tab[y][x] == '.':
				continue
			else:
				walcz_z_losowym_sasiadem(tab,y,x)
	input()

print ('Koniec')
input()

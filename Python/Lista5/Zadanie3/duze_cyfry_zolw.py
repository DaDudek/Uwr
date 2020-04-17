from turtle import *
def przejdz_do_nowej_linii():
	pu()
	bk(75)
	rt(90)
	fd(20)
	rt(-90)
	pd()
def rysuj_kwadrat(kolor):
	fillcolor(kolor)
	begin_fill()
	for i in range(4):
		fd(15)
		rt(90)
	end_fill()
	fd(15)
def rysuj_pusty_kwadrat():
	pu()
	for i in range(4):
		fd(15)
		rt(90)
	fd(15)
	pd()
def rysuj_0(kolor):
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii() #linia1
	for i in range(3):
		rysuj_kwadrat(kolor)
		rysuj_pusty_kwadrat()
		rysuj_pusty_kwadrat()
		rysuj_pusty_kwadrat()
		rysuj_kwadrat(kolor)
		przejdz_do_nowej_linii()
	rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	rysuj_kwadrat(kolor)
	rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
def rysuj_1(kolor):
	for i in range(2):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(0,2):	
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii() #1
	rysuj_pusty_kwadrat()
	for i in range(0,2):
		rysuj_kwadrat(kolor)
	for i in range(0,2):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii() #2
	for i in range(2):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(0,2):	
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii() #3
	for i in range(2):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(0,2):	
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#4
	rysuj_pusty_kwadrat()
	for i in range(0,3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
def rysuj_2(kolor):
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#1
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#2
	for i in range(2):
		rysuj_pusty_kwadrat()
	for i in range(2):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#3
	rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#4
	for i in range(5):
		rysuj_kwadrat(kolor)
def rysuj_3(kolor):
	for i in range(4):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#1
	for i in range(4):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#2
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#3 
	for i in range(4):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#4
	for i in range(4):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
def rysuj_4(kolor):
	rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#1
	rysuj_kwadrat(kolor)
	for i in range(4):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#2
	for i in range(5):
		rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#3
	for i in range(2):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(2):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#4
	for i in range(2):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(2):
		rysuj_pusty_kwadrat()
def rysuj_5(kolor):
	for i in range(5):
		rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#1
	rysuj_kwadrat(kolor)
	for i in range(4):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#2
	for i in range(4):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#3
	for i in range(4):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#4
	for i in range(4):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
def rysuj_6(kolor):
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#1
	rysuj_kwadrat(kolor)
	for i in range(4):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#2
	for i in range(4):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#3
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#4
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
def rysuj_7(kolor):
	for i in range(5):
		rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#1
	for i in range(3):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#2
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#3
	rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#4
	rysuj_kwadrat(kolor)
	for i in range(4):
		rysuj_pusty_kwadrat()
def rysuj_8(kolor):
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#1
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#2
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#3
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#4
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
def rysuj_9(kolor):
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
	przejdz_do_nowej_linii()#1
	rysuj_kwadrat(kolor)
	for i in range(3):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#2
	rysuj_pusty_kwadrat()
	for i in range(4):
		rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#3
	for i in range(4):
		rysuj_pusty_kwadrat()
	rysuj_kwadrat(kolor)
	przejdz_do_nowej_linii()#4
	rysuj_pusty_kwadrat()
	for i in range(3):
		rysuj_kwadrat(kolor)
	rysuj_pusty_kwadrat()
def rysuj_cyfre(n,kolor):
	if(n==0):
		rysuj_0(kolor)
	if(n==1):
		rysuj_1(kolor)
	if(n==2):
		rysuj_2(kolor)
	if(n==3):
		rysuj_3(kolor)
	if(n==4):
		rysuj_4(kolor)
	if(n==5):
		rysuj_5(kolor)
	if(n==6):
		rysuj_6(kolor)
	if(n==7):
		rysuj_7(kolor)
	if(n==8):
		rysuj_8(kolor)
	if(n==9):
		rysuj_9(kolor)


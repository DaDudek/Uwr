from math import *
def blok(n,znak):
	tmp=""
	for i in range(n):
		tmp=tmp+znak
	return tmp
def bloki(m):
	tmp=1
	counter=1
	wynik=[]
	while (tmp<m+1):
		if counter>6:
			counter=1
		if counter==6:
			wynik.append("$"*tmp)
		if counter==5:
			wynik.append("%"*tmp)
		if counter==4:
			wynik.append("&"*tmp)
		if counter==3:
			wynik.append("#"*tmp)
		if counter==2:
			wynik.append("*"*tmp)
		if counter==1:
			wynik.append("@"*tmp)
		tmp=tmp+1
		counter=counter+1
	return wynik
def filtr(L):
	Lista_wynikowa=[]
	for i in range(len(L)):
		tmp=int(sqrt(len(L[i])))
		if(tmp * tmp ==len(L[i])):
			Lista_wynikowa.append(L[i])
	return Lista_wynikowa
x=len(filtr(bloki(111)))
Lista=filtr(bloki(111))
for i in range(x):
	print(Lista[i])


def F(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1
def oblicz_energie(a):
	List=[]
	x=F(a)
	List.append(x)
	while x !=1:
		x=F(x)
		List.append(x)
	return len(List)		 
def analiza_collatza(a,b):
	Lista_energii=[] #tablica energii dla zbioru <a,b>
	for i in range(a,b+1):
		y=oblicz_energie(i)
		Lista_energii.append(y)
	dlugosc=len(Lista_energii)
	Lista_energii=list(sorted(Lista_energii))
	mediana=0	#mediana początek
	if(dlugosc%2==0):
		mediana=Lista_energii[int((dlugosc-1)/2)]+Lista_energii[int((dlugosc/2))]
		mediana=mediana/2
	else:
		mediana=Lista_energii[int((dlugosc)/2)]
	print("Mediana to "+str(mediana)) #mediana koniec

	srednia=0 #średnia początek
	for i in range(dlugosc):
		srednia=srednia+Lista_energii[i]
	srednia=srednia/dlugosc#średnia koniec
	
	najmniejsza=Lista_energii[0]
	najwieksza=Lista_energii[0]
	for i in range(dlugosc):
		if Lista_energii[i] > najwieksza:
			najwieksza=Lista_energii[i]
		if Lista_energii[i] < najmniejsza:
			najmniejsza=Lista_energii[i] 
	print("Największa energia to "+str(najwieksza))
	print("Najmniejsza energia to "+str(najmniejsza))
	print("Średnia energia to: "+str(srednia))
	return Lista_energii
	
print(analiza_collatza(7,11))
	


def pary(n):
	tablica_wspolrzednych=[]
	for i in range(n+1):
		for j in range(i,-1,-1):
			tmp=i
			wspolrzedna=[tmp-j,j]
			tablica_wspolrzednych.append(wspolrzedna)
	print(tablica_wspolrzednych)
	return tablica_wspolrzednych
def pary_pythonowo(n):
	tablica_wspolrzednych=[[i-j,j] for i in range(n+1) for j in range(i,-1,-1)]
	print(tablica_wspolrzednych)
	return tablica_wspolrzednych
pary(4)
print()
pary_pythonowo(4)

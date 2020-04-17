def poprawna_macierz(macierz):
	flaga=True
	macierz
	tmp=len(macierz)
	for i in range(0,tmp):
		if len(macierz[i])!=tmp:
			flaga=False
	return flaga
def transpozycja(macierz):
	if not(poprawna_macierz(macierz)):
		return False
	tmp=len(macierz)
	lista=list()
	for a in range(tmp):
		lista_pomocnicza=list()
		for b in range(tmp):
				lista_pomocnicza.append(0)
		lista.append(lista_pomocnicza)
	for i in range(tmp):
		for j in range(tmp):
			lista[i][j]=macierz[j][i]
	return lista
#testowe macierze
macierz2x2=[[1,8],[2,7]]
macierz2x3=[[1,2,3],[2,3,4]]
macierz3x3=[[1,2,3],[2,3,4],[3,4,5]]
macierz3x4=[[1,2,3,4],[3,2,1,4],[4,5,7,5]]
macierz1x5=[[1,2,3,4,5]]
macierz3x2=[[1,2,],[2,3],[3,4]]
#test_poprawnosci
print(poprawna_macierz(macierz2x2))
print(poprawna_macierz(macierz2x3))
print(poprawna_macierz(macierz3x3))
print(poprawna_macierz(macierz3x4))
print(poprawna_macierz(macierz1x5))
print(poprawna_macierz(macierz3x2))
print()
print()
print()
print()
#testy_transpozycji
print(transpozycja(macierz2x2))
print(transpozycja(macierz3x3))
print(transpozycja(macierz2x3))
print(transpozycja(macierz3x4))
print(transpozycja(macierz3x2))

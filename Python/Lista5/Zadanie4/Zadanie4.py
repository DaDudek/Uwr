def usun_duplikaty(List):
	wynik=[]
	pozycje_powtarzające=[]
	for i in range(len(List)):
		List[i]=(List[i],i)
	posortowana_z_duplikatami=sorted(List) #tworze liste postaci(liczba,pozycja)

	for i in range(1,len(List)):
		if posortowana_z_duplikatami[i][0] == posortowana_z_duplikatami[i-1][0]:
			pozycje_powtarzające.append(i) #tworze liste miejsc na których coś się powtarza(i to index pierwszego powtórzenia)

	pozycje_powtarzające.reverse() #jade od konca aby index sie nie przesunal
	for i in pozycje_powtarzające:
		del posortowana_z_duplikatami[i]

	posortowana_po_pozycji=sorted(posortowana_z_duplikatami, key=lambda posortowana: (posortowana[1]))#sortuje po pozycji

	for i in range(len(posortowana_po_pozycji)): #gubię index
		wynik.append(posortowana_po_pozycji[i][0])
	return wynik

List=[8,1,3,2,3,5,6,8,865,321,412,1,3,2,2,2,2]
print(usun_duplikaty(List))

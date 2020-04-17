zbior_powtorzen=set()
zbior_wynikowy=set()
lista_slow=[]
zbior_slow=set()
for wiersz in open('slowa.txt'):
	slowo= wiersz[:-1]
	lista_slow.append(slowo)
	zbior_slow.add(slowo)
for i in range(len(lista_slow)):
	odwrocone_slowo=lista_slow[i][::-1]
	if((odwrocone_slowo in zbior_slow) and lista_slow[i] not in zbior_powtorzen): #uzywam zbiorow bo szybsze 
		zbior_wynikowy.add((lista_slow[i],odwrocone_slowo))
		zbior_powtorzen.add(odwrocone_slowo)
print(len(zbior_wynikowy))
#print(zbior_wynikowy)

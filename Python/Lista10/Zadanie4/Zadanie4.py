"""1 12 13 14 123 124 134 1234 2 23 24 234 3 34 4 PODCIĄG
1 3 4 5 6 7 8 10 2 9  SUMA"""

def f(L): #wersja 2 łatwiejsza
	if len(L) == 0:
		return [0]
	s=f(L[1:])# bez pierwszego elementu
	return s + [L[0] + rest for rest in s]
list=f([1,2,3,100])
print(set(list))

"""
funkcja f działa tak że bierze 1 element i wywołuje samą siebie bez niego	
dla zbioru 1,2,3,4 dojdziemy do końca i mamy zbiór pusty 0
wtedy możemy do niego dodać 4 lub nie - otrzymujemy więc 0,4
potem bierzemy 3 i mamy 0,4,3,7 i tak dalej gdyby nie było elementu s w s+ [L[0] to zwracałaby tylko ostatni 
s to jakiś zbiór w którym nie dodaliśmy x a [L[0] + rest for rest in s] to zbiór w którym dodaliśmy  więc robiąc tą 
pętle dodajemy do każdego 
"""

from random import choice, randint
def randperm(n):
    tab=[]
    wynik=[]
    for i in range(n):
        tab.append(i)
    while (len(wynik)!=n):
        tmp=choice(tab)
        if tmp not in wynik:
            wynik.append(tmp)
    return wynik
def randperm_better(n):
	wynik=[]
	for i in range(n):
		wynik.append(i)
	for i in range(n):
		random_position=randint(0,n-1)
		tmp=wynik[random_position]
		wynik[random_position]=wynik[i]
		wynik[i]=tmp
	return wynik
print(randperm_better(10**6))
print("Mniejsze liczby")
for i in range(20):
	print(randperm_better(10))


def perm(L):    
    if L == []:
        return [[]]
    e = L[0]
    reszta = perm(L[1:])
    return [ r[:p] + [e] + r[p:] for r in reszta for p in range(len(r)+1)]   #kod z wykładu wygeneruje mi permutacje zbioru[0,1,2,3,4,5,6,7,8,9]

wynik=perm([i for i in range(10)])


def check_sum(words_list,dict_of_letters): ##sprawdza czy dodawanie jest prawdziwe
	numbers_list = ["","",""] #na wejsciu dostaje 3 slowa dlatego przygotowuje 3 miejsca
	for i in range(len(words_list)):
		for letters in words_list[i]:
			numbers_list[i]=numbers_list[i]+str(dict_of_letters[letters]) #sumuje wartosci liter w danym slowie,wartosc litery ustawiona za pomoca permutacji 0-9
	if (int(numbers_list[0])+int(numbers_list[1])==int(numbers_list[2])):
		if (int(dict_of_letters[words_list[0][0]])!=0 and int(dict_of_letters[words_list[1][0]])!=0 and int(dict_of_letters[words_list[2][0]])!=0): #sprawdza czy liczba nie zaczyna sie na 0
			return True
	return False

def arithmetical_riddle(words):
	dict_of_letters={}
	set_of_letters=set()
	words_list=words.split()
	words_list.remove("=")
	words_list.remove("+")
	string_of_letters=""
	for word in words_list:
		for letter in word:
			set_of_letters.add(letter) #zbiera wszystkie unikalne litery
			dict_of_letters[letter]=0 #ustawia słownik postaci litera-liczba(na start same 0)
	if len(set_of_letters)>10: #jeśli więcej niż 10 liter to nie mamy dość cyfr
		return None
	for letter in set_of_letters:
		string_of_letters=string_of_letters+letter #robimy ciąg uniknalnych liter
	for elements in wynik: # przeglądamy permutacje w poszukiwaniu odpowiedniego podciągu
		for i in range(len(string_of_letters)):
			dict_of_letters[string_of_letters[i]]=str(elements[i]) #ustawiamy k-tą litere ciągu na k-tą cyfre permutacji
			if check_sum(words_list,dict_of_letters):
				return dict_of_letters
	return None
print(arithmetical_riddle("send + more = money"))
print(arithmetical_riddle("ciacho + ciacho = nadwaga"))


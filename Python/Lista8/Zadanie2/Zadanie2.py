#slownjik domyslny dla braku liter
def spread_the_word(word): # dziele słowo na słownik postaci litera-liczba_wystąpień
	dictionary={}
	for letter in word:
		if letter not in dictionary:
			dictionary[letter]=1
		else:
			dictionary[letter]=dictionary[letter]+1
	return dictionary
def check_word(word1,word2):
	flaga=True
	key=spread_the_word(word1)
	word_to_check=spread_the_word(word2)
	if len(key)<len(word_to_check): #jeśli klucz ma mniej unikatowych liter to na pewno się nie da ułożyć z niego słowa sprawdzanego 
		flaga=False
		return flaga 
	for letter in word2:
		if word_to_check[letter]>key[letter]: # jeżeli słowo które chcemy ułożyć z klucza ma więcej wystąpień litery niż klucz to się nie da
			flaga=False
	return flaga
print(check_word("lokomotywa","kotka"))
print(check_word("lokomotywa","aktyw"))

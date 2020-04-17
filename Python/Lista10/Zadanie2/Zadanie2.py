alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
dict_of_letters = dict(zip(alphabet,[i for i in range(len(alphabet))]))
dict_of_words = dict()
test_file = open("popularne_slowa.txt")
def make_dict_of_words(test_file):
	tmp=0
	for word in test_file:
		word = word.strip()
		flaga = False
		for letter in word:
			if letter not in alphabet:
				flaga = True
				break
		if flaga:
			continue #aby nie dodawac smieci
		if len(word) > tmp:
			tmp = len(word) #aby znalezc najdluzsze
		if len(word) not in dict_of_words:
			sets = set()
			sets.add(word)
			dict_of_words[len(word)] = sets #slownik dlugiosc-{slowa tej dlugosci}
		else:
			dict_of_words[len(word)].add(word)
	return tmp
def ceaser(s,k):
	while k < 0:
		k = len(alphabet)+k
	przesuniecie = k % (len(alphabet))
	coded_word=[]
	for word in s.split():
		for letters in word:
			tmp = dict_of_letters[letters]+przesuniecie
			while tmp >= len(dict_of_letters):
				tmp = tmp-len(dict_of_letters)
			coded_word.append(alphabet[tmp])
		coded_word.append(" ")
	coded_word = coded_word[:-1]
	return "".join(coded_word)

def find_the_longest_word(test_file):
	counter = make_dict_of_words(test_file) #dlugosc najdluzszego slowa
	list_of_ceasers_word = []
	for i in range(counter,0,-1):
		if i in dict_of_words:
			for word in dict_of_words[i]:
				for k in range(len(alphabet)):
					if ceaser(word,k) in dict_of_words[i] and k!=0:
						if ceaser(ceaser(word,k), len(alphabet)-k) == word and k != len(alphabet)/2:
								list_of_ceasers_word.append([word,ceaser(word,k)])
			if len(list_of_ceasers_word) != 0:
				return list_of_ceasers_word

print(find_the_longest_word(test_file))

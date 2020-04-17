test_file=open("popularne_slowa.txt")
def make_set_of_words(test_file): #wczytanie słów z pliku do zbioru
	set_of_words=set()
	for word in test_file:
		word=word.strip()
		set_of_words.add(word)
	return set_of_words
set_of_words=make_set_of_words(test_file)
def split_word(word): #dzielenie słowa na słownik litera-ilość_wystąpień
	dictionary={}
	for letter in word:
		if letter not in dictionary:
			dictionary[letter]=1
		else:
			dictionary[letter] += 1
	return dictionary
def equality_of_dictionary(dict1,dict2): #porównanie czy w obu słownikach jest tyle samo takich samych liter
	for key in dict1:
		if key in dict2:	
			if dict1[key]!=dict2[key]:
				return False	
		else:
			return False
	return True
def look_for_candidates(key,word2): #sprawdzenie czy słowo może byc podsłowem innego
	testing_dict=split_word(word2)
	key_dict=split_word(key)
	for letter in testing_dict:
		if letter in key_dict:
			if testing_dict[letter] > key_dict[letter]:
				return False
		else:
			return False

	return True
def make_candidates_set(word,set_of_words): #stworzenie zbioru kandydatów na zagadke 
	candidate_set=set()
	for testing_word in set_of_words:
		if look_for_candidates(word,testing_word):
			candidate_set.add(testing_word)
	return candidate_set
def find_riddle(word): #wyszukiwanie zagadki 
	set_of_use_words=set()
	list_of_pairs=[]
	set_of_candidates=make_candidates_set(word,set_of_words)
	for word1 in set_of_candidates:
		for word2 in set_of_candidates:
			if len(word1)+len(word2)!=len(word)-1:
					continue
			else:
				checked_dict=split_word(word)
				connection_word=word1+" "+word2
				connection_set=split_word(connection_word)
				if equality_of_dictionary(connection_set,checked_dict):
					if word1 not in set_of_use_words:
						list_of_pairs.append([word1,word2])
						set_of_use_words.add(word1)
						set_of_use_words.add(word2)
	return list_of_pairs
print(find_riddle("obca makabra"))#barack obama
print()
print(find_riddle("dawid dudek"))



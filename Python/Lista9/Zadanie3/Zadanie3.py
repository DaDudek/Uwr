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
def find_missing_letters(dict1,dict2):
	missing_letters=""
	dictionary=dict(dict1)
	for letter in dict2:
		tmp=dict1[letter]
		tmp2=dict2[letter]
		dictionary[letter]=tmp-tmp2
	for letter in dictionary:
		if dictionary[letter]!=0 and letter!=" ":
			missing_letters=missing_letters+(letter*dictionary[letter])
	final_missing_letters="".join(sorted(missing_letters))
	return final_missing_letters
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
def make_candidates_dictionary(word,set_of_words): #stworzenie zbioru kandydatów na zagadke 
	candidate_set=set()
	candidate_dictionary={}
	for testing_word in set_of_words:
		if look_for_candidates(word,testing_word):
			candidate_set.add(testing_word)
	for words in candidate_set:
		sorted_word="".join(sorted(words))
		if sorted_word not in candidate_dictionary:
			candidate_dictionary[sorted_word]=[words]
		else:
			candidate_dictionary[sorted_word].append(words)
	return candidate_dictionary
def find_riddle(word,set_of_words):
	candidate_dictionary=make_candidates_dictionary(word,set_of_words)
	list_of_riddle_words=list()
	riddle_word_dictionary=split_word(word)
	for key1 in candidate_dictionary:
		for key2 in candidate_dictionary:
			if look_for_candidates(word,key1+key2):
				dict_of_two_keys=split_word(key1+key2)
				missing_letters=find_missing_letters(riddle_word_dictionary,dict_of_two_keys)
				if missing_letters in candidate_dictionary:
					for i in range(len(candidate_dictionary[missing_letters])):
						for j in range(len(candidate_dictionary[key1])):
							for k in range(len(candidate_dictionary[key2])):
								list_of_riddle_words.append([candidate_dictionary[key1][j],candidate_dictionary[key2][k],candidate_dictionary[missing_letters][i]])
	print(len(list_of_riddle_words))
	#return list_of_riddle_words
print(find_riddle("teresa krawczyk",set_of_words))
#find_riddle("sebastian dudek",set_of_words)


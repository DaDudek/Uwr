alphabet="aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
dict_of_letters=dict(zip(alphabet,[i for i in range(32)]))
def ceaser(s,k):
	while k<0:
		k=len(alphabet)+k
	przesuniecie=k%(len(alphabet))
	coded_word=[]
	for word in s.split():
		for letters in word:
			tmp=dict_of_letters[letters]+przesuniecie
			while tmp>len(dict_of_letters):
				tmp=tmp-len(dict_of_letters)
			coded_word.append(alphabet[tmp])
		coded_word.append(" ")
	coded_word=coded_word[:-1] #usuwanie nadmiarowej spacji
	return "".join(coded_word)
print(ceaser("dawid",13))
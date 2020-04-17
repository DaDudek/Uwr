from random import * 
corpus_file=open("korpus.txt")
dictionary=open("pol_ang.txt")
def count_words_in_corpus(): #zlicza liczbę wystąpień w korpusie
	corpus={}
	for lines in corpus_file:
			lines=lines.lower()
			words=lines.split()
			for word in words:
				if word not in corpus:
					corpus[word]=1
				else:
					corpus[word] += 1
	return corpus

def find_translated_words(): # szuka wszystkich tłumaczeń polskiego słowa na angielskie
	pol_ang={}
	for lines in dictionary:
		lines=lines.strip()
		if "=" not in lines:
			continue
		fields=lines.split("=")
		if len(fields)!= 2:
			continue
		key,translate=fields
		if key in pol_ang:
			pol_ang[key].append(translate)
		else:
			pol_ang[key]=[translate]
	return pol_ang

def translate(words):
	corpus=count_words_in_corpus()
	pol_ang=find_translated_words()
	score=[]
	words_list=words.split()
	for word in words_list:
		do_losowania=[] ## za kazdym razem potrzebuje nowe
		if word in pol_ang:
			tmp="" #sprawdza czy nasze tłumaczenie jest w korpusie
			for i in range(len(pol_ang[word])):
				if pol_ang[word][i] in corpus:	
					tmp=pol_ang[word][i]
					break
			if tmp!="":
				for i in range(len(pol_ang[word])): #porównuje które z tłumaczeń wystąpiło najwięcej razy w korpusie 
					if pol_ang[word][i] in corpus:	
						if corpus[pol_ang[word][i]]>corpus[tmp]:
							tmp=pol_ang[word][i]
				for k in range(len(pol_ang[word])): #wiem ze corpus[tmp] jest najwiekszy wiec dodaje warunek ktory doda rowniez pozostale najwieksze
					if pol_ang[word][k] in corpus:	
						if corpus[pol_ang[word][k]]==corpus[tmp]:
							do_losowania.append(pol_ang[word][k])
			
			
			score.append(choice(do_losowania))
		else:
			print("Brak tłumaczenia dla słowa")	
	return " ".join(score)
print(translate("mężczyzna leżeć w szpital a żona być smutny"))


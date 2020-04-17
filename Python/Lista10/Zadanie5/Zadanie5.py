def make_binary(number,lenght):
	tab=[]
	tmp=number
	while number!=0:
		if number%2==0:
			tab.append("0")
		else:
			tab.append("1")
		number=int(number/2)
	tab.reverse()
	binary_number="".join(tab)
	while len(binary_number)!=lenght:
		binary_number="0"+binary_number
	return binary_number

def generate_subsets(L):
	tab=[]
	subsets=[]
	for i in range(2**len(L)):
		tab.append(make_binary(i,len(L)))
	for k in range(1,len(tab)):
		tmps=[]
		for j in range(len(tab[k])):
			if tab[k][j]!="0":
				tmps.append(L[j])
		subsets.append(tmps)
	return subsets
def generate_abstraction_class(L):
	subsets=generate_subsets(L)
	abstraction_class=[]
	if len(L)>2:
		abstraction_class.append([[x] for x in L])
	trash=[]
	for element in subsets:
		missing=subtraction_for_list(L,element)
		if len(missing)==0:
			abstraction_class.append(L)
		if missing and element not in trash:
			abstraction_class.append([element,missing])
			if len(missing) != 2:
				x=generate_abstraction_class(missing)
				for elements in x:
					abstraction_class.append([element,elements])
			if (len(element)!=2):
				y = generate_abstraction_class(element)
				for some_elements in y:
					abstraction_class.append([some_elements,missing])
		trash.append(element)
		trash.append(missing)
	abstraction_class=clean_abstraction_class(abstraction_class)
	return abstraction_class
def subtraction_for_list(L1,L2):
	help_list=[e for e in L1]
	for element in L2:
		help_list.remove(element)
	return help_list
def clean_abstraction_class(L):
	for element in L:
		if L.count(element)>1:
			tmp= L.count(element)
			for i in range(tmp-1):
				L.remove(element)
	return L
x=generate_abstraction_class([1,2,3,4])
[print(xs) for xs in x]

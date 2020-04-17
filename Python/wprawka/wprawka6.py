def splitList(List):
	if len(List)%2==0:
		return List[:int(len(List)/2)],List[int(len(List)/2):]
	else:
		return List[:int((len(List)+1)/2)],List[int((len(List)+1)/2):]
def merge(L1,L2):
	List=list()
	i=0
	j=0
	while (i<len(L1) and j<len(L2)):
		if L1[i]<=L2[j]:
			List.append(L1[i])
			i=i+1
		else:
			List.append(L2[j])
			j=j+1
	while(i<len(L1)):
		List.append(L1[i])
		i=i+1
	while(j<len(L2)):
		List.append(L2[j])
		j=j+1
	return List
def mergesort(L):
	if len(L)==1:
		return L
	else:
		L1,L2=splitList(L)
		sorted_list=merge(mergesort(L1),mergesort(L2))
	return sorted_list
print(splitList([1,2,3,4,5,6,7,8,9]))
print()
print(merge([1,3,5,8,12],[2,4,6,7,8,12]))
print()
print(mergesort([1,325,457,58,234,12,754,875,2143,21452,134123,14,23523,13,-2,231523,2]))

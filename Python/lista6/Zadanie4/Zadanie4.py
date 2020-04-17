def podziel(napis):	
	Lista_slow=[]
	napis=napis+" "
	tmp=""
	i=0
	while(i<len(napis)-1):
		if napis[i]!=" ":
			tmp=tmp+napis[i]
			i=i+1
		if napis[i]==" ":
			if tmp!="":
				Lista_slow.append(tmp)
			tmp=""
			i=i+1
	return Lista_slow
napis="  Ala    ma     kota  a on ma owce    a  "
print(podziel(napis))

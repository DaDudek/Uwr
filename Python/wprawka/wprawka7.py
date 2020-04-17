numbers=[i for i in range(10)]
def f(L,i):
    if len(L)==1:
        return str(L)
    tmp=""
    for el in L[1:]:
        tmp=tmp+str(el)
    try1=str(L[0])+"+"+f(L[1:],0)
    try2=str(L[0])+"-"+f(L[1:],0)
    try3=str(L[0])+"*"+f(L[1:],0)
    if eval(try1)==2020:
        return try1
    if eval(try2)==2020:
        return try2
    if eval(try3)==2020:
        return try3

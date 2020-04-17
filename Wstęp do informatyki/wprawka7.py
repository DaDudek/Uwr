def f(L):
    Listdod=[]
    Listujm=[]
    Listmnoz=[]
    if len(L)==1:
        return [str(L[0])]
    for el in f(L[1:]):
        Listdod.append(str(L[0])+"+"+str(el))
        Listdod.append(str(L[0])+el)
    for el in f(L[1:]):
        Listujm.append(str(L[0]) + "-" + str(el))
    for el in f(L[1:]):
        Listmnoz.append(str(L[0]) + "*" + str(el))
    List=Listdod+Listmnoz+Listujm
    for el in List:
        if el[0]=="0":
            el=el[1:]
        if el[0]=="*":
            el = el[1:]
        if eval(el)==2020:
            if "0" not in el and (el[0]=="+" or el[0]=="-"): 
                return "0"+el
    return List
print(f([x for x in range(10)]))
class TreeItem:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
class ListItem:
    def __init__(self,value):
        self.val=value
        self.next=None
tree1=TreeItem(1)
tree2=TreeItem(2)
tree3=TreeItem(3)
tree4=TreeItem(4)
tree5=TreeItem(5)
tree6=TreeItem(6)
tree7=TreeItem(7)

trs4=TreeItem(400)
trs3=TreeItem(300)
trs2=TreeItem(200)
trs1=TreeItem(100)
trs7=TreeItem(700)
trs6=TreeItem(600)
trs5=TreeItem(500)



trs4.left=trs2
trs4.right=trs6

trs2.left=trs1
trs2.right=trs3

trs6.left=trs5
trs6.right=trs7

tree4.left=tree2
tree4.right=tree6

tree2.left=tree1
tree2.right=tree3

tree6.left=tree5
tree6.right=tree7

tree9=TreeItem(9)
tree7.right=tree9


"""Zadanie 1a) wstawiaj 1 -> 2 ->3 ... 
1b) wstaw środek przedziału i jako lewe dziecko ustaw środek lewego podziału a jako prawe środek prawego"""

def glebokosc(root): # zadanie 3
    if root.left==None and root.right==None:
        return 0
    lewa=0
    prawa=0
    if root.left!=None:
        lewa=glebokosc(root.left)+1
    if root.right!=None:
        prawa=glebokosc(root.right)+1
    return max(lewa,prawa)
def write(root): # Zad 4
    if(root!=None):
        write( root.left)
        if root.val>0:
            print(root.val)
        write( root.right)

def Zadanie_6(root1,root2):
    pierw=root2
    while root2.left!=None:
        root2=root2.left
    root2.left=root1
    return pierw

def wypisz(t):
    if(t!=None):
        print(t.val)
        wypisz(t.left)
        wypisz(t.right)
def ile_elementow(root): # zadanie 3
    if root.left==None and root.right==None:
        return 1
    lewa=0
    prawa=0
    if root.left!=None:
        lewa=ile_elementow(root.left)
    if root.right!=None:
        prawa=ile_elementow(root.right)
    return lewa+prawa+1
def rotacja(korzen,rodzic,dziecko):
    pierw=korzen
    u=rodzic
    v=dziecko
    if v.right!=None:
        prawe_dziecka=v.right
        tmp=prawe_dziecka
        v.right=u
        u.left=tmp
        return pierw
    else:
        v.right=u
def pomocnicza(root,lista): # Zad 4
    if(root!=None):
        lista.next=ListItem(root.val)
        pomocnicza( root.left,lista.next)
        lista.next=ListItem(root.val)
        pomocnicza( root.right,lista.next)
lista=ListItem(0)
pomocnicza(tree4,lista)
lista=lista.next
while lista.next!=None:
    print(lista.val)
    lista=lista.next
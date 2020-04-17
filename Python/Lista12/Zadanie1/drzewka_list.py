def add_to_tree(tree, e):
    if tree == []:
        tree += [e, [], []]
    a, left, right = tree
    if e < a:  
        add_to_tree(left, e)
    if e > a:  
        add_to_tree(right, e)

def in_tree(e, tree):
    if tree == []:
        return False
    a, left, right = tree    
    if a == e:
        return True
    if e < a:
        return in_tree(e, left)
    return in_tree(e, right)
    
    
def list_to_tree(L):
    tree = []
    for e in L:
        add_to_tree(tree, e)
    return tree

def tree_to_list(tree):
    if tree == []:
        return []
    a, left, right = tree  
    return tree_to_list(left) + [a] + tree_to_list(right)

def nasz_iterator(tree):
    if tree == []:
        return
    a, left, right = tree  
    for e in nasz_iterator(left):
        yield e
    yield a
    
    for e in nasz_iterator(right):
        yield e
        
        

def tree_set_sort(L):
    t = list_to_tree(L)
    return tree_to_list(t)
    
      

class Set:
    def __init__(self, *args):
        self.tree = []
        for e in args:
            self.add(e)
        
    def add(self, e):
       add_to_tree(self.tree, e)
       
    def __contains__(self, e):
        return in_tree(e, self.tree)   
    
    def __or__(self, other):
        wynik = Set()
        for e in self:
            wynik.add(e)
        for e in other:
            wynik.add(e)
        return wynik
    
    def __iter__(self):
        return nasz_iterator(self.tree)
               
    def __str__(self):
        lista = tree_to_list(self.tree)
        
        return '{' + ','.join([str(x) for x in lista]) + '}'                     

    def __len__(self):
        return len(tree_to_list(self.tree))
    """ewentualnie counter=0 for e in list counter++"""

    def __and__(self, other):
        wynik=Set()
        for e in self:
            if in_tree(e,list_to_tree(other)):
                wynik.add(e)
        return wynik
    """używam list to tree ponieważ konstruktor bazowo tworzy tablice"""

    def __sub__(self, other):
        wynik=Set()
        for e in self:
            if not in_tree(e,list_to_tree(other)):
                wynik.add(e)
        return wynik


print(len(Set(4,7,2,3)))
print(Set(1,2) - Set(2,3,4))
print(Set(1,2) & Set(2,3,4))

   


class Num:
    def __init__(self,value):
        self.value=value
    def eval(self,dict_of_value):
        return self.value


class Var:
    def __init__(self,value):
        self.value=value
    def eval(self,dict_of_values):
        if "*" not in self.value and "-" not in self.value and "+" not in self.value and "/" not in self.value:
            return dict_of_values[self.value]

    def __add__(self, other):
        return Var("("+self.value + "+" + other.value+")")
    def __str__(self):
        return self.value


class Exp:
    def __init__(self,operator,lewe,prawe):
        self.operator=operator
        self.lewe=lewe
        self.prawe=prawe
    def eval(self,dict_of_value):
        wl=self.lewe.eval(dict_of_value)
        wp=self.prawe.eval(dict_of_value)
        return


e1=Num(3)
e2=Var("x")
e3=Exp("+",e1,e2)
e3.eval({"x":5, "y":8})
print(e3.eval({"x":5}))


e4=Var("x")+Var("y")
print(e4)
e6=Var("y")+Var("x")
print(e6)


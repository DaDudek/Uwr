from hidden_cart import HiddenCart


class HiddenCartReader:
    def __init__(self, file):
        self.file = file
        self.list_of_hidden_cart = []

    def make_hidden_carts(self,):
        tmp=0
        for line in self.file:
            if tmp:
                line.strip()
                counter = 0
                for word in line.split(";"):
                    if counter == 0:
                        name = word
                    elif counter == 1:
                        cart_type = word
                    elif counter == 2:
                        if word == "transport" or word == "power_station":
                            value = word
                        else:
                            if int(word) > 40:
                                value = int(word) * 1000
                            else:
                                value = int(word)
                    elif counter == 3:
                        info = word
                    counter += 1
                cart = HiddenCart(name, cart_type, value, info)
                self.list_of_hidden_cart.append(cart)
            tmp += 1
        return self.list_of_hidden_cart

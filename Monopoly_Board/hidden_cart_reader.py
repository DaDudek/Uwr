from hidden_cart import HiddenCart


class HiddenCartReader:
    """
    This is a class for create hidden cart from csv file

        Attributes:
            file -> csv file where are information about all hidden carts
    """
    def __init__(self, file):
        """
        The constructor for HiddenCartReader class.

        :param file: csv file where are information about all hidden carts

        list_of_hidden_cart: (list) : when reader create cart its append her here
        """
        self.file = file
        self.list_of_hidden_cart = []

    def make_hidden_carts(self,):
        """
         The function to create all hidden carts - main function of that class

         This function read all lines from file, split it and create cart

        :return: void -> only change object
        """
        tmp = 0
        for line in self.file:
            if tmp:
                line.strip()
                counter = 0
                name = ""
                cart_type = ""
                value = 0
                info = ""
                for word in line.split(","):
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

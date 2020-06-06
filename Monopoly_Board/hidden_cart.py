from cart import Cart


class HiddenCart(Cart):
    """
        This is a class for represents HiddenCart objects - cell number 2, 7, 17, 22, 33, 36

        This class extends Cart class

        Attributes:
            coordinate, name: act the same as on Cart class (coordinate -1 because what hidden cart we roll is random)
            cart_type (String) : give information what event whe get from this cart
            value (String/int) : give information about how handle event from cart_type (get money/lose money etc)
            info (String) : Information about what we roll to display on screen for user
    """
    def __init__(self, name, cart_type, value, info):
        """

        :param name:  act the same as on Cart class
        :param cart_type: (String) : give information what event whe get from this cart
        :param value: (String/int) : give information about how handle event from cart_type (get money/lose money etc)
        :param info: (String) : Information about what we roll to display on screen for user
        """
        super().__init__(-1, name)
        self.cart_type = cart_type
        self.value = value
        self.info = info

    def __str__(self):
        return self.info

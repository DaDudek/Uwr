from cart import Cart


class HiddenCart(Cart):
    def __init__(self, name, cart_type, value, info):
        super().__init__(-1, name)
        self.cart_type = cart_type
        self.value = value
        self.info = info.strip()

    def __str__(self):
        return self.info

from cart import Cart


class TaxCart(Cart):
    def __init__(self, coordinate, name, section, amount_of_tax):
        super().__init__(coordinate, name,)
        self.section=section
        self.amount_of_tax = amount_of_tax

    def stand_in_cell(self, player, board):
        player.money -= self.amount_of_tax
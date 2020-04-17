from cart import Cart
from player_communication import PlayerCommunication

class TransportCart(Cart):
    def __init__(self, coordinate, name, section, cost, mortgage_value, value_with_houses, owner=None):
        super().__init__(coordinate, name,)
        self.number_of_hotel = 0
        self.section = section
        self.cost = cost
        self.mortgage_value = mortgage_value
        self.value_with_houses = value_with_houses
        self.owner = owner
        self.number_of_houses = 0

    def stand_in_cell(self, player, board):
        if self.owner is None and player.money > self.cost:
            print("Gracz " + player.name)
            print("Czy chcesz kupić pole: " + self.name + " o cenie: " + str(self.cost))
            print("Jeśli tak wpisz 1, wpp wpisz 0")  # moze generowac wyjatki
            if PlayerCommunication().choose_option():
                super().buy_cell(player, self.cost, self.section, self.coordinate)
        elif self.owner is not None:
            if not self.owner.in_prison:
                self.owner.money += self.value_with_houses[self.number_of_houses]
                player.money -= self.value_with_houses[self.number_of_houses]
                print(player.name + " zapłaciłeś graczowi " + self.owner.name)

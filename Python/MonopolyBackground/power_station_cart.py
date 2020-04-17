from cart import Cart
from random import randint
from player_communication import PlayerCommunication

class PowerStationCart(Cart):
    def __init__(self, coordinate, name, section, cost, mortgage_value, owner=None):
        super().__init__(coordinate, name,)
        self.section = section
        self.cost = cost
        self.mortgage_value = mortgage_value
        self.owner = owner

    def stand_in_cell(self, player, board):
        if self.owner is None and player.money > self.cost:
            print("Gracz " + player.name)
            print("Czy chcesz kupić pole: " + self.name + " o cenie: " + str(self.cost))
            print("Jeśli tak wpisz 1, wpp wpisz 0")  # moze generowac wyjatki
            if PlayerCommunication().choose_option():
                super().buy_cell(player, self.cost, self.section, self.coordinate)
        elif self.owner is not None:
            if not self.owner.in_prison:
                throw_a_dice = randint(2, 12)
                if self.owner.countries[self.section] == board.id_type_cells:
                    self.owner.money += 10 * throw_a_dice * 10000
                    player.money -= 10 * throw_a_dice * 10000
                else:
                    self.owner.money += 4 * throw_a_dice * 10000
                    player.money -= 4 * throw_a_dice * 10000
            print(player.name +" zapłaciłeś graczowi "+ self.owner.name)

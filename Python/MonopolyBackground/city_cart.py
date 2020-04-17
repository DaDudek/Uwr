from cart import Cart
from player_communication import PlayerCommunication


class CityCart(Cart):
    def __init__(self, coordinate, name, section, cost, house_prize, hotel_prize, mortgage_value,
                 value_with_houses, value_with_hotel, owner=None):
        super().__init__(coordinate, name, 0, 0)
        self.section = section
        self.cost = cost
        self.house_prize = house_prize
        self.hotel_prize = hotel_prize
        self.mortgage_value = mortgage_value
        self.value_with_houses = value_with_houses
        self.value_with_hotel = value_with_hotel
        self.owner = owner
        self.number_of_houses = 0
        self.number_of_hotel = 0
        self.how_much_to_pay=value_with_hotel if self.number_of_houses == 5 else self.value_with_houses[self.number_of_houses]

    def stand_in_cell(self, player, board):
        if self.owner is None and player.money > self.cost:
            print("Gracz " + player.name)
            print("Czy chcesz kupić pole: " + self.name + " o cenie: " + str(self.cost))
            print("Jeśli tak wpisz 1, wpp wpisz 0")  # moze generowac wyjatki
            if PlayerCommunication().choose_option():
                super().buy_cell(player, self.cost, self.section, self.coordinate)
        elif player.money <= self.cost:
            print("Gracz " + player.name + " nie stać cię na zakup tego pola")
        elif self.owner is not None:
            if not self.owner.in_prison:
                if self.number_of_hotel == 1:
                    self.owner.money += self.value_with_hotel
                    player.money -= self.value_with_hotel
                elif self.owner.countries[self.section] == board.id_type_cells:
                    self.owner.money += 2 * self.value_with_houses[self.number_of_houses]
                    player.money -= 2 * self.value_with_houses[self.number_of_houses]
                else:
                    self.owner.money += self.value_with_houses[self.number_of_houses]
                    player.money -= self.value_with_houses[self.number_of_houses]
            print(player.name +" zapłaciłeś graczowi "+ self.owner.name)


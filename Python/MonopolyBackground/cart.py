from random import choice
from player_communication import PlayerCommunication
"""cena zastawu, cena domku, cena hoteli, cena sprzedazy domkow, cena sprzedazy hoteli, """


class Cart:
    def __init__(self, coordinate, name="event", number_of_houses=0, number_of_hotel=0):
        self.name=name
        self.coordinate=coordinate
        self.owner = None

    def __str__(self):
        return "Pole: " + self.name

    def buy_cell(self, player, cost, section, coordinate):
        self.owner = player
        player.property.append(self)
        player.money -= cost
        if section not in player.countries:
            player.countries[section] = [coordinate]
        else:
            player.countries[section].append(coordinate)

    def stand_in_event_cell(self, player, board):
        if player.coordinate in [0, 10, 20]:
            pass
        elif player.coordinate == 30:
            print(player.name + " Idziesz do więzienia (na dwie tury)")
            del board.board[player.coordinate][1]
            player.coordinate = 10
            board.board[10].append(player)
            print("Czy chcesz się wykupić za 500k ?")
            print("1: Tak", "0: Nie")
            option = PlayerCommunication().choose_option()
            if option and player.money > 500 * 1000:
                player.money -= 500 * 1000
            else:
                if player.out_of_prison == 0:
                    player.prison_counter = 2
                    player.in_prison = True


    def stand_in_hidden_cell(self, player, board):
        hidden_cart = choice(board.hidden)
        if hidden_cart.cart_type == "get_money":
            player.money += hidden_cart.value
        elif hidden_cart.cart_type == "lose_money":
            player.money -= hidden_cart.value
        elif hidden_cart.cart_type == "go_back_by_index":
            pass
            del board.board[player.coordinate][1]
            player.coordinate -= hidden_cart.value
            if player.coordinate == -1:
                player.coordinate = 39
            board.board[player.coordinate].append(player)
        elif hidden_cart.cart_type == "go_to_place_by_kind":
            del board.board[player.coordinate][1]
            if hidden_cart.value == "transport":
                if 0 <= player.coordinate <= 4 or 35 <= player.coordinate <= 39:
                    if 35 <= player.coordinate <= 39:
                        player.money += 2000 * 1000
                    player.coordinate = 5
                elif 5 <= player.coordinate <= 14:
                    player.coordinate = 15
                elif 15 <= player.coordinate <= 24:
                    player.coordinate = 25
                elif 25 <= player.coordinate <= 34:
                    player.coordinate = 35
            else:
                if 12 <= player.coordinate < 38:
                    player.coordinate = 38
                else:
                    player.coordinate = 12
            board.board[player.coordinate].append(player)
        elif hidden_cart.cart_type == "go_to_place_by_index":
            del board.board[player.coordinate][1]
            if player.coordinate > hidden_cart.value:
                player.money += 2000 * 1000 # za przejscie przez start
            player.coordinate = hidden_cart.value
            board.board[player.coordinate].append(player)
        elif hidden_cart.cart_type == "pay_for_buildings":
            player.money -= hidden_cart.value * player.number_of_houses
            player.money -= hidden_cart.value * player.number_of_hotel
        elif hidden_cart.cart_type == "get_out_of_prison":
            player.out_of_prison += 1
        elif hidden_cart.cart_type == "go_to_prison":
            del board.board[player.coordinate][1]
            player.coordinate = 10
            board.board[10].append(player)
            print("Czy chcesz się wykupić za 500k ?")
            print("1: Tak","0: Nie")
            option = PlayerCommunication().choose_option()
            if option and player.money > 500 * 1000:
                player.money -= 500 * 1000
            else:
                if player.out_of_prison == 0:
                    player.prison_counter = 2
                    player.in_prison = True
        elif hidden_cart.cart_type == "pay_other_players":
            for players in board.players_queue[1:]:
                players.money += hidden_cart.value
                player.money -= hidden_cart.value
        elif hidden_cart.cart_type == "get_from_players":
            for players in board.players_queue[1:]:
                players.money -= hidden_cart.value
                player.money += hidden_cart.value
        print(player.name + " " + hidden_cart.info)

    def stand_in_cell(self, player, board):
        if player.coordinate in board.id_type_cells["hidden"]:
            self.stand_in_hidden_cell(player, board)
        else:
            self.stand_in_event_cell(player, board)

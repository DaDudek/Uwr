from random import randint
from player_communication import PlayerCommunication


class Player:
    def __init__(self, name,):
        self.name = name
        self.money = 10000000
        self.coordinate = 0
        self.number_of_houses = 0
        self.number_of_hotel = 0
        self.property = []
        self.countries = {} # key section value number of cell
        self.in_prison = False
        self.prison_counter = 0
        self.out_of_prison = 0
        self.pair_counter = 0
        self.have_pair = False
    def go_bankrupt(self):
        self.number_of_houses = 0
        self.number_of_hotel = 0
        for cart in self.property:
            cart.owner = None
        self.property = []
        self.countries = {}
        self.in_prison = False
        self.prison_counter = 0
        self.out_of_prison = 0
        self.pair_counter = 0
        self.have_pair = False
    def choose_cart(self, player):
        print("Wybierz karte: ")
        counter = 0
        for el in player.property:
            print(counter + 1,": ", el)
            counter += 1
        return player.property[PlayerCommunication().choose_option()-1]

    def choose_player(self, player_list):
        counter = 0
        print("Wybierz gracza")
        for players in player_list:
            print(counter + 1, " : ", players )
            counter += 1
        return player_list[PlayerCommunication().choose_option()-1]

    def make_trade(self, seller, cart, buyer, cost):
        seller.money += cost
        buyer.money -= cost
        seller.property.remove(cart)
        buyer.property.append(cart)
        seller.countries[cart.section].remove(cart.coordinate)
        if cart.section in buyer.countries:
            buyer.countries[cart.section].append(cart.coordinate)
        else:
            buyer.countries[cart.section] = [cart.coordinate]
        cart.owner = buyer

    def buy_from_player(self, board,):
        players_with_carts = []
        for player in board.players_queue:
            if len(player.property):
                players_with_carts.append(player)
        if not len(players_with_carts):
            print("Nie ma od kogo kupić")
        else:
            player = self.choose_player(players_with_carts)
            cart = self.choose_cart(player)
            if not (cart.number_of_houses or cart.number_of_hotel):
                print("Podaj proponowana kwote")
                cost = PlayerCommunication().choose_option()
                print("Gracz: " + player.name + " czy wyrazasz zgode na zakup tej karty za  " + str(cost) + " ?")
                print("Tak: 1", "Nie: 0")
                option = PlayerCommunication().choose_option()
                if option:
                    self.make_trade(player, cart, self, cost)
            else:
                print("Budowle na polu, zakaz handlu")

    def sell_to_player(self, board):
        player = self.choose_player(board)
        cart = self.choose_cart(self)
        if not (cart.number_of_houses or cart.number_of_hotel):
            print("Podaj proponowana kwote")
            cost = PlayerCommunication().choose_option()
            print("Gracz: " + player.name + " czy chcesz kupic ta karte za  " + str(cost) + " ?")
            print("Tak: 1", "Nie: 0")
            option = PlayerCommunication().choose_option()
            if option:
                self.make_trade(self, cart, player, cost)
        else:
            print("Budowle na polu, zakaz handlu")

    def check_for_buying_house(self, board, cell):
        if cell.section in self.countries and self.money > cell.house_prize and cell.number_of_houses < 4:
            for place in board.sector[cell.section]:
                if place not in self.countries[cell.section]:
                    return False
            return True
        return False

    def check_for_buying_hotel(self, cell): #cell by cart:
        if cell.number_of_houses == 4 and self.money > cell.hotel_prize and cell.number_of_hotel < 1:
            return True
        return False

    def buy_house(self, board, cell):
        if self.check_for_buying_house(board, cell):
            self.number_of_houses += 1
            self.money -= cell.house_prize
            cell.number_of_houses += 1
        else:
            print("nie spełniasz warunków zakupu domku ")

    def buy_hotel(self, cell):
        if self.check_for_buying_hotel(cell):
            self.number_of_hotel += 1
            self.money -= cell.hotel_prize
            cell.number_of_hotel += 1
            cell.number_of_houses = 0
        else:
            print("nie spełniasz warunków zakupu hotelu")

    def sell_house(self, cell):
        if cell.number_of_houses > 0:
            cell.number_of_houses -= 1
            self.money += int(cell.house_prize * 0.5)
            self.number_of_houses -= 1
        else:
            print("Nie spelniasz warunkow sprzedazy")

    def sell_hotel(self, cell):
        if cell.number_of_hotel > 0:
            cell.number_of_hotel -= 1
            self.money += cell.hotel_prize
            self.number_of_hotel -= 1
        else:
            print("Nie masz czego sprzedać")

    def move(self, board):
        if self.prison_counter == 0:
            self.in_prison = False
            dice1= randint(1, 6)
            dice2=randint(1, 6)
            how_many_cells = dice1 + dice2
            if dice2 == dice1:
                self.have_pair = True
                self.pair_counter += 1
                if self.pair_counter != 3:
                    print("Wylosowałeś pare masz dodatkowy ruch")
                else:
                    "Trzecia para - idziesz do więzienia"
                    self.pair_counter = 0
                    self.have_pair = False
            else:
                self.pair_counter = 0
                self.have_pair = False
            del board.board[self.coordinate][1]
            if self.pair_counter == 3:
                self.coordinate = 30
                board.board[30].append(self)
            else:
                if self.coordinate + how_many_cells > 39:
                    self.money += 2000 * 1000
                board.board[(self.coordinate + how_many_cells) % 40].append(self)
                self.coordinate = (self.coordinate + how_many_cells) % 40
        else:
            self.prison_counter -= 1
            print(self.name + " pozostalo " + str(self.prison_counter) + " tur w więzieniu")

    def __str__(self):
        return self.name + " pieniądze: " + str(self.money) + " posiadłości: " + " ,".join(
            [x.name for x in self.property])


class Player:
    def __init__(self, board):
        """
        Constructor of player class

        :param board: (board)

        number (int) player number - between 1 and 4
        in_bankrupt (boolean) flag to know if player bankrupt
        money - (int/double) give information about how much money player have
        coordinate - (int) coordinate where player is  - between 0 and 39
        number_of_houses (int) flag to check how many house player have (for future)
        number_of_hotel (int) flag to check how many hotel player have (for future)
        property - (list) list of cell that player have (card objects not int)
        countries - (dict) key is country kind (yellow, red etc),
                            value is list of card objects form that country that player have
        in_prison - (int) flag to know if the player is in prison
        prison_counter - (int) flag to know how many turn more player is in prison
        out_of_prison - (int) flag to know that player have "out of jail card" - for future
        have_pair - (boolean) flag to know that player can roll dice again
        """
        self.number = 0
        self.is_bankrupt = False
        self.money = 15000000
        self.coordinate = 0
        self.number_of_houses = 0
        self.number_of_hotel = 0
        self.property = []
        self.countries = {}  # key section value number of cell
        self.in_prison = False
        self.prison_counter = 0
        self.out_of_prison = 0
        self.pair_counter = 0
        self.have_pair = False
        board.players_queue.append(self)
        board.board[0].append(self)

    def card_out_of_prison(self):
        """
        The function to return how many out_of_jail cards player have (for future)

        :return: (int) value of how many cards
        """
        return self.out_of_prison

    def out_of_prison_by_cash(self):
        """
        This function is used to go out from jail using cash (one of three option)

        :return: void -> (only change objects)
        """
        self.in_prison = False
        self.prison_counter = 0
        self.money -= 500 * 1000

    def out_of_prison_by_card(self):
        """
            This function is used to go out from jail using card (one of three option, for future)

            :return: void -> (only change objects)
        """
        if self.out_of_prison > 0:
            self.in_prison = False
            self.prison_counter = 0
            self.out_of_prison -= 1

    def stand_in_prison(self):
        """
            This function is used to count turn if player in prison  (if player in prison he lose 2 turn)

            :return: void -> (only change objects)
        """
        if self.prison_counter > 0:
            self.prison_counter -= 1
        else:
            self.in_prison = 0

    def go_bankrupt(self):
        """
        This function is used to free all the cells when player is bankrupt

        :return: void -> (only change objects)
        """
        self.number_of_houses = 0
        self.number_of_hotel = 0
        for card in self.property:
            card.owner = None
        self.property = []
        self.countries = {}
        self.in_prison = False
        self.prison_counter = 0
        self.out_of_prison = 0
        self.pair_counter = 0
        self.have_pair = False
        self.is_bankrupt = True

    def make_trade(self, seller, card, buyer, cost):
        """
        This function is used to make trade between two player - one of them pays
                                                                    to get a cell that the second one have

        :param seller: (player) person who is selling
        :param card: (card) cell that is gonna be sell
        :param buyer: (player) player who bought cell
        :param cost: (int) how much seller get for selling the cell

        :return: void -> only change objects
        """
        seller.money += cost
        buyer.money -= cost
        seller.property.remove(card)
        buyer.property.append(card)
        seller.countries[card.section].remove(card.coordinate)
        if card.section in buyer.countries:
            buyer.countries[card.section].append(card.coordinate)
        else:
            buyer.countries[card.section] = [card.coordinate]
        card.owner = buyer

    def sell_to_player(self, player, card, cost):
        """
        This function first check if player can sell a cell to another player and after using make trade to do this
         # who sell, who buy, what buy, what is a prize

        :param player: (player) player who is gonna to buy a cell
        :param card: (card) what sell is going to be sold
        :param cost: (int) what is a prize for cell

        :return:  void -> only change objects
        """
        if (card.coordinate in [5, 15, 25, 35] or not (card.number_of_houses or card.number_of_hotel))\
                and player.money >= cost:
            self.make_trade(self, card, player, cost)

    def check_for_buying_house(self, board, cell):
        """
        This function is used to check is player is able to buy a house on some cell

        :param board: (board) background logic of board
        :param cell: (cell) where player want to stand house

        :return: (boolean) True if player is able, False if not
        """
        if cell.section in self.countries and self.money > cell.house_prize and\
                cell.number_of_houses < 4 and not cell.number_of_hotel:
            for place in board.sector[cell.section]:
                if place not in self.countries[cell.section]:
                    return False
            return True
        return False

    def check_for_buying_hotel(self, cell):
        """
            This function is used to check is player is able to buy a house on some cell
                we don't need board object because if houses stand on cell than we are sure he have country

            :param cell: (cell) where player want to stand house

            :return: (boolean) True if player is able, False if not
        """
        if cell.number_of_houses == 4 and self.money > cell.hotel_prize and cell.number_of_hotel < 1:
            return True
        return False

    def check_for_sell(self, cell, background):
        """
        This function is used to check is player is able to sell cell (to other player or to bank)
            we check power_station alone because this kind of cells don't have house/hotel
            we also check the traspont because we use fake houses there

        :param cell: (cell) cell that player want to sell
        :param background: (board) background logic of board

        :return: (int) return 0 if player is not able or 1 if he is
        """
        if cell.owner != self:
            return 0
        if cell.section == "power_station" or cell.section == "transport":
            return 1
        for city in self.countries[cell.section]:
            if background.board[city][0].number_of_hotel or background.board[city][0].number_of_houses:
                return 0
        return 1

    def buy_house(self, board, cell):
        """
        This function first check is player is able to buy cell and if he is, function do it

        :param board: (board) background logic of board
        :param cell: (cell) cell that player want to buy

        :return: void -> only change object
        """
        if self.check_for_buying_house(board, cell):
            self.number_of_houses += 1
            self.money -= cell.house_prize
            cell.number_of_houses += 1

    def buy_hotel(self, cell):
        """
        This function first check is player is able to buy hotel and if he is, function do it

        :param cell: (cell) cell where player want to stand hotel

        :return: void -> only change object
        """
        if self.check_for_buying_hotel(cell):
            self.number_of_hotel += 1
            self.money -= cell.hotel_prize
            cell.number_of_hotel += 1
            cell.number_of_houses = 0

    def sell_house(self, cell):
        """
        This function first check is player have houses on cell, and if he is function sell it

        :param cell: (cell) cell where player want to stand hotel

        :return: void -> only change object
        """
        if cell.number_of_houses > 0:
            cell.number_of_houses -= 1
            self.money += int(cell.house_prize * 0.5)
            self.number_of_houses -= 1

    def sell_hotel(self, cell):
        """
            This function first check is player have hotel on cell, and if he is function sell it

            :param cell: (cell) cell where player want to stand hotel

            :return: void -> only change object
            """
        if cell.number_of_hotel > 0:
            cell.number_of_hotel -= 1
            self.money += cell.hotel_prize * 0.5
            self.number_of_hotel -= 1

    def move(self, board, x, y):
        """
        This function is used to move player,
            first check is prison_counter  is 0 to give information about not being in prison/end of being there
            than function check is player have pair (if yes and its not third time in row he have another move)
            if it is third time in row player go to prison, if player don't have pair he is moved on the end of queue
            and deleting from cell where he was before throw the dice.
            In the end function check is player went through the start and if its true he get money

        :param board: (board) background logic of board
        :param x: (int) what is score of first dice (between 1 and 6)
        :param y: (int) what is score of second dice (between 1 and 6)

        :return: 1 if player must go to jail/is in jail, 0 in other case
        """
        if self.prison_counter == 0:
            self.in_prison = False
            how_many_cells = y + x
            if x == y:
                self.have_pair = True
                self.pair_counter += 1
                if self.pair_counter == 3:
                    self.pair_counter = 0
                    self.have_pair = False
                    self.in_prison = 1
                    self.prison_counter = 2
                    self.coordinate = 10
                    board.board[10].append(self)
                    return 1
            else:
                self.pair_counter = 0
                self.have_pair = False
                queue = board.players_queue[1:]
                board.players_queue = queue
                board.players_queue.append(self)
            del board.board[self.coordinate][1]  # board.board[x][0] is always card
            if self.coordinate + how_many_cells > 39:
                self.money += 2000 * 1000
            board.board[(self.coordinate + how_many_cells) % 40].append(self)
            self.coordinate = (self.coordinate + how_many_cells) % 40
            return 0
        else:
            return 1

    def bank_account(self):
        """
        This function is used to return how much player have money

        :return: (double) return how much player have money
        """
        return self.money

    def paid_tax(self, amout_of_tax):
        """
        This function is used to "paid tax" when player stand on tax cell

        :param amout_of_tax: (int) how much player must paid ( he paid to bank - just lose money)

        :return: void -> only change objects
        """
        self.money -= amout_of_tax

    def __str__(self):
        return str(self.number) + " pieniądze: " + str(self.money) + " posiadłości: " + " ,".join(
            [x.name for x in self.property])

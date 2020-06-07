from random import choice


class Card:
    """
        This is a class for represents Cell objects - all type of cells extends this class

             Attributes:
                coordinate: (int) number on board - between 0 and 39
                name: (String) name of cell
                owner: (player) player who own cell
                """

    def __init__(self, coordinate, name="event", number_of_houses=0, number_of_hotel=0):
        """

        :param coordinate: (int) number on board - between 0 and 39
        :param name: (String) name of cell
        :param number_of_hotel and house is used in other class
        """
        self.name = name
        self.coordinate = coordinate
        self.owner = None

    def __str__(self):
        return "Pole: " + self.name

    def sell_cell(self, cell):
        """
        The function to sell cell to bank, delete cell from player property and countries and give him money

        :param cell: (card)

        :return: void -> only change objects
        """
        player = cell.owner
        player.property.remove(cell)
        player.money += cell.cost * 0.8
        player.money = int(player.money)
        player.countries[cell.section].remove(cell.coordinate)
        cell.owner = None

    def buy_cell(self, player, cost, background_board, coordinate):
        """

        The function to sell buy cell from bank (when somebody stand on free cell)

        :param player:
        :param cost:
        :param background_board:
        :param coordinate:
        :return: void -> only change objects
        """
        cell = background_board.board[player.coordinate][0]
        section = cell.section
        self.owner = player
        player.property.append(self)
        player.money -= cost
        if section not in player.countries:
            player.countries[section] = [coordinate]
        else:
            player.countries[section].append(coordinate)



    def check_how_much_to_paid(self, board):
        """
        The function to return how much player who stand on cell must paid
        :param board: (board) Hidden part of game board - logic part of apk
        :return: (int) amount to pay
        """
        if self.number_of_hotel == 1:
            return self.value_with_hotel
        elif self.owner.countries[self.section] == board.sector[self.section] and self.number_of_houses == 0:
            return 2 * self.value_with_houses[self.number_of_houses]
        else:
            return self.value_with_houses[self.number_of_houses]

    def paid_for_staying(self, player, cost):
        """
        The function to take money from player for stand on not free cell
        :param player: (player) player who stand on this cell
        :param cost: (int) cost to paid for stand on cell
        :return: void - only change object
        """
        if not self.owner.in_prison:
            self.owner.money += cost
            player.money -= cost

    def stand_in_cell(self, player, board):
        """
        The function to give information about cell that player stand after roll

        :param player: (player) player who stand on this cell
        :param board: (board) Hidden part of game board - logic part of apk
        :return: (int / String) 7 - if player stand on 0, 10, 20 (nothing happend then)
                 4 - if player stand on go to prison cell
                 hidden card info - when player stand on hidden cell (2, 7, 17, 22, 33, 36)
        """
        if player.coordinate in board.id_type_cells["hidden"]:
            return self.stand_in_hidden_cell(player, board)
        else:
            return self.stand_in_event_cell(player, board)

    def stand_in_event_cell(self, player, board):
        """
        The function to give information about cell that player stand after roll

        :param player: (player) player who stand on this cell
        :param board: (board) Hidden part of game board - logic part of apk
        :return: (int) 7 - if player stand on 0, 10, 20 (nothing happend then)
                 4 - if player stand on go to prison cell
        """
        if player.coordinate in [0, 10, 20, 30]:
            return 7
        elif player.coordinate == 30:
            del board.board[player.coordinate][1]
            player.coordinate = 10
            board.board[10].append(player)
            player.prison_counter = 2
            player.pair_counter = 0
            player.in_prison = True
            return 4

    def stand_in_hidden_cell(self, player, board):
        """
        The function to give information about cell that player stand after roll

            :param player: (player) player who stand on this cell
            :param board: (board) Hidden part of game board - logic part of apk
            :return: (int) 7 - if player stand on 0, 10, 20 (nothing happend then)
                        4 - if player stand on go to prison cell
                """
        hidden_card = choice(board.hidden)
        if hidden_card.card_type == "get_money":
            player.money += hidden_card.value
        # elif hidden_card.card_type == "get_out_of_prison":
        #   player.out_of_prison += 1  for future
        return hidden_card.info

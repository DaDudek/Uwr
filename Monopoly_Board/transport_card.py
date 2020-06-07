from card import Card


class TransportCard(Card):
    """
        This is a class for represents City objects - cell number 5, 15, 25, 35

        This class extends card class

            Attributes:
                coordinate: act the same as on card class
                name: act the same as on card class
                section:(String) always transport, use to check for bonus (depends on how many transportcard owner have)
                cost: (int) how much user must paid when he want to buy this cell
                mortgage_value: (int) : in future can be used to use mortgage mechanic
                value_with_houses: (dict) how much user must paid when stand on cell
                                                with house(depends on how many transportcard owner have)
                owner: (player): who is owner of this cell - before buy/after sell to bank owner == None
            """
    def __init__(self, coordinate, name, section, cost, mortgage_value, value_with_houses, owner=None):
        """

        :param coordinate: act the same as on card class
        :param name: act the same as on card class
        :param section: (String) always transport, use to check for bonus (depends on how many transportcard owner have)
        :param cost: (int) how much user must paid when he want to buy this cell
        :param mortgage_value: (int) : in future can be used to use mortgage mechanic
        :param value_with_houses:  (dict) how much user must paid when stand on cell
                                                with house(depends on how many transportcard owner have)
        :param owner: (player): who is owner of this cell - before buy/after sell to bank owner == None
        """
        super().__init__(coordinate, name,)
        self.number_of_hotel = 0
        self.section = section
        self.cost = cost
        self.mortgage_value = mortgage_value
        self.value_with_houses = value_with_houses
        self.owner = owner
        self.number_of_houses = 0

    def stand_in_cell(self, player, board):
        """
        The function to give information about cell that player stand after roll

        :param player: (player) player who stand on this cell
        :param board: (board) Hidden part of game board - logic part of apk
        :return: 1 - if player is able to bought this cell
                    -1 - if cell don't have owner but player don't have enough money
                    -2 - if player already own this cell
                    0 - if someone else own this cell
        """
        if self.owner is None and player.money >= self.cost:
            return 1
        elif player.money < self.cost and self.owner is None:
            return -1
        elif self.owner == player:
            return -2
        elif self.owner is not None:
            return 0

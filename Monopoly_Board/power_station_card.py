from card import Card


class PowerStationCard(Card):
    """
        This is a class for represents PowerStation objects - cell number 12 and 28

        This class extends card class

        Attributes:
            coordinate, name: act the same as on card class
            section (String): always power_station, use to check for bonus (when you have cell 12 and 28)
            cost (int): how much user must paid when he want to buy this cell
            mortgage_value (int) : not use in this version of game, but in future can be used to use mortgage mechanic
            owner (player): who is owner of this cell - before buy/after sell to bank owner == None
    """
    def __init__(self, coordinate, name, section, cost, mortgage_value, owner=None):
        """
        The constructor for ComplexNumber class.

        :param coordinate: act the same as on card class
        :param name: act the same as on card class
        :param section: (String): always power_station, use to check for bonus (when you have cell 12 and 28)
        :param cost: (int): how much user must paid when he want to buy this cell
        :param mortgage_value: (int) : in future can be used to use mortgage mechanic
        :param owner: (player): who is owner of this cell - before buy/after sell to bank owner == None
        """
        super().__init__(coordinate, name,)
        self.section = section
        self.cost = cost
        self.mortgage_value = mortgage_value
        self.owner = owner

    def stand_in_cell(self, player, board):
        """
         The function to give information about cell that player stand after roll

        :param player: (player) player who stand on this cell
        :param board: (board) Hidden part of game board - logic part of apk
        :return: 1 - if player is able to bought this cell
                 -1 - if cell don't have owner but player don't have enough money
                 -2 - if player already own this cell
                 3 - if someone else own this cell
        """

        if self.owner is None and player.money >= self.cost:
            return 1
        elif player.money < self.cost and self.owner is None:
            return -1
        elif self.owner == player:
            return -2
        elif self.owner is not None:
            return 3

    def check_how_much_to_paid(self, cells_number):
        """
            The function to give information about how many player must paid for stand on there, where cell have owner
        :param cells_number: (int): how many points on dice player have
        :return: (int) how many player must paid (depends on whether owner have cell 12 and 28 or only one of them)
        """
        if len(self.owner.countries[self.section]) == 2:
            return 10 * cells_number * 10000
        return 4 * cells_number * 10000


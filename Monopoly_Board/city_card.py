from card import Card


class CityCard(Card):
    """
            This is a class for represents City objects - cell number 1, 3, 6, 8, 9, 11, 13, 14, 16,
                                                            18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39

            This class extends card class

            Attributes:
                coordinate: act the same as on card class
                name: act the same as on card class
                section: (String) color of cell (brown, yellow etc), used to check does the player have a state
                cost: (int) how much user must paid when he want to buy this cell
                house_prize: (int) how much user must paid when he want to buy a house
                hotel_prize: (int) how much user must paid when he want to buy a hotel
                mortgage_value: (int) : in future can be used to use mortgage mechanic
                value_with_houses: (dict) how much user must paid when stand on cell with house(depends on houses number)
                value_with_hotel: (int) how much user must paid when stand on cell with hotel
                owner: (player): who is owner of this cell - before buy/after sell to bank owner == None
        """
    def __init__(self, coordinate, name, section, cost, house_prize, hotel_prize, mortgage_value,
                 value_with_houses, value_with_hotel, owner=None):
        """

        :param coordinate: act the same as on card class
        :param name: act the same as on card class
        :param section: (String) color of cell (brown, yellow etc), used to check does the player have a state
        :param cost: (int) how much user must paid when he want to buy this cell
        :param house_prize: (int) how much user must paid when he want to buy a house
        :param hotel_prize: (int) how much user must paid when he want to buy a hotel
        :param mortgage_value: (int) : in future can be used to use mortgage mechanic
        :param value_with_houses: (dict) how much user must paid when stand on cell with house(depends on houses number)
        :param value_with_hotel: (int) how much user must paid when stand on cell with hotel
        :param owner: (player): who is owner of this cell - before buy/after sell to bank owner == None
        """
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
        self.how_much_to_pay = value_with_hotel if self.number_of_houses == 5 \
            else self.value_with_houses[self.number_of_houses]

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

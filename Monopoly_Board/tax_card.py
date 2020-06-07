from card import Card


class TaxCard(Card):
    """
            This is a class for represents Hiddencard objects - cell number 2, 7, 17, 22, 33, 36

            This class extends card class

            Attributes:
                coordinate, name: act the same as on card class
                section (String): always "pay", use to check for card type
                amount_of_tax: (int) how much player must paid
        """
    def __init__(self, coordinate, name, section, amount_of_tax):
        """

        :param coordinate: act the same as on card class (can be 2 or 38)
        :param name: act the same as on card class
        :param section: (String): always "pay", use to check for card type
        :param amount_of_tax: (int) how much player must paid
        """
        super().__init__(coordinate, name,)
        self.section = section
        self.amount_of_tax = amount_of_tax

    def stand_in_cell(self, player, board):
        """
        The function to give information about cell that player stand after roll

        :param player: (player) player who stand on this cell
        :param board: (board) Hidden part of game board - logic part of apk

        :return: 2 - player stand on tax cell
        """
        return 2

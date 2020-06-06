from Buyer import Buyer
from Seller import Seller


class Tradesman:
    """
    This class is used to do trades between players
    """
    def __init__(self, background, graphic_board):
        """
        Constructor of Tradesman class

        :param background (board): Hidden part of game board - logic part of apk
        :param graphic_board (graphic_board): Graphic part of game board - what user see
        """
        self.background = background
        self.graphic_board = graphic_board

    def make_trade(self, option):
        """
        This function is used to handle te buying event or selling event
        :param option: (int) if option != 0 it means that player want to buy something,
                                            else it means that he want to sell
        :return: void -> only change object
        """
        if option:
            Buyer(self.background, self.graphic_board).buy()
        else:
            Seller(self.background, self.graphic_board).sell()

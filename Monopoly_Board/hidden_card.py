from card import Card


class HiddenCard(Card):
    """
        This is a class for represents Hiddencard objects - cell number 2, 7, 17, 22, 33, 36

        This class extends card class

        Attributes:
            coordinate, name: act the same as on card class (coordinate -1 because what hidden card we roll is random)
            card_type (String) : give information what event whe get from this card
            value (String/int) : give information about how handle event from card_type (get money/lose money etc)
            info (String) : Information about what we roll to display on screen for user
    """
    def __init__(self, name, card_type, value, info):
        """

        :param name:  act the same as on card class
        :param card_type: (String) : give information what event whe get from this card
        :param value: (String/int) : give information about how handle event from card_type (get money/lose money etc)
        :param info: (String) : Information about what we roll to display on screen for user
        """
        super().__init__(-1, name)
        self.card_type = card_type
        self.value = value
        self.info = info

    def __str__(self):
        return self.info

from hidden_card import HiddenCard


class HiddencardReader:
    """
    This is a class for create hidden card from csv file

        Attributes:
            file -> csv file where are information about all hidden cards
    """
    def __init__(self, file):
        """
        The constructor for HiddencardReader class.

        :param file: csv file where are information about all hidden cards

        list_of_hidden_card: (list) : when reader create card its append her here
        """
        self.file = file
        self.list_of_hidden_card = []

    def make_hidden_cards(self,):
        """
         The function to create all hidden cards - main function of that class

         This function read all lines from file, split it and create card

        :return: void -> only change object
        """
        tmp = 0
        for line in self.file:
            if tmp:
                line.strip()
                counter = 0
                name = ""
                card_type = ""
                value = 0
                info = ""
                for word in line.split(","):
                    if counter == 0:
                        name = word
                    elif counter == 1:
                        card_type = word
                    elif counter == 2:
                        if word == "transport" or word == "power_station":
                            value = word
                        else:
                            if int(word) > 40:
                                value = int(word) * 1000
                            else:
                                value = int(word)
                    elif counter == 3:
                        info = word
                    counter += 1
                card = HiddenCard(name, card_type, value, info)
                self.list_of_hidden_card.append(card)
            tmp += 1
        return self.list_of_hidden_card

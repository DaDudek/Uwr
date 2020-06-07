from banker import Banker


class Board:
    """
        This is a class for represent board on game - most of the logic need this class

        Attributes:
             player_number (int) : how many players play on this game (basic 4)

    """
    def __init__(self, player_number=4):
        """
        The constructor for ComplexNumber class.

            :param player_number:  how many players play on this game (basic 4)

            board: (dict) this represent board with cells - key is a cell number,
                board[cell][0] is always cell card, board[cell][x], x>0 -> player who stand on the cell
            id_type_cells: (dict) key is a kind of cell (cities, power_stations etc)
                                        value is list of number of that kind cells
            hidden: (list) this is list of all hidden card
                            (in this version is only one event but it is prepare for future when will be more events)
            players_queue: (list (of players)) this represent players_queue, is used to control players order
            sector: (dict) this represent countries, key is country kind (yellow, red etc),
                                                        value is list of coordinates cell from that country
            actual_player: (player) represent current player
        """
        self.player_number = player_number
        self.board = {x: [] for x in range(40)}
        self.id_type_cells = {}
        self.hidden = []
        self.players_queue = []
        self.sector = {}
        self.actual_player = None

    def make_board(self):
        """
        The function to init board with all the cells  - banker create there and put on the board

        :return: void -> only change object
        """
        banker = Banker(open("monopoly_cards.csv"))
        banker.make_all_cards()
        for i in range(40):
            self.board[i] = [banker.cards[i]]
        self.id_type_cells = banker.id
        self.hidden = banker.hidden_cards
        self.sector = banker.sector

    def check_transport_cells(self):
        """
        This function is used to check how many transport cards player have

        :param players_queue: (list) list of player thats play the game

        :return: void -> only change object
        """
        for player in self.players_queue:
            #print(player.countries)
            if "transport" not in player.countries:
                player.countries["transport"] = []
            for transport in player.countries["transport"]:
                self.board[transport][0].number_of_houses = len(player.countries["transport"]) - 1


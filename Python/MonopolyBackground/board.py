from banker import Banker


class Board:
    def __init__(self, player_number=4):
        self.player_number = player_number
        self.board = {x: [] for x in range(40)}
        self.id_type_cells = {}
        self.hidden = []
        self.players_queue = []
        self.sector = {}

    def make_board(self):
        banker = Banker(open("monopoly_carts.csv"))
        banker.make_all_carts()
        for i in range(40):
            self.board[i] = [banker.carts[i]]
        self.id_type_cells = banker.id
        self.hidden = banker.hidden_carts
        self.sector=banker.sector

import pygame


class BoardAvatar:
    """

    """
    def __init__(self, coordinate_x, coordinate_y, screen, player_number, color, board):
        """
        This is a class for represents BoardAvatar objects

        :param coordinate_x: (int) coordinate x from graphic board
        :param coordinate_y: (int) coordinate y from graphic board
        :param screen: (pygame.display) its screen what user see
        :param player_number: (int) player number - between 1 and 4
        :param color: (tuple) one of four colors - help to recognize who is who
        :param board: (board) graphic board that user see

        in_prison - (int) flag to know if the player is in prison
        in_bankrupt (boolean) flag to know if player bankrupt
        money - give information about how much money player have
        after_rol (int) flag to know if the player roll the dice
        radius (int) size of circle that represent player on board
        properties (list) list of int that represent player properties
        """
        self.in_prison = 0
        self.is_bankrupt = False
        self.money = 15000000
        self.after_roll = 0
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.color = color
        self.screen = screen
        self.radius = 8
        self.sector = 0
        self.properties = []
        self.player_number = player_number
        self.cell = 0
        board.player_list.append(self)

    # place to stand
    def stand_avatar(self):
        """
        function to draw circle that represent player on user screen

        :return: void -> only drawing on screen
        """
        pygame.draw.circle(self.screen, self.color, [self.coordinate_x - self.radius, self.coordinate_y - self.radius],
                           self.radius)

    def go_to_prison(self):
        """
        This function change player coordinate to draw him on prison cell
        :return: void -> only change object
        """
        self.coordinate_x = 56
        self.coordinate_y = 819 - 20 * self.player_number
        self.cell = 10

    def move_avatar_by_one_cell(self):
        """
        This function is used to change player coordinate -> move for one cell to better visual effect

        :return: void -> only change object
        """
        if not self.cell:
            self.coordinate_x = 654
            self.coordinate_y = 819 - 20 * self.player_number

        elif 9 >= self.cell > 0:
            self.coordinate_x = self.coordinate_x - 60

        elif self.cell == 10:
            self.coordinate_x = 20 + 20 * self.player_number
            self.coordinate_y = 657

        elif 19 >= self.cell > 10:
            self.coordinate_y = self.coordinate_y - 60

        elif self.cell == 20:
            self.coordinate_x = 175
            self.coordinate_y = 20 + 20 * self.player_number

        elif 29 >= self.cell > 20:
            self.coordinate_x = self.coordinate_x + 60

        elif self.cell == 30:
            self.coordinate_x = 819 - 20 * self.player_number
            self.coordinate_y = 161

        elif 39 > self.cell > 30:
            self.coordinate_y = self.coordinate_y + 65

        elif self.cell == 39:
            self.coordinate_y = 819 - 20 * self.player_number
            self.coordinate_x = 762
        self.cell = (self.cell + 1) % 40


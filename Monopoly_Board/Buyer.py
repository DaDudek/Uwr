import pygame


class Buyer:
    """
    This is a class for buying houses/hotels/cells from bank/other player

    Attributes:
        background (board): Hidden part of game board - logic part of apk
        graphic_board (graphic_board): Graphic part of game board - what user see
    """
    def __init__(self, background, graphic_board):
        """
        The constructor for ComplexNumber class.

        :param background: (board): Hidden part of game board - logic part of apk
        :param graphic_board: (graphic_board): Graphic part of game board - what user see
        """
        self.background = background
        self.graphic_board = graphic_board

    def buy(self):
        """
            The function to choose - buy from bank or buy from other player

        :return: void - only change objects
        """
        self.graphic_board.screen.blit(pygame.image.load("graphic/buy_choice.png"), (127, 127))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                cur = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 392 >= cur[0] >= 158 and 350 >= cur[1] >= 250:
                        self.buy_from_player()
                        not_exit = 0
                    elif 662 >= cur[0] >= 399 and 350 >= cur[1] >= 250:
                        self.buy_from_bank()
                        not_exit = 0

    def buy_from_player(self):
        """
        The function to handle buying cell from other player

        First user choose other player from whose he want buy cell

        Than we generate all cells that can be bought

        In the end whe look what cell user choose and make a transaction
        :return: void only changes objects
        """
        not_exit = 1
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        player_who_sell = self.graphic_board.choose_player(self.graphic_board.player_list, self.background)
        player_who_sell_avatar = self.graphic_board.convert_player_to_avatar(player_who_sell)
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        pygame.display.update()
        for cell in player_who_sell_avatar.properties:
            if player_who_sell.check_for_sell(self.background.board[cell][0], self.background):
                name = "graphic/cell" + str(cell) + ".png"
                x = self.graphic_board.property_coordinates[cell][0]
                y = self.graphic_board.property_coordinates[cell][1]
                self.graphic_board.screen.blit(pygame.image.load(name), (x, y))
        self.graphic_board.screen.blit(pygame.image.load("graphic/property_button.png"), (160, 610))
        pygame.display.update()
        while not_exit:
            cur = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 670 >= cur[0] >= 160 and 670 >= cur[1] >= 610:
                        not_exit = 0
                    else:
                        for cell in player_who_sell_avatar.properties:
                            if self.graphic_board.property_coordinates[cell][0] + 120 >= cur[0] >= \
                                    self.graphic_board.property_coordinates[cell][0]:
                                if self.graphic_board.property_coordinates[cell][1] + 60 >= cur[1] >= \
                                        self.graphic_board.property_coordinates[cell][1]:
                                    offer = self.graphic_board.get_offer(self.background.actual_player)
                                    if int(offer) * 1000 < self.background.actual_player.money:
                                        permission = self.graphic_board.ask_for_permission(player_who_sell)
                                        if permission:
                                            player_who_sell.sell_to_player(self.background.actual_player,
                                                                           self.background.board[cell][0],
                                                                           int(offer) * 1000)
                                            player_who_sell_avatar.properties.remove(cell)
                                            self.graphic_board.player_list[0].properties.append(cell)
                                        not_exit = 0
                                        break
                                    else:
                                        not_exit = 0
                                        break

    def buy_from_bank(self):
        """
            The function to choose what user want to buy from bank - house or hotel
        :return: void only changes objects
        """
        self.graphic_board.screen.blit(pygame.image.load("graphic/buy_trade.png"), (127, 127))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                cur = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 394 >= cur[0] >= 213 and 369 >= cur[1] >= 195:
                        self.buy_house()
                        not_exit = 0
                    elif 600 >= cur[0] >= 421 and 366 >= cur[1] >= 197:
                        self.buy_hotel()
                        not_exit = 0

    def buy_house(self):
        """
            The function to handle buying house from bank

            First generate all cells where house can be stand

            Than whe look what cell user choose and buy a house for this cell (if have money)

            :return: void only changes objects
        """
        not_exit = 1
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        for cell in self.graphic_board.player_list[0].properties:
            if cell in self.graphic_board.cells_where_house_can_stand:
                if self.background.actual_player.check_for_buying_house(self.background,
                                                                        self.background.board[cell][0]):
                    name = "graphic/cell" + str(cell) + ".png"
                    x = self.graphic_board.property_coordinates[cell][0]
                    y = self.graphic_board.property_coordinates[cell][1]
                    self.graphic_board.screen.blit(pygame.image.load(name), (x, y))
        self.graphic_board.screen.blit(pygame.image.load("graphic/property_button.png"), (160, 610))
        pygame.display.update()
        while not_exit:
            cur = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 670 >= cur[0] >= 160 and 670 >= cur[1] >= 610:
                        not_exit = 0
                    else:
                        for cell in self.graphic_board.player_list[0].properties:
                            if self.graphic_board.property_coordinates[cell][0] + 120 >= cur[0] >=\
                                    self.graphic_board.property_coordinates[cell][0]:
                                if self.graphic_board.property_coordinates[cell][1] + 60 >= cur[1] >=\
                                        self.graphic_board.property_coordinates[cell][1]:
                                    self.background.actual_player.buy_house(self.background,
                                                                            self.background.board[cell][0])
                                    not_exit = 0
                                    break

    def buy_hotel(self):
        """
                The function to handle buying hotel from bank

                First generate all cells where house can be stand

                Than whe look what cell user choose and buy a house for this cell (if have money)

                :return: void only changes objects
        """
        not_exit = 1
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        for cell in self.graphic_board.player_list[0].properties:
            if cell in self.graphic_board.cells_where_house_can_stand:
                if self.background.actual_player.check_for_buying_hotel(self.background.board[cell][0]):
                    name = "graphic/cell" + str(cell) + ".png"
                    x = self.graphic_board.property_coordinates[cell][0]
                    y = self.graphic_board.property_coordinates[cell][1]
                    self.graphic_board.screen.blit(pygame.image.load(name), (x, y))
        self.graphic_board.screen.blit(pygame.image.load("graphic/property_button.png"), (160, 610))
        pygame.display.update()
        while not_exit:
            cur = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 670 >= cur[0] >= 160 and 670 >= cur[1] >= 610:
                        not_exit = 0
                    else:
                        for cell in self.graphic_board.player_list[0].properties:
                            if self.graphic_board.property_coordinates[cell][0] + 120 >= cur[0] >=\
                                    self.graphic_board.property_coordinates[cell][0]:
                                if self.graphic_board.property_coordinates[cell][1] + 60 >= cur[1] >=\
                                        self.graphic_board.property_coordinates[cell][1]:
                                    self.background.actual_player.buy_hotel(self.background.board[cell][0])
                                    not_exit = 0
                                    break

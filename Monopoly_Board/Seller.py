import pygame


class Seller:
    """
       This is a class for selling houses/hotels/cells to bank/other player

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

    def sell(self):
        """
            The function to choose - sell to bank sell to other player

            :return: void - only change objects
        """
        self.graphic_board.screen.blit(pygame.image.load("graphic/sell_choice.png"), (127, 127))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                cur = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 392 >= cur[0] >= 158 and 350 >= cur[1] >= 250:
                        self.sell_to_player()
                        not_exit = 0
                    elif 662 >= cur[0] >= 399 and 350 >= cur[1] >= 250:
                        self.sell_to_bank()
                        not_exit = 0

    def sell_to_player(self):
        """
            The function to handle selling cell to other player

            First player choose other player who want buy hsi cell

            Than function generate all cells that can be sold, next user choose cells that he want sell

            In the end whe look what cell user choose and make a transaction

            :return: void only changes objects
               """
        not_exit = 1
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        player_to_sell = self.graphic_board.choose_player(self.graphic_board.player_list, self.background)
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        pygame.display.update()
        for cell in self.graphic_board.player_list[0].properties:
            if self.background.actual_player.check_for_sell(self.background.board[cell][0], self.background):
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
                            if self.graphic_board.property_coordinates[cell][0] + 120 >= cur[0] >= \
                                    self.graphic_board.property_coordinates[cell][0]:
                                if self.graphic_board.property_coordinates[cell][1] + 60 >= cur[1] >= \
                                        self.graphic_board.property_coordinates[cell][1]:
                                    offer = self.graphic_board.get_offer(self.background.actual_player)
                                    if int(offer) * 1000 <= player_to_sell.money:
                                        permission = \
                                            self.graphic_board.ask_for_permission(player_to_sell)
                                        if permission:
                                            self.background.actual_player.sell_to_player(player_to_sell,
                                                                                         self.background.board[cell][0],
                                                                                         int(offer) * 1000)
                                            self.graphic_board.player_list[0].properties.remove(cell)
                                            buyer_avatar = self.graphic_board.convert_player_to_avatar(player_to_sell)
                                            buyer_avatar.properties.append(cell)
                                            not_exit = 0
                                            break
                                    else:
                                        not_exit = 0
                                        break

    def sell_to_bank(self):
        """
            The function to handle selling something to bank

            this function decide whether player want to sell cell/house/hotel (depends on what button player choose)

            :return: void only changes objects
        """
        self.graphic_board.screen.blit(pygame.image.load("graphic/trade.png"), (127, 127))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                cur = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 394 >= cur[0] >= 213 and 369 >= cur[1] >= 195:  # sell-house-bank
                        self.sell_house()
                        not_exit = 0
                    elif 600 >= cur[0] >= 421 and 366 >= cur[1] >= 197:
                        self.sell_hotel()
                        not_exit = 0
                    elif 494 >= cur[0] >= 314 and 592 >= cur[1] >= 422:  # sell-to-bank
                        self.sell_cell_to_bank()
                        not_exit = 0

    def sell_house(self, ):
        """
            The function to handle selling house to bank

            First generate all cells where house stand

            Than whe look what cell user choose and sell house from this cell

            :return: void only changes objects
        """
        not_exit = 1
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        for cell in self.graphic_board.player_list[0].properties:
            if cell in self.graphic_board.cells_where_house_can_stand:
                if self.background.board[cell][0].number_of_houses:
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
                            if self.graphic_board.property_coordinates[cell][0] + 120 >= cur[0] >= \
                                    self.graphic_board.property_coordinates[cell][0]:
                                if self.graphic_board.property_coordinates[cell][1] + 60 >= cur[1] >= \
                                        self.graphic_board.property_coordinates[cell][1]:
                                    self.background.actual_player.sell_house(self.background.board[cell][0])
                                    not_exit = 0
                                    break

    def sell_hotel(self):
        """
            The function to handle selling hotel to bank

            First generate all cells where hotel stand

            Than whe look what cell user choose and sell hotel from this cell

            :return: void only changes objects
        """
        not_exit = 1
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        for cell in self.graphic_board.player_list[0].properties:
            if self.graphic_board.cells_where_house_can_stand:
                if self.background.board[cell][0].number_of_hotel:
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
                            if self.graphic_board.property_coordinates[cell][0] + 120 >= cur[0] >= \
                                    self.graphic_board.property_coordinates[cell][0]:
                                if self.graphic_board.property_coordinates[cell][1] + 60 >= cur[1] >= \
                                        self.graphic_board.property_coordinates[cell][1]:
                                    self.background.actual_player.sell_hotel(self.background.board[cell][0])
                                    not_exit = 0
                                    break

    def sell_cell_to_bank(self):
        """
            The function to handle selling cell to bank

            First generate all cells that can be sold (not building in all cells of country)

            Than whe look what cell user choose and sell this cell

            :return: void only changes objects
        """
        not_exit = 1
        self.graphic_board.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        for cell in self.graphic_board.player_list[0].properties:
            if self.background.actual_player.check_for_sell(self.background.board[cell][0], self.background):
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
                            if self.graphic_board.property_coordinates[cell][0] + 120 >= cur[0] >= \
                                    self.graphic_board.property_coordinates[cell][0]:
                                if self.graphic_board.property_coordinates[cell][1] + 60 >= cur[1] >= \
                                        self.graphic_board.property_coordinates[cell][1]:
                                    self.background.board[cell][0].sell_cell(self.background.board[cell][0])
                                    self.graphic_board.player_list[0].properties.remove(cell)
                                    not_exit = 0
                                    break

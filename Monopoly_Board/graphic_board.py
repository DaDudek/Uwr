import pygame
import random
import time
from board_avatar import BoardAvatar
from board import Board
from player import Player
from Tradesman import Tradesman


class GraphicBoard:
    """
    This is one of the most important class in game - its where we use MCV
            and this class is responsible for everything that users see
    """
    def __init__(self, name, logo, screen):
        """
        Constructor of GraphicBoard class

        :param name: (String) name of the game window
        :param logo: (String) name of picture of the game window logo
        :param screen: (pygame.display) screen where we draw everything (pygame thing)

        main_screen_image: (String) name of main picture of the game
        player_list (list) list of BoardAvatar objects
        cells_where_house_can_stand : (list) list of city cells where player can stand a house/hotel
        property_coordinates -> (dict) this is dict where key is cell number
                                    and value is list of 2 int - x and y coordinate,
                                    this is used when we want to draw some player property
        cell_image: (String) name of graphic with cell picture what we want to draw on screen
                                (after stand or user click)
        size_X (int) width of game window
        size_Y (int) high of game window

        house_coordinate - dict with cell number key and value of other dict where key is number_of_house on cell
                and value is where this house must stand (to draw correct)
        hotel_coordinate - dict with cell number key and list of [x, y] coordinate

        house/hotel_coordinate it used to draw houses and hotels on good spot in board

        """
        self.main_screen_image = "graphic/monopoly_board_buttons.png"
        self.player_list = []
        self.cells_where_house_can_stand = [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34,
                                            37, 39]
        self.property_coordinates = dict()
        self.cell_image = None
        self.size_X = 819
        self.size_Y = 819
        self.name = name
        self.logo = logo
        self.screen = screen
        self.house_coordinate = None
        self.hotel_coordinate = None
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(pygame.image.load("graphic/" + self.logo))

    def choose_button(self, mouse_pos, background_board):
        """
        This function is used to handle event after player click button -
            we check what button player choose and use the correct function

        :param mouse_pos: (tuple) tuple of mouse position
        :param background_board: (board) hidden logic way of board

        :return: void -> only change objects
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if 686 >= mouse_pos[0] >= 502 and 688 >= mouse_pos[1] >= 504:
            self.roll_the_dice(self.player_list[0], background_board)
        elif 686 >= mouse_pos[0] >= 502 and 500 >= mouse_pos[1] >= 317:
            self.check_properties(self.player_list[0].properties)
        elif 498 >= mouse_pos[0] >= 317 and 500 >= mouse_pos[1] >= 317:
            self.choose_player_property(self.player_list)
        elif 688 >= mouse_pos[0] >= 502 and 310 >= mouse_pos[1] >= 132:
            self.end_turn(self.player_list[0], background_board)
        elif 498 >= mouse_pos[0] >= 317 and 688 >= mouse_pos[1] >= 504:
            self.sell_or_buy(background_board)
        else:
            self.click_cell_image(mouse_pos, 1)

    # choose_button methods

    def roll_the_dice(self, player, background_board):
        """
            Its function to handle roll_the_dice button

            First we check is player is after rolling and if its not true we handle one of two option
            - player can be in prison, or player can be free - depends on this we use more specialist function
            x, y is score of dice

            :param player: (BoardAvatar) avatar of player
            :param background_board: (board) hidden logic part of board

            :return: void -> only change object
        """
        if not player.after_roll:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            #x = 1
            #y = 0
            actual_player = background_board.actual_player
            background_player = background_board.players_queue[0]
            in_prison = background_player.move(background_board, x, y)
            background_board.check_transport_cells()
            if in_prison:
                self.roll_dice_in_prison(player, background_board, in_prison)
            else:
                self.roll_dice_not_in_prison(player, background_board, x, y, actual_player, background_player,
                                             in_prison)

    def check_properties(self, property_list):
        """
        This function is used to handle my properties/ other players properties button
            we iter for all cells in property_list and display it on screen to player can look what he/other player have

        :param property_list:  its player.property - list of Cell objects

        :return: void -> only draw something on screen
        """
        not_exit = 1
        self.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        for cell in property_list:
            name = "graphic/cell" + str(cell) + ".png"
            x = self.property_coordinates[cell][0]
            y = self.property_coordinates[cell][1]
            self.screen.blit(pygame.image.load(name), (x, y))
        self.screen.blit(pygame.image.load("graphic/property_button.png"), (160, 610))
        pygame.display.update()
        while not_exit:
            cur = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 670 >= cur[0] >= 160 and 670 >= cur[1] >= 610:
                        not_exit = 0

    def choose_player_property(self, player_list):
        """
        This function is for other players property button

        First generate all players from list of BoardAvatars
                after we look whose player user choose and drawing his property

        :param player_list: (list) List of BoardAvatar Objects

        :return: void -> only drawing something on screen
        """
        not_exits = 1
        self.screen.blit(pygame.image.load("graphic/choose_player.png"), (127, 127))
        generate = self.generate_players_to_choose(player_list)
        players_number = generate[0]
        players = generate[1]
        while not_exits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    if 570 >= cur[0] >= 420 and 300 >= cur[1] >= 200 and 1 in players_number:
                        self.check_properties(players[1].properties)
                        not_exits = 0
                    elif 400 >= cur[0] >= 250 and 300 >= cur[1] >= 200 and 0 in players_number:
                        self.check_properties(players[0].properties)
                        not_exits = 0
                    elif 570 >= cur[0] >= 420 and 440 >= cur[1] >= 340 and 3 in players_number:
                        self.check_properties(players[3].properties)
                        not_exits = 0
                    elif 400 >= cur[0] >= 250 and 440 >= cur[1] >= 340 and 2 in players_number:
                        self.check_properties(players[2].properties)
                        not_exits = 0
            pygame.display.update()

    def end_turn(self, player, background_board):
        """
        This function is used to handle end turn button

        First check is player roll the dice or not and use more specific function depends on option,
            In the end its check is someone lose already

        :param player: (BoardAvatar) its avatar of player
        :param background_board: (Board) hidden logic part of board

        :return: void -> only change something
        """
        if player.after_roll:
            self.end_after_roll(player, background_board)
        else:
            self.end_before_roll()
        self.check_for_bankrupt(background_board)

    def sell_or_buy(self, background_board):
        """
        This function is used to handle sell/buy button
        we check what user want and create a Tradesman object with correct option

        :param background_board: (Board) hidden logic part of board

        :return: void -> only change objects
        """
        self.screen.blit(pygame.image.load("graphic/buy_sell.png"), (127, 127))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                cur = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 380 >= cur[0] >= 173 and 409 >= cur[1] >= 300:
                        Tradesman(background_board, self).make_trade(1)
                        not_exit = 0
                    elif 635 >= cur[0] >= 431 and 409 >= cur[1] >= 300:
                        Tradesman(background_board, self).make_trade(0)
                        not_exit = 0

    # end of choose_button methods

    # some trades methods
    def number_checker(self, offer):
        """
        This function is to convert what player write when want to sell something -> when user write some numbers
            this programs do space to number was easier to read -> this method delete this space

        :param offer: (String) player offer with spaces
        :return: (int) converted offer to int (without spaces)

        """
        number = ""
        for letter in offer:
            if letter != " ":
                number += letter
        return number

    def get_offer(self, action_starter):
        """
        This function is created to handle taking number from user's keybord

        Pygame don't have textbox so we must checking everything ourselves,
            so we only take numbers and backspace. When user end write number accept it with enter

        :param action_starter: (player) player who start action (it may be selling or buying from other player)

        :return: (int) converted offer (from String and spaces to int)
        """
        not_exit = 1
        self.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
        pygame.display.update()
        offer = ""
        while not_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if len(offer) <= 24:
                        if event.key == pygame.K_0:
                            if len(offer):
                                offer += "0"
                        elif event.key == pygame.K_1:
                            offer += "1"
                        elif event.key == pygame.K_2:
                            offer += "2"
                        elif event.key == pygame.K_3:
                            offer += "3"
                        elif event.key == pygame.K_4:
                            offer += "4"
                        elif event.key == pygame.K_5:
                            offer += "5"
                        elif event.key == pygame.K_6:
                            offer += "6"
                        elif event.key == pygame.K_7:
                            offer += "7"
                        elif event.key == pygame.K_8:
                            offer += "8"
                        elif event.key == pygame.K_9:
                            offer += "9"
                    if event.key == pygame.K_BACKSPACE:
                        if len(offer):
                            offer = self.number_checker(offer)
                            offer = offer[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(offer):
                            not_exit = 0
                    if len(offer) < 24:
                        offer = self.make_spaces(self.number_checker(offer))
            self.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
            self.show_message(400, 200, "one milion is 1000 thousand", 50)
            self.show_message(400, 250, "you offer (in thousand)", 50)
            self.show_message(400, 600, "person who start action", 50)
            self.show_message(400, 650, "still have " + self.make_spaces(str(action_starter.money)) + " $", 50)
            self.show_message(400, 300, offer, 45)
            pygame.display.update()

        return self.number_checker(offer)

    def player_returner(self, player_list, number):
        """
        This is function to convert int number to Player object

        :param player_list: (list) list of Player object
        :param number: (int) number of player to return

        :return: (player) its return player object
        """
        for player in player_list:
            if player.number == number:
                return player

    def convert_player_to_avatar(self, player):
        """
        This function is convert player object to BoardAvatar object (using number field)
        :param player:
        :return:
        """
        for players in self.player_list:
            if players.player_number == player.number:
                return players

    def ask_for_permission(self, who_is_asked):
        """
        This function is used to take permission for sell/buy from player

        Its also show how much money have asked person

        :param who_is_asked: (player) player object - user who is asked to give permission

        :return: return 1 if user give permission for transaction, 0 in other way
        """
        self.screen.blit(pygame.image.load("graphic/ask_for_permission.png"), (127, 127))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                cur = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 380 >= cur[0] >= 173 and 409 >= cur[1] >= 300:
                        return 1
                    elif 635 >= cur[0] >= 431 and 409 >= cur[1] >= 300:
                        return 0
            self.show_message(400, 600, "person who get this offer", 50)
            self.show_message(400, 650, "still have " + self.make_spaces(str(who_is_asked.money)) + " $", 50)
            pygame.display.update()

    # end of some trades methods

    # graphic option when stand on cell

    def hidden_cell_graphic(self, message):
        """
        This function is used to show message from hidden cell

        :param message: (String) its message from hidden cell to show player -

        :return:
        """
        self.screen.blit(pygame.image.load("graphic/hidden_cell_message.png"), (127, 127))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                cur = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 635 >= cur[0] >= 173 and 409 >= cur[1] >= 300:
                        not_exit = 0
            self.show_message(400, 200, message, 50)
            pygame.display.update()

    def go_to_prison_graphic(self, player, background_board):
        """
        This is function to handle graphic side of what happened when players go to prison.
            Player have three option - can wait 2 turn, can paid 500k or use go out from jail card

        :param player: (BoardAvatar) Its avatar of player
        :param background_board: hidden logic of board

        :return:
        """
        not_exit = 1
        self.screen.blit(pygame.image.load("graphic/in_prison.png"), (127, 127))
        self.show_message(455, 644, str(background_board.actual_player.prison_counter), 35)
        self.show_message(525, 358, str(background_board.actual_player.card_out_of_prison()), 35)
        self.show_message(527, 498, self.make_spaces(str(background_board.actual_player.money)), 35)
        pygame.display.update()
        while not_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    if 600 >= cur[0] >= 220 and 395 >= cur[1] >= 280 \
                            and background_board.actual_player.card_out_of_prison():
                        background_board.actual_player.out_of_prison_by_card()
                        not_exit = 0
                        player.after_roll = 1
                    elif 600 >= cur[0] >= 220 and 531 >= cur[1] >= 416 \
                            and background_board.actual_player.money > 500 * 1000:
                        background_board.actual_player.out_of_prison_by_cash()
                        not_exit = 0
                        player.after_roll = 1
                    elif 600 >= cur[0] >= 220 and 674 >= cur[1] >= 559:
                        not_exit = 0
                        player.after_roll = 1
                        background_board.actual_player.stand_in_prison()
        player.go_to_prison()
        self.make_graphic_board(background_board.actual_player, background_board)

    def tax_cell(self, player, background_board):
        """
        This function is to handle graphic way of standing on tax cell
            user have 3 option - if he have enough money he can paid tax,
                               - if don't have enough money but have some cells/houses/hotels must sell it
                               - if don't have enough money end anything to sell - player loose

        :param player: (BoardAvatar) Avatar of player
        :param background_board: (board) hidden logic part of board

        :return: void -> only change object
        """
        not_exit = 1
        tax_to_paid = background_board.board[player.cell][0].amount_of_tax
        self.screen.blit(pygame.image.load("graphic/tax_cell.png"), (315, 130))
        self.show_message(520, 253, tax_to_paid, 35)
        pygame.display.update()
        while not_exit:
            self.show_message(524, 335,
                              self.make_spaces(str(background_board.actual_player.money + int(tax_to_paid))), 35)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    self.click_cell_image(cur, 1)
                    if self.cell_image:
                        self.screen.blit(pygame.image.load(self.cell_image), (128, 131))
                        pygame.display.update()
                    if 664 >= cur[0] >= 385 and 504 >= cur[1] >= 396 and background_board.actual_player.property != []:
                        Tradesman(background_board, self).make_trade(0)
                        self.make_graphic_board(background_board.actual_player, background_board)
                        self.screen.blit(pygame.image.load("graphic/tax_cell.png"), (315, 130))
                        self.show_message(520, 253, tax_to_paid, 35)
                        pygame.display.update()
                    elif 664 >= cur[0] >= 385 and 620 >= cur[1] >= 520 and background_board.actual_player.money >= 0:
                        not_exit = 0
                    elif background_board.actual_player.property == [] and background_board.actual_player.money < 0:
                        not_exit = 0
                        background_board.actual_player.is_bankrupt = True
                        player.is_bankrupt = True

    def not_enough_money(self, player, background_board):
        """
        This is function to handle graphic way of event that happend when player stand on free cell
                but don't have enough money to buy it

        :param player: (BoardAvatar) Avatar of player
        :param background_board: (board) hidden logic part of board

        :return: void -> only change object
        :return:
        """
        self.screen.blit(pygame.image.load("graphic/not_enough_money.png"), (315, 130))
        pygame.display.update()
        not_exit = 1
        while not_exit:
            self.show_message(524, 335, self.make_spaces(str(background_board.actual_player.money)), 35)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    self.click_cell_image(cur, 1)
                    if self.cell_image:
                        self.screen.blit(pygame.image.load(self.cell_image), (128, 131))
                        pygame.display.update()
                    if 664 >= cur[0] >= 385 and 504 >= cur[1] >= 396:
                        Tradesman(background_board, self).make_trade(0)
                        self.make_graphic_board(background_board.actual_player, background_board)
                        self.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
                        self.roll_dice_cell_image(player)
                        self.screen.blit(pygame.image.load("graphic/not_enough_money.png"), (315, 130))
                        pygame.display.update()
                    elif 664 >= cur[0] >= 385 and 620 >= cur[1] >= 520:
                        not_exit = 0

    # end of graphic option when stand on cell

    # show something methods

    def make_spaces(self, offer):
        """
        This is function that makes offer to be easier to read for user - make space every 3 numbers

        :param offer: (String) String offer from user keyboard

        :return: (String) new offer - offer with spaces
        """
        new_offer = ""
        counter = 1
        for i in range(len(offer) - 1, -1, -1):
            tmp = offer[i]
            tmp = tmp + new_offer
            new_offer = tmp
            if counter % 3 == 0 and counter != 0:
                tmp = " "
                tmp = tmp + new_offer
                new_offer = tmp
                counter = 1
            else:
                counter += 1
        return new_offer

    def show_message(self, coor_x, coor_y, message, size):
        """
        This is function to show some message on screen - like player current money, dice score etc

        :param coor_x: (int) x coordinate of message (this point will be center of message)
        :param coor_y: (int) y coordinate of message (this point will be center of message)
        :param message: (String) message to show on screen
        :param size: (int) size of letters in screen

        :return: void -> only show message on screen
        """
        font = pygame.font.SysFont(None, size)
        screen_text = font.render(str(message), True, (0, 0, 0))
        text_rect = screen_text.get_rect(center=(coor_x, coor_y))
        self.screen.blit(screen_text, text_rect)

    # end of show something methods

    # stand methods

    def stand_on_not_your_cell(self, player, cost, background):
        """
        This function is used to handle graphic side of event that happening when player stand on other player's cell
            player have 3 options   - if he have enough money he must paid player
                                    - if don't have enough money but have some cells/houses/hotels must sell it
                                    - if don't have enough money end anything to sell - player loose

        :param player: (BoardAvatar) Avatar of player
        :param cost: how much player must paid for staying in cell
        :param background: (board) hidden logic part of board

        :return: void -> only change object
        """
        not_exit = 1
        self.screen.blit(pygame.image.load("graphic/occup_cell.png"), (315, 130))
        self.show_message(520, 253, cost, 35)
        pygame.display.update()
        while not_exit:
            self.show_message(524, 335, self.make_spaces(str(background.actual_player.money + int(cost))), 35)
            pygame.display.update()
            if background.actual_player.money < 0 and player.properties == []:
                background.actual_player.go_bankrupt()
                self.player_list[0].is_bankrupt = True
                not_exit = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    self.click_cell_image(cur, 1)
                    if self.cell_image:
                        self.screen.blit(pygame.image.load(self.cell_image), (128, 131))
                        pygame.display.update()
                    if 664 >= cur[0] >= 385 and 504 >= cur[1] >= 396 and background.actual_player.property != []:
                        Tradesman(background, self).make_trade(0)
                        self.make_graphic_board(background.actual_player, background)
                        self.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
                        self.screen.blit(pygame.image.load("graphic/occup_cell.png"), (315, 130))
                        if self.cell_image:
                            self.screen.blit(pygame.image.load(self.cell_image), (128, 131))
                            pygame.display.update()
                        self.show_message(520, 253, cost, 35)
                        pygame.display.update()
                    elif 664 >= cur[0] >= 385 and 620 >= cur[1] >= 520 and background.actual_player.money >= 0:
                        not_exit = 0

    def stand_on_free_cell(self, player, background_board, actuall_player):
        """
        This is function to handle staying in free cell event, if player see this its mean that he have enough money
        so he have 2 options - can buy it or not

        :param (BoardAvatar) Avatar of player
        :param background_board: (board) hidden logic part of board
        :param actuall_player: (player) player that playing this turn

        :return: void -> only change object
        """
        not_exits = 1
        while not_exits:
            cur = pygame.mouse.get_pos()
            self.screen.blit(pygame.image.load("graphic/stand on free cell big.png"), (315, 130))
            self.show_message(515, 600, self.make_spaces(str(actuall_player.money)), 35)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_cell_image(cur, 1)
                    if self.cell_image:
                        self.screen.blit(pygame.image.load(self.cell_image), (128, 131))
                    if 498 >= cur[0] >= 402 and 389 >= cur[1] >= 281:
                        cell = background_board.board[player.cell][0]
                        bplayer = background_board.board[player.cell][len(background_board.board[player.cell]) - 1]
                        cell.buy_cell(bplayer, cell.cost, background_board, player.cell)
                        player.properties.append(player.cell)
                        player.money = bplayer.bank_account()
                        not_exits = 0
                    elif 653 >= cur[0] >= 554 and 389 >= cur[1] >= 281:
                        not_exits = 0
                    elif 658 >= cur[0] >= 400 and 513 >= cur[1] >= 423:
                        self.check_properties(player.properties)

    def stand_on_your_cell(self):
        """
        This function is used to inform user that he stand on his cell

        :return: void -> only change object
        """
        not_exit = 1
        self.screen.blit(pygame.image.load("graphic/own_cell.png"), (315, 130))
        pygame.display.update()
        while not_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    self.click_cell_image(cur, 1)
                    if self.cell_image:
                        self.screen.blit(pygame.image.load(self.cell_image), (128, 131))
                        pygame.display.update()
                    if 665 >= cur[0] >= 390 and 650 >= cur[1] >= 525:
                        not_exit = 0

    def stand_houses(self, background):
        """
        This function is used to draw all houses on board

        We check all cities where cells can stand,
        first we set size of house, than we check how_many house stand in cell
        In the end we draw this house

        :param background: (board) hidden logic part of board

        :return:
        """
        for cell in self.cells_where_house_can_stand:
            if 10 > cell > 0 or 30 > cell > 20:
                size = [26, 17]
            else:
                size = [15, 24]
            how_many = background.board[cell][0].number_of_houses
            for i in range(how_many):
                x = self.house_coordinate[cell][i + 1][0]
                y = self.house_coordinate[cell][i + 1][1]
                pygame.draw.rect(self.screen, (103, 25, 77), (x, y, size[0], size[1]))

    def stand_hotel(self, background):
        """
            This function is used to draw all hotels on board

            We check all cities where cells can stand,
            first we set size of house, than we check how_many hotel stand in cell ( 0 or 1)
            In the end we draw this hotel

            :param background: (board) hidden logic part of board

            :return:
        """
        for cell in self.cells_where_house_can_stand:
            if 10 > cell > 0 or 30 > cell > 20:
                size = [50, 30]
            else:
                size = [30, 45]
            how_many = background.board[cell][0].number_of_hotel
            for i in range(how_many):
                x = self.hotel_coordinate[cell][0]
                y = self.hotel_coordinate[cell][1]
                pygame.draw.rect(self.screen, (0, 102, 102), (x, y, size[0], size[1]))

    # end of stand methods

    # end turn methods
    def end_after_roll(self, player, background_board):
        """
        This function is used to change player queue after user end turn and is after roll

        :param player: (BoardAvatar) avatar of player
        :param background_board: (board) hidden part of board

        :return:
        """
        not_exit = 1
        queue = self.player_list[1:]
        queue.append(player)
        self.player_list = queue
        while not_exit:
            self.screen.blit(pygame.image.load("graphic/end_turn_after_roll.png"), (127, 127))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    if 630 >= cur[0] >= 200 and 571 >= cur[1] >= 400:
                        not_exit = 0
                        player.after_roll = 0
                        background_board.actual_player = background_board.players_queue[0]

    def end_before_roll(self):
        """
        This function is used to inform player that he can't end turn before roll the dice

        :return:
        """
        not_exit = 1
        while not_exit:
            self.screen.blit(pygame.image.load("graphic/end_turn_before_roll.png"), (127, 127))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    if 630 >= cur[0] >= 200 and 571 >= cur[1] >= 400:
                        not_exit = 0

    def check_for_bankrupt(self, background_board):
        """
        In this function we check is player bankrupt in this turn - if its true we remove him from list and queue

        :param background_board: (board) hidden part of board

        :return:
        """
        tmp = self.player_list
        for player in tmp:
            if player.is_bankrupt:
                self.player_list.remove(player)
        tmp1 = background_board.players_queue
        for player in tmp1:
            if player.is_bankrupt:
                player.go_bankrupt()
                background_board.players_queue.remove(player)

    # end of end turn methods

    # check_property methods
    def generate_players_to_choose(self, player_list):
        """
        This function is used to generate all of the players that user can choose

        :param player_list: list of BoardAvatar objects

        :return:
        """
        players_number = []
        players = dict()
        for player in player_list[1:]:
            players_number.append(player.player_number)
            players[player.player_number] = player
        if 0 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_1.png"), (250, 200))
        if 1 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_2.png"), (420, 200))
        if 2 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_3.png"), (250, 340))
        if 3 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_4.png"), (420, 340))
        pygame.display.update()
        return [players_number, players]

    def choose_player(self, player_list, background):
        """
        This function is used to return player object from user click

        :param player_list: list of BoardAvatar object
        :param background: (board) hidden part of board

        :return:
        """
        not_exits = 1
        self.screen.blit(pygame.image.load("graphic/choose_player.png"), (127, 127))
        players_number = []
        players = dict()
        for player in player_list[1:]:
            players_number.append(player.player_number)
            players[player.player_number] = player
        if 0 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_1.png"), (250, 200))
        if 1 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_2.png"), (420, 200))
        if 2 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_3.png"), (250, 340))
        if 3 in players_number:
            self.screen.blit(pygame.image.load("graphic/player_4.png"), (420, 340))
        pygame.display.update()
        while not_exits:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    if 570 >= cur[0] >= 420 and 300 >= cur[1] >= 200 and 1 in players_number:
                        return self.player_returner(background.players_queue, 1)
                    elif 400 >= cur[0] >= 250 and 300 >= cur[1] >= 200 and 0 in players_number:
                        return self.player_returner(background.players_queue, 0)
                    elif 570 >= cur[0] >= 420 and 440 >= cur[1] >= 340 and 3 in players_number:
                        return self.player_returner(background.players_queue, 3)
                    elif 400 >= cur[0] >= 250 and 440 >= cur[1] >= 340 and 2 in players_number:
                        return self.player_returner(background.players_queue, 2)

    # end of check property methods

    # roll_dice_methods

    def move_after_dice(self, player, background_board, x, y, actuall_player):
        """
        In this function is used to moving player's avatar cell after cell

        :param player: (BoardAvatar) player's avatar
        :param background_board: (board) hidden part of board logic
        :param x: (int) score from first dice
        :param y: (int) score from second dice
        :param actuall_player: (player) player that's playing his turn now

        :return: void -> only change objects and draw new board
        """
        how_many = x + y
        while how_many:
            player.move_avatar_by_one_cell()
            how_many -= 1
            self.make_graphic_board(actuall_player, background_board)
            self.show_message(400, 250, self.make_spaces(str(actuall_player.money)), 35)
            self.screen.blit(pygame.image.load("graphic/how_many.png"), (502, 504))
            message = str(x) + " and " + str(y)
            self.show_message(600, 615, message, 35)
            pygame.display.update()
            for players in self.player_list:
                players.stand_avatar()
            pygame.display.update()
            time.sleep(0.5)
        self.roll_dice_cell_image(player)
        self.make_graphic_board(background_board.actual_player, background_board)

    def roll_dice_in_prison(self, player, background_board, in_prison):
        """
        This function is used to handle rolling dice when player is in prison,
            give information from player and him to the end of queue

        :param player: (BoardAvatar) player's avatar
        :param background_board: (board) hidden part of board logic
        :param in_prison: 1 if player is in prison, 0 if is not

        :return: void -> only change object
        """
        if in_prison:
            self.go_to_prison_graphic(player, background_board)
            queue = background_board.players_queue[1:]
            background_board.players_queue = queue + [background_board.players_queue[0]]

    def choose_after_stand_on_cell(self, player, background_board, x, y, is_free, background_player):
        """
        This function is used to handle all of the events that happened when player stand on cell - depend on is_free
            if is_free == 1 - it means that player stand on free cell
            if is_free == -1 - it means that player stand on free cell but don't have money to buy it,
                                he have option to sell something, when he stop selling and have enough money,
                                he get chance to buy that cell
            if is_free == 2 - it means player stand on tax cell
            if is_free == 0 - it means that player stand on other player's cell (other than power_station)
            if is_free == -2 - it means that player stand on his own cell
            if is_free == 3 - it means that player stand on other player's power_station cell
            if is_free == 4 it means that player stand on go to prison cell
            if is_free == 7 it means that player stand on cell that is in [0, 10, 20]
            else it means player stand in hidden cell

            depends on is_free value we use more specific function


        :param player: (BoardAvatar) player's avatar
        :param background_board: (board) hidden part of board logic
        :param x: (int) value of first dice
        :param y: (int) value of second dice
        :param is_free: (int) option - card objects have function stand_in_cell that return this value
        :param background_player: (player) first player in queue

        :return: void -> only change objects and draw in screen
        """
        on_cell = background_board.board[player.cell]
        if is_free == 1:
            self.stand_on_free_cell(player, background_board, background_player)
        elif is_free == -1:
            self.not_enough_money(player, background_board)
            if background_board.actual_player.money >= on_cell[0].cost:
                self.screen.blit(pygame.image.load("graphic/clean_mid.png"), (127, 127))
                self.roll_dice_cell_image(player)
                self.stand_on_free_cell(player, background_board, background_player)
        elif is_free == 2:
            background_player.paid_tax(background_board.board[player.cell][0].amount_of_tax)
            self.tax_cell(player, background_board)
        elif is_free == 0:
            card = background_board.board[player.cell][0]
            cost = card.check_how_much_to_paid(background_board)
            card.paid_for_staying(background_player, cost)
            self.stand_on_not_your_cell(player, cost, background_board)
        elif is_free == -2:
            self.stand_on_your_cell()
        elif is_free == 3:
            card = background_board.board[player.cell][0]
            cost = card.check_how_much_to_paid(x + y)
            card.paid_for_staying(background_player, cost)
            self.stand_on_not_your_cell(player, cost, background_board)
        elif is_free == 4:
            self.go_to_prison_graphic(player, background_board)
        elif is_free == 7:
            pass
        else:
            self.hidden_cell_graphic(is_free)

    def roll_dice_not_in_prison(self, player, background_board, x, y, actuall_player, background_player, in_prison):
        """
        This function is used to handle roll the dice button if player is not in prison

        First we move avatar, then we check what kind of cell is this and depends on it we use more specific function

        In the end it check is player have pair - if its true it means player have another move
            (unless it was third time in row - if this happened player go to prison)

        :param player: (BoardAvatar) player's avatar
        :param background_board: (board) hidden part of board logic
        :param x: (int) value of first dice
        :param y: (int) value of second dice
        :param actuall_player: (player) actual playing player
        :param background_player: (player) first player in queue
        :param in_prison: 1 if player is in prison, 0 in other way
        :return:
        """
        self.move_after_dice(player, background_board, x, y, actuall_player)
        on_cell = background_board.board[player.cell]
        is_free = on_cell[0].stand_in_cell(background_board.actual_player, background_board)
        self.choose_after_stand_on_cell(player, background_board, x, y, is_free, background_player)
        if x == y and not in_prison:
            player.after_roll = 0
            queue = [background_board.actual_player]
            queue = queue + background_board.players_queue[1:]
            background_board.players_queue = queue
        else:
            player.after_roll = 1

    # end of roll_the_dice methods

    # loading_photos

    def make_graphic_board(self, actuall_player, background):
        """
        This function is used to draw board on screen all the time

        First we fill screen with white to clean it, then we load main_screen_image (its board with buttons)

        Than we must draw all of the players, houses and hotels because we clean everything before

        In the end we check what is current cell image (it depends on what player click), show current player money
        and update the screen (pygame function needed to change something on screen)

        :param actuall_player: (player) player object represent who is playing this turn
        :param background: (board) board object represent hidden part of board logic

        :return: void -> only draw something
        """
        self.screen.fill((255, 255, 255))
        self.screen.blit(pygame.image.load(self.main_screen_image),
                         (0, 0))
        for player in self.player_list:
            player.stand_avatar()
        self.stand_houses(background)
        self.stand_hotel(background)
        if self.cell_image:
            self.screen.blit(pygame.image.load(self.cell_image), (128, 131))
        self.show_message(400, 250, self.make_spaces(str(actuall_player.money)), 35)
        pygame.display.update()

    def click_cell_image(self, mouse_poss, mouse_click):
        """
        This function is used to set to draw cell from board when player click their on screen

        :param mouse_poss: (tuple) is tuple with mouse position on screen (pygame can check that)
        :param mouse_click: (int) this is information that player also click the cell, not only have cursor on it

        :return: void -> only set something to draw
        """
        # I row
        if 814 >= mouse_poss[0] >= 688 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/start cell.png"
        elif 686 >= mouse_poss[0] >= 625 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/Gdynia.png"
        elif 623 >= mouse_poss[0] >= 565 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/Random cell.png"
        elif 563 >= mouse_poss[0] >= 500 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/tajpej.png"
        elif 498 >= mouse_poss[0] >= 442 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/Tax1.png"
        elif 438 >= mouse_poss[0] >= 372 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/train station.png"
        elif 368 >= mouse_poss[0] >= 313 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/TOKIO.png"
        elif 310 >= mouse_poss[0] >= 252 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/Random cell.png"
        elif 250 >= mouse_poss[0] >= 188 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/Barcelona.png"
        elif 183 >= mouse_poss[0] >= 128 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/Ateny.png"
        elif 125 >= mouse_poss[0] >= 2 and 816 >= mouse_poss[1] >= 688 and mouse_click:
            self.cell_image = "graphic/prison cell.png"
        # II row
        elif 122 >= mouse_poss[0] >= 2 and 688 >= mouse_poss[1] >= 631 and mouse_click:
            self.cell_image = "graphic/Istambul.png"
        elif 122 >= mouse_poss[0] >= 2 and 629 >= mouse_poss[1] >= 567 and mouse_click:
            self.cell_image = "graphic/power station.png"
        elif 122 >= mouse_poss[0] >= 2 and 564 >= mouse_poss[1] >= 504 and mouse_click:
            self.cell_image = "graphic/Kijów.png"
        elif 122 >= mouse_poss[0] >= 2 and 502 >= mouse_poss[1] >= 442 and mouse_click:
            self.cell_image = "graphic/toronto.png"
        elif 122 >= mouse_poss[0] >= 2 and 438 >= mouse_poss[1] >= 372 and mouse_click:
            self.cell_image = "graphic/aiport.png"
        elif 122 >= mouse_poss[0] >= 2 and 370 >= mouse_poss[1] >= 318 and mouse_click:
            self.cell_image = "graphic/Rzym.png"
        elif 122 >= mouse_poss[0] >= 2 and 315 >= mouse_poss[1] >= 254 and mouse_click:
            self.cell_image = "graphic/Random cell.png"
        elif 122 >= mouse_poss[0] >= 2 and 252 >= mouse_poss[1] >= 193 and mouse_click:
            self.cell_image = "graphic/SZANGHAJ.png"
        elif 122 >= mouse_poss[0] >= 2 and 191 >= mouse_poss[1] >= 130 and mouse_click:
            self.cell_image = "graphic/VANCOUVER.png"
        elif 122 >= mouse_poss[0] >= 2 and 128 >= mouse_poss[1] >= 2 and mouse_click:
            self.cell_image = "graphic/parking cell.png"
        # III row
        elif 817 >= mouse_poss[0] >= 690 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/policeman cell.png"
        elif 686 >= mouse_poss[0] >= 625 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/Jerozolima.png"
        elif 623 >= mouse_poss[0] >= 565 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/water supply.png"
        elif 563 >= mouse_poss[0] >= 500 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/HonkKong.png"
        elif 498 >= mouse_poss[0] >= 441 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/Pekin.png"
        elif 439 >= mouse_poss[0] >= 370 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/Harbor.png"
        elif 368 >= mouse_poss[0] >= 312 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/Londyn.png"
        elif 310 >= mouse_poss[0] >= 252 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/Nowy Jork.png"
        elif 254 >= mouse_poss[0] >= 186 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/Random cell.png"
        elif 184 >= mouse_poss[0] >= 125 and 126 >= mouse_poss[1] >= 1 and mouse_click:
            self.cell_image = "graphic/sydney.png"
        # IV row
        elif 815 >= mouse_poss[0] >= 689 and 688 >= mouse_poss[1] >= 631 and mouse_click:
            self.cell_image = "graphic/Montreal.png"
        elif 815 >= mouse_poss[0] >= 689 and 629 >= mouse_poss[1] >= 566 and mouse_click:
            self.cell_image = "graphic/Tax2.png"
        elif 815 >= mouse_poss[0] >= 689 and 564 >= mouse_poss[1] >= 504 and mouse_click:
            self.cell_image = "graphic/Ryga.png"
        elif 815 >= mouse_poss[0] >= 689 and 503 >= mouse_poss[1] >= 440 and mouse_click:
            self.cell_image = "graphic/Random cell.png"
        elif 815 >= mouse_poss[0] >= 689 and 438 >= mouse_poss[1] >= 372 and mouse_click:
            self.cell_image = "graphic/cosmodrome.png"
        elif 815 >= mouse_poss[0] >= 689 and 370 >= mouse_poss[1] >= 318 and mouse_click:
            self.cell_image = "graphic/Kapsztad.png"
        elif 815 >= mouse_poss[0] >= 689 and 315 >= mouse_poss[1] >= 254 and mouse_click:
            self.cell_image = "graphic/Random cell.png"
        elif 815 >= mouse_poss[0] >= 689 and 252 >= mouse_poss[1] >= 193 and mouse_click:
            self.cell_image = "graphic/Belgrad.png"
        elif 815 >= mouse_poss[0] >= 689 and 191 >= mouse_poss[1] >= 130 and mouse_click:
            self.cell_image = "graphic/Paryż.png"

    def roll_dice_cell_image(self, player):
        """
        This function is used set to draw cell card after player roll the dice -
                what image to draw depends on player.cell

        :param player: (boardAvatar) player avatar on board

        :return: void -> only set to draw something on screen
        """
        # I row
        if player.cell == 0:
            self.cell_image = "graphic/start cell.png"
        elif player.cell == 1:
            self.cell_image = "graphic/Gdynia.png"
        elif player.cell in [2, 7, 17, 22, 33, 36]:
            self.cell_image = "graphic/Random cell.png"
        elif player.cell == 3:
            self.cell_image = "graphic/tajpej.png"
        elif player.cell == 4:
            self.cell_image = "graphic/Tax1.png"
        elif player.cell == 5:
            self.cell_image = "graphic/train station.png"
        elif player.cell == 6:
            self.cell_image = "graphic/TOKIO.png"
        elif player.cell == 8:
            self.cell_image = "graphic/Barcelona.png"
        elif player.cell == 9:
            self.cell_image = "graphic/Ateny.png"
        elif player.cell == 10:
            self.cell_image = "graphic/prison cell.png"
        # II row
        elif player.cell == 11:
            self.cell_image = "graphic/Istambul.png"
        elif player.cell == 12:
            self.cell_image = "graphic/power station.png"
        elif player.cell == 13:
            self.cell_image = "graphic/Kijów.png"
        elif player.cell == 14:
            self.cell_image = "graphic/toronto.png"
        elif player.cell == 15:
            self.cell_image = "graphic/aiport.png"
        elif player.cell == 16:
            self.cell_image = "graphic/Rzym.png"
        elif player.cell == 18:
            self.cell_image = "graphic/SZANGHAJ.png"
        elif player.cell == 19:
            self.cell_image = "graphic/VANCOUVER.png"
        elif player.cell == 20:
            self.cell_image = "graphic/parking cell.png"
        # III row
        elif player.cell == 30:
            self.cell_image = "graphic/policeman cell.png"
        elif player.cell == 29:
            self.cell_image = "graphic/Jerozolima.png"
        elif player.cell == 28:
            self.cell_image = "graphic/water supply.png"
        elif player.cell == 27:
            self.cell_image = "graphic/HonkKong.png"
        elif player.cell == 26:
            self.cell_image = "graphic/Pekin.png"
        elif player.cell == 25:
            self.cell_image = "graphic/Harbor.png"
        elif player.cell == 24:
            self.cell_image = "graphic/Londyn.png"
        elif player.cell == 23:
            self.cell_image = "graphic/Nowy Jork.png"
        elif player.cell == 21:
            self.cell_image = "graphic/sydney.png"
        # IV row
        elif player.cell == 39:
            self.cell_image = "graphic/Montreal.png"
        elif player.cell == 38:
            self.cell_image = "graphic/Tax2.png"
        elif player.cell == 37:
            self.cell_image = "graphic/Ryga.png"
        elif player.cell == 35:
            self.cell_image = "graphic/cosmodrome.png"
        elif player.cell == 34:
            self.cell_image = "graphic/Kapsztad.png"
        elif player.cell == 32:
            self.cell_image = "graphic/Belgrad.png"
        elif player.cell == 31:
            self.cell_image = "graphic/Paryż.png"

    # init methods
    def board_init(self):
        """
        This is function used to when player start the game and must select how many players gonna play the game,
        (he can choose between 2 and 4), also this function init all coordinate needed to draw things correct

        :return: void -> only change object
        """
        self.screen.blit(pygame.image.load("graphic/menu.png"), (0, 0))
        self.init_houses_coordinate()
        self.init_property_coor()
        self.init_hotel_coor()
        pygame.display.update()
        not_exit = 1
        while not_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cur = pygame.mouse.get_pos()
                    if 623 >= cur[0] >= 188 and 215 >= cur[1] >= 84:
                        return self.init_for_two_players()
                    elif 623 >= cur[0] >= 188 and 377 >= cur[1] >= 247:
                        return self.init_for_three_players()
                    elif 623 >= cur[0] >= 188 and 533 >= cur[1] >= 407:
                        return self.init_for_four_players()
                    elif 623 >= cur[0] >= 188 and 700 >= cur[1] >= 571:
                        not_exit = 0
                        quit()

    def init_houses_coordinate(self):
        """
            This function is used to init coordinates where house can stand -
                its dict with cell number key and value of other dict where key is number_of_house on cell
                and value is where this house must stand (to draw correct)

            :return: void -> only change object
        """
        cell1 = {1: [630, 695], 2: [662, 695], 3: [630, 720], 4: [662, 720]}
        cell3 = {1: [504, 695], 2: [536, 695], 3: [504, 720], 4: [536, 720]}
        cell6 = {1: [315, 695], 2: [347, 695], 3: [315, 720], 4: [347, 720]}
        cell8 = {1: [190, 695], 2: [220, 695], 3: [190, 720], 4: [220, 720]}
        cell9 = {1: [130, 695], 2: [160, 695], 3: [130, 720], 4: [160, 720]}
        cell11 = {1: [85, 632], 2: [106, 632], 3: [85, 663], 4: [106, 663]}
        cell13 = {1: [85, 506], 2: [106, 506], 3: [85, 540], 4: [106, 540]}
        cell14 = {1: [85, 446], 2: [106, 446], 3: [85, 476], 4: [106, 476]}
        cell16 = {1: [85, 322], 2: [106, 322], 3: [85, 350], 4: [106, 350]}
        cell18 = {1: [85, 198], 2: [106, 198], 3: [85, 226], 4: [106, 226]}
        cell19 = {1: [85, 136], 2: [106, 136], 3: [85, 164], 4: [106, 164]}
        cell21 = {1: [127, 86], 2: [159, 86], 3: [127, 106], 4: [159, 106]}
        cell23 = {1: [254, 86], 2: [282, 86], 3: [254, 106], 4: [282, 106]}
        cell24 = {1: [316, 86], 2: [347, 86], 3: [316, 106], 4: [347, 106]}
        cell26 = {1: [443, 86], 2: [473, 86], 3: [443, 106], 4: [473, 106]}
        cell27 = {1: [506, 86], 2: [536, 86], 3: [506, 106], 4: [536, 106]}
        cell29 = {1: [631, 86], 2: [661, 86], 3: [631, 106], 4: [661, 106]}
        cell31 = {1: [693, 132], 2: [715, 132], 3: [693, 160], 4: [715, 160]}
        cell32 = {1: [693, 193], 2: [715, 193], 3: [693, 222], 4: [715, 222]}
        cell34 = {1: [693, 318], 2: [715, 318], 3: [693, 350], 4: [715, 350]}
        cell37 = {1: [693, 506], 2: [715, 506], 3: [693, 538], 4: [715, 538]}
        cell39 = {1: [693, 633], 2: [715, 633], 3: [693, 663], 4: [715, 663]}
        self.house_coordinate = {1: cell1, 3: cell3, 6: cell6, 8: cell8, 9: cell9,
                                 11: cell11, 13: cell13, 14: cell14, 16: cell16, 18: cell18, 19: cell19,
                                 21: cell21, 23: cell23, 24: cell24, 26: cell26, 27: cell27, 29: cell29,
                                 31: cell31, 32: cell32, 34: cell34, 37: cell37, 39: cell39}

    def init_hotel_coor(self):
        """
        This function is used to init coordinates where hotel can stand
                (its dict with cell number key and list of [x,y] coordinate)

        :return: void -> only change object
        """
        self.hotel_coordinate = {1: [630, 695], 3: [504, 695], 6: [315, 695], 8: [190, 695], 9: [130, 695],
                                 11: [85, 632], 13: [85, 506], 14: [85, 446], 16: [85, 322], 18: [85, 198],
                                 19: [85, 136],
                                 21: [127, 86], 23: [254, 86], 24: [316, 86], 26: [443, 86], 27: [506, 86],
                                 29: [631, 86],
                                 31: [693, 132], 32: [693, 193], 34: [693, 318], 37: [693, 506], 39: [693, 633]}

    def init_property_coor(self):
        """
        This function is used to init coordinates of cells when we want to draw some player property,
        This init dict where key is cell number and value is list of 2 int (x, y coordinate)

        :return: void -> only change object
        """
        self.property_coordinates = {1: [160, 140], 3: [160, 205], 5: [160, 270], 15: [160, 335], 25: [160, 400],
                                     35: [160, 465], 12: [160, 530],
                                     6: [290, 140], 8: [290, 205], 9: [290, 270], 21: [290, 335], 23: [290, 400],
                                     24: [290, 465], 28: [290, 530],
                                     11: [420, 140], 13: [420, 205], 14: [420, 270], 26: [420, 335], 27: [420, 400],
                                     29: [420, 465], 37: [420, 530],
                                     16: [550, 140], 18: [550, 205], 19: [550, 270], 31: [550, 335], 32: [550, 400],
                                     34: [550, 465], 39: [550, 530]}

    def init_for_two_players(self):
        """
            This function is used to init players and their avatar when player choose 2 players game

            :return: (board) board object with players in cell 0 (start cell)
        """
        BoardAvatar(756, self.size_Y, self.screen, 0, (255, 0, 0), self)
        BoardAvatar(756, self.size_Y - 20, self.screen, 1, (0, 255, 0), self)
        b = Board(2)
        player1 = Player(b)
        player1.id = 1
        player2 = Player(b)
        player1.number = 0
        player2.number = 1
        b.make_board()
        b.board[0].append(player1)
        b.board[0].append(player2)
        return b

    def init_for_three_players(self):
        """
            This function is used to init players and their avatar when player choose 3 players game

            :return: (board) board object with players in cell 0 (start cell)
        """
        BoardAvatar(756, self.size_Y, self.screen, 0, (255, 0, 0), self)
        BoardAvatar(756, self.size_Y - 20, self.screen, 1, (0, 255, 0), self)
        BoardAvatar(756, self.size_Y - 40, self.screen, 2, (0, 0, 255), self)
        b = Board(3)
        player1 = Player(b)
        player2 = Player(b)
        player3 = Player(b)
        player1.number = 0
        player2.number = 1
        player3.number = 2
        b.make_board()
        b.board[0].append(player1)
        b.board[0].append(player2)
        b.board[0].append(player3)
        return b

    def init_for_four_players(self):
        """
        This function is used to init players and their avatar when player choose 4 players game

        :return: (board) board object with players in cell 0 (start cell)
        """
        BoardAvatar(756, self.size_Y, self.screen, 0, (255, 0, 0), self)
        BoardAvatar(756, self.size_Y - 20, self.screen, 1, (0, 255, 0), self)
        BoardAvatar(756, self.size_Y - 40, self.screen, 2, (0, 0, 255), self)
        BoardAvatar(756, self.size_Y - 60, self.screen, 3, (0, 255, 255), self)
        b = Board(4)
        player1 = Player(b)
        player2 = Player(b)
        player3 = Player(b)
        player4 = Player(b)
        player1.number = 0
        player2.number = 1
        player3.number = 2
        player4.number = 3
        b.make_board()
        b.board[0].append(player1)
        b.board[0].append(player2)
        b.board[0].append(player3)
        b.board[0].append(player4)
        return b

    # end of init methods

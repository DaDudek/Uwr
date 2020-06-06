import pygame
from graphic_board import GraphicBoard

# Initialize pygame
pygame.init()
# create the screen
"""
    This is Main class of game - we init here GraphicBoard and Board, 
"""
screen = pygame.display.set_mode((819, 819))
gb = GraphicBoard("Monopoly by Dawid", "logo.png", screen)
background_board = gb.board_init()
background_board.actual_player = background_board.players_queue[0]
# gb.player_list[0].properties = [1,3,5,6,8,9,11,12,13,14,15,16,18,19,21,23,24,25,26,27,28,29,31,32,34,35,37,39]
# gb.player_list[0].properties = [1,3,6,8,9,11,13,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39]
#gb.player_list[1].properties = [1,3]

# gb.player_list[2].properties = [8]
# background_board.board[8][0].owner = background_board.board[0][3]
# background_board.board[0][3].property.append(background_board.board[8][0])

#background_board.board[0][2].countries["brown"] = [1,3]

#for i in gb.player_list[1].properties:
 #   background_board.board[i][0].owner = background_board.board[0][2]
  #  background_board.board[0][2].property.append(background_board.board[i][0])
# dla testow

# background_board.board[1][0].number_of_hotel = 1
# background_board.board[3][0].number_of_houses = 1
background_board.board[0][1].money = 600 * 10000000


# Game Loop
running = True
while running:
    """Main game loop - its end when only 1 player survives"""
    gb.make_graphic_board(background_board.actual_player, background_board)
    if len(gb.player_list) == 1:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gb.choose_button(pygame.mouse.get_pos(), background_board)

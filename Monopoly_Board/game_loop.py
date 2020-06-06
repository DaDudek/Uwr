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

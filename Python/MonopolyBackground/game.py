import player
import board
from player_communication import PlayerCommunication

#TODO: brak hajsu za przejscie przy pojsciu do pociagu   - poszedł fix przetestować czy działa
#TODO: kontrpropozycje do sprzedazy i kupna
#TODO: WYSWIETLENIE INFO O GRACZY - do rozważenia
#TODO: MOZLIWOSC KUPOWANIA RZECZY OSOBY KTÓRA ZBANKRUTOWAŁA - poszedł fix potrzebny test
#TODO: oblsuzyc ilosc graczy <1  - raczej zbędne bo będą kafełki na odpowiednią liczbę graczy

class Game:
    def __init__(self, name="Monopoly"):
        self.name = name

    def prepare_game(self):
        print("Podaj ilość graczy")
        count_players = PlayerCommunication().choose_option()
        game_board = board.Board(count_players)
        game_board.make_board()
        for i in range(count_players):
            print("Podaj nazwę gracza")
            name=PlayerCommunication().choose_name()
            new_player=player.Player(name)
            game_board.board[0].append(new_player)
            game_board.players_queue.append(new_player)
        for el in game_board.board[0]:
            print(el, end=" ; ")
        print()
        print()
        return game_board

    def start_game(self, game_board):
        while len(game_board.players_queue) > 1:
            current_player = game_board.players_queue[0]
            if current_player.money > 0:
                print(current_player.name + " wybierz opcje:")
                print("1: rzuć kostkami", "2: kup budowle", "3: sprzedaj budowle", "4: handluj z innym graczem")
                option = PlayerCommunication().choose_option()
                """ if not len(current_player.property) and option != 1:
                    print("Brak kart")
                    print("Wybierz 1: rzuć kostkami","4: handluj z innym graczem")
                    option = 1 """
                while option != 1:
                    if not len(current_player.property) and option != 4:
                        print("Brak kart")
                        print("Wybierz 1: rzuć kostkami", "4: handluj z innym graczem")

                    else:
                        if option == 2:
                            print(current_player.name + " wybierz opcje:")
                            print("1: Kup domek", "2: kup hotel", "3: pomyłka")
                            sub_option = PlayerCommunication().choose_option()
                            if sub_option == 1:
                                cart = current_player.choose_cart(current_player)
                                current_player.buy_house(game_board, cart)
                            elif sub_option == 2:
                                cart = current_player.choose_cart(current_player)
                                current_player.buy_hotel(cart)
                        elif option == 3:
                            print(current_player.name + " wybierz opcje:")
                            print("1: sprzedaj domek", "2: sprzedaj hotel", "3: pomyłka")
                            sub_option = PlayerCommunication().choose_option()
                            if sub_option == 1:
                                cart = current_player.choose_cart(current_player)
                                current_player.sell_house(cart)
                            elif sub_option == 2:
                                cart = current_player.choose_cart(current_player)
                                current_player.sell_hotel(cart)
                        elif option == 4:
                            print(current_player.name + " wybierz opcje")
                            print("1: sprzedaj karte", "2:kup karte", "3: pomyłka ")
                            sub_option = PlayerCommunication().choose_option()
                            if not len(current_player.property) and sub_option == 1:
                                while sub_option == 1:
                                    print("Brak kart do sprzedazy")
                                    print("Wybierz: 2: kup kartę","3: pomyłka")
                                    sub_option = PlayerCommunication().choose_option()
                            if sub_option == 1:
                                current_player.sell_to_player(game_board)
                            elif sub_option == 2:
                                current_player.buy_from_player(game_board)
                        print(current_player.name + " wybierz opcje:")
                        print("1: rzuć kostkami", "2: kup budowle", "3: sprzedaj budowle", "4: handluj z innym graczem")
                    option = PlayerCommunication().choose_option()
                current_player.move(game_board)
                player_tmp_coord = current_player.coordinate
                game_board.board[current_player.coordinate][0].stand_in_cell(current_player, game_board)
                for el in game_board.board[current_player.coordinate]:
                    print(el, end=" ; ")
                if not current_player.have_pair:
                    game_board.players_queue = game_board.players_queue[1:]
                    if current_player.money > 0:
                        game_board.players_queue.append(current_player)
                    elif current_player.money <= 0 :
                        current_player.go_bankrupt
                        continue
                if player_tmp_coord != current_player.coordinate:
                    print()
                    game_board.board[current_player.coordinate][0].stand_in_cell(current_player, game_board)
                    for el in game_board.board[current_player.coordinate]:
                        print(el, end=" ; ")

                print()
                print()

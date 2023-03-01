from domain import Board
from services import Services

class UI:
    def __init__(self):
        self._easy_player_board = Board(8, 8)
        self._easy_computer_board = Board(8,8)
        self._easy_displayed_computer_board = Board(8,8)
        self._easy_player_board_seen_by_computer = Board(8, 8)
        self._hard_player_board = Board(10, 10)
        self._hard_computer_board = Board(10, 10)
        self._hard_displayed_computer_board = Board(10, 10)
        self._hard_player_board_seen_by_computer = Board(10, 10)
        self._services = Services()
    def start(self):
        try_again = 1
        while try_again:
            option = input("Choose the level (easy or hard):  ")
            option = option.strip()
            option = option.lower()
            if option == 'easy':
                stricken_cases = []
                computer_cabins = []
                computer_planes_directions = []
                self._services.create_easy_computer_board(self._easy_computer_board.board, computer_cabins,
                                                          computer_planes_directions)
                print(self._easy_computer_board)
                player_cabins = []
                player_planes_directions = []
                planes_number = 0
                while planes_number < 3:
                    print(self._easy_player_board)
                    go_on_flag = 1
                    while go_on_flag == 1:
                        try:
                            print('Enter the position (eg D2) of the cabin of plane number', planes_number + 1, ':')
                            pos = input()
                            direction = input("Enter direction (right | left | up | down): ")
                            pos = pos.replace(' ', '')
                            print(pos)
                            i = pos[0]
                            j = pos[1]
                            i = i.upper()
                            i = ord(i) - 65
                            j = int(j) - 1
                            self._services.choose_planes_easy(self._easy_player_board.board, direction, i, j,
                                                              str(planes_number + 1))
                            go_on_flag = 0
                        except:
                            print("Invalid input! Try again.")
                    player_cabins.append((i, j))
                    player_planes_directions.append(direction)
                    planes_number = planes_number + 1
                game_over = 0
                while game_over == 0:
                    print("YOUR BOARD IS:")
                    print(self._easy_player_board)
                    print("COMPUTER'S BOARD IS:")
                    print(self._easy_displayed_computer_board)
                    go_on_flag = 1
                    while go_on_flag == 1:
                        try:
                            strike = input("CHOOSE A STRIKE: ")
                            strike = strike.replace(' ', '')
                            i = strike[0]
                            j = strike[1]
                            i = i.upper()
                            i = ord(i) - 65
                            j = int(j) - 1
                            self._services.strike_planes(self._easy_displayed_computer_board.board,
                                                         self._easy_computer_board.board, computer_cabins, i, j,
                                                         computer_planes_directions)
                            go_on_flag = 0
                        except:
                            print("Invalid input! Try again.")
                    if self._services.game_over(self._easy_computer_board.board):
                        print("YOUR BOARD IS:")
                        print(self._easy_player_board)
                        print("COMPUTER'S BOARD IS:")
                        print(self._easy_displayed_computer_board)
                        print("GAME OVER. YOU WON!")
                        return
                    self._services.computer_strikes(self._easy_player_board_seen_by_computer.board,
                                                    self._easy_player_board.board, player_cabins,
                                                    player_planes_directions,
                                                    stricken_cases)
                    if self._services.game_over(self._easy_player_board.board):
                        print("YOUR BOARD IS:")
                        print(self._easy_player_board)
                        print("COMPUTER'S BOARD IS:")
                        print(self._easy_displayed_computer_board)
                        print("GAME OVER. COMPUTER WON!")
                        return
            elif option == 'hard':
                stricken_cases = []
                computer_cabins = []
                computer_planes_directions = []
                self._services.create_hard_computer_board(self._hard_computer_board.board, computer_cabins,
                                                          computer_planes_directions)
                print(self._hard_computer_board)
                player_cabins = []
                player_planes_directions = []
                planes_number = 0
                while planes_number < 3:
                    print(self._hard_player_board)
                    go_on_flag = 1
                    while go_on_flag == 1:
                        try:
                            print('Enter the position of the cabin of plane number', planes_number + 1, ':')
                            pos = input()
                            direction = input("Enter direction: ")
                            pos = pos.replace(' ', '')
                            print(pos)
                            i = pos[0]
                            j = pos[1]
                            i = i.upper()
                            i = ord(i) - 65
                            j = int(j) - 1
                            self._services.choose_planes_hard(self._hard_player_board.board, direction, i, j,
                                                              str(planes_number + 1))
                            go_on_flag = 0
                        except:
                            print("Invalid input! Try again.")
                    player_cabins.append((i, j))
                    player_planes_directions.append(direction)
                    planes_number = planes_number + 1
                game_over = 0
                while game_over == 0:
                    print("YOUR BOARD IS:")
                    print(self._hard_player_board)
                    print("COMPUTER'S BOARD IS:")
                    print(self._hard_displayed_computer_board)
                    go_on_flag = 1
                    while go_on_flag == 1:
                        try:
                            strike = input("CHOOSE A STRIKE: ")
                            strike = strike.replace(' ', '')
                            i = strike[0]
                            j = strike[1]
                            i = i.upper()
                            i = ord(i) - 65
                            j = int(j) - 1
                            self._services.strike_planes(self._hard_displayed_computer_board.board,
                                                         self._hard_computer_board.board, computer_cabins, i, j,
                                                         computer_planes_directions)
                            go_on_flag = 0
                        except:
                            print("Invalid input! Try again.")
                    if self._services.game_over(self._hard_computer_board.board):
                        print("YOUR BOARD IS:")
                        print(self._hard_player_board)
                        print("COMPUTER'S BOARD IS:")
                        print(self._hard_displayed_computer_board)
                        print("GAME OVER. YOU WON!")
                        return
                    self._services.computer_strikes(self._hard_player_board_seen_by_computer.board,
                                                    self._hard_player_board.board, player_cabins,
                                                    player_planes_directions,
                                                    stricken_cases)
                    if self._services.game_over(self._hard_player_board.board):
                        print("YOUR BOARD IS:")
                        print(self._hard_player_board)
                        print("COMPUTER'S BOARD IS:")
                        print(self._hard_displayed_computer_board)
                        print("GAME OVER. COMPUTER WON!")
                        return
            else:
                print("Invalid option! Try again.")


x = UI()
x.start()
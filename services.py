import random
from random import randint


class Services:
    def choose_planes_easy(self, board, direction, i, j, symbol):
        """
        It marks the chosen planes on the 8x8 board.
        :param board: board
        :param direction: up, down, right or left
        :param i: row of the cabin
        :param j: column  of the cabin
        :param symbol: '1', '2' or '3' (first, second, or third chosen plane)
        """
        if direction == 'left':
            if 2 <= j <= 7 and 1 <= i <= 7 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(j-2, j+2):
                    if board[i][k] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(j - 2, j + 2):
                    board[i][k] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        elif direction == 'right':
            if 1 <= j <= 6 and 1 <= i <= 7 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(j-1, j+3):
                    if board[i][k] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(j - 1, j + 3):
                    board[i][k] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        elif direction == 'up':
            if 1 <= j <= 7 and 2 <= i <= 7 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(i-2, i+2):
                    if board[k][j] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(i - 2, i + 2):
                    board[k][j] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        elif direction == 'down':
            if 1 <= j <= 7 and 1 <= i <= 6 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(i-1, i+3):
                    if board[k][j] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(i - 1, i + 3):
                    board[k][j] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        else:
            raise ValueError

    def create_easy_computer_board(self, computer_board, cabins, planes_directions):
        """
        It marks the randomly chosen planes on the computer's 8x8 board.
        :param computer_board: computer's board
        :param cabins: the array with the indexes of the planes' cabins
        :param planes_directions: the directions of the planes
        """
        directions = ['up', 'down', 'left', 'right']
        planes_number = 0
        while planes_number < 3:
            go_on_flag = 1
            while go_on_flag == 1:
                try:
                    i = randint(1, 7)
                    j = randint(1, 7)
                    direction = random.choice(directions)
                    self.choose_planes_easy(computer_board, direction, i, j, str(planes_number+1))
                    go_on_flag = 0
                except:
                    continue
            cabins.append((i,j))
            planes_directions.append(direction)
            planes_number = planes_number + 1

    def choose_planes_hard(self, board, direction, i, j, symbol):
        """
        It marks the chosen planes on the 10x10 board.
        :param board: board
        :param direction: up, down, right or left
        :param i: row of the cabin
        :param j: column  of the cabin
        :param symbol: '1', '2' or '3' (first, second, or third chosen plane)
        """
        if direction == 'left':
            if 2 <= j <= 9 and 1 <= i <= 9 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(j-2, j+2):
                    if board[i][k] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(j - 2, j + 2):
                    board[i][k] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        elif direction == 'right':
            if 1 <= j <= 8 and 1 <= i <= 9 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(j-1, j+3):
                    if board[i][k] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(j - 1, j + 3):
                    board[i][k] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        elif direction == 'up':
            if 1 <= j <= 9 and 2 <= i <= 9 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(i-2, i+2):
                    if board[k][j] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(i - 2, i + 2):
                    board[k][j] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        elif direction == 'down':
            if 1 <= j <= 9 and 1 <= i <= 8 and board[i - 1][j - 1] == '-' and board[i - 1][j + 1] == '-' and board[i + 1][j - 1] == '-' and \
                        board[i + 1][j + 1] == '-':
                for k in range(i-1, i+3):
                    if board[k][j] == '-':
                        continue
                    else:
                        raise ValueError
                for k in range(i - 1, i + 3):
                    board[k][j] = symbol
                board[i - 1][j - 1] = symbol
                board[i - 1][j + 1] = symbol
                board[i + 1][j - 1] = symbol
                board[i + 1][j + 1] = symbol
            else:
                raise ValueError
        else:
            raise ValueError

    def create_hard_computer_board(self, computer_board, cabins, planes_directions):
        """
        It marks the randomly chosen planes on the computer's 10x10 board.
        :param computer_board: computer's board
        :param cabins: the array with the indexes of the planes' cabins
        :param planes_directions: the directions of the planes
        """
        directions = ['up', 'down', 'left', 'right']
        planes_number = 0
        while planes_number < 3:
            go_on_flag = 1
            while go_on_flag == 1:
                try:
                    i = randint(1, 9)
                    j = randint(1, 9)
                    direction = random.choice(directions)
                    self.choose_planes_easy(computer_board, direction, i, j, str(planes_number+1))
                    go_on_flag = 0
                except:
                    continue
            cabins.append((i,j))
            planes_directions.append(direction)
            planes_number = planes_number + 1

    def destroy_plane(self, board, i, j, direction):
        """
        It marks the shot plane on the board.
        :param board: board
        :param i: cabin's row
        :param j: cabin's column
        :param direction: plane's direction
        """
        if direction == 'up':
            for k in range(i - 2, i + 2):
                board[k][j] = 'X'
            board[i - 1][j - 1] = 'X'
            board[i - 1][j + 1] = 'X'
            board[i + 1][j - 1] = 'X'
            board[i + 1][j + 1] = 'X'
        elif direction == 'down':
            for k in range(i - 1, i + 3):
                board[k][j] = 'X'
            board[i - 1][j - 1] = 'X'
            board[i - 1][j + 1] = 'X'
            board[i + 1][j - 1] = 'X'
            board[i + 1][j + 1] = 'X'
        elif direction == 'left':
            for k in range(j - 2, j + 2):
                board[i][k] = 'X'
            board[i - 1][j - 1] = 'X'
            board[i - 1][j + 1] = 'X'
            board[i + 1][j - 1] = 'X'
            board[i + 1][j + 1] = 'X'
        elif direction == 'right':
            for k in range(j - 1, j + 3):
                board[i][k] = 'X'
            board[i - 1][j - 1] = 'X'
            board[i - 1][j + 1] = 'X'
            board[i + 1][j - 1] = 'X'
            board[i + 1][j + 1] = 'X'

    def strike_planes(self, displayed_board, actual_board, cabins, i, j, directions):
        """
        It marks the shot plane or the shot part of the plane on the board.
        :param displayed_board: the board that is displayed (only with the shot parts)
        :param actual_board: the actual computer's board
        :param cabins: plane's cabins
        :param i: cabins' rows
        :param j: cabins' columns
        :param directions: plane's directions
        """
        strike_flag = 0
        for k in range(0, len(cabins)):
            if cabins[k] == (i, j):
                self.destroy_plane(displayed_board, i, j, directions[k])
                self.destroy_plane(actual_board, i, j, directions[k])
                strike_flag = 1
        if strike_flag == 0:
            if actual_board[i][j] == '1' or actual_board[i][j] == '2' or actual_board[i][j] == '3':
                displayed_board[i][j] = 'O'
                actual_board[i][j] = 'O'

    def game_over(self, board):
        """
        It checks whether all the planes have been found.
        :return: 0 if false, else 1
        """
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == '1' or board[i][j] == '2' or board[i][j] == '3':
                    return 0
        return 1

    def empty_board(self, board):
        """
        It checks whether no planes have been hit yet (whether it's the first round).
        :param board: player's board
        :return: 1 if true, 0 if false
        """
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == '1' or board[i][j] == '2' or board[i][j] == '3' or board[i][j] == 'X' or board[i][j] == 'O':
                    return 0
        return 1

    def airs(self, board):
        """
        It checks whether there are any O's on the board.
        :return: the number of O's
        """
        count = 0
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == 'O':
                    count = count + 1
        return count

    def computer_strikes(self, seen_player_board, actual_player_board, cabins, directions, stricken_cases):
        """
        It marks the hit parts of the plane by the computer.
        Strategy: if there are any hit parts of the plane (O's or airs) it randomly strikes one of the parts around it.
                  It doesn't strike parts of the board that have been hit already.
        :param seen_player_board: the board that is only seen by the computer (with the strikes)
        :param actual_player_board: the entire player's board (with the planes and with the strikes)
        :param cabins: the planes' cabins
        :param directions: the planes' directions
        """
        if self.empty_board(seen_player_board):
            i = randint(1, 7)
            j = randint(1, 7)
            self.strike_planes(seen_player_board, actual_player_board, cabins, i, j, directions)
            if seen_player_board[i][j] == '-':
                stricken_cases.append((i, j))
        else:
            if self.airs(seen_player_board) >= 1:
                i = 0
                j = 0
                while i == 0 and j == 0:
                    i = randint(1, 7)
                    j = randint(1, 7)
                    if seen_player_board[i][j] != 'O':
                        i = 0
                        j = 0
                if i < 7 and j < 7:
                    choose_i = [i - 1, i, i + 1]
                    choose_j = [j - 1, j, j + 1]
                    aux_i = random.choice(choose_i)
                    aux_j = random.choice(choose_j)
                    go_on_flag = 1
                    while go_on_flag == 1:
                        if (aux_i == i and aux_j == j) or (aux_i,aux_j) in stricken_cases or seen_player_board[aux_i][aux_j] == 'X':
                            aux_i = random.choice(choose_i)
                            aux_j = random.choice(choose_j)
                        else:
                            self.strike_planes(seen_player_board, actual_player_board, cabins, aux_i,
                                               aux_j, directions)
                            stricken_cases.append((aux_i, aux_j))
                            go_on_flag = 0
                else:
                    choose_i = [i - 1, i]
                    choose_j = [j - 1, j]
                    aux_i = random.choice(choose_i)
                    aux_j = random.choice(choose_j)
                    go_on_flag = 1
                    while go_on_flag == 1:
                        if (aux_i == i and aux_j == j) or (aux_i,aux_j) in stricken_cases or seen_player_board[aux_i][aux_j] == 'X':
                            aux_i = random.choice(choose_i)
                            aux_j = random.choice(choose_j)
                        else:
                            self.strike_planes(seen_player_board, actual_player_board, cabins, aux_i,
                                               aux_j, directions)
                            stricken_cases.append((aux_i, aux_j))
                            go_on_flag = 0
            else:
                i = 0
                j = 0
                while i == 0 and j == 0:
                    i = randint(1, 7)
                    j = randint(1, 7)
                    if seen_player_board[i][j] == '-' and not ((i,j) in stricken_cases):
                        self.strike_planes(seen_player_board, actual_player_board, cabins, i, j, directions)
                        stricken_cases.append((i, j))
                    else:
                        i = 0
                        j = 0

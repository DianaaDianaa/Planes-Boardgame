import unittest
from domain import Board
from services import Services


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self._services = Services()

    def test_board(self):
        board1 = Board(10, 10)
        board2 = Board(10, 10)
        self.assertEqual(board1.board, board2.board)

    def test_choose_planes_easy(self):
        board = Board(8, 8)
        self._services.choose_planes_easy(board.board, 'down', 3, 2, '1')
        self.assertEqual(board.board[3][2], '1')

    def test_create_easy_computer_board(self):
        board = Board(8, 8)
        cabins = []
        planes_directions = []
        self._services.create_easy_computer_board(board.board, cabins, planes_directions)
        self.assertEqual(len(cabins), 3)
        self.assertEqual(len(planes_directions), 3)

    def test_choose_planes_hard(self):
        board = Board(10, 10)
        self._services.choose_planes_hard(board.board, 'down', 3, 2, '1')
        self.assertEqual(board.board[3][2], '1')

    def test_create_hard_computer_board(self):
        board = Board(10, 10)
        cabins = []
        planes_directions = []
        self._services.create_hard_computer_board(board.board, cabins, planes_directions)
        self.assertEqual(len(cabins), 3)
        self.assertEqual(len(planes_directions), 3)

    def test_destroy_plane(self):
        board = Board(8, 8)
        i = 1
        j = 5
        self._services.destroy_plane(board.board, i, j, 'down')
        for k in range(i - 1, i + 3):
            self.assertEqual(board.board[k][j], 'X')
        self.assertEqual(board.board[i-1][j-1], 'X')
        self.assertEqual(board.board[i-1][j+1], 'X')
        self.assertEqual(board.board[i+1][j-1], 'X')
        self.assertEqual(board.board[i+1][j+1], 'X')

    def test_strike_planes(self):
        seen_board = Board(8, 8)
        actual_board = Board(8, 8)
        cabins = []
        i = 1
        j = 5
        cabins.append((i, j))
        directions = []
        directions.append('down')
        for k in range(i - 1, i + 3):
            actual_board.board[k][j] = '1'
        actual_board.board[i - 1][j - 1] = '1'
        actual_board.board[i - 1][j + 1] = '1'
        actual_board.board[i + 1][j - 1] = '1'
        actual_board.board[i + 1][j + 1] = '1'
        i = 3
        j = 1
        cabins.append((i, j))
        directions.append('right')
        for k in range(j - 1, j + 3):
            actual_board.board[i][k] = '2'
        actual_board.board[i - 1][j - 1] = '2'
        actual_board.board[i - 1][j + 1] = '2'
        actual_board.board[i + 1][j - 1] = '2'
        actual_board.board[i + 1][j + 1] = '2'
        i = 5
        j = 4
        cabins.append((i, j))
        directions.append('up')
        for k in range(i - 2, i + 2):
            actual_board.board[k][j] = '3'
        actual_board.board[i - 1][j - 1] = '3'
        actual_board.board[i - 1][j + 1] = '3'
        actual_board.board[i + 1][j - 1] = '3'
        actual_board.board[i + 1][j + 1] = '3'
        i = 1
        j = 5
        self._services.strike_planes(seen_board.board, actual_board.board, cabins, i, j, directions)
        for k in range(i - 1, i + 3):
            self.assertEqual(seen_board.board[k][j], 'X')
        self.assertEqual(seen_board.board[i-1][j-1], 'X')
        self.assertEqual(seen_board.board[i-1][j+1], 'X')
        self.assertEqual(seen_board.board[i+1][j-1], 'X')
        self.assertEqual(seen_board.board[i+1][j+1], 'X')

    def test_game_over(self):
        board1 = Board(8, 8)
        i = 1
        j = 5
        self._services.destroy_plane(board1.board, i, j, 'down')
        self.assertEqual(self._services.game_over(board1.board), 1)
        board2 = Board(8, 8)
        i = 3
        j = 1
        for k in range(j - 1, j + 3):
            board2.board[i][k] = '2'
        board2.board[i - 1][j - 1] = '2'
        board2.board[i - 1][j + 1] = '2'
        board2.board[i + 1][j - 1] = '2'
        board2.board[i + 1][j + 1] = '2'
        self.assertEqual(self._services.game_over(board2.board), 0)

    def test_empty_board(self):
        board1 = Board(8, 8)
        self.assertEqual(self._services.empty_board(board1.board), 1)
        board2 = Board(8, 8)
        i = 3
        j = 1
        for k in range(j - 1, j + 3):
            board2.board[i][k] = '2'
        board2.board[i - 1][j - 1] = '2'
        board2.board[i - 1][j + 1] = '2'
        board2.board[i + 1][j - 1] = '2'
        board2.board[i + 1][j + 1] = '2'
        self.assertEqual(self._services.empty_board(board2.board), 0)

    def test_airs(self):
        board1 = Board(8, 8)
        self.assertEqual(self._services.airs(board1.board), 0)
        board2 = Board(8, 8)
        board2.board[2][3] = 'O'
        self.assertEqual(self._services.airs(board2.board), 1)

    def test_computer_strikes(self):
        seen_board = Board(8, 8)
        actual_board = Board(8, 8)
        cabins = []
        i = 1
        j = 5
        cabins.append((i, j))
        directions = []
        directions.append('down')
        for k in range(i - 1, i + 3):
            actual_board.board[k][j] = '1'
        actual_board.board[i - 1][j - 1] = '1'
        actual_board.board[i - 1][j + 1] = '1'
        actual_board.board[i + 1][j - 1] = '1'
        actual_board.board[i + 1][j + 1] = '1'
        i = 3
        j = 1
        cabins.append((i, j))
        directions.append('right')
        for k in range(j - 1, j + 3):
            actual_board.board[i][k] = '2'
        actual_board.board[i - 1][j - 1] = '2'
        actual_board.board[i - 1][j + 1] = '2'
        actual_board.board[i + 1][j - 1] = '2'
        actual_board.board[i + 1][j + 1] = '2'
        i = 5
        j = 4
        cabins.append((i, j))
        directions.append('up')
        for k in range(i - 2, i + 2):
            actual_board.board[k][j] = '3'
        actual_board.board[i - 1][j - 1] = '3'
        actual_board.board[i - 1][j + 1] = '3'
        actual_board.board[i + 1][j - 1] = '3'
        actual_board.board[i + 1][j + 1] = '3'
        stricken_cases = []
        self._services.computer_strikes(seen_board.board, actual_board.board, cabins, directions, stricken_cases)
        if self._services.empty_board(seen_board.board) == 0:
            if self._services.airs(seen_board.board) != 0:
                for i in range(0, len(seen_board.board)):
                    for j in range(0, len(seen_board.board)):
                        if seen_board.board[i][j] == 'O':
                            self.assertEqual(seen_board.board[i][j], actual_board.board[i][j])


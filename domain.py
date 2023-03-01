class Board:
    def __init__(self, lines=8, columns=8, empty="-"):
        self.__lines = lines
        self.__columns = columns
        self.__emptySpace = empty
        self.__board = self.__createBoard()

    def __createBoard(self):
        return [[self.__emptySpace for _ in range(self.__columns)] for _ in range(self.__lines)]

    @property
    def board(self):
        return self.__board

    @property
    def rows(self):
        return self.__lines

    @property
    def columns(self):
        return self.__columns

    def __str__(self):
        boardInString = " "
        alphabet = "ABCDEFGHIJ"
        for number in range(self.__lines):
            boardInString += f" {number + 1}"
        boardInString += "\n"
        for line in range(self.__lines):
            convertToString = " ".join([str(self.__board[line][column]) for column in range(self.__columns)]) + "\n"
            boardInString += alphabet[line] + " " + convertToString
        return boardInString



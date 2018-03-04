class Board:
    dimensions = []
    target_color = ''
    board = []

    def __init__(self, filename):
        self.make_board_from_file(filename)

    def make_board_from_file(self, filename):
        with open(filename, 'r') as file:
            self.dimensions = [int(number) for number in file.readline().split()]
            self.board = [line.split() for line in file.readlines()]
        self.target_color = self.board.pop()[0]

    def display(self):
        for line in self.board:
            print(line)
        print("------------------")

    def fill(self, row, column, color):
        orig_color = self.board[row][column]
        self.board[row][column] = color
        if self.board[row][column - 1] == orig_color:  # North
            self.fill(row, column - 1, color)
        if self.board[row][column + 1] == orig_color:  # South
            self.fill(row, column + 1, color)
        if self.board[row - 1][column] == orig_color:  # West
            self.fill(row - 1, column, color)
        if self.board[row + 1][column] == orig_color:  # East
            self.fill(row + 1, column, color)


game = Board('2018-01-19-input.txt')
game.display()
game.fill(0,2,'B')
game.display()
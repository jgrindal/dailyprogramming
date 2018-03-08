import copy

class Board:
    board = [['x', 'x', 'o'],['o', 'o', ' '],['o', ' ', 'o']]
    def __init__(self):
        print(self.is_won())

    def is_won(self):
        possibles = self.get_possibles()
        winner = self.evaluate(possibles)
        return winner

    def evaluate(self, possibles):
        won = False
        for poss in possibles:
            if set(poss) == {'x'} or set(poss) == {'o'}:
                won = True
        return won

    def get_possibles(self):
        possibles = []
        d1 = []
        d2 = []
        possibles = copy.copy(self.board)
        for i in range(len(self.board)):
            column = []
            for row in self.board:
                column.append(row[i])
            possibles.append(column)

            d1.append(self.board[len(self.board) - i - 1][i])
            d2.append(self.board[i][i])
        possibles.append(d1)
        possibles.append(d2)
        return possibles

Board()
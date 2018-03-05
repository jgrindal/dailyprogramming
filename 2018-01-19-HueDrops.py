import copy


COLORS = 'R O Y G B V'.split()


class BoardState:
    dimensions = []
    target_color = ''
    board = []

    def __init__(self, filename='', state=None):
        if filename:
            self.make_board_from_file(filename)
        if state:
            self.make_board_from_state(state)

    def make_board_from_file(self, filename):
        with open(filename, 'r') as file:
            self.dimensions = [int(number) for number in file.readline().split()]
            self.board = [line.split() for line in file.readlines()]
        self.target_color = self.board.pop()[0]

    def make_board_from_state(self, state):
        self.dimensions = state.pop(0)
        self.target_color = state.pop()
        self.board = state

    def display(self):
        for line in self.board:
            print(line)
        print("------------------")

    def fill(self, row=0, column=0, color=None):
        orig_color = self.board[row][column]
        self.board[row][column] = color
        top_row = False
        bottom_row = False
        left_column = False
        right_column = False
        if row == 0:
            top_row = True
        if row == self.dimensions[1] - 1:
            bottom_row = True
        if column == 0:
            left_column = True
        if column == self.dimensions[0] - 1:
            right_column = True
        if not left_column and self.board[row][column - 1] == orig_color:  # West
            self.fill(row, column - 1, color)
        if not right_column and self.board[row][column + 1] == orig_color:  # East
            self.fill(row, column + 1, color)
        if not top_row and self.board[row - 1][column] == orig_color:  # North
            self.fill(row - 1, column, color)
        if not bottom_row and self.board[row + 1][column] == orig_color:  # South
            self.fill(row + 1, column, color)

    def is_solved(self):
        solved = True
        for row in self.board:
            for cell in row:
                if cell != self.target_color:
                    solved = False
        return solved

    def score(self):
        score = 0
        for row in self.board:
            for cell in row:
                if cell == self.target_color:
                    score += 1
        return score


class StateTreeNode:
    state = None
    parent = None
    children = []

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    def add_child(self, child_to_add):
        child_to_add.parent = self
        self.children.append(child_to_add)

    def consolidate_children(self):
        consolidated_children = []
        for child in self.children:
            if child not in consolidated_children:
                consolidated_children.append(child)


class StateTree:
    head = None

    def __init__(self, head):
        self.head = StateTreeNode(head, None)

    def find(self, state_to_find):
        return self.head


initial_state = BoardState(filename='2018-01-19-input.txt')
parent_state = initial_state


for set_color in COLORS:
    child_state = copy.deepcopy(parent_state)
    child_state.fill(color=set_color)


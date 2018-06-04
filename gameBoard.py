from copy import deepcopy


class Game():
    """docstring for GameBoard"""

    def __init__(self):
        super().__init__()
        # cursor_location is the location of blank tile
        self.cursor_location = [2, 2]
        self.default = [['8', '7', '6'],
                        ['5', '4', '3'],
                        ['2', '1', ' ']]

        self.board = deepcopy(self.default)

        self.goal = [['1', '2', '3'],
                     ['4', '5', '6'],
                     ['7', '8', ' ']]
        self.counter = 0
        self.win = False

    # if the given position can move (the cursor tile can replace it), it
    # moves.
    def move(self, position):
        # do nothing if the game end
        if self.win:
            return

        (x, y) = position
        (cx, cy) = self.cursor_location

        # check the cursor location and move
        if x == cx and y + 1 == cy:
            self.move_left()
        if x == cx and y - 1 == cy:
            self.move_right()
        if x + 1 == cx and y == cy:
            self.move_up()
        if x - 1 == cx and y == cy:
            self.move_down()

    def move_up(self):
        if self.cursor_location[0] > 0:
            old = self.cursor_location[:]
            self.cursor_location[0] -= 1
            self.move_cursor(old)

    def move_down(self):
        if self.cursor_location[0] < 2:
            old = self.cursor_location[:]
            self.cursor_location[0] += 1
            self.move_cursor(old)

    def move_left(self):
        if self.cursor_location[1] > 0:
            old = self.cursor_location[:]
            self.cursor_location[1] -= 1
            self.move_cursor(old)

    def move_right(self):
        if self.cursor_location[1] < 2:
            old = self.cursor_location[:]
            self.cursor_location[1] += 1
            self.move_cursor(old)

    def move_cursor(self, old):
        self.add1()

        (x, y) = old
        (nx,  ny) = self.cursor_location

        dummy = self.board[x][y]
        self.board[x][y] = self.board[nx][ny]
        self.board[nx][ny] = dummy
        self.check_win()

    def check_win(self):
        if self.board == self.goal:
            self.win = True

    def add1(self):
        self.counter += 1

    def reset(self):
        self.counter = 0
        self.win = False
        self.cursor_location = [2, 2]
        self.board = deepcopy(self.default)

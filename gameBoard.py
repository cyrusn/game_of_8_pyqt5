from copy import deepcopy


class Game():
    """docstring for GameBoard"""

    def __init__(self):
        super().__init__()
        # cursor_loc is the location of blank tile
        self.default = [['8', '7', '6'],
                        ['5', '4', '3'],
                        ['2', '1', ' ']]

        self.board = deepcopy(self.default)
        self.counter = 0
        self.win = False

        self.__cursor_loc = [2, 2]
        self.__goal = [['1', '2', '3'],
                       ['4', '5', '6'],
                       ['7', '8', ' ']]

    # if the given position can move (the cursor tile can replace it), it
    # moves.
    def move(self, position):
        # do nothing if the game end
        if self.win:
            return

        (x, y) = position
        # store cursor loc, using tuple because tuple is immutable
        (cx, cy) = self.__cursor_loc

        # check the cursor location and update
        if x == cx and y + 1 == cy:
            self.__update_cursor_loc('left')
        if x == cx and y - 1 == cy:
            self.__update_cursor_loc('right')
        if x + 1 == cx and y == cy:
            self.__update_cursor_loc('up')
        if x - 1 == cx and y == cy:
            self.__update_cursor_loc('down')

        # update the board by with old cursor_loc as argument.
        # the updated cursor_loc can be retrieved in __update_board() by
        # self.__cursor_loc
        self.__update_board((cx, cy))

    def __update_cursor_loc(self, direction):
        if direction == 'up':
            self.__cursor_loc[0] -= 1

        if direction == 'down':
            self.__cursor_loc[0] += 1

        if direction == 'left':
            self.__cursor_loc[1] -= 1

        if direction == 'right':
            self.__cursor_loc[1] += 1

    def __update_board(self, old):
        self.__counter_increment()

        (x, y) = old
        (nx,  ny) = self.__cursor_loc

        dummy = self.board[x][y]
        self.board[x][y] = self.board[nx][ny]
        self.board[nx][ny] = dummy
        self.__check_win()

    def __check_win(self):
        if self.board == self.__goal:
            self.win = True

    def __counter_increment(self):
        self.counter += 1

    def reset(self):
        self.counter = 0
        self.win = False
        self.__cursor_loc = [2, 2]
        self.board = deepcopy(self.default)

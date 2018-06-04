#!/usr/bin/python3

import sys
from functools import partial
from copy import deepcopy
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication,
                             QHBoxLayout,
                             QVBoxLayout, QLabel)


class GameOf8(QWidget):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.win = False
        self.cursor_location = [2, 2]
        self.buttons = []
        self.positions = [(i, j) for i in range(3) for j in range(3)]

        self.default = [['8', '7', '6'],
                        ['5', '4', '3'],
                        ['2', '1', ' ']]

        self.board = deepcopy(self.default)

        self.goal = [['1', '2', '3'],
                     ['4', '5', '6'],
                     ['7', '8', ' ']]
        self.initUI()

    def initUI(self):
        resetLayout = QHBoxLayout()

        resetButton = QPushButton("Reset")
        resetButton.clicked.connect(self.on_reset)
        resetLayout.addWidget(resetButton)

        layout = QVBoxLayout()

        counterLabel = QLabel()

        self.counterLabel = counterLabel
        self.update_counterLabel()
        self.boardLayout = QGridLayout()

        layout.addWidget(counterLabel)
        layout.addLayout(self.boardLayout)
        layout.addLayout(resetLayout)
        self.initGameBoard()

        self.setLayout(layout)
        self.setWindowTitle('Game of 8')
        self.show()

    def initGameBoard(self):
        for i, j in self.positions:
            name = self.default[i][j]
            position = (i, j)
            button = QPushButton(name)
            button.clicked.connect(
                lambda _, pos=position, btn=button: self.on_click(pos, btn))
            self.buttons.append((position, button))
            self.boardLayout.addWidget(button, *position)

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

        x = old[0]
        y = old[1]
        nx = self.cursor_location[0]
        ny = self.cursor_location[1]
        dummy = self.board[x][y]
        self.board[x][y] = self.board[nx][ny]
        self.board[nx][ny] = dummy
        self.check_win()
        self.update_counterLabel()

    def check_win(self):
        if self.board == self.goal:
            self.win = True

    def on_click(self, pos, btn):
        if self.win:
            return

        x = pos[0]
        y = pos[1]
        cx = self.cursor_location[0]
        cy = self.cursor_location[1]

        if x == cx and y + 1 == cy:
            self.move_left()
        if x == cx and y - 1 == cy:
            self.move_right()
        if x + 1 == cx and y == cy:
            self.move_up()
        if x - 1 == cx and y == cy:
            self.move_down()

        for position, button in self.buttons:
            x = position[0]
            y = position[1]
            button.setText(self.board[x][y])

    def add1(self):
        self.counter += 1

    def update_counterLabel(self):
        counter_string = ""
        if self.win:
            counter_string = "You win! Total steps: %d" % (self.counter)
        else:
            counter_string = "Steps: %d" % (self.counter)

        self.counterLabel.setText(counter_string)

    def on_reset(self):
        self.counter = 0
        self.win = False
        self.cursor_location = [2, 2]
        self.update_counterLabel()
        self.board = deepcopy(self.default)
        for position, button in self.buttons:
            x = position[0]
            y = position[1]
            button.setText(self.default[x][y])

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GameOf8()
    sys.exit(app.exec_())

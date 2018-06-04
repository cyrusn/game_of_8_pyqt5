#!/usr/bin/python3

import sys
from gameBoard import Game
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QPushButton, QApplication, QHBoxLayout,
    QVBoxLayout, QLabel
)

button_style = '''
                QPushButton {
                    background-color: white; border-radius: 4px;
                    border: 1px solid grey; width: 100px; height: 60px;
                    font-size: 24px;
                }
                '''

counter_style = 'QLabel {font-size: 24px;}'


class GameOf8(QWidget):

    def __init__(self):
        super().__init__()
        self.buttons = []
        self.positions = [(i, j) for i in range(3) for j in range(3)]
        self.game = Game()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        counterLabel = self.initCounterLabel()
        boardLayout = self.initBoardLayout()
        resetLayout = self.initResetLayout()

        layout.addWidget(counterLabel)
        layout.addLayout(boardLayout)
        layout.addLayout(resetLayout)

        self.setWindowTitle('Game of 8')
        self.setLayout(layout)
        self.show()

    def initResetLayout(self):
        resetLayout = QHBoxLayout()
        resetButton = self.initResetButton()
        resetLayout.addWidget(resetButton)
        return resetLayout

    def initResetButton(self):
        resetButton = QPushButton("Reset")
        resetButton.setStyleSheet(button_style)
        resetButton.clicked.connect(self.on_reset)
        return resetButton

    def initCounterLabel(self):
        counterLabel = QLabel()
        counterLabel.setStyleSheet(counter_style)
        counter_string = self.generate_counter_string()
        counterLabel.setText(counter_string)
        self.counterLabel = counterLabel
        return counterLabel

    def initBoardLayout(self):
        boardLayout = QGridLayout()
        for i, j in self.positions:
            name = self.game.default[i][j]
            position = (i, j)
            button = QPushButton(name)
            button.setStyleSheet(button_style)
            button.clicked.connect(
                lambda _, pos=position: self.on_click(pos)
            )
            self.buttons.append((position, button))
            boardLayout.addWidget(button, *position)
        return boardLayout

    def on_click(self, pos):
        self.game.move(pos)
        self.update_counterLabel()
        self.update_boardLayout(self.game.board)

    def update_boardLayout(self, board):
        for position, button in self.buttons:
            (x, y) = position
            button.setText(board[x][y])

    def generate_counter_string(self):
        if self.game.win:
            return "You win! Total steps: %d" % (self.game.counter)
        else:
            return "Steps: %d" % (self.game.counter)

    def update_counterLabel(self):
        counter_string = self.generate_counter_string()
        self.counterLabel.setText(counter_string)

    def on_reset(self):
        self.game.reset()

        # reset counterLabel
        self.update_counterLabel()

        # reset the boardLayout to default one
        self.update_boardLayout(self.game.default)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GameOf8()
    sys.exit(app.exec_())

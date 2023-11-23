# 实现Game2048类
import random


class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()
        self.steps = 0

    def reset(self):
        self.__init__()

    def add_new_tile(self):
        empty_tiles = [(x, y) for x in range(4) for y in range(4) if self.board[x][y] == 0]
        if not empty_tiles:
            return False
        x, y = random.choice(empty_tiles)
        self.board[x][y] = random.choice([2, 4])

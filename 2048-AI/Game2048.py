# 实现Game2048类
import random


class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.steps = 0
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def reset(self):
        self.__init__()

    def add_new_tile(self):
        empty_tiles = [(x, y) for x in range(4) for y in range(4) if self.board[x][y] == 0]
        if not empty_tiles:
            return False
        x, y = random.choice(empty_tiles)
        self.board[x][y] = random.choice([2, 4])

    def move(self, direction):
        pass

    def status(self):
        # 未结束返回True,已结束返回False
        pass

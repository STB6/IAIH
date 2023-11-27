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
        # direction:0,1,2,3分别表示上下左右
        # 返回值:是否移动成功
        # 如果移动成功，则添加一个新的方块，并按照2048规则加分
        moved = False
        for _ in range(4):
            if direction == 0:  # up
                for x in range(1, 4):
                    for y in range(4):
                        if self.board[x][y] != 0 and (self.board[x - 1][y] == 0 or self.board[x - 1][y] == self.board[x][y]):
                            self.board[x - 1][y] += self.board[x][y]
                            self.board[x][y] = 0
                            moved = True
                            if self.board[x - 1][y] != 0:
                                self.score += self.board[x - 1][y]
            elif direction == 1:  # down
                for x in range(2, -1, -1):
                    for y in range(4):
                        if self.board[x][y] != 0 and (self.board[x + 1][y] == 0 or self.board[x + 1][y] == self.board[x][y]):
                            self.board[x + 1][y] += self.board[x][y]
                            self.board[x][y] = 0
                            moved = True
                            if self.board[x + 1][y] != 0:
                                self.score += self.board[x + 1][y]
            elif direction == 2:  # left
                for x in range(4):
                    for y in range(1, 4):
                        if self.board[x][y] != 0 and (self.board[x][y - 1] == 0 or self.board[x][y - 1] == self.board[x][y]):
                            self.board[x][y - 1] += self.board[x][y]
                            self.board[x][y] = 0
                            moved = True
                            if self.board[x][y - 1] != 0:
                                self.score += self.board[x][y - 1]
            elif direction == 3:  # right
                for x in range(4):
                    for y in range(2, -1, -1):
                        if self.board[x][y] != 0 and (self.board[x][y + 1] == 0 or self.board[x][y + 1] == self.board[x][y]):
                            self.board[x][y + 1] += self.board[x][y]
                            self.board[x][y] = 0
                            moved = True
                            if self.board[x][y + 1] != 0:
                                self.score += self.board[x][y + 1]
        if moved:
            self.add_new_tile()
        return moved

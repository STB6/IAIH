# 实现Game2048类
# reset()           重置棋盘
# add_tile()        随机添加数字
# print_board()     打印棋盘
# move(dirction)    向左/右/上/下移动
# max_tile()        返回当前最大数字
# score()           返回当前分数
import random


class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.add_tile()
        self.add_tile()

    # 重置棋盘
    def reset(self):
        self.__init__()

    # 随机添加数字
    def add_tile(self):
        empty_positions = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_positions:
            r, c = random.choice(empty_positions)
            self.board[r][c] = 2
            return True
        return False

    # 打印棋盘
    def print_board(self):
        for i in range(4):
            row_str = " ".join([f"{str(self.board[i][j]):^4}" for j in range(4)])
            print(f"{row_str}")
            print()

    # 向左压缩棋盘
    def compress(self):
        compressed = False
        for i in range(4):
            pos = 0
            for j in range(4):
                if self.board[i][j] != 0:
                    if j != pos:
                        self.board[i][pos] = self.board[i][j]
                        self.board[i][j] = 0
                        compressed = True
                    pos += 1
        return compressed

    # 合并相邻相同的数字
    def merge(self):
        merged = False
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j + 1] and self.board[i][j] != 0:
                    self.board[i][j] *= 2
                    self.board[i][j + 1] = 0
                    merged = True
        return merged

    # 左右反转棋盘
    def reverse(self):
        self.board = [row[::-1] for row in self.board]

    # 转置棋盘
    def transpose(self):
        self.board = [list(row) for row in zip(*self.board)]

    def move_left(self):
        compressed = self.compress()
        merged = self.merge()
        if merged:
            self.compress()
        return compressed or merged

    def move_right(self):
        self.reverse()
        changed = self.move_left()
        self.reverse()
        return changed

    def move_up(self):
        self.transpose()
        changed = self.move_left()
        self.transpose()
        return changed

    def move_down(self):
        self.transpose()
        changed = self.move_right()
        self.transpose()
        return changed

    def move(self, direction):
        if direction == 0:
            return self.move_left()
        elif direction == 1:
            return self.move_right()
        elif direction == 2:
            return self.move_up()
        else:
            return self.move_down()

    def max_tile(self):
        return max(max(row) for row in self.board)

    def score(self):
        return sum(sum(row) for row in self.board) + self.max_tile()

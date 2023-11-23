# 实现TTT类
# 使用长度为9的列表表示棋盘,其中X存储为1,O存储为-1,空位存储为0
# reset()                   重置棋盘
# current_side()            返回当前执子方
# print_board()             打印棋盘
# place(x, y)               落子,成功返回True,失败返回False
# ai_place(priority_list)   传入落子优先级列表,依次尝试落子,并返回最终落子坐标
# get_board_for_ai()        返回棋盘状态,当前执子方永远为1
# status()                  X赢返回1,O赢返回-1,和棋返回0,棋局未结束返回None
class TTT:
    def __init__(self):
        self.reset()

    def reset(self):
        # 使用长度为9的列表来表示棋盘,X为1, O为-1, 空位为0
        self.board = [0] * 9
        self.steps = 1

    def current_side(self):
        # 返回当前执子方
        return 1 if self.steps % 2 == 1 else -1

    def print_board(self):
        # 打印棋盘
        print("---------")
        print("| |A|B|C|")
        print("|-+-+-+-|")
        for i in range(3):
            row_str = "|".join(
                ["X" if self.board[i * 3 + j] == 1 else "O" if self.board[i * 3 + j] == -1 else " " for j in range(3)]
            )
            print(f"|{i+1}|{row_str}|")
            print("|-+-+-+-|")
        print("---------")

    def place(self, x, y):
        # 落子,成功返回True,失败返回False
        index = x * 3 + y
        if self.board[index] == 0:
            self.board[index] = self.current_side()
            self.steps += 1
            return True
        return False

    def ai_place(self, priority_list):
        # 传入落子优先级列表,依次尝试落子,并返回最终落子坐标
        for index in priority_list:
            if self.board[index] == 0:
                self.board[index] = self.current_side()
                self.steps += 1
                return divmod(index, 3)

    def get_board_for_ai(self):
        # 返回棋盘状态,当前执子方永远为1
        return [cell * self.current_side() for cell in self.board]

    def status(self):
        # X赢返回1,O赢返回-1,和棋返回0,棋局未结束返回None
        lines = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != 0:
                return self.board[line[0]]
        if self.steps == 10:
            return 0
        return None

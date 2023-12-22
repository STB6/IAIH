from Game2048 import Game2048


def play(self):
    while True:
        self.print_board()
        dir = input("请输入移动方向：w上 s下 a左 d右 q退出\n")
        if dir == "w":
            changed = self.move_up()
        elif dir == "s":
            changed = self.move_down()
        elif dir == "a":
            changed = self.move_left()
        elif dir == "d":
            changed = self.move_right()
        elif dir == "q":
            break
        else:
            print("输入错误，请重新输入！")
            continue
        if changed:
            self.add_tile()


if __name__ == "__main__":
    game = Game2048()
    # 初始化一个前两行均为2的棋盘
    for i in range(2):
        for j in range(4):
            game.board[i][j] = 2
    play(game)

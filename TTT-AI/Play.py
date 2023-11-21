# 实现play方法
# 用于使玩家与AI对战
from TTT import TTT
from Decide import decide


def get_player_input():
    while True:
        coord = input("请输入落子坐标(如1A):")
        if len(coord) == 2 and coord[0] in "123" and coord[1].upper() in "ABC":
            x, y = int(coord[0]) - 1, "ABC".index(coord[1].upper())
            return x, y
        print("输入无效,请重新输入")


def play(gene):
    while True:
        game = TTT()
        player_side = input("请选择执子方,X(先手)还是O(后手),输入Q退出:").upper()
        while player_side not in ["X", "O", "Q"]:
            player_side = input("输入无效,请选择执子方,X(先手)还是O(后手),输入Q退出:").upper()
        if player_side == "Q":
            break
        player_turn = player_side == "X"
        while game.status() is None:
            if player_turn:
                game.print_board()
                x, y = get_player_input()
                while not game.place(x, y):
                    print("该位置已被占用,请重新选择")
                    x, y = get_player_input()
            else:
                x, y = game.ai_place(decide(gene, game.get_board_for_ai()))
                print(f"AI落子在: {x+1}{'ABC'[y]}")
            player_turn = not player_turn
        game.print_board()
        status = game.status()
        if status == 0:
            print("和棋")
        elif (status == 1 and player_side == "X") or (status == -1 and player_side == "O"):
            print("玩家胜利")
        else:
            print("AI胜利")
        print("开始新对局")

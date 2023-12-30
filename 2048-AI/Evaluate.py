# 实现evaluate方法
# 适应度即为其游戏得分
# evaluate(gene)    适应度评估方法,返回个体适应度
from Decide import decide
from Game2048 import Game2048


def evaluate(gene):
    game = Game2048()
    while game.status():
        for i in decide(gene, game.board):
            if game.move(i):
                game.add_tile()
                break
        else:
            break
    return 2 ** (game.score() / 200)

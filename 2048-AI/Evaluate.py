# 实现evaluate方法
# 格式适应度即为其游戏得分
# evaluate(gene)    适应度评估方法,返回个体适应度
from Decide import decide
from Game2048 import Game2048


def evaluate(gene):
    game = Game2048()
    while game.status():
        game.move(decide(gene, game.board))
    return game.score

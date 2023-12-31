# 实现evaluate方法
# 适应度即为其游戏得分
# evaluate(gene)    适应度评估方法,返回个体适应度
import math
from Decide import decide
from Game2048 import Game2048

# 全局常量
TIMES = 16  # 每个个体的适应度评估次数,越大适应度越准确


# 适应度评估函数
def evaluate(gene):
    game = Game2048()
    average_score = 0
    max_tiles = []
    for i in range(TIMES):
        while game.status():
            for i in decide(gene, game.board):
                if game.move(i):
                    game.add_tile()
                    break
            else:
                break
        average_score += game.score() / TIMES
        max_tiles.append(game.max_tile())
        game.reset()
    return (math.exp(average_score / 512) - 1,), sum(max_tiles) / TIMES, max(max_tiles)

# 实现evaluate方法
# 适应度即为其游戏得分
# evaluate(gene)    适应度评估方法,返回个体适应度
import math
import concurrent.futures
from Decide import decide
from Game2048 import Game2048


TIMES = 32  # 每个个体的适应度评估次数,越大适应度越准确


# 个体适应度评估函数
def evaluate_individual(gene):
    game = Game2048()
    average_score = 0
    max_tile_record = [0] * 16  # 分别对应4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072
    for i in range(TIMES):
        while True:
            for i in decide(gene, game.board):
                if game.move(i):
                    game.add_tile()
                    break
            else:
                break
        average_score += game.score() / TIMES
        max_tile_record[round(math.log2(game.max_tile()) - 2)] += 1
        game.reset()
    fitness = math.exp(average_score / 512) - 1
    return (fitness,), max_tile_record


# 种群适应度评估函数
def evaluate(gene_list):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(evaluate_individual, gene_list))
    for gene, result in zip(gene_list, results):
        gene.fitness.values, gene.information = result

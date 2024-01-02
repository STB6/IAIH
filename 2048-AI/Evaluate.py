# 实现evaluate方法
# 适应度即为其游戏得分
# evaluate(gene)    适应度评估方法,返回个体适应度
import math
from Decide import decide
from Game2048 import Game2048

# 全局常量
TIMES = 32  # 每个个体的适应度评估次数,越大适应度越准确


# 适应度评估函数
def evaluate(gene):
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
    fitness = math.exp(average_score / 512) - 1 - max_tile_record[4] * 0.8 - max_tile_record[5] * 0.4 - max_tile_record[6] * 0.2 + max_tile_record[8] * 0.2
    return (fitness,), max_tile_record


if __name__ == "__main__":
    from GAEvolution import generate

    gene_list = generate()
    print("fn\t64\t128\t256\t512\t1024\t2048")
    print(f"{round(gene_list[0].fitness.values[0], 2)}\t" + "\t".join(str(gene_list[0].information[i]) for i in [4, 5, 6, 7, 8, 9]))

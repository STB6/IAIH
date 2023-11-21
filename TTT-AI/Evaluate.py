# 实现evaluate方法
# 通过双循环赛,评估种群中所有个体的适应度
# battle(gene1, gene2)  让gene1和gene2对战,gene1为先手,返回两者的分数
# evaluate(gene_list)   适应度评估方法,返回包含所有基因分数的列表
from Decide import decide
from TTT import TTT


def battle(gene1, gene2):
    # 实现两个AI对战
    game = TTT()
    score1, score2 = 0, 0
    while game.status() is None:
        current_side = game.current_side()
        current_gene = gene1 if current_side == 1 else gene2
        priority_list = decide(current_gene, game.get_board_for_ai())
        game.ai_place(priority_list)
    status = game.status()
    if status == 1:
        score1 += 2  # gene1胜利(先手),加2分
    elif status == -1:
        score2 += 3  # gene2胜利(后手),加3分
    return score1, score2


def evaluate(gene_list):
    # 适应度评估方法
    num_genes = len(gene_list)
    scores = [0] * num_genes
    for i in range(num_genes):
        for j in range(num_genes):
            if i != j:
                result = battle(gene_list[i], gene_list[j])
                scores[i] += result[0]
                scores[j] += result[1]
    return scores

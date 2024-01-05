# 实现遗传算法
# generate()    生成随机种群,返回gene_list
# evolve()      遗传进化操作
import random
import Decide
from deap import creator, base, tools
from Evaluate import evaluate


GENE_LENGTH = Decide.INPUT_NODES * Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 * Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 * Decide.OUTPUT_NODES + Decide.OUTPUT_NODES
POPULATION_SIZE = 128  # 种群大小,应为8的倍数
MUTATION_AMPLITUDE = 0.1  # 变异幅度


# 创建适应度类和个体类
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# 设置工具箱
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -1.0, 1.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=GENE_LENGTH)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 注册交叉、变异和选择方法
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=MUTATION_AMPLITUDE)
toolbox.register("select", tools.selRoulette)


# 生成随机种群
def generate():
    gene_list = toolbox.population(POPULATION_SIZE)

    # 评估当前适应度
    evaluate(gene_list)

    # 按适应度对种群进行排序
    gene_list.sort(key=lambda x: x.fitness.values, reverse=True)

    return gene_list


# 遗传进化操作
def evolve(gene_list):
    # 选择
    gene_list[POPULATION_SIZE // 8 : POPULATION_SIZE // 2] = toolbox.select(gene_list[POPULATION_SIZE // 8 : POPULATION_SIZE // 8 * 7], POPULATION_SIZE // 2 - POPULATION_SIZE // 8)
    gene_to_be_mutated = gene_list[: POPULATION_SIZE // 4]
    del gene_list[POPULATION_SIZE // 2 :]

    # 交叉
    random.shuffle(gene_list)
    for i in range(0, POPULATION_SIZE // 4, 2):
        gene_list.append(creator.Individual(gene_list[i]))
        gene_list.append(creator.Individual(gene_list[i + 1]))
        toolbox.mate(gene_list[-1], gene_list[-2])

    # 变异
    for gene in gene_to_be_mutated:
        gene_list.append(creator.Individual(gene))
        toolbox.mutate(gene_list[-1])

    # 评估当前适应度
    evaluate(gene_list)

    # 按适应度对种群进行排序
    gene_list.sort(key=lambda x: x.fitness.values, reverse=True)


def save(gene_list):
    with open("./TTT-AI/gene_list.txt", "w") as file:
        for gene in gene_list:
            file.write(str(gene) + "\n")


def load():
    gene_list = []
    with open("./TTT-AI/gene_list.txt", "r") as file:
        for line in file:
            gene_list.append(creator.Individual(eval(line)))
    evaluate(gene_list)
    return gene_list

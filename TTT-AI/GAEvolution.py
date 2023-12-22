# 实现遗传算法
# generate()    生成随机种群,返回gene_list
# evolve()      遗传操作,将最后一代gene_list按照适应度从高到低排序后返回
import random
import Decide
from deap import creator, base, tools
from Evaluate import evaluate

# 全局常量
GENE_LENGTH = (
    Decide.INPUT_NODES * Decide.HIDDEN_NODES1
    + Decide.HIDDEN_NODES1
    + Decide.HIDDEN_NODES1 * Decide.HIDDEN_NODES2
    + Decide.HIDDEN_NODES2
    + Decide.HIDDEN_NODES2 * Decide.OUTPUT_NODES
    + Decide.OUTPUT_NODES
)
POPULATION_SIZE = 30  # 种群大小
CROSSOVER_PROB = 0.5  # 交叉概率
MUTATION_PROB = 0.2  # 变异概率
MUTATION_AMPLITUDE = 0.1  # 变异幅度
GENERATIONS = 200  # 代数


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
toolbox.register("select", tools.selTournament, tournsize=3)


def generate():
    # 生成随机种群
    return toolbox.population(POPULATION_SIZE)


def evolve(gene_list):
    # 遗传操作
    for generation in range(GENERATIONS):
        # 一次性计算整个种群的适应度
        fitnesses = evaluate(gene_list)
        for ind, fit in zip(gene_list, fitnesses):
            ind.fitness.values = (fit,)
        # 选择
        selected = tools.selBest(gene_list, len(gene_list))
        # 克隆选中的个体
        offspring = list(map(toolbox.clone, selected))
        # 交叉和变异
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CROSSOVER_PROB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            if random.random() < MUTATION_PROB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # 更新种群
        gene_list[:] = offspring
        # 输出当前代数
        print(f"Generation {generation + 1} completed")
    # 在最后一代结束时,按适应度对种群排序
    gene_list.sort(key=lambda ind: ind.fitness.values, reverse=True)
    return gene_list

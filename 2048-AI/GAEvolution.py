# 实现遗传算法
# generate()    生成随机种群,返回gene_list
# evolve()      遗传操作,将最后一代gene_list按照适应度从高到低排序后返回
import random
import Decide
from deap import creator, base, tools
from Evaluate import evaluate

# 全局常量
GENE_LENGTH = Decide.INPUT_NODES * Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 * Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 * Decide.OUTPUT_NODES + Decide.OUTPUT_NODES
POPULATION_SIZE = 100  # 种群大小
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
    # 进化指定代数
    for generation in range(GENERATIONS):
        # 评估当前代的每个个体的适应度
        for individual in gene_list:
            individual.fitness.values = (evaluate(individual),)
        # 选择下一代
        offspring = toolbox.select(gene_list, len(gene_list))
        # 克隆选出的个体
        offspring = list(map(toolbox.clone, offspring))

        # 应用交叉和变异
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CROSSOVER_PROB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTATION_PROB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # 评估产生的变异个体的适应度
        for mutant in offspring:
            if not mutant.fitness.valid:
                mutant.fitness.values = (evaluate(mutant),)
        gene_list[:] = offspring
        fittest_individual = max(gene_list, key=lambda x: x.fitness.values[0])
        print(f"Generation {generation + 1} completed. Fittest individual fitness: {fittest_individual.fitness.values[0]}")
    # 按适应度对最后一代进行排序
    gene_list.sort(key=lambda x: x.fitness.values, reverse=True)
    return gene_list

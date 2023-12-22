# 实现遗传算法
# generate()    生成随机种群,返回gene_list
# evolve()      遗传操作,将最后一代gene_list按照适应度从高到低排序后返回
import random
import Decide
from deap import creator, base, tools
from Evaluate import evaluate

# 全局常量
GENE_LENGTH = Decide.INPUT_NODES * Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 * Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 * Decide.OUTPUT_NODES + Decide.OUTPUT_NODES
POPULATION_SIZE = 30  # 种群大小
CROSSOVER_PROB = 0.5  # 交叉概率
MUTATION_PROB = 0.2  # 变异概率
MUTATION_AMPLITUDE = 0.1  # 变异幅度
GENERATIONS = 200  # 代数

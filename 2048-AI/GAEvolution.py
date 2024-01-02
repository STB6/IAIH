# 实现遗传算法
# generate()    生成随机种群,返回gene_list
# evolve()      遗传进化操作
import random
import Decide
import concurrent.futures
from deap import creator, base, tools
from Evaluate import evaluate

# 全局常量
GENE_LENGTH = Decide.INPUT_NODES * Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 + Decide.HIDDEN_NODES1 * Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 + Decide.HIDDEN_NODES2 * Decide.OUTPUT_NODES + Decide.OUTPUT_NODES
POPULATION_SIZE = 160  # 种群大小,应为8的倍数
MUTATION_AMPLITUDE = 0.15  # 变异幅度
GENERATIONS = 1000  # 代数


# 创建适应度类和个体类
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax, information=list)

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

    # 尝试读取上一次的最优个体
    try:
        with open("best_gene.txt", "r") as f:
            gene_list[0] = creator.Individual(eval(f.read()))
            print("Last best gene loaded.")
    except FileNotFoundError:
        print("Start from scratch.")

    # 评估当前适应度
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(evaluate, gene_list))
    for gene, result in zip(gene_list, results):
        gene.fitness.values, gene.information = result

    # 按适应度对种群进行排序
    gene_list.sort(key=lambda x: x.fitness.values, reverse=True)

    return gene_list


# 遗传进化操作
def evolve(gene_list):
    for generation in range(GENERATIONS):
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
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(evaluate, gene_list))
        for gene, result in zip(gene_list, results):
            gene.fitness.values, gene.information = result

        # 按适应度对种群进行排序
        gene_list.sort(key=lambda x: x.fitness.values, reverse=True)

        # 信息输出
        print(f"Generation {generation + 1} finished. Best 16 genes:")
        print("fn\t64\t128\t256\t512\t1024\t2048")
        for gene in gene_list[:16]:
            print(f"{round(gene.fitness.values[0], 2)}\t" + "\t".join(str(gene.information[i]) for i in [4, 5, 6, 7, 8, 9]))
        if generation % 10 == 9:
            with open("best_gene.txt", "w") as f:
                f.write(str(gene_list[0]))
            print("Best gene saved.")


def main():
    gene_list = generate()
    evolve(gene_list)


if __name__ == "__main__":
    main()

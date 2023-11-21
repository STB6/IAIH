from GAEvolution import generate, evolve
from Play import play


def main():
    # 生成随机种群
    population = generate()
    # 遗传进化
    evolved_population = evolve(population)
    # 让最后一代的最优AI与玩家对战
    best_individual = evolved_population[0]
    play(best_individual)


if __name__ == "__main__":
    main()

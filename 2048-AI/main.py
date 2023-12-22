from GAEvolution import generate, evolve


def main():
    population = generate()
    final_population = evolve(population)
    best_individual = final_population[0]
    print("Best Individual: ", best_individual)
    print("Best Fitness: ", best_individual.fitness.values)


if __name__ == "__main__":
    main()

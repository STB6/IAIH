from GAEvolution import *

GENERATIONS = 10000  # 遗传代数


def main():
    while True:
        answer = input("Start from last generation? (Y/N) ")
        if answer == "Y":
            try:
                gene_list = load()
            except Exception:
                print("Loading failed.")
                print("Start from scratch.")
                gene_list = generate()
            break
        elif answer == "N":
            print("Start from scratch.")
            gene_list = generate()
            break
        else:
            print("Invalid input.")

    for genegration in range(GENERATIONS):
        evolve(gene_list)
        if genegration % 10 != 9:
            print(f"Generation {genegration + 1} finished.")
        else:
            save(gene_list)
            print(f"Generation {genegration + 1} finished and saved.")
        print("fn\t64\t128\t256\t512\t1024\t2048")
        for gene in gene_list[:16]:
            print(f"{round(gene.fitness.values[0], 2)}\t" + "\t".join(str(gene.information[i]) for i in [4, 5, 6, 7, 8, 9]))
        print()
    print("Evolution finished.")


if __name__ == "__main__":
    main()

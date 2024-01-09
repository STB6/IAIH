from GAEvolution import *
from Play import play

GENERATIONS = 1000  # 遗传代数


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
    print("Evolution finished.")
    play([0])


if __name__ == "__main__":
    main()

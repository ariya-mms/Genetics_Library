import random


def swap_mutation(chromosome):
    random_num = random.randint
    # avoid choosing same gene
    i = 0
    j = 0
    while i is j:
        i, j = random_num(chromosome.length), random_num(chromosome.length)
    chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]
    return chromosome

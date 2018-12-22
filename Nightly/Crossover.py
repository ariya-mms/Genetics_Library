import numpy as np
import Chromosome
# np.random.seed(75)

def single_point_crossover(population, selection_method, pc):
    p1 = selection_method(pop)
    p2 = selection_method(pop)

    chrom_length = len(p1)

    point = np.random.randint(1, chrom_length - 1)

    if np.random.random() < pc:
        c1 = Chromosome(chrom_length)
        c2 = Chromosome(chrom_length)
        for i in range(chrom_length):
            if i < point:
                c1.genes[i] = p1.genes[i]
                c2.genes[i] = p2.genes[i]
            else:
                c1.genes[i] = p2.genes[i]
                c2.genes[i] = p1.genes[i]
    else:
        c1 = deepcopy(p1)
        c2 = deepcopy(p2)

    # Reset fitness of each parent
    c1.reset()
    c2.reset()

    return c1, c2
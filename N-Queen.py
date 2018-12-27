from genetics import chrom, initpop, selection
import numpy as np

POPULATION_SIZE = 10
BOARD_SIZE = 10
TOURNAMENT_SIZE = 3
ELITISM_COUNT = 2
Pc = 0.9
Pm = 0.1


def calc_chrom_fit(chromosome):
    genes = chromosome.genes
    clashes = 0
    for i in range(len(genes)):
        for j in range(len(genes)):
            if i != j:
                dx = abs(i - j)
                dy = abs(genes[i] - genes[j])
                if dx == dy:
                    clashes += 1
    return (28 - clashes)*100/28


def calc_pop_fit(
        population, best_fitness=float('-inf'), best_chrome=None):
    for chromosome in population:
        chromosome.fitness = calc_chrom_fit(chromosome)
        if chromosome.fitness > best_fitness:
            best_fitness = chromosome.fitness
            best_chrome = chromosome
    return best_fitness, best_chrome


population = initpop.pseudo_rand('permutational', POPULATION_SIZE, BOARD_SIZE)
best_fitness = float('-inf')
best_fitness, best_individual = calc_pop_fit(
    population, best_fitness)
generation = 1
while best_fitness != 100.0:
        # for generation in range(1, generation_size):
        # Create New Population
    new_population = np.array([], dtype=chrom.Chromosome)
    # Choose parents to crossover
    for _ in range(int(POPULATION_SIZE / 2)):
            # Selection
        parent1 = selection.tournament(population)
        parent2 = selection.tournament(population)

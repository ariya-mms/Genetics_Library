from genetics import chrom, initpop, selection, chross, mutation
import numpy as np
import random

POPULATION_SIZE = 10
BOARD_SIZE = 10
TOURNAMENT_SIZE = 3
ELITISM_COUNT = 2
Pc = 0.9
Pm = 0.1
listt = list(np.ndarray((4,4)))

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


def elites_of_current_population(population=None, count=ELITISM_COUNT):
    size = len(population)
    # sort population ascending and choose count number of best individuals
    sorted(population)
    return [population[size-i] for i in range(1, count+1)]


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
        # CrossOver
        if Pc > random.random():
            child1, child2 = chross.pmx(parent1, parent2)
        new_population = np.append(new_population, [child1, child2])
    # Mutation
    for i in range(POPULATION_SIZE):
        if Pm > random.random:
            new_population[i] = mutation.swap_mutation(new_population[i])
    # Elitism (2 => pop_size-2)
    # np.random.shuffle(new_population)   # TODO WTF?
    new_population = np.concatenate(
        (elites_of_current_population(current_population), new_population[:POPULATION_SIZE - elitism_count]))
    # Evaluate Fitness and best Fitness for new Population
    best_fitness, best_individual = calculate_population_fitness(
        new_population, best_fitness)
    # add new generation to generation list
    current_population = new_population
    # generations = np.append(generations, current_population)
    generation += 1
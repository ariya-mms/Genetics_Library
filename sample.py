"""An example to demonstrate usage of Genetics library
by solving N-Queen problem

Returns:
    None -- [description]
"""

from genetics import chrom, initpop
import numpy as np

POPULATION_SIZE = 10
BOARD_SIZE = 10
TOURNAMENT_SIZE = 3
ELITISM_COUNT = 2
Pc = 0.9
Pm = 0.1


def calculate_individual_fitness(individual):
    """[summary]

    Arguments:
        individual {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    chromosome = individual.genes
    clashes = 0
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if i != j:
                dx = abs(i - j)
                dy = abs(chromosome[i] - chromosome[j])
                if dx == dy:
                    clashes += 1
    return (28 - clashes)*100/28


def calculate_population_fitness(
        population=None, best_fitness=float('-inf'), best_individual=None):
    """[summary]

    Keyword Arguments:
        population {[type]} -- [description] (default: {None})
        best_fitness {[type]} -- [description] (default: {float('-inf')})
        best_individual {[type]} -- [description] (default: {None})

    Returns:
        [type] -- [description]
    """

    for individual in population:
        individual.fitness = calculate_individual_fitness(individual)
        if individual.fitness > best_fitness:
            best_fitness = individual.fitness
            best_individual = individual
    return best_fitness, best_individual


population = initpop.pseudo_rand('permutational', POPULATION_SIZE, BOARD_SIZE)
best_fitness = float('-inf')
best_fitness, best_individual = calculate_population_fitness(
    population, best_fitness)
generation = 1
while best_fitness != 100.0:
        # for generation in range(1, generation_size):
        # Create New Population
    new_population = np.array([], dtype=chrom.chromosome)
    # Choose parents to crossover
    for _ in range(int(POPULATION_SIZE / 2)):
            # Selection
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        # CrossOver
        child1, child2 = pmx_crossover(parent1, parent2, pc)
        new_population = np.append(new_population, [child1, child2])
    # Mutation
    for i in range(pop_size):
        new_population[i] = swap_mutation(new_population[i], pm)
    # Elitism (2 => pop_size-2)
    # np.random.shuffle(new_population)   # TODO WTF?
    new_population = np.concatenate(
        (elites_of_current_population(
            population), new_population[:pop_size - elitism_count]))
    # Evaluate Fitness and best Fitness for new Population
    best_fitness, best_individual = calculate_population_fitness(
        new_population, best_fitness)
    # add new generation to generation list
    population = new_population
    # generations = np.append(generations, population)
    generation += 1

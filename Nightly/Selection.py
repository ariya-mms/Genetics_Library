import numpy as np
# np.random.seed(75)

# 1 - Truncation Selection :


def truncation_selection(population=None, truncation_threshold=0.5):
    # sort population by Chromosome fitness ascending
    sorted_pop_arr = sorted(population, key=lambda chrom: chrom.fitness)
    chrom_length = sorted_pop_arr[0].length
    return sorted_pop_arr[np.random.randint(0, int(chrom_length * truncation_threshold))]

# 2 - Tournament Selection


def tournament_selection(population=None, tour_size=2):
    selected_group = np.random.choice(population, tour_size)
    best_individual = selected_group[0]
    for indiv in selected_group:
        if indiv.fitness > best_individual.fitness:
            best_individual = indiv
    # return one parent
    return best_individual

# 3 - Stochastic Universal Sampling
"""
 stochastic_universal_sampling

 @description select n members of a population, with probability of
              selection proportional to fitness

 @param population: the given population

 @return a list of individuals of length n

 @limitations nothing!
"""


def stochastic_universal_sampling(population=None):
    total_fitness = sum([chrom.fitness for chrom in population])
    choice_point = np.random.random() * total_fitness
    accumulated_fitness = 0
    selected_individual = None
    # select individual by greatness of it's fitness just like roulette selection
    for individual in population:
        accumulated_fitness += individual.fitness
        while choice_point < accumulated_fitness:
            selected_individual = individual
            choice_point += total_fitness
    return selected_individual


def roulette_selection(population=None):
    i = 0
    fitness_arr = np.array(list(map(lambda c: c.fitness, population)))
    sum_of_fitness = np.sum(fitness_arr)
    sel_prob = fitness_arr / sum_of_fitness
    sum_prob = sel_prob[i]
    pointer = np.random.rand()
    while sum_prob < pointer:
        i += 1
        sum_prob += sel_prob[i]
    return population[i]


def roulette_selection_v2(population=None):
    pass


"""
 linear_ranking_selection

 @description For ranking selection the individuals are sorted according their fitness values and   
              the rank N is assigned to the best individual and the rank 1 to the worst individual The selection
              probability is linearly assigned to the individuals according
              to their rank.

 @param population: the given population

 @return a list of individuals of length n

 @limitations nothing!
"""


def linear_ranking_selection(population=None):
    # sort population by Chromosome fitness ascending
    sorted_pop_arr = sorted(population, key=lambda chrom: chrom.fitness)

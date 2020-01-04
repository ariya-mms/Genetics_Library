"""Selection module

Returns:
    chrome(s) -- [description]
"""

import numpy as np
import random

# TODO add an argument to selection operators to specify
# how many chroms to return

# TODO can it be enhanced?
def truncation(population, truncation_threshold=0.5):
    """Truncation selection
    
    Arguments:
        population {list(chrom)} -- [description]
    
    Keyword Arguments:
        truncation_threshold {float} -- selection range (default: {0.5})
    
    Returns:
        chrom -- [description]
    """

    # sort population by Chromosome fitness descending
    sorted_pop_arr = sorted(
        population, key=lambda chromosome: chromosome.fitness, True)
    chrom_length = sorted_pop_arr[0].length
    return sorted_pop_arr[np.random.randint(0, int(
            chrom_length * truncation_threshold))]


# TODO modified - Does it work properly?
def tournament(population, tour_size=2):
    """Returns the best candidate in tournament from randomly chosen chromosomes
    
    Arguments:
        population {list(chrom)} -- [description]
    
    Keyword Arguments:
        tour_size {int} -- size of randomly chosen chromosomes (default: {2})
    
    Returns:
        chorm -- [description]
    """

    selected_group = np.random.choice(population, tour_size)
    return max(selected_group, key=lambda chromosome: chromosome.fitness)


# TODO it can be enhanced
def stoch_uni_sampling(population):
    """Stochastic Universal Sampling
    
    Arguments:
        population {list(chorme)} -- [description]
    
    Returns:
        chrom -- [description]
    """

    total_fitness = sum([chromosome.fitness for chromosome in population])
    choice_point = np.random.random() * total_fitness
    accumulated_fitness = 0
    selected_individual = None
    # select individual by greatness of it's fitness
    # just like roulette selection
    for individual in population:
        accumulated_fitness += individual.fitness
        while choice_point < accumulated_fitness:
            selected_individual = individual
            choice_point += total_fitness
    return selected_individual


# TODO can it be enhanced?
def roulette(population):
    """Roulette Wheel Selection
    
    Arguments:
        population {list(chorm)} -- [description]
    
    Returns:
        chorm -- [description]
    """

    i = 0
    fitness_arr = np.array(
        list(map(lambda chromosome: chromosome.fitness, population)))
    sum_of_fitness = np.sum(fitness_arr)
    sel_prob = fitness_arr / sum_of_fitness
    sum_prob = sel_prob[i]
    pointer = np.random.rand()
    while sum_prob < pointer:
        i += 1
        sum_prob += sel_prob[i]
    return population[i]


# TODO confirm its functionality    (Done)
def roulette_with_stoch(population):
    """Roulette Wheel Selection with Stochastic Acceptance
    
    Arguments:
        population {list(chrom)} -- [description]
    
    Returns:
        chrom -- [description]
    """

    # calculate max fitness value
    maxfit = max(population, lambda chromosome: chromosome.fitness)
    # select
    while True:
        # randomly select an individual with uniform probability
        chromosome = random.choice(population)
        # with probability wi/wmax to accept the selection
        if (chromosome.fitness / maxfit) >= random.random():
            return chromosome


# TODO confirm its functionality    (Done)
# TODO Nedds some editions to work properly (Done)
# TODO this function may can be enhanced through
# functional programming in Python
def linear_rank(population):
    """Linear Ranking Selection
    
    Arguments:
        population {list(chrom)} -- [description]
    
    Returns:
        chrom -- [description]
    """

    # sort population by Chromosome fitness ascending
    sorted_pop = sorted(population, key=lambda chromosome: chromosome.fitness)

    sum_of_ranks = 0
    for i in range(len(population)):
        sum_of_ranks += i+1
    select_prob = (sorted_pop / sum_of_ranks)

    i = 0
    sum_prob = select_prob[i]
    pointer = np.random.rand()
    while sum_prob < pointer:
        i += 1
        sum_prob += select_prob[i]
    return population[i]


# TODO confirm its functionality
# FIXME
# TODO this function may can be enhanced through
# functional programming in Python
def exponential_rank(population):
    """Exponential Ranking Selection
    
    Arguments:
        population {list(chorm)} -- [description]
    
    Returns:
        chrom -- [description]
    """

    # sort population by Chromosome fitness ascending
    sorted_pop = sorted(population, key=lambda chromosome: chromosome.fitness)

    sum_of_ranks = 0
    for i in range(len(population)):
        sum_of_ranks += (i+1) ** 2  # TODO what to do with 2?
    sel_prob = sorted_pop / sum_of_ranks

    i = 0
    sum_prob = sel_prob[i]
    pointer = np.random.rand()
    while sum_prob < pointer:
        i += 1
        sum_prob += sel_prob[i]
    return population[i]


# TODO confirm its functionality
# FIXME
def self_adapt_tournament(population):
    pass

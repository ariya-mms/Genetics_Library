"""[summary]

Returns:
    [type] -- [description]
"""

# from . import chrom
import numpy as np
import random

# TODO add an argument to selection operators to specify
# how many chroms to return


def truncation(population, truncation_threshold=0.5):
    """[summary]
    
    Arguments:
        population {[type]} -- [description]
    
    Keyword Arguments:
        truncation_threshold {float} -- [description] (default: {0.5})
    
    Returns:
        [type] -- [description]
    """
    # sort population by Chromosome fitness ascending
    sorted_pop_arr = sorted(
        population, key=lambda chromosome: chromosome.fitness)
    chrom_length = sorted_pop_arr[0].length
    return sorted_pop_arr[np.random.randint(0, int(
            chrom_length * truncation_threshold))]


def tournament(population=None, tour_size=2):
    """[summary]
    
    Keyword Arguments:
        population {[type]} -- [description] (default: {None})
        tour_size {int} -- [description] (default: {2})
    
    Returns:
        [type] -- [description]
    """
    selected_group = np.random.choice(population, tour_size)
    best_individual = selected_group[0]
    for indiv in selected_group:
        if indiv.fitness > best_individual.fitness:
            best_individual = indiv
    # return one parent
    return best_individual


def stoch_uni_sampling(population):
    """stochastic_universal_sampling.

    @description select n members of a population,
            with probability of selection proportional to fitness
    @param population: the given population
    @return a list of individuals of length n
    @limitations nothing!
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


def roulette(population):
    """[summary]
    
    Arguments:
        population {[type]} -- [description]
    
    Returns:
        [type] -- [description]
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

# TODO does it work?
def roulette_with_stoch(population):
    """Input: a list of N fitness values (list or tuple).

    Output: selected chromosome
    """
    # calculate max fitness value
    maxfit = max(population, lambda chromosome: chromosome.fitness)
    # select: O(1)
    while True:
        # randomly select an individual with uniform probability
        chrom = random.choice(population)
        # with probability wi/wmax to accept the selection
        if population[chrom] / maxfit >= random.random():
            return chrom


# TODO Nedds some editions to work properly
# TODO this function may can be enhanced through
# functional programming in Python
def linear_rank(population):
    """linear_ranking_selection.

    @description For ranking selection the individuals are sorted
            according their fitness values and the rank N is assigned
            to the best individual and the rank 1 to the worst individual
            The selection probability is linearly assigned to the individuals
            according to their rank.
    @param population: the given population
    @return a list of individuals of length n
    @limitations nothing!
    """
    # sort population by Chromosome fitness ascending
    sorted_pop = sorted(population, key=lambda chromosome: chromosome.fitness)

    sum_of_ranks = 0
    for i in range(len(population)):
        sum_of_ranks += i+1
    sel_prob = sorted_pop / sum_of_ranks

    i = 0
    sum_prob = sel_prob[i]
    pointer = np.random.rand()
    while sum_prob < pointer:
        i += 1
        sum_prob += sel_prob[i]
    return population[i]

# TODO Nedds some editions to work properly
# TODO this function may can be enhanced through
# functional programming in Python
def exponential_rank(population):
    """[summary]

    Arguments:
        population {[type]} -- [description]

    Returns:
        [type] -- [description]
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

# TODO just do it!
def self_adapt_tournament(population):
    """[summary]
    
    Arguments:
        population {[type]} -- [description]
    """

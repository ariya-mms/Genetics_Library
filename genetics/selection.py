import numpy as np
import random

# TODO add an argument to selection operators to specify
# how many chroms to return
import sys
print(sys.path)
# TODO can it be enhanced?
def truncation(population, truncation_threshold=0.5):
    # sort population by Chromosome fitness ascending
    sorted_pop_arr = sorted(
        population, key=lambda chromosome: chromosome.fitness)
    chrom_length = sorted_pop_arr[0].length
    return sorted_pop_arr[np.random.randint(0, int(
            chrom_length * truncation_threshold))]


# TODO modified - Does it work properly?
def tournament(population, tour_size=2):
    selected_group = np.random.choice(population, tour_size)
    return max(selected_group, key=lambda chromosome: chromosome.fitness)


# TODO it can be enhanced
def stoch_uni_sampling(population):
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
    # calculate max fitness value
    maxfit = max(population, lambda chromosome: chromosome.fitness)
    # select: O(1)
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

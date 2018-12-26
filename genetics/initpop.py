from . import chrom
import numpy as np

# TODO Study articles related to Quasi-Random & Centroid bla bla


def pseudo_rand(type, pop_size, chrom_length, low=None, high=None):
    if type is 'permutational':
        chromosomes = list()
        for i in range(pop_size):
            chromosomes.append(chrom.chromosome(
                np.random.shuffle(np.arange(chrom_length)), id=i))
    elif type is 'binary':
        chromosomes = list()
        for i in range(pop_size):
            chromosomes.append(chrom.chromosome(
                np.random.choice((0, 1), chrom_length), id=i))
    elif type is 'discrete':
        chromosomes = list()
        for i in range(pop_size):
            chromosomes.append(chrom.chromosome(
                np.random.randint(low, high, chrom_length), id=i))
    elif type is 'float':
        chromosomes = list()
        for i in range(pop_size):
            chromosomes.append(chrom.chromosome(
                np.random.uniform(low, high, chrom_length), id=i))
    else:
        raise TypeError("Enter a valid type!")


def quasi_rand(type, pop_size, chrom_length):
    pass


def centro_vor_tessel(type, pop_size, charm_length):
    pass

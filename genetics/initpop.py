from . import chrom
import numpy as np

# TODO Study articles related to Quasi-Random & Centroid bla bla


def pseudo_rand(type, pop_size, chrom_length):
    if type is 'permutational':
        chromosomes = list()
        for _ in range(pop_size):
            chromosomes.append(np.random.shuffle(np.arange(chrom_length)))


def quasi_rand(type, pop_size, chrom_length):
    pass


def centro_vor_tessel(type, pop_size, charm_length):
    pass

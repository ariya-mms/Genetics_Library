import chrom
import numpy as np

def pseudo_rand(type ,pop_size, chrom_length):
    chromosomes = list()
    for _ in range(pop_size):
        chromosomes.append(np.random.shuffle(np.arange(chrom_length)))

def quasi_rand(type, pop_size, chrom_length):
    pass


def centro_vor_tessel(type, pop_size, charm_length):
    chromosomes = list()
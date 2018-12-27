from . import chrom
import numpy as np

# TODO Study articles related to Quasi-Random & Centroid bla bla
# TODO Add an argument to whether give ID to chromes or not


def pseudo_rand(type, pop_size, chrom_length, low=None, high=None):
    chromosomes = list()
    
    if type is 'permutational':
        gene = np.arange(chrom_length)
        for i in range(pop_size):
            np.random.shuffle(gene)
            chromosomes.append(chrom.Chromosome(
                gene, id=i))
    elif type is 'binary':
        for i in range(pop_size):
            chromosomes.append(chrom.Chromosome(
                np.random.choice((0, 1), chrom_length), id=i))
    elif type is 'discrete':
        for i in range(pop_size):
            chromosomes.append(chrom.Chromosome(
                np.random.randint(low, high+1, chrom_length), id=i))
    elif type is 'float':
        for i in range(pop_size):
            chromosomes.append(chrom.Chromosome(
                np.random.uniform(low, high, chrom_length), id=i))
    else:
        raise TypeError("Enter a valid type!")

    return chromosomes


def quasi_rand(type, pop_size, chrom_length):
    pass


def centro_vor_tessel(type, pop_size, charm_length):
    pass

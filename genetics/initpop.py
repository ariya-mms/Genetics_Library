from . import chrom
import numpy as np

# TODO Study articles related to Quasi-Random & Centroid bla bla
# TODO Add an argument to whether give ID to chromes or not
# TODO move mutation & crossover operators to subpackages & submodules


def pseudo_rand(ctype, pop_size, chrom_length, low=None, high=None):
    chromosomes = list()
    
    if ctype == 'permutational':
        gene = np.arange(chrom_length)
        for i in range(pop_size):
            np.random.shuffle(gene)
            chromosomes.append(chrom.Simple_Gene(
                gene, chrm_id=i))
    elif ctype == 'binary':
        for i in range(pop_size):
            chromosomes.append(chrom.Simple_Gene(
                np.random.choice((0, 1), chrom_length), chrm_id=i))
    elif ctype == 'discrete':
        for i in range(pop_size):
            chromosomes.append(chrom.Simple_Gene(
                np.random.randint(low, high+1, chrom_length), chrm_id=i))
    elif ctype == 'float':
        for i in range(pop_size):
            chromosomes.append(chrom.Simple_Gene(
                np.random.uniform(low, high, chrom_length), chrm_id=i))
    else:
        raise TypeError("Enter a valid chromosome type!")

    return chromosomes


def quasi_rand(ctype, pop_size, chrom_length):
    pass


def centro_vor_tessel(ctype, pop_size, charm_length):
    pass

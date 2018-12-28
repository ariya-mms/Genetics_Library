from . import chrom
import numpy as np

# TODO Study articles related to Quasi-Random & Centroid bla bla
# TODO Add an argument to whether give ID to chromes or not


def pseudo_rand(gtype: str, pop_size: int, chrom_length: int, low=None, high=None):
    chromosomes = list()
    if gtype == 'permutational':
        gene = np.arange(chrom_length)
        for i in range(pop_size):
            np.random.shuffle(gene)
            chromosomes.append(chrom.Simple_Gene(
                'permutational', gene, chrm_id=i))
    elif gtype == 'binary':
        for i in range(pop_size):
            chromosomes.append(chrom.Simple_Gene(
                'binary', np.random.choice((0, 1), chrom_length), chrm_id=i))
    elif low is None or high is None:
        raise ValueError()
    else:
        if gtype == 'discrete':
            for i in range(pop_size):
                chromosomes.append(chrom.Simple_Gene(
                    'discrete', np.random.randint(low, high+1, chrom_length), chrm_id=i))
        elif gtype == 'float':
            for i in range(pop_size):
                chromosomes.append(chrom.Simple_Gene(
                    'float', np.random.uniform(low, high, chrom_length), chrm_id=i))
        else:
            raise TypeError("Enter a valid chromosome type!")
    return chromosomes


def quasi_rand(ctype, pop_size, chrom_length):
    pass


def centro_vor_tessel(ctype, pop_size, charm_length):
    pass

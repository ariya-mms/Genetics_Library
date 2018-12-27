import numpy as np


# TODO add required functions
# TODO add type argument to chrom to facilitate raising useful exceptioins
class Chromosome():
    def __init__(self, genes, id=-1, fitness=-1, length=0):
        self.id = id
        self.genes = genes
        self.fitness = fitness
        self.length = len(genes)

    # TODO Enhance this function
    def describe(self):
        print('ID=#{}, fitenss={}, \ngenes=\n{}'.format(
            self.id, self.fitness, self.genes))

    def reset_attrs():
        self.id = -1
        self.fitenss = -1

    def __len__(self):
        return len(genes)

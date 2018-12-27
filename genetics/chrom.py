import numpy as np


# TODO add required functions
class Chromosome():
    def __init__(self, genes, id=-1, fitness=-1, length=0):
        self.id = id
        self.genes = genes
        self.fitness = fitness
        self.length = length

    # TODO Enhance this function
    def describe(self):
        print('ID=#{}, fitenss={}, \ngenes=\n{}'.format(
            self.id, self.fitness, self.genes))

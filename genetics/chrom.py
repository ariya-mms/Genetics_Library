"""Module to define chromsome classes

Returns:
    chrom -- [description]
"""     

import numpy as np

# TODO add a static method or counter to assign ID more professionally!


class Chrom():
    """General chromosome class to inherit from
    
    Returns:
        [type] -- [description]
    """

    fitness = -1.0
    def __init__(self, gtype:str, genes:np.array, chrm_id=-1):
        self.type = gtype
        self.genes = genes
        self.id = chrm_id

    def __len__(self):
        return len(self.genes)

    def describe(self):
        print("ID=#{} \ntype={} \nfitenss={} \ngenes=\n{}".format(
            self.id, self.type, self.fitness, self.genes))

    def flatten(self):
        return self.genes.flatten()


class Simple_Gene(Chrom):
    """Chromosome class with single data in each gene
    
    Arguments:
        Chrom {chrom} -- [description]
    """

    def describe(self):
        print('Simple Gene')
        super().describe()


class Vector_Gene(Chrom):
    """Chromosome class with vector data in each gene
    
    Arguments:
        Chrom {chrom} -- [description]
    """

    def __init__(self, gtype:str, genes:np.ndarray, glength:int, chrm_id=-1):
        self.type = gtype
        self.genes = genes
        self.glength = glength
        self.id = chrm_id

    def describe(self):
        print('Vector Gene')
        super().describe()


# TODO
class Complex_Gene(Chrom):
    def describe(self):
        print('Comlex Gene')
        super().describe()

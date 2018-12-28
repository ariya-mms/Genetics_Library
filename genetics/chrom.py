import numpy as np


class Chrom():
    def __init__(self, genes:np.ndarray, ctype:str, chrm_id=-1, fitness=-1.0):
        self.id = chrm_id
        self.genes = genes
        self.fitness = fitness
        self.type = ctype

    def __len__(self):
        return len(self.genes)

    def describe(self):
        print("ID=#{} \ntype={} \nfitenss={} \ngenes=\n{}".format(
            self.id, self.type, self.fitness, self.genes))

    def flatten(self):
        return self.genes.flatten()


class Simple_Gene(Chrom):
    def describe(self):
        print('Simple Gene')
        super().describe()


class Vector_Gene(Chrom):
    def __init__(self, genes:np.ndarray, ctype:str, glength:int, chrm_id=-1, fitness=-1.0):
        self.id = chrm_id
        self.genes = genes
        self.fitness = fitness
        self.type = ctype

    def describe(self):
        print('Vector Gene')
        super().describe()


# TODO
class Complex_Gene(Chrom):
    def describe(self):
        print('Comlex Gene')
        super().describe()
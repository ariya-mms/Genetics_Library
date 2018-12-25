"""A test script to figure out how to use and deal with library to solva a problem like N-Queen
"""
from genetics import chrom, initpop, genes
import numpy as np

POPULATION_SIZE = 10
BOARD_SIZE = 10
TOURNAMENT_SIZE = 3
ELITISM_COUNT = 2
Pc = 0.9
Pm = 0.1

c = chrom.chromosome(genes=np.array([1,2,3]),id=1,fitness = 125.2)
c.describe()

def nqueen(pop_size=POPULATION_SIZE, chrom_size=BOARD_SIZE, pm=Pm,
           pc=Pc, elitism_count=ELITISM_COUNT):
    best_fitness = float('-inf')
    current_populatioin

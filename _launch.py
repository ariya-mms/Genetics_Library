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

population = initpop.pseudo_rand('permutational', POPULATION_SIZE, BOARD_SIZE)

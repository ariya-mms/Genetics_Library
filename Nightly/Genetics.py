import numpy as np
np.random.seed(75)

# new commit in 19 Azar
class ChromosomeType:
    BINARY = 'binary'  # its wrong ?!
    # discrete or permutation
    SIMPLE_MATRIX = 'matrix'
    COMPLEX_MATRIX = 'c_matrix'


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ChromosomeInitError(Error):
    """Exception raised for errors in Initialising a Genetic module.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = "<!CHROMOSOME!> " + message + " <!CHROMOSOME!>"


class Chromosome:
    def __init__(self, genes=None, ctype=ChromosomeType.BINARY, length=None, id=None, fitness=-1.0, flatten=False,
                 lengths=None):
        self.id = id
        self.fitness = fitness
        if genes is None:
            if length is None:
                raise ChromosomeInitError("your chromosome must have length to init")
            if ctype == ChromosomeType.BINARY:
                self.genes = np.array(np.random.rand(length) > 0.5, dtype=int)
            else:
                # TODO create random chromes by discrete or permutation style

                pass
                # self.genes = self.get_shuffled_array(length)
        elif np.array(genes).shape == (1,):
            # chrom types ??
            self.genes = genes
        else:
            raise ChromosomeInitError("genes wrong input. It's not flatten")

        if not flatten and genes is not None:
            self.flatten_features()

        if lengths is not None:
            self.lengths = lengths

    def get_shuffled_array(self, length):
        array = np.arange(length)
        np.random.shuffle(array)
        return array

    def flatten_features(self):
        # 2 dimensional matrix with same size elements
        if self.genes.ndim > 1 and self.lengths is None:
            self.genes = self.genes.flatten()
        # complex array with custom array of lengths
        elif self.lengths is not None:
            self.genes = self.genes.flatten()
        else:
            raise ChromosomeInitError("you insert dynamic genes array without Lengths attribute")

    def describe(self):
        print('ID=#{}, fitenss={}, \ngenes=\n{}'.format(self.id, self.fitness, self.genes))


# Population

# 1 - Pseudo Random
# do everything random in initializing
def population_init_random(pop_size=None, chrom_size=None, ctype=None):
    if pop_size is None or pop_size < 1:
        raise ChromosomeInitError("population size must have positive integer value")
    population = np.array([])
    for _ in range(pop_size):
        population = np.append(population, Chromosome(length=chrom_size, ctype=ctype))
    return population


# 2 - Quasi Random Sequence
"""
the initial population is often selected randomly using pseudorandom numbers.(function above)
It’s usually more important that the points are as evenly distributed as possible than that
they imitate random points. In this paper, we study the use of quasi-random sequences in the
initial population of a genetic algorithm. Sample points in a quasi-random sequence are designed to 
have good distribution properties
"""
def population_init_quasi_random():
    pass








# arr = population_init_random(pop_size=10, chrom_size=5, ctype=ChromosomeType.BINARY)
# for c in arr:
#     print(c.genes)

# # Provide some example if you want!
# def chromosome_test():
#     c = Chromosome(genes=np.array([1, 2, 3]), id=1, fitness=125.2)
#     c.describe()
#
#     c2 = Chromosome(genes=np.array([[1, 2], [2, 1]]).flatten(), id=2,
#                     fitness=140, flatten=True)
#     c2.describe()

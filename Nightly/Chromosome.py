import numpy as np


# np.random.seed(75)


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
            self.length = length
            if length is None:
                raise ChromosomeInitError("your chromosome must have length to init")
            if ctype == ChromosomeType.BINARY:
                self.genes = np.array(np.random.rand(length) > 0.5, dtype=int)
            else:
                # TODO create random chromes by discrete or permutation style
                self.genes = np.random.permutation(length)
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


def get_shuffled_array(length):
    array = np.arange(length)
    np.random.shuffle(array)
    return array

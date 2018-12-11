import numpy as np

np.random.seed(75)


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
                self.genes = self.get_shuffled_array(length)
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


# Selection
# 1 - Truncation Selection :
def truncation_selection(population=None, truncation_threshold=0.5):
    # sort population by Chromosome fitness ascending
    sorted_pop_arr = sorted(population, key=lambda chrom: chrom.fitness)
    chrom_length = sorted_pop_arr[0].length
    return sorted_pop_arr[np.random.randint(0, int(chrom_length * truncation_threshold))]


# 2 - Tournament Selection
def tournament_selection(population=None, tour_size=2):
    selected_group = np.random.choice(population, tour_size)
    best_individual = selected_group[0]
    for indiv in selected_group:
        if indiv.fitness > best_individual.fitness:
            best_individual = indiv
    # return one parent
    return best_individual


# 3 - Stochastic Universal Sampling
"""
 stochastic_universal_sampling

 @description select n members of a population, with probability of
              selection proportional to fitness

 @param population: the given population
 @param n: the number of individuals required
 @param fitness: a function that quantifies
                 the value of an individual

 @return a list of individuals of length n

 @limitations nothing!
"""


def stochastic_universal_sampling(population=None):
    total_fitness = sum([chrom.fitness for chrom in population])
    choice_point = np.random.random() * total_fitness
    accumulated_fitness = 0
    selected_individual = None
    # select individual by greatness of it's fitness just like roulette selection
    for individual in population:
        accumulated_fitness += individual.fitness
        while choice_point < accumulated_fitness:
            selected_individual = individual
            choice_point += total_fitness
    return selected_individual


# *************************************************************
# ***********************test app******************************
# **************************************************************
def calculate_individual_fitness(individual: Chromosome):
    chromosome = individual.genes
    clashes = 0;
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if i != j:
                dx = abs(i - j)
                dy = abs(chromosome[i] - chromosome[j])
                if dx == dy:
                    clashes += 1
    return (28 - clashes) * 100 / 28


def calculate_population_fitness(population=None, best_fitness=float('-inf'), best_individual=None):
    for individual in population:
        individual.fitness = calculate_individual_fitness(individual)
        if individual.fitness > best_fitness:
            best_fitness = individual.fitness
            best_individual = individual
    return best_fitness, best_individual


def test_selections():
    current_population = population_init_random(100, 8, ctype=ChromosomeType.SIMPLE_MATRIX)
    # print(np.array([c.genes for c in current_population]))
    best_fitness, best_individual = calculate_population_fitness(current_population, -1)
    print("best :> ", best_individual.genes, " f :> ", best_fitness)
    for i in range(int(len(current_population) / 5)):
        # Selection
        parent1 = stochastic_universal_sampling(current_population)
        print("gen "+str(i)+". ", parent1.genes, " f :> ", parent1.fitness)


test_selections()

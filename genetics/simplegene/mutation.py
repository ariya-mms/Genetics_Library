"""Mutation module

Raises:
    exception -- [description]
    TypeError -- [description]
    IndexError -- [description]

Returns:
    chrom -- [description]
"""

from .. import chrom
import random

# TODO add ability to check chrome type and raise exception
# in functions or a seperate function


# def swap_mutation(chromosome):
#     # avoid choosing same gene
#     # i = 0
#     # j = 0
#     # while i is j:
#     #     i, j = random.randint(0, chromosome.length), random.randint(
#     #         0, chromosome.length)
#     # TODO does it work?
#     i, j = random.choices(len(chromosome), k=2)

#     chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]
#     return chromosome


def uniform(c, ctype, high, low, num=1):
    """Uniform mutation
    
    Arguments:
        c {chrom} -- [description]
        ctype {str} -- [description]
        high {int} -- [description]
        low {int} -- [description]
    
    Keyword Arguments:
        num {int} -- [description] (default: {1})
    
    Raises:
        TypeError -- [description]
    
    Returns:
        chrom -- [description]
    """

    chromosome = chrom.Simple_Gene(c.genes)
    for _ in range(num):
        if ctype == 'discrete':
            chromosome.genes[random.randint(
                0, len(chromosome))] = random.randint(low, high)
        elif ctype == 'float':
            chromosome.genes[random.randint(0, len(chromosome))] = random.randrange(
                low, high, _int=float)
        else:
            raise TypeError("Enter a valid chromosome type!")
    return chromosome


def inorder(parameter_list):
    """[summary]
    
    Arguments:
        parameter_list {[type]} -- [description]
    """

    pass


def twors(c):
    """Twors mutation: Swap mutation
    
    Arguments:
        c {chorm} -- [description]
    
    Returns:
        chorm -- [description]
    """

    chromosome = chrom.Simple_Gene(c.genes)
    i, j = random.choices(len(chromosome), k=2)
    chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]
    return chromosome


def reverse_seq(c):
    """Reverse Sequence mutation
    
    Arguments:
        c {chrom} -- [description]
    
    Returns:
        chrom -- [description]
    """

    chromosome = chrom.Simple_Gene(c.genes)
    i, j = sorted(random.choices(len(chromosome), k=2))
    while i < j:
        chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]
        i -= 1
        j -= 1
    return chromosome


def part_shuffle(c, pm=0.1):
    """Partial Shuffle Mutation (PSM)
    
    Arguments:
        c {chrom} -- [description]
    
    Keyword Arguments:
        pm {float} -- [description] (default: {0.1})
    
    Returns:
        chrom -- [description]
    """

    chromosome = chrom.Simple_Gene(c.genes)
    # for i, _ in enumerate(chromosome):
    for i in range(len(chromosome))
        if pm > random.random():
            j = random.randint(0, len(chromosome))
            chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]
    return chromosome


def scramble(c):
    """Scramble Mutation
    
    Arguments:
        c {chrom} -- [description]
    
    Returns:
        chrom -- [description]
    """

    chromosome = chrom.Simple_Gene(c.genes)
    i, j = sorted(random.choices(len(chromosome), k=2))
    random.shuffle(chromosome.genes[i:j])
    return chromosome


def distance_based(c, i, d):
    """Distance Based mutation
    
    Arguments:
        c {chrom} -- [description]
        i {int} -- [description]
        d {int} -- [description]
    
    Raises:
        IndexError -- [description]
    
    Returns:
        chrom -- [description]
    """

    chromosome = chrom.Simple_Gene(c.genes)
    if (d > i) or ((i + d) > len(c)):
        raise IndexError("Enter proper 'gene index' & 'distance' arguments")
    j = random.randint(i-d, i+d)
    chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]
    return chromosome

from . import chrom
import numpy as np
from copy import deepcopy
import random

# TODO add ability to check chrome type and raise exception
# in functions or a seperate function


# TODO Check its functionality
def singlepoint(parent1, parent2):

    point = random.randint

    child1 = chrom.Chromosome(parent1.genes)
    child2 = chrom.Chromosome(parent2.genes)

    # TODO check the loop
    for i in range(point):
        child1.genes[i] = parent2.genes[i]
        child2.genes[i] = parent1.genes[i]

    return child1, child2


# TODO Check its functionality
def multipoint(parent1, parent2, points=3):

    chrom_length = parent1.length
    points = set()
    for _ in range(chrom_length):
        points.add(random.randint(chrom_length))

    child1 = chrom.Chromosome(parent1.genes)
    child2 = chrom.Chromosome(parent2.genes)

    points = sorted(list(points))
    flag = True

    # FIXME
    for point in points:
        flag = not flag
        if flag:
            for i in range(point):
                child1.genes[i] = parent2.genes[i]
                child2.genes[i] = parent1.genes[i]

    return child1, child2


# TODO check its functionality
def uniform(parent1, parent2):

    child1 = chrom.Chromosome(parent1.genes)
    child2 = chrom.Chromosome(parent2.genes)

    for i in range(parent1.length):
        if random.random() > 0.5:
            child1.genes[i] = parent2.genes[i]
            child2.genes[i] = parent1.genes[i]


def flat(parent1, parent2):

    child1 = chrom.Chromosome(np.zeros)
    child2 = chrom.Chromosome(np.zeros)

    for i in range(len(parent1)):
        rand = random.random()
        child1[i] = (rand*parent1[i]) + ((1-rand)*parent2[i])
        child2[i] = (rand*parent2[i]) + ((1-rand)*parent1[i])


def order(parent1, parent2):

    length = len(parent1)
    child1 = chrom.Chromosome(np.zeros(length))
    child2 = chrom.Chromosome(np.zeros(length))

    i = 0
    j = 0
    while i is j:
        i, j = sorted(random.random(length), random.random(length))

    child1[i:j] = parent1[i:j]
    child1[i:j] = parent2[i:j]

    for k in range(i, j):
        pass


# TODO Understand it
# TODO can it be enhanced?
def pmx(parent1, parent2):

    random_num = random.randint()
    child1 = deepcopy(parent1)
    child2 = deepcopy(parent2)

    size = len(parent1.genes)
    # create CO points
    point1 = random_num(size)
    point2 = random_num(size-1)
    if point2 >= point1:
        point2 += 1
    else:
        point1, point2 = point2, point1

    p1, p2 = np.full(size, 0, int), np.full(size, 0, int)
    for i in range(size):
        p1[child1.genes[i]] = i
        p2[child2.genes[i]] = i

    for i in range(point1, point2):
        # Keep track of the selected values
        temp1 = child1.genes[i]
        temp2 = child2.genes[i]
        # Swap the matched value
        child1.genes[i], child1.genes[p1[temp2]] = temp2, temp1
        child2.genes[i], child2.genes[p2[temp1]] = temp1, temp2
        # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    child1.reset_attrs()
    child2.reset_attrs()

    # return two individuals
    return child1, child2

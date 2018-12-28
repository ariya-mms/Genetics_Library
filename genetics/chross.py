from . import chrom
import numpy as np
import random

# TODO add ability to check chrome type and raise exception
# in functions or a seperate function


# TODO Check its functionality
def singlepoint(parent1, parent2):

    point = random.randint(0, len(parent1))

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
        points.add(random.randint(0, chrom_length))

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

    return child1, child2


def flat(parent1, parent2):

    child1 = chrom.Chromosome(np.zeros)
    child2 = chrom.Chromosome(np.zeros)

    # for i in range(len(parent1)):
    for i, _ in enumerate(parent1):
        rand = random.random()
        child1.genes[i] = (rand*parent1.genes[i]) + ((1-rand)*parent2.genes[i])
        child2.genes[i] = (rand*parent2[i]) + ((1-rand)*parent1[i])

    return child1, child2


def order(parent1, parent2):

    length = len(parent1)
    child1 = chrom.Chromosome(np.zeros(length))
    child2 = chrom.Chromosome(np.zeros(length))

    # i = 0
    # j = 0
    # while i is j:
    #     i, j = sorted(random.random(length), random.random(length))
    # TODO does it work?
    i, j = sorted(random.choices(len(parent1), k=2))

    child1.genes[i:j] = parent1.genes[i:j]
    child2.genes[i:j] = parent2.genes[i:j]

    list1 = list()
    list2 = list()

    for k in range(len(parent1)):
        if parent2.genes[k] not in child1.genes[i:j]:
            list1.append(parent2.genes[k])
        if parent1.genes[k] not in child2.genes[i:j]:
            list2.append(parent1.genes[k])

    child1.genes[:i] = list1[:i]
    child1.genes[j:] = list1[i:]
    child2.genes[:i] = list2[:i]
    child2.genes[j:] = list2[i:]

    return child1, child2


# TODO Understand it
# TODO can it be enhanced?
def pmx(parent1, parent2):

    random_num = random.randint(0, len(parent1))
    # TODO I removed deepcopy. does it work?
    child1 = parent1[:]
    child2 = parent2[:]

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


# FIXME
# TODO NEEDS TO BE VALIDATED
def edge_recomb(parent1, parent2, arr, ind):  # edge recombination operator
    neigh_list = {}  # adjacency list
    length = len(parent1.permutation)  # expected length of a child
    for i, base in enumerate(parent1.permutation):  # create nodes
        neigh_list[base] = {parent1.permutation[i - 1],
                            parent1.permutation[(i + 1) % length]}
    for i, base in enumerate(parent2.permutation):  # add neighbours to each node
        neigh_list[base].add(parent2.permutation[i - 1])
        neigh_list[base].add(parent2.permutation[(i + 1) % length])

    # a starting point of a child is a starting point of one of the parents
    neigh_chosen = [parent1.permutation[0],
                    parent2.permutation[0]][random.randint(0, 1)]
    child = [neigh_chosen]

    while len(child) < length:  # run until child has desired length
        min_length = 5  # each list has lower length than 5
        min_neigh_list = []
        for k in neigh_list:  # for every node
            # remove a chosen fragment from the node
            if neigh_chosen in neigh_list[k]:
                neigh_list[k].remove(neigh_chosen)
        # if a node is a neighbour of previously chosen
        min_neigh_list = neigh_list[neight_chosen]
        del neigh_list[neigh_chosen]
        # for k in neigh_list[neigh_chosen]:
        #     # remember nodes with the fewest neighbours
        #     if len(neigh_list[k]) < min_length:
        #         min_length = len(neigh_list[k])
        #         min_neigh_list = [k]
        #     elif len(neigh_list[k]) == min_length:
        #         min_neigh_list.append(k)
        # del neigh_list[neigh_chosen]  # delete list of the chosen node
        if len(min_neigh_list) > 0:  # if the chosen node has any neighbours
            # get the best match out of neighbours as next
            max_overlap = overlap(neigh_chosen, max(
                min_neigh_list, key=lambda x: overlap(neigh_chosen, x)))
            possibilities = list(filter(lambda x: overlap(
                neigh_chosen, x) == max_overlap, min_neigh_list))
            neigh_chosen = possibilities[random.randint(
                0, len(possibilities) - 1)]
        else:
            # get the best match out of every node as next
            max_overlap = overlap(neigh_chosen, max(
                neigh_list, key=lambda x: overlap(neigh_chosen, x)))
            possibilities = list(filter(lambda x: overlap(
                neigh_chosen, x) == max_overlap, neigh_list))
            neigh_chosen = possibilities[random.randint(
                0, len(possibilities) - 1)]
        child.append(neigh_chosen)  # add the node to the solution
    arr[ind] = Gene(child)

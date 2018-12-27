def crossover(g1, g2, arr, ind):  # edge recombination operator
    neigh_list = {}  # adjacency list
    length = len(g1.permutation)  # expected length of a child
    for i, base in enumerate(g1.permutation):  # create nodes
        neigh_list[base] = {g1.permutation[i - 1],
                            g1.permutation[(i + 1) % length]}
    for i, base in enumerate(g2.permutation):  # add neighbours to each node
        neigh_list[base].add(g2.permutation[i - 1])
        neigh_list[base].add(g2.permutation[(i + 1) % length])

    # a starting point of a child is a starting point of one of the parents
    neigh_chosen = [g1.permutation[0], g2.permutation[0]][random.randint(0, 1)]
    child = [neigh_chosen]

    while len(child) < length:  # run until child has desired length
        min_length = 5  # each list has lower length than 5
        min_neigh_list = []
        for k in neigh_list:  # for every node
            # remove a chosen fragment from the node
            if neigh_chosen in neigh_list[k]:
                neigh_list[k].remove(neigh_chosen)
        # if a node is a neighbour of previously chosen
        for k in neigh_list[neigh_chosen]:
            # remember nodes with the fewest neighbours
            if len(neigh_list[k]) < min_length:
                min_length = len(neigh_list[k])
                min_neigh_list = [k]
            elif len(neigh_list[k]) == min_length:
                min_neigh_list.append(k)
        del neigh_list[neigh_chosen]  # delete list of the chosen node
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

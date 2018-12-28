

# TODO add required functions
# TODO add type argument to chrom to facilitate raising useful exceptioins
class Chromosome():
    def __init__(self, genes, chrm_id=-1, fitness=-1):
        self.id = chrm_id
        self.genes = genes
        self.fitness = fitness
        self.length = len(genes)

    # TODO Enhance this function
    def describe(self):
        print('ID=#{}, fitenss={}, \ngenes=\n{}'.format(
            self.id, self.fitness, self.genes))

    def reset_attrs(self):
        self.id = -1
        self.fitenss = -1

    def __len__(self):
        return len(self.genes)

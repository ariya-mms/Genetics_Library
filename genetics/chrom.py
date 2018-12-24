class chromosome():
    def __init__(self, genes, id=None, fitness=-1, flatten= False, lengths=None):
        self.id = id
        self.genes = genes
        self.fitness = fitness
        
        # if you need more parameters for specific problem, extend this class
    def flatten_feaures():
        # in this function you should implement your logic to flatten features
        pass
    
    
    def describe(self):
        print('ID=#{}, fitenss={}, \ngenes=\n{}'.format(self.id, self.fitness, self.genes))
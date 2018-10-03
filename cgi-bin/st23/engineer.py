from .master import Master


class Engineer(Master):
    def __init__(self, lastname, category, numEducations, rank):
        super().__init__(lastname, category)
        self.numEducations = numEducations
        self.rank = rank

        
    def get_inf(self):
        return (self.__class__.__name__, self.lastname, self.category, self.numEducations, self.rank)
class Master:
    def __init__(self, lastname, category):
        self.lastname = lastname
        self.category = category


    def get_inf(self):
        return (self.__class__.__name__, self.lastname, self.category)
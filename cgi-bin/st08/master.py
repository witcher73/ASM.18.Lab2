from .bachelor import Bachelor


class Master(Bachelor):
    def __init__(self, lastname: str, university: str, scientific_adviser: str):
        super().__init__(lastname, university)
        self.scientific_adviser = scientific_adviser


    def get_information(self):
        return 'Магистр', self.lastname, self.university, self.scientific_adviser
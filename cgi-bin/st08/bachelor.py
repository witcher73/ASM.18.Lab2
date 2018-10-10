class Bachelor:
    def __init__(self, lastname: str, university: str):
        self.lastname = lastname
        self.university = university


    def get_information(self):
        return 'Бакалавр', self.lastname, self.university
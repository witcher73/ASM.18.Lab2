# Класс сотрудника
class Director:
    params = ['FIO_name', 'Department']
    placeholder = ['ФИО', 'Отдел']

    def __init__(self, self_url, q):
        self.url = self_url
        self.q = q
        self.FIO_name: str = ''  # ФИО
        self.Department: str = ''  # отдел
        self.type: str = 'Руководителя'

    def save(self):
        for param in self.params:
            if param in self.q:
                setattr(self, param, self.q.getvalue(param))

    def __str__(self):
        naming = self.type + ' '
        for ind, param in enumerate(self.params):
            naming += '{0}: {1} '.format(self.placeholder[ind], getattr(self, param))
        return naming + '</br>'


# Класс сотрудника
class Person:
    params = ['first_name', 'last_name', 'age']
    placeholder = ['ФИО', 'Отдел', 'Стаж работы']

    def __init__(self, self_url, q):
        self.url = self_url
        self.q = q
        self.first_name: str = ''  # фио
        self.last_name: str = ''  # отдел
        self.age: int = ''  # стаж
        self.type: str = 'Новый сотрудник'

    def save(self):
        for param in self.params:
            if param in self.q:
                setattr(self, param, self.q.getvalue(param))

    def __str__(self):
        naming = self.type + ' '
        for ind, param in enumerate(self.params):
            naming += '{0}: {1} '.format(self.placeholder[ind], getattr(self, param))
        return naming + '</br>'

from .Person import Person


# Класс руководителя, расширяющий класс сотрудника
class Director(Person):
    params = Person.params + ['workplace', 'salary']
    placeholder = Person.placeholder + ['должность', 'Зарплата']

    def __init__(self, self_url, q):
        Person.__init__(self, self_url, q)
        self.type = 'Назначить руководителя'
        self.url = self_url
        self.q = q
        self.degree: str = ''  
        self.workplace: str = ''
        self.salary: int = ''  # размер зарплаты

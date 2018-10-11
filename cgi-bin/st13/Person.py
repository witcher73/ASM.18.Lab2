from .Director import Director


# Класс руководителя, расширяющий класс сотрудника
class Person(Director):
    params = Director.params + ['experience', 'salary']
    placeholder = Director.placeholder + ['Стаж работы', 'Зарплата']

    def __init__(self, self_url, q):
        Director.__init__(self, self_url, q)
        self.type = 'Сотрудника'
        self.url = self_url
        self.q = q
        self.degree: str = ''  # должность руководителя
        self.experience: int = ''  # стаж работы
        self.salary: int = ''  # размер зарплаты

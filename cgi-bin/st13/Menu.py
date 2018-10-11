class Menu:
    EXIT_CODE: int = 6

    def __init__(self, organization, url, student_id):
        self.organization = organization
        self.instance = self.get()
        self.url = url
        self.student_id = student_id

    def get(self):
        return [
            ['Добавить нового сотрудника', self.organization.add_person],
            ['Назначить руководителя', self.organization.add_director],
            ['Редактировать отдел', self.organization.edit],
            ['Показать общий список', self.organization.show_people],
            ['delete all', self.organization.clear_men]
        ]

    # если student_id == None, переходим на начальную страницу
    @staticmethod
    def back_button(url, student_id=None):
        if student_id is None:
            print('<a href="{0}">Назад</a>'.format(url))
        else:
            print('<a href="{0}?student={1}">Назад</a>'.format(url, student_id))

    def show_menu(self, self_url, student_id):
        print('<pre>------------------------------')
        for i, item in enumerate(self.instance):
            print('<a href="{0}?student={1}&act={3}">[{3}] {2}</a>'.format(self_url, student_id, item[0], i))
        Menu.back_button(self.url)
        print("------------------------------</pre>")

    @staticmethod
    def not_found():
        print('<html><head></head><body><h1>404 Страница не найдена/h1><p>Страница по данному адресу не найдена.</p></body></html>')

    @staticmethod
    def response_ok():
        print("Content-type: text/html; charset=utf-8\n\n")

    def start(self, index):
        try:
            if index != Menu.EXIT_CODE:
                self.instance[index][1]()
        except IndexError:
            Menu.not_found()

import pickle

import os

from .Form import Form, Menu
from .Person import Director, Person


# Класс-контейнер Организации
class Organization:
    _FILENAME_STORAGE = os.environ['PATH_TRANSLATED'] +'/cgi-bin/st13/store/storage'
    _FILENAME_UN_STORAGE = os.environ['PATH_TRANSLATED'] +'/cgi-bin/st13/store/organization_storage'
    params = ['name']
    placeholder = ['Имя']

    def __init__(self, selfurl, q):
        self.people = []
        self.url = selfurl
        self.q = q
        self.name = 'Отдел'
        self.type = 'отдел'
        self.get_name()
        self.get_list()

    def add_person(self):
        form = Form(self.url, self.q)
        man: Person = Person(self.url, self.q)
        if form.is_saving():
            self.add_man(man)
        form.render(man)

    def add_director(self):
        form = Form(self.url, self.q)
        man: Director = Director(self.url, self.q)
        if form.is_saving():
            self.add_man(man)
        form.render(man)

    def add_man(self, man):
        man.save()
        index = int(self.q.getvalue('id', -1))
        self.get_list()
        if index != -1:
            self.people[index] = man
        else:
            self.people.append(man)
        self.save_list()

    def remove_man(self, index):
        self.get_list()
        if len(self.people) == 0:
            return
        if -1 < int(index) < len(self.people):
            self.people.pop(int(index))
            print(self.name + ' Удален один сотрудник')
        else:
            print('Неверный индекс')
        self.save_list()
        self.back()

    def clear_men(self):
        print('Все сотрудники удалены.</br>')
        self.people = []
        self.save_list()
        self.back()

    def show_people(self):
        self.get_list()
        if len(self.people) == 0:
            print('Организация ' + self.name + ' пуста')
            self.back()
            return
        print('Организация ' + self.name + ' содержит: </br>')
        for index, man in enumerate(self.people):
            print(
                '<a href={0}?student={1}&act=-1&id={2}>удалить</a>'.format(self.url, self.q.getvalue('student'), index))
            href = '&id={0}'.format(index)
            if type(man) is Director:
                href += '&act=0'
            else:
                href += '&act=1'
            for param in man.params:
                href += '&{0}={1}'.format(param, getattr(man, param))
            print('<a href={1}?student={2}{3}>{0}</a>'.format(man, self.url, self.q.getvalue('student'), href))
        self.back()

    def save_list(self):
        with open(self._FILENAME_STORAGE, 'wb') as f:
            pickle.dump(self.people, f)
        print('Данные обновлены.')

    def get_list(self):
        try:
            with open(self._FILENAME_STORAGE, 'rb') as f:
                mans = pickle.load(f)
                self.people = mans
        except:
            pass

    def save_name(self):
        with open(self._FILENAME_UN_STORAGE, 'wb') as f:
            pickle.dump(self.name, f)
        print('Наименование организации сохранено')

    def get_name(self):
        try:
            if os.path.getsize(self._FILENAME_UN_STORAGE) > 0:
                with open(self._FILENAME_UN_STORAGE, 'rb') as f:
                    self.name = pickle.load(f)
        except:
            pass

    def edit(self):
        if 'name' in self.q:
            self.name = self.q.getvalue('name')
            self.save_name()
        form = Form(self.url, self.q)
        form.render(self)

    def back(self):
        Menu.back_button(self.url, self.q.getvalue('student'))

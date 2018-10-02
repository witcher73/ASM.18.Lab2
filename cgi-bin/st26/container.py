# -*- coding: utf-8 -*-

from pickle import dump, load

from .student import StudentCl
from .teacher import TeacherCl


class Container:

    def __init__(self, q, selfurl):
        self.db = []
        self.q = q
        self.selfurl = selfurl

    def add_list_student(self):
        """
        Добавление студента в список.
        """
        self.read_list()
        std = StudentCl(self.q)
        self.db.append(std)
        std.add()
        std.save_form(self.q)
        if std.name != ' ':
            self.write_list()

    def add_list_teacher(self):
        """
        Добавсление преподавателя в список.
        """
        self.read_list()
        tchr = TeacherCl(self.q)
        self.db.append(tchr)
        tchr.add()
        tchr.save_form(self.q)
        if tchr.name != ' ':
            self.write_list()

    def save_form(self):
        self.read_list()
        self.db[int(self.q.getvalue('id'))].save_form(self.q)
        self.write_list()
        self.get_list()

    def edit_list(self):
        """
        Редактирование записи в списке.
        """
        self.read_list()
        self.db[int(self.q.getvalue('id'))].edit(self.q)

    def get_list(self):
        """
        Вывод списка.
        """
        self.read_list()
        print(f'<br><a href="{self.selfurl}">Меню</a> | <a href="{self.selfurl}?student={self.q.getvalue("student")}">Обновить</a><br>')
        if len(self.db) == 0:
            print('<br>Список пуст<br>')
        else:
            print("""
            <table border>
             <Caption><H3>Список</H3></Caption>
              <tr><th rowspan="2" width="15%">Тип</th><th colspan="3">Информация</th><th colspan="2">Доп. информация</th><th rowspan="2">Действия</th></tr>
              <tr><th width="25%">ФИО</th><th>Возраст</th><th width="20%">Телефон</th>
              <th>Кафедра</th></tr>""")
            i = 0
            for item in self.db:
                    item.show_form()
                    print(f"""
                      <td>
                       <a href="{self.selfurl}?student={self.q.getvalue('student')}&action=delete_list&id={i}">Удалить</a> /
                       <a href="{self.selfurl}?student={self.q.getvalue('student')}&action=edit_list&id={i}">Изменить</a>
                      </td>
                     </tr>
                     """)
                    i += 1
        print(f"""
            </table>
             <br><a href="{self.selfurl}?student={self.q.getvalue('student')}&action=add_student">Добавить студента</a>
             <br><a href="{self.selfurl}?student={self.q.getvalue('student')}&action=add_teacher">Добавить преподавателя</a>
             <br><a href="{self.selfurl}?student={self.q.getvalue('student')}&action=clear_list">Очистить список</a>
        """)

    def delete_list(self):
        """
        Удаление записи из списка.
        """
        self.read_list()
        self.db.pop(int(self.q.getvalue('id')))
        self.write_list()
        self.get_list()

    def read_list(self):
        """
        Загрузка списка из файла.
        """
        with open('cgi-bin/st26/db.dat', 'rb') as f:
            self.db = load(f)

    def write_list(self):
        """
        Запись списка в файл.
        """
        with open('cgi-bin/st26/db.dat', 'wb') as f:
            dump(self.db, f)

    def clear_list(self):
        """
        Очистка списка.
        """
        self.read_list()
        self.db.clear()
        self.write_list()
        self.get_list()

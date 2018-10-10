# -*- coding: utf-8 -*-

from .student import StudentCl


class TeacherCl(StudentCl):

    def __init__(self, q):
        super().__init__(q)
        self.tch = ''

    def add(self):
        print(f"""
        <Caption><H3>Добавление преподавателя</H3></Caption>
         <form>
          <input type=hidden name=student value="{self.q.getvalue('student')}">
          <input type=hidden name=action value="add_teacher">
           <table border="0">
            <tr><td>ФИО:</td><td><input type=text name=name value="{self.name}"></td></tr>
            <tr><td>Возраст:</td><td><input type=text name=age value="{self.age}"></td></tr>
            <tr><td>Телефон:</td><td><input type=text name=phone value="{self.phone}"></td></tr>
            <tr><td>Кафедра:</td><td><input type=text name=tch value="{self.tch}"></td></tr>
            <tr><td><input type=submit value="Сохранить"></td></tr>
            </table>
          </form>
          <p><a href="?student={self.q.getvalue('student')}">Назад</a></p>
        """)

    def save_form(self, q):
        super().save_form(q)
        self.tch = q.getvalue('tch')

    def show_form(self):
        print(f"""
        <tr>
         <td>Преподаватель</td>
         <td>{self.name}</td>
         <td align="center">{self.age}</td>
         <td>{self.phone}</td>
         <td colspan="2">{self.tch}</td>
        """)

    def edit(self, q):
        print(f"""
        <Caption><H3>Редактирование записи</H3></Caption>
         <form>
          <input type=hidden name=student value="{q.getvalue('student')}">
          <input type=hidden name=action value="save_form">
          <input type=hidden name=id value="{q.getvalue('id')}">
        """)
        self.edit_form()
        print(f"""
          <tr><td><input type=submit value="Сохранить"></td></tr>
         </form>
         </table>
        <p><a href="?student={q.getvalue('student')}">Назад</a></p>
        """)

    def edit_form(self):
        super().edit_form()
        print(f'<tr><td>Кафедра:</td><td><input type=text name=tch value="{self.tch}"></td></tr>')

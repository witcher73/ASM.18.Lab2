# -*- coding: utf-8 -*-


class StudentCl:

    def __init__(self, q):
        self.q = q
        self.name = ''
        self.age = ''
        self.phone = ''

    def add(self):
        print(f"""
        <Caption><H3>Добавление студента</H3></Caption>
         <form>
          <input type=hidden name=student value="{self.q.getvalue('student')}">
          <input type=hidden name=action value="add_student">
           <table border="0"><tr><td>ФИО:</td><td><input type=text name=name value="{self.name}"></td></tr>
           <tr><td>Возраст:</td><td><input type=text name=age value="{self.age}"></td></tr>
           <tr><td>Телефон:</td><td><input type=text name=phone value="{self.phone}"></td></tr>
           <tr><td><input type=submit value="Сохранить"></td></tr>
          </form>
         </table>
        <p><a href="?student={self.q.getvalue('student')}">Назад</a></p>
        """)

    def save_form(self, q):
        if 'name' in self.q:
            self.name = q.getvalue('name')
            self.age = q.getvalue('age')
            self.phone = q.getvalue('phone')
        else:
            self.name = ' '

    def show_form(self):
        print(f"""
        <tr>
         <td>Студент</td>
         <td>{self.name}</td>
         <td align="center">{self.age}</td>
         <td>{self.phone}</td>
         <th colspan="2">-</th>
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
        print(f"""
        <table border="0">
         <tr><td>ФИО:</td><td><input type=text name=name value="{self.name}"></td></tr>
          <tr><td>Возраст:</td><td><input type=text name=age value="{self.age}"></td></tr>
          <tr><td>Телефон:</td><td><input type=text name=phone value="{self.phone}"></td></tr>
        """)

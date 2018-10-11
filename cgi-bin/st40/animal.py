# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:14:07 2018

@author: student
"""

class Animal():
    def __init__(self, q):
        self.q = q
        self.name = None
        self.view = None
       
    #@property
    #def Input(self):
    #    self.name = input('Введите кличку животного: ')
    #    self.view = input('Введите вид животного:')
       
        
    #@property
    #def print(self):
    #    print('''Кличка: {0} Вид: {1} '''.format(self.name, self.view))
    
    def Add(self):
        print(f"""
        <Caption><H3>Добавление животного</H3></Caption>
         <form>
          <input type=hidden name=animal value="{self.q.getvalue('animal')}">
          <input type=hidden name=action value="AddAnimal">
           <table border="0">
           
           <tr><td>Кличка:</td><td><input type=text name=name value="{self.name}"></td></tr>
              <tr><td>Вид:</td><td><input type=text name=view value="{self.view}"></td></tr>
           
           <tr><td><input type=submit value="Сохранить"></td></tr>
          </form>
         </table>
        <p><a href="?animal={self.q.getvalue('animal')}">Назад</a></p>
        """)
           
    def Edit(self, q):
        print(f"""
        <Caption><H3>Редактирование записи</H3></Caption>
         <form>
          <input type=hidden name=animal value="{q.getvalue('animal')}">
          <input type=hidden name=action value="SaveForm">
          <input type=hidden name=id     value="{q.getvalue('id')}">
        """)
        self.EditForm()
        print(f"""
          <tr><td><input type=submit value="Сохранить"></td></tr>
         </form>
        </table>
        <p><a href="?animal={q.getvalue('animal')}">Назад</a></p>
        """)

    def EditForm(self):
        print(f"""
        <table border="0">
         <tr><td>Кличка:</td><td><input type=text name=name value="{self.name}"></td></tr>
            <tr><td>Вид:</td><td><input type=text name=view value="{self.view}"></td></tr>
        """)
        
    def SaveForm(self, q):
        if 'name' in self.q:
            self.name = q.getvalue('name')
            self.view = q.getvalue('view')
        else:
            self.name = ' '
    
    def ShowForm(self):
        print(f"""
        <tr>
         <td>Животное</td>
         <td>{self.name}</td>
         <td align="center">{self.view}</td>
         <th colspan="2">-</th>
        """)
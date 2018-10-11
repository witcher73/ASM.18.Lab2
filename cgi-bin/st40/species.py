# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:14:07 2018

@author: student
"""

from .animal import Animal

class Species(Animal):
    def __init__(self):
        super().__init__()
        self.breed = None
        self.generations = None

    def Add(self):
        print(f"""
        <Caption><H3>Добавление породистого животного</H3></Caption>
         <form>
          <input type=hidden name=animal value="{self.q.getvalue('animal')}">
          <input type=hidden name=action  value="AddSpecies">
           <table border="0">
                        <tr><td>Кличка:</td><td><input type=text name=name        value="{self.name}"></td></tr>
                           <tr><td>Вид:</td><td><input type=text name=view        value="{self.view}"></td></tr>
                        <tr><td>Породa:</td><td><input type=text name=breed       value="{self.breed}"></td></tr>
            <tr><td>Количество предков:</td><td><input type=text name=generations value="{self.generations}"></td></tr>
            
            <tr><td><input type=submit value="Сохранить"></td></tr>
            </table>
          </form>
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
        super().EditForm()
        print(f"""<tr><td>Породa:</td><td><input type=text name=breed       value="{self.breed}"></td></tr>
      <tr><td>Количество предков:</td><td><input type=text name=generations value="{self.generations}"></td></tr>
              """)

    def SaveForm(self, q):
        super().SaveForm(q)
        self.breed = q.getvalue('breed')
        self.generations = q.getvalue('generations')


    def ShowForm(self):
        print(f"""
        <tr>
         <td>П</td>
         <td>{self.name}</td>
         <td align="center">{self.age}</td>
         <td>{self.phone}</td>
         <td colspan="2">{self.tch}</td>
        """)
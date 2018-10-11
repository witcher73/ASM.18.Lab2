# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:14:09 2018

@author: student
"""

from .species import Species
from .animal import Animal
#from pickle import dump, load
import pickle

FILENAME = 'shkurenkov40.txt'
class Container():
   
    def __init__(self, q, selfurl):
        self.DBA = []
        self.q = q
        self.selfurl = selfurl       
        
        
    @property
    def AddAnimal(self):
        "Добавление животное в список. "
        self.ReadFile()
        animal = Animal(self.q)
        self.DBA.append(animal)
        animal.Add()
        animal.SaveForm(self.q)    

    @property
    def AddSpecies(self):
        "Добавление породистое животное в список.      "
        self.ReadFile()
        species = Species(self.q)
        self.DBA.append(species)
        species.Add()
        species.SaveForm()

    @property
    def ClearContainer(self):
        "Очистить список.      "
        self.ReadFile()
        self.DBA.clear()
        self.WriteFile()
        self.ShowContainer()    

    @property
    def DeleteAnimal(self):
        "Удаление животного."
        self.ReadFile()
        self.DBA.pop(int(self.q.getvalue('id')))
        self.WriteFile()
        self.ShowContainer()

    @property
    def  EditAnimal(self):
        "Редактирование элемента в списке."
        self.ReadFile()
        self.DBA[int(self.q.getvalue('id'))].edit(self.q)

    @property
    def ReadFile(self):
        "Загрузка списка из файла."
        with open("cgi-bin/st40/shkurenkov", "rb") as file:
            self.DBA = pickle.load(file)
            file.close()
    
    @property
    def SaveForm(self):
        self.ReadFile()
        self.db[int(self.q.getvalue('id'))].SaveForm(self.q)
        self.WriteFile()
        self.ShowContainer()
    
    @property
    def ShowContainer(self):
         "Вывод списка."
         self.ReadFile()
         print(f'<br><a href="{self.selfurl}">Меню</a> | <a href="{self.selfurl}?animal={self.q.getvalue("animal")}">Обновить</a><br>')
         if len(self.DBA) == 0:
            print('<br>Список пуст<br>')
         else:
            print("""
            <table border>
             <Caption><H3>Список</H3></Caption>
              <tr><th rowspan="2" width="15%">Тип</th><th colspan="3">Информация</th><th colspan="2">Доп. информация</th><th rowspan="2">Действия</th></tr>
              <tr><th width="25%">Кличка</th><th>Вид</th><th width="20%">Породa</th>
              <th>Количество предков </th></tr>""")
            
            i = 0
            for item in self.DBA:
                    item.ShowForm()
                    print(f"""
                      <td>
                       <a href="{self.selfurl}?animal={self.q.getvalue('animal')}&action=delete_list&id={i}">Удалить</a> /
                       <a href="{self.selfurl}?animal={self.q.getvalue('animal')}&action=edit_list&id={i}">Изменить</a>
                      </td>
                     </tr>
                     """)
                    i =i+ 1
         print(f"""
            </table>
             <br><a href="{self.selfurl}?animal={self.q.getvalue('animal')}&action=AddAnimal">Добавить животное</a>
             <br><a href="{self.selfurl}?animal={self.q.getvalue('animal')}&action=AddSpecies">Добавить пороистое животное</a>
             <br><a href="{self.selfurl}?animal={self.q.getvalue('animal')}&action=ClearContainer">Очистить список</a>
         """)
        
         if len(self.container) == 0:
                                     print("Список животных пуст.")
                                     return
         print("Общее число животных: ",len(self.container))
         for animal in self.container:
                                         animal.print
                
                       
    @property
    def WriteFile(self):
        "Запись в файл."
        with open("cgi-bin/st40/shkurenkov","wb") as file:
            pickle.dump(self.DBA, file)
            file.close()
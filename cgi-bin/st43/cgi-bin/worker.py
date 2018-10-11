#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 10:03:50 2018

@author: Shush_000
"""

class Worker():
# метод вызывается всякий раз, когда вы создаете (или создаете экземпляр) объект
# на основе этого класса
# Слово self это способ описания любого объекта

    def __init__(self,q):
# атрибуты
        self.q = q
        self.name = ''
        self.age = ''
        self.otdel = ''
        self.position = ''

    def __str__(self):
        return f'Сотрудник. {self.name}, {self.age}, {self.otdel}, {self.position}'
    def show_form(self):
        print(f"""
        <tr>
         <td>Сотрудник</td>
         <td>{self.name}</td>
         <td>{self.age}</td>
         <td>{self.otdel}</td>
         <td>{self.position}</td>
         <th colspan="2">-</th>
        """)

if __name__ == '__main__':
 







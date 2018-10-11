#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 11:06:30 2018

@author: Shush_000
"""

from .worker import Worker


class Boss(Worker):

    def __init__(self,q):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__(q)
        self.experience = ''

    def __str__(self):
        return f'Директор отдела. {self.name}, {self.age}, {self.experience}'
    def show_form(self):
        print(f"""
        <tr>
         <td>Директор</td>
         <td>{self.name}</td>
         <td>{self.age}</td>
         <td>{self.experience}</td>
         <td colspan="2">{self.tch}</td>
        """)

if __name__ == '__main__':
   
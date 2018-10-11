#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 11:23:12 2018

@author: Shush_000
"""

# "Pickling" - процесс преобразования объекта Python в поток байтов

import pickle
from .worker import Worker
from .boss import Boss


class Otdel:
    def __init__(self, q, selfurl):
        self.ll = []
        self.q = q
        self.selfurl = selfurl
    ll = []

    def add_worker(self):
        worker = Worker()
        worker.input_w()
        self.ll.append(worker)
        worker.save_form(self.q)

    def add_boss(self):
        boss = Boss()
        boss.input_b()
        self.ll.append(boss)
        boss.save_form(self.q)
        
    def write_file(self):
        file = open("spisok.dat", "wb")
        pickle.dump(self.ll, file)
        file.close()
        print("Записано")

    def read_file(self):
        file = open("spisok.dat", "rb")
        self.ll += pickle.load(file)
        file.close()
        print("Прочитано")
        
    def save_form(self):
        self.read_file()
        self.ll[int(self.q.getvalue('id'))].save_form(self.q)
        self.write_file()
        self.get_list()
        
    def get_list(self):
        self.read_list()
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
      

    def output_spiska(self):
        for Number, Object in enumerate(self.ll, start=1):
            print(Number, Object)
            
    def redact(self):
        self.output_spiska()
        num=input('Введите номер объекта: ')
        if type (self.ll[int(num)])== Worker:
            worker=Worker()
            worker.input_w()
            self.ll[int(num)]=worker
        else:
            boss=Boss()
            boss.input_b()
            self.ll[int(num)]=boss
            print('Редактировано')

    def clear(self):
        self.ll.clear()
        print("Удалено")


if __name__ == '__main__':
    pass

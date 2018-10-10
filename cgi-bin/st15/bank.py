import pickle
import os
from .visa import visa
from .master import master

class cont:
    filename='cgi-bin/st15/file.pkl'
    
    def __init__(self, q, selfurl):
        self.__items = []
        self.q = q
        self.selfurl = selfurl
        self.load_from_file()
    
    def addv(self):
        self.load_from_file()
        self.__items.append(visa())
        self.edit()
        self.save_to_file()
    def addm(self):
        self.load_from_file()
        self.__items.append(master())
        self.edit()
        self.save_to_file()
          
    def edit(self):
        print("""<form>
                <input type="hidden" name="student" value="{}" />
                <input type="hidden" name="act" value="get" />""".format(self.q.getvalue('student')))
        _id = int(self.q.getvalue('id') if 'id' in self.q else len(self.__items)-1)
        print('<input type="hidden" name="id" value="{}" />'.format(_id))
        print('<table align="center">')
        self.__items[_id].edit()
        print('</table> <P></P>')
        print('<p align="center"><input type="submit" value="Отпарвить"></form>')
        
    def print_all(self):
        print("""<html>
              <title>Kazak Laba 2</title>
              <head><h1 align="center">Лабаратолрная работа №2</h1></head>
              <body align="center">
              <table align="center" border="5" bordercolor="green" cellpadding="2" cellspacing="1"><tr align="center"><td>Имя</td><td>Фамилия</td><td>Возраст</td><td>Paypass</td><td>Действия</td></tr>
        
        
        """)
        
        
        for i, item in enumerate(self.__items):
            item.prnt()
            print('<td><a href={0}?student={1}&act=edit&id={2}><button>Редактировать</button></a><br><a href={0}?student={1}&act=delete&id={2}><button>Удалить</button></a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
        print('</table><br>')
        print(f"""<p><a href={self.selfurl}?student={self.q.getvalue('student')}&act=addv><button>Заявка на визу</button></a>
              <a href={self.selfurl}?student={self.q.getvalue('student')}&act=addm><button>Заявка на мастер</button></a></p>
              <a href={self.selfurl}?student={self.q.getvalue('student')}&act=clear><button>Удалить все заявки</button></a><br>
              <p><a href={self.selfurl}><button>Назад</button></a>
              """)
    
    def get(self):
        self.load_from_file()
        self.__items[int(self.q.getvalue('id'))].get(self.q)
        self.save_to_file()
        self.print_all()
          
    def delete_item(self):
        self.__items.pop(int(self.q.getvalue('id')))
        self.save_to_file()
        self.print_all()
    
    def clear(self):
        self.__items.clear()
        self.save_to_file()
        self.print_all()
    
    def save_to_file(self):
        pickle.dump(self.__items, open(self.filename, 'wb'))
    
    def load_from_file(self):
        if (os.path.exists(self.filename)):
            self.__items = pickle.load(open(self.filename, 'rb'))
          
          
        

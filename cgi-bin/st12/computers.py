import pickle, copy, os
from .computer_case import Computer_case
from .notebook import Notebook

class Computers:
    def __init__(self, q, selfurl):
        self.l=list()
        self.q = q
        self.selfurl = selfurl

    def write(self):
        self.read_file()
        if (len(self.l)!=0):
            print('<table border><Caption><H3>PC catalog</H3></Caption><tr><td>Название ПК</td><td>Материнская плата </td><td>ЦП</td><td>Жесткий диск</td><td>Оперативная память</td><td>Графический процессор</td><td>Монитор</td><td>Действие</td></tr>')
            i=0
            for o in self.l:
                print('<tr height="20">')
                o.write()
                if type(o) is Computer_case: print('<td>Not included</td>')
                print('<td><a href="{0}?student={1}&action=1&type=4&id={2}">Изменить</a> | <a href="{0}?student={1}&action=3&id={2}">Удалить</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
            print('</table>')
        print('<br><br><a href="{0}">Назад</a> | <a href="{0}?student={1}&action=1">Добавить ПК</a>'.format(self.selfurl, self.q['student'].value))

    def read(self):
        self.read_file()
        if ('type' in self.q):       
            if (self.q['type'].value!="3"):
                if (self.q['type'].value=="1"): Computer_case(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="2"): Notebook(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="4"): self.l[int(self.q['id'].value)].write_ch()
                print('<br><br><input type="submit" value="Save">')
                print('</form>')
            else:
                if (len(self.l)==int(self.q['id'].value)):
                    if (self.q['add'].value=="1"): self.l.append(Computer_case(self.q, self.selfurl))
                    if (self.q['add'].value=="2"): self.l.append(Notebook(self.q, self.selfurl))
                self.l[int(self.q['id'].value)].read()
                self.write_file()
                self.write()
        else:
            k=len(self.l)
            print('<a href="{0}?student={1}&action=1&type=1&id={2}">ПК</a> | <a href="{0}?student={1}&action=1&type=2&id={2}">Ноутбук</a>'.format(self.selfurl, self.q['student'].value, k))


    def f(self):
        print(self.selfurl)
        print('<a href="{0}?student={1}&lol={2}">{3}</a>'.format(self.selfurl, self.q['student'].value, 3, "fds"))
        print(self.q)

   
    

    def delete(self):
        self.read_file()
        self.l.pop(int(self.q['id'].value))
        self.write_file()
        self.write()       
            
       
    def read_file(self):
        if (os.path.exists("cgi-bin/st04/file.dat")):
            self.l = pickle.load(open("cgi-bin/st04/file.dat", "rb"))

    def write_file(self):
        pickle.dump(self.l, open("cgi-bin/st04/file.dat", "wb"))

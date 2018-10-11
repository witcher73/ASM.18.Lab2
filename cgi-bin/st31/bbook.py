from .book import *

class bbook(book):
    def __init__(self):
        b().__init__()
        self.publ = ""
        self.num = ""

    def tbl (self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> автор: ')
        print('<input type = "text" name = "author" value="{0}">'.format(self.author))
        print('название: ')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('год: ')
        print('<input type = "text" name = "year" value="{0}">'.format(self.year))
        print('издательство: ')     
        print('<input type = "text" name = "publ" value="{0}">'.format(self.publ))
        print('<br><br>номер: ' )    
        print('<input type = "text" name = "num" value="{0}">'.format(self.num))
        print('<br><br><input type = "submit" value = "Добавить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')

    def read(self, q ,selfurl):
        b().read(q ,selfurl)
        if ('publ' in self.q):
            self.publ = self.q['publ'].value
        else: self.publ = ""
        if ('num' in self.q):
            self.num = self.q['num'].value
        else: self.num = ""

    def write(self):
        print(
    '''<br>
автор: {0}
название: {1}
год: {2}
издательство: {3}
номер: {4}
'''.format(self.author,
           self.name,
           self.year,
           self.publ,
           self.num))
        

from .bbook import *
import pickle
import  cgi

FILENAME = 'cgi-bin/st31/31.txt'

class Container():
    
    def __init__(self, q, selfurl):
        self.container = []
        self.q = q
        self.selfurl = selfurl

    def tbl(self):
        #self.write_in_file()
        self.read_from_file()
        print("<style> table, td, th { border-collapse: collapse; border-left: 10px solid #663399; background-author: lightgrey;} ")
        print("table { width: 100%; } td {height: 50px; text-align: center;font-size: 20px;font-family: Monaco, Courier, monospace; } ")
        print("h1 { font-size: 15px; font-style: oblique; } </style>")

        print('<table>')
        print("<tr>")
        print("<td><a href = {0}?action=2&index=-1&student={1}> Добавить книгу</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=3&index=-1&student={1}> Добавить журнал</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=8&student={1}> Очистить список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=0> В меню</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")    

    def show(self):
        print('<br><br><h1>Список<br><br>')
        for i in self.container:
            print("   {0}-я книга".format(self.container.index(i) + 1))
            i.write()
            print("<br><a href = {0}?action=4&index={1}&student={2}> Редактировать</a> / ".format(self.selfurl, self.container.index(i), self.q['student'].value))
            print("<a href = {0}?action=5&index={1}&student={2}>Удалить<br><br></a>".format(self.selfurl, self.container.index(i), self.q['student'].value))
        if len(self.container) == 0:
            print("<br>Список пуст<br></h1>")
            
    def add(self):
        self.read_from_file()
        if self.q["action"].value == "2":
            book().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "3":
            bbook().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "6":
            book = book()
            book.read(self.q, self.selfurl)
            self.container.append(book)
        elif self.q["action"].value == "7":
            book = bbook()
            book.read(self.q, self.selfurl)
            self.container.append(book)
        elif self.q["action"].value == "5":
            self.container.pop(int(self.q["index"].value))
        self.write_in_file()
        self.show ()

    def edit(self):
        self.read_from_file()      
        if self.q["action"].value == "4":
            self.container[int(self.q["index"].value)].tbl(self.q, self.selfurl)
        elif (self.q["action"].value == "6") or (self.q["action"].value == "7"):
            self.container[int(self.q["index"].value)].read(self.q,self.selfurl)
        self.write_in_file()
        self.show()

    def delete(self):
        book_number = int(input('введите номер удаляемого в списке'))
        self.container.pop(book_number)
    
    def clear_container(self):
        self.read_from_file()
        self.container.clear()
        self.write_in_file()                        
    
    def write_in_file(self):
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.container, file)

    def read_from_file(self):
        with open(FILENAME, 'rb') as file:
            self.container = pickle.load(file)

                       
            
        

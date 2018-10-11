import pickle,cgi, os
from Specialist import Specialist
from Head import Head


class Container:
    def __init__(self, q, selfurl):
        self.workers = []
        self.q = q
        self.selfurl = selfurl

    def addworker(self):  #Добавить сотрудника
        self.fromfile()
        self.workers.append(Specialist())
        self.edittarget()
        self.infile()

    def addhead(self):    #Добавить главу
        self.fromfile()
        self.workers.append(Head())
        self.edittarget()
        self.infile()

    def get(self):
        self.fromfile()
        self.workers[int(self.q.getvalue('id'))].get(self.q)
        self.infile()
        self.show()

    def clearcontainer(self): #Удаление
        self.workers.pop(int(self.q.getvalue('id')))
        self.infile()
        self.show()

    def delete_target(self):
        self.workers.pop(int(self.q.getvalue('id')))
        self.infile()
        self.show()

    def show(self):        #Вывод на всех элементов на экран
        print('<table border cellspacing="0"><tr align="center"><td>Имя</td><td>Фамилия</td><td>Должность</td><td>Возраст</td><td>Идентификатор</td><td>Код</td><td>Спецid</td><td>Actions</td></tr>')
        for i, worker in enumerate(self.workers):
            worker.output()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Edit</a><br><a href={0}?worker={1}&act=delete&id={2}>Delete</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('worker'), i))
            print('</table><br>')
        print('<a href={}?student={}&act=add_base>Add Worker</a><br>'.format(self.selfurl, self.q.getvalue('worker')))
        print('<a href={}?student={}&act=add_derived>Add Head</a><br>'.format(self.selfurl, self.q.getvalue('worker')))
        print('<a href={}?student={}&act=clear>Clear</a><br>'.format(self.selfurl, self.q.getvalue('worker')))
        print(f'<a href={self.selfurl}>Назад</a>')

    def infile(self):      #Запись в файл
        pickle.dump(self.workers,open('workers.txt',"wb"))

    def fromfile(self):    #Чтение из файла
        if (os.path.exists("workers.txt")):
            self.workers=pickle.load(open("workers.txt","rb"))

    def edittarget(self):  #Редактировать элемент
        print(""""<form>
                <input type="hidden" name="worker" value="{}" />
                <input type="hidden" name="act" value="get" />""".format(self.q.getvalue('worker'))        )
        number = int(self.q.getvalue('id') if 'id' in self.q else len(self.workers)-1)
        print('<input type="hidden" name="id" value="{}" />'.format(number))
        print('<table>')
        self.workers[number].edit()
        print('</table> <P></P>')
        print('<input type="submit" value="Save"></form>')
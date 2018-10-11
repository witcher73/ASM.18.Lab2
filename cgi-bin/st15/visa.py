class visa:
    def __init__(self):
        self.name=''
        self.sname=''
        self.age=''
    def prnt(self):
        print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.name, self.sname,self.age, '-'))
    def edit(self):
        print('<tr><td>Имя:</td><td><input type="text" name="name" value="{}"></td><tr>'.format(self.name))
        print('<tr><td>Фамилия:</td><td><input type="text" name="sname" value="{}"></td><tr>'.format(self.sname))
        print('<tr><td>Возраст:</td><td><input type="text" name="age" value="{}"></td></tr>'.format(self.age))
    def get(self, q):
        self.name=q.getvalue('name')
        self.sname=q.getvalue('sname')
        self.age=q.getvalue('age')
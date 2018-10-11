import cgi
class Specialist:
    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.position = ''
        self.age = ''
        self.ident = ''

    def fprint(self):
        print('<td>{0}<td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></td>'.format(self.fname,
                                                                                                            self.lname,
                                                                                                            self.position,
                                                                                                            self.age,
                                                                                                            self.ident,
                                                                                                            '-', '-'))

    def output(self):
        print('<tr><td>Имя:</td><td><input type="text" name="fname" value="{0}"></td><tr>'.format(self.fname))
        print('<tr><td>Фамилия:</td><td><input type="text" name="lname" value="{0}"></td><tr>'.format(self.lname))
        print('<tr><td>Должность:</td><td><input type="text" name="position" value="{0}"></td><tr>'.format(self.position))
        print('<tr><td>Возраст:</td><td><input type="text" name="age" value="{0}"></td><tr>'.format(self.age))
        print('<tr><td>Идентификатор:</td><td><input type="text" name="ident" value="{0}"></td><tr>'.format(self.ident))

    def get(self, q):
        self.fname = q.getvalue('fname')
        self.lname = q.getvalue('lname')
        self.position = q.getvalue('posi    tion')
        self.age = q.getvalue('age')
        self.ident = q.getvalue('ident')
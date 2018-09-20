import cgi


class Character:
    
    
    def __init__(self,q,selfurl):
         self.selfurl = selfurl
         self.q = q
         self.name = ""
         self.klas = ""
         self.specialization = ""


    def input(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("name","--")
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('klas' in self.q):
            self.klas = self.q['klas'].value
        else: self.klas = ""
        if ('specialization' in self.q):
            self.specialization = self.q['specialization'].value
        else: self.specialization = ""


    def output_ch(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("id","--")
        print('<form action="{0}?student={1}&action=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("1"))
        print('<input type="text" name="type" value="{0}" style="display:none">'.format("3"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}" style="display:none">'.format(self.q['type'].value))
        print('<br>Name:<br><input type="text" name="name" value="{0}">'.format(self.name))
        print('<br>Klas:<br><input type="text" name="klas" value="{0}">'.format(self.klas))
        print('<br>Specialization:<br><input type="text" name="specialization" value="{0}">'.format(self.specialization))


    def output(self):
        print('<td>{0}</td>'.format(self.name))
        print('<td>{0}</td>'.format(self.klas))
        print('<td>{0}</td>'.format(self.specialization))



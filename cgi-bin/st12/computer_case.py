import cgi
class Computer_case:
    def __init__(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        self.name=""
        self.motherboard=""
        self.CPU=""
        self.HDD=""
        self.RAM=""
        self.GPU=""

        
    def read(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("name","--")
        if ('Название' in self.q):
            self.name = self.q['name'].value
        else: self.name=""
        if ('Материнская плата' in self.q):
            self.motherboard = self.q['motherboard'].value
        else: self.motherboard = ""
        if ('ЦП' in self.q):
            self.CPU = self.q['CPU'].value
        else: self.CPU = ""
        if ('Жесткий диск' in self.q):
            self.HDD = self.q['HDD'].value
        else: self.HDD = ""
        if ('Оперативная память' in self.q):
            self.RAM = self.q['RAM'].value
        else: self.RAM = ""
        if ('Графический процессор' in self.q):
            self.GPU = self.q['GPU'].value
        else: self.GPU = ""
        
    def write_ch(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("id","--")
        print('<form action="{0}?student={1}&action=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("1"))
        print('<input type="text" name="type" value="{0}" style="display:none">'.format("3"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}" style="display:none">'.format(self.q['type'].value))
        print('Название:<br><input type="text" name="name" value="{0}">'.format(self.name))
        print('<br>Материнская плата:<br><input type="text" name="motherboard" value="{0}">'.format(self.motherboard))
        print('<br>ЦП:<br><input type="text" name="CPU" value="{0}">'.format(self.CPU))
        print('<br>Жесткий диск:<br><input type="text" name="HDD" value="{0}">'.format(self.HDD))
        print('<br>Оперативная память:<br><input type="text" name="RAM" value="{0}">'.format(self.RAM))
        print('<br>Графический процессор:<br><input type="text" name="GPU" value="{0}">'.format(self.GPU))

    def write(self):
        print('<td>{0}</td>'.format(self.name))
        print('<td>{0}</td>'.format(self.motherboard))
        print('<td>{0}</td>'.format(self.CPU))
        print('<td>{0}</td>'.format(self.HDD))
        print('<td>{0}</td>'.format(self.RAM))
        print('<td>{0}</td>'.format(self.GPU))

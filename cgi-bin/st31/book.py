class book():
    def __init__(self):
        self.author = ""
        self.name = ""
        self.year = ""

    
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
        print('<br><br><input type = "submit" value = "Добавить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')


    def read(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('author' in self.q):
            self.author = self.q['author'].value
        else: self.author = ""
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('year' in self.q):
            self.year = self.q['year'].value
        else: self.year = ""

    def write(self):
        print("<br> автор: {0} | название: {1} | год: {2} ".format(self.author,self.name,self.year))





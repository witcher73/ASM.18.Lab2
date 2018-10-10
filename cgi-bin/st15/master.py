from .visa import visa
class master(visa):
    def __init__(self):
        super().__init__()
        self.pp=''
    def edit(self):
        super().edit()
        print('<tr><td>PayPass:</td><td><input type="text" name="pp" value="{}"></td><tr>'.format(self.pp))
    def get(self, q): 
        super().get(q)
        self.pp = q.getvalue('pp')
    def prnt(self):
        print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.name, self.sname, self.age, self.pp))
    

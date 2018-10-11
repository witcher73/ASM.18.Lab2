from .computer_case import Computer_case
import cgi

class Notebook(Computer_case):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self.display=""
        self.q=q
        self.selfurl=selfurl

    def write(self):
        Computer_case.write(self)
        print('<td>{0}</td>'.format(self.display))


    def read(self):
        Computer_case.read(self)
        if ('display' in self.q):
            self.displмay = self.q['display'].value
        else: self.display = ""

   
        

    def write_ch(self):
        Computer_case.write_ch(self)
        print('<br>Монитор:<br><input type="display" name="display" value="{0}">'.format(self.display))
    	

    
    

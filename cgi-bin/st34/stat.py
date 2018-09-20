import cgi


from .character import Character

class Stat(Character):


    def __init__(self,q,selfurl):
        super().__init__(q,selfurl)
        self.haste = ""
        self.q = q
        self.selfurl = selfurl

         
    def input(self):
        Character.input(self)
        if('haste' in self.q):
            self.haste = self.q['haste'].value
        else: self.haste = ""
            

    def output_ch(self):
        Character.output_ch(self)
        print('<br>Haste:<br><input type="text" name="haste" value="{0}">'.format(self.haste))


    def output(self):
        Character.output(self)
        print('<td>{0}</td>'.format(self.haste))
# print("\nHealth:" + self.Health + "\nHaste:" + self.Haste)

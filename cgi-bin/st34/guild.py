import pickle,os
import cgi


from .character import Character
from .stat import Stat


class Guild:


    def __init__(self,q,selfurl):
        self.l = list()
        self.q = q
        self.selfurl = selfurl
    

    def input(self):
        self.inputfile()
        if ('type' in self.q):
            if (self.q['type'].value!="3"):
                if (self.q['type'].value=="1"): Character(self.q, self.selfurl).output_ch()
                if (self.q['type'].value=="2"): Stat(self.q, self.selfurl).output_ch()
                if (self.q['type'].value=="4"): self.l[int(self.q['id'].value)].output_ch()
                print('<br><br><input type="submit" value="Save">')
                print('</form>')
            else:
                if (len(self.l)==int(self.q['id'].value)):
                    if (self.q['add'].value=="1"): self.l.append(Character(self.q, self.selfurl))
                    if (self.q['add'].value=="2"): self.l.append(Stat(self.q, self.selfurl))
                self.l[int(self.q['id'].value)].input()
                self.outputfile()
                self.output()
        else:
            k=len(self.l)
            print('<a href="{0}?student={1}&action=1&type=1&id={2}">Character</a> | <a href="{0}?student={1}&action=1&type=2&id={2}">Stat</a>'.format(self.selfurl, self.q['student'].value, k))


    def output(self):
        self.inputfile()
        if (len(self.l)!=0):
            print('<table border><tr><td>Name</td><td>Klas</td><td>Specialization</td><td>Haste</td><td>Action</td></tr>')
            i=0
            for o in self.l:
                print('<tr height="20">')
                o.output()
                if type(o) is Character: print('<td>10</td>')
                print('<td><a href="{0}?student={1}&action=1&type=4&id={2}">Change</a> | <a href="{0}?student={1}&action=3&id={2}">Delete</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
            print('</table>')
        print('<br><br><a href="{0}">Back</a> | <a href="{0}?student={1}&action=1">Add members</a>'.format(self.selfurl, self.q['student'].value))


    def delete(self):
        self.inputfile()
        self.l.pop(int(self.q['id'].value))
        self.outputfile()
        self.output()
        
        
    def inputfile(self):
        if (os.path.exists("file.txt")):
            self.l = pickle.load(open("file.txt", "rb"))


    def outputfile(self):
        pickle.dump(self.l, open("file.txt", "wb"))
        
        
    def clear(self):
        self.l.clear()


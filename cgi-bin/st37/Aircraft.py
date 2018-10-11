import pickle, cgi, os
from .Cargoplane import *
from .Airbus import *

class Aircraft:
    def __init__(self, q, selfurl):
        self.aircraft = []
        self.q = q
        self.selfurl = selfurl
      
    def input_cargoplane(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="add_cargoplane" />')
        print('<table>')
        Cargoplane().edit()
        print('</table>')
        print('<input type="submit" value="Save">')
        print('</form>')
        
    def input_airbus(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="action" value="get" />')
        print('<input type="hidden" name="id" value="add_airbus" />')
        print('<table>')
        Airbus().edit()
        print('</table>')
        print('<input type="submit" value="Save">')
        print('</form>')
        
    def show(self):
        print('<table border cellspacing="0"><tr align="center"><td>Model</td><td>Power</td><td>Maximum speed</td><td>Carrying capacity</td><td>Crew</td><td>Payload</td><td>Number of seats</td><td>Cruising speed</td><td>Options</td></tr>')
        i = 0
        for item in self.aircraft:
            print('<br>')
            item.show_list()
            print('<td><a href={0}?student={1}&act=edit&id={2}>edit</a><br><a href={0}?student={1}&act=delete&id={2}>delete</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            i += 1
        print('</table><br>')
        print('<a href={0}?student={1}&act=add_cargoplane>Добавить грузовой самолёт</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=add_airbus>Добавить пассажирский самолёт</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=clear>Очистить список</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}>Назад</a></p>'.format(self.selfurl))
    
    def get_aircraft(self):
        if self.q.getvalue('id') == 'add_cargoplane':
            ap = Cargoplane()
            ap.get(self.q)
            self.aircraft.append(ap)
        elif self.q.getvalue('id') == 'add_airbus':
            ap = Airbus()
            ap.get(self.q)
            self.aircraft.append(ap)
        else:
            self.aircraft[int(self.q.getvalue('id'))].get(self.q)
        self.show()
    
    def edit_aircraft(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        iid = self.q.getvalue('id')
        print('<input type="hidden" name="id" value="{0}" />'.format(iid))
        print('<table>')
        self.aircraft[int(iid)].edit()
        print('</table>')
        print('<input type="submit" value="Save">')
        print('</form>')
             
    def save_file(self):
        pickle.dump(self.aircraft, open('cgi-bin/st37/data.dat', 'wb'))
    
    def load_file(self):
        if (os.path.exists('cgi-bin/st37/data.dat')):
            self.aircraft = pickle.load(open('cgi-bin/st37/data.dat', 'rb'))
        
    def del_aircraft(self):
        self.aircraft.pop(int(self.q.getvalue('id')))
        self.show()
        
    def clear_list(self):
        self.aircraft.clear()
        self.show()

import pickle
import os
from .dslr import DSLR
from .slr import SLR

class Container:
    FILENAME = 'cgi-bin/st45/dump.pkl'
    
    
    def __init__(self, q, selfurl):
        self.list = []
        self.q = q
        self.selfurl = selfurl
        self.open()
    
    def add_dslr(self):
        self.open()
        self.list.append(DSLR())
        self.edit_item()
        self.save()
        
    def add_slr(self):
        self.open()
        self.list.append(SLR())
        self.edit_item()
        self.save()
    
    def edit_item(self):
        print("""<form>
            <input type="hidden" name="student" value="{}" />
            <input type="hidden" name="act" value="get" />""".format(self.q.getvalue('student')))
				
        _id = int(self.q.getvalue('id') if 'id' in self.q else len(self.list)-1) 
        print('<input type="hidden" name="id" value="{}" />'.format(_id))
        print('<table>')
        self.list[_id].edit()
        print('</table> <P></P>')
        print('<input type="submit" value="Save"></form>')
        
    def show(self):
        print('<table border cellspacing="0"><tr align="center"><td>Model</td><td>Year</td><td>Price</td><td>Lens</td><td>Diafragma</td><td>option</td></tr>')
        for i, item in enumerate(self.list):
            item.show()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Edit</a><br><a href={0}?student={1}&act=delete&id={2}>Delete</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
        print('</table><br>')
        print('<a href={}?student={}&act=add_dslr>Add DSLR</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={}?student={}&act=add_slr>Add SLR</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={}?student={}&act=clear>Очистить список</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print(f'<a href={self.selfurl}>Назад</a>')
    
    def get(self):
        self.open()
        self.list[int(self.q.getvalue('id'))].get(self.q)
        self.save()
        self.show()
        
    def delete_list(self):
    	self.list.pop(int(self.q.getvalue('id')))
    	self.save()
    	self.show()
        
    def clear(self):
    	self.list.clear()
    	self.save()
    	self.show()
        
    def save(self):
    	pickle.dump(self.list, open(self.FILENAME, 'wb'))
    
    def open(self):
        if (os.path.exists(self.FILENAME)):
            self.list = pickle.load(open(self.FILENAME, 'rb'))
    	
    

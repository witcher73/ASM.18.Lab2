import pickle
import os

from .base import Base
from .derived import Derived

class Container:
	PKL_FILENAME = 'cgi-bin/st06/dump.pkl'

	def __init__(self, q, selfurl):
		self.__items = []
		self.q = q
		self.selfurl = selfurl
		self.load_from_file()
	
	def add_base(self):
		self.load_from_file()
		self.__items.append(Base())
		self.edit_item()
		self.save_to_file()

	def add_derived(self):
		self.load_from_file()
		self.__items.append(Derived())
		self.edit_item()
		self.save_to_file()

	def edit_item(self):
		print("""<form>
                <input type="hidden" name="student" value="{}" />
                <input type="hidden" name="act" value="get" />""".format(self.q.getvalue('student')))
				
		_id = int(self.q.getvalue('id') if 'id' in self.q else len(self.__items)-1) # because id()

		print('<input type="hidden" name="id" value="{}" />'.format(_id))
		print('<table>')
		self.__items[_id].edit()
		print('</table> <P></P>')
		print('<input type="submit" value="Save"></form>')

	def print_all(self):
		print('<table border cellspacing="0"><tr align="center"><td>Field1</td><td>Field2</td><td>Field3</td><td>Actions</td></tr>')
		for i, item in enumerate(self.__items):
			item.show()
			print('<td><a href={0}?student={1}&act=edit&id={2}>Edit</a><br><a href={0}?student={1}&act=delete&id={2}>Delete</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
		print('</table><br>')
		print('<a href={}?student={}&act=add_base>Add Base</a><br>'.format(self.selfurl, self.q.getvalue('student')))
		print('<a href={}?student={}&act=add_derived>Add Derived</a><br>'.format(self.selfurl, self.q.getvalue('student')))
		print('<a href={}?student={}&act=clear>Очистить список</a><br>'.format(self.selfurl, self.q.getvalue('student')))
		print(f'<a href={self.selfurl}>Назад</a>')

	def get(self):
		self.load_from_file()
		self.__items[int(self.q.getvalue('id'))].get(self.q)
		self.save_to_file()
		self.print_all()

	def delete_item(self):
		self.__items.pop(int(self.q.getvalue('id')))
		self.save_to_file()
		self.print_all()


	def clear(self):
		self.__items.clear()
		self.save_to_file()
		self.print_all()

	def save_to_file(self):
		pickle.dump(self.__items, open(self.PKL_FILENAME, 'wb'))


	def load_from_file(self):
		if (os.path.exists(self.PKL_FILENAME)):
			self.__items = pickle.load(open(self.PKL_FILENAME, 'rb'))
        
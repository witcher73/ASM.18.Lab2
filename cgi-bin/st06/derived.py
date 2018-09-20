from .base import Base

class Derived(Base):
	def __init__(self):
		super().__init__()
		self.field3 = ''

	def edit(self):
		super().edit()
		print('<tr><td>Field3:</td><td><input type="text" name="field3" value="{}"></td><tr>'.format(self.field3))


	def get(self, q): 
		super().get(q)
		self.field3 = q.getvalue('field3')

	def show(self):
		print('<td>{}</td><td>{}</td><td>{}</td>'.format(self.field1, self.field2, self.field3))


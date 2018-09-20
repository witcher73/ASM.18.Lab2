class Base:
	def __init__(self):
		self.field1 = ''
		self.field2 = ''
	
	def show(self):
		print('<td>{}</td><td>{}</td><td>{}</td>'.format(self.field1, self.field2, '-'))


	def edit(self):
		print('<tr><td>Field1:</td><td><input type="text" name="field1" value="{}"></td><tr>'.format(self.field1))
		print('<tr><td>Field2:</td><td><input type="text" name="field2" value="{}"></td></tr>'.format(self.field2))
    
	def get(self, q): 
		self.field1 = q.getvalue('field1')
		self.field2 = q.getvalue('field2')
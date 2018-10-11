class DSLR:
    def __init__(self):
        self.model = ''
        self.year = ''
        self.price = ''
	
    def show(self):
        print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.model, self.year, self.price, '-', '-'))
    
    def edit(self):
        print('<tr><td>model:</td><td><input type="text" name="model" value="{}"></td><tr>'.format(self.model))
        print('<tr><td>year:</td><td><input type="text" name="year" value="{}"></td></tr>'.format(self.year))
        print('<tr><td>price:</td><td><input type="text" name="price" value="{}"></td></tr>'.format(self.price))
        
    def get(self, q): 
        self.model = q.getvalue('model')
        self.year = q.getvalue('year')
        self.price = q.getvalue('price')
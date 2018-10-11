from .dslr import DSLR

class SLR(DSLR):
    def __init__(self):
        super().__init__()
        self.lens = ''
        self.flens = ''
    
    def edit(self):
        super().edit()
        print('<tr><td>lens:</td><td><input type="text" name="lens" value="{}"></td><tr>'.format(self.lens))
        print('<tr><td>flens:</td><td><input type="text" name="flens" value="{}"></td><tr>'.format(self.lens))
        
    def get(self, q): 
        super().get(q)
        self.lens = q.getvalue('lens')
        self.flens = q.getvalue('flens')
        
    def show(self):
        print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.model, self.year, self.price, self.lens, self.flens))
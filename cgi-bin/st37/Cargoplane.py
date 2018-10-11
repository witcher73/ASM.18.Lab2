import cgi

class Cargoplane:
    def __init__(self):    
        self.model = None
        self.power = None
        self.max_speed = None
        self.crew = None
        self.carrying_cap = None
                
    def edit(self):
        print('<tr><td>Model:</td><td><input type="text" name="model" value="{}"></td><tr>'.format(self.model))
        print('<tr><td>Power:</td><td><input type="text" name="power" value="{}"></td></tr>'.format(self.power))
        print('<tr><td>Maximum speed:</td><td><input type="text" name="max_speed" value="{}"></td></tr>'.format(self.max_speed))
        print('<tr><td>Crew:</td><td><input type="text" name="crew" value="{}"></td></tr>'.format(self.crew))
        print('<tr><td>Carrying capacity:</td><td><input type="text" name="carrying_cap" value="{}"></td></tr>'.format(self.carrying_cap))

    def get(self, q): 
        self.model = q.getvalue('model')
        self.power = q.getvalue('power')
        self.max_speed = q.getvalue('max_speed')
        self.crew = q.getvalue('crew')
        self.carrying_cap = q.getvalue('carrying_cap')
        
    def show_list(self):
        print('<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td>'.format(self.model, self.power, self.max_speed, self.crew, self.carrying_cap,'-', '-', '-'))

        
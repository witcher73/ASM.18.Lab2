from .Cargoplane import Cargoplane

class Airbus(Cargoplane):
    def __init__(self):
        super().__init__()
        self.payload = None
        self.cruis_speed = None
        self.num_of_seats = None
         
    def edit(self):
        super().edit()
        print('<tr><td>Payload:</td><td><input type="text" name="payload" value="{}"></td><tr>'.format(self.payload))
        print('<tr><td>Cruising speed:</td><td><input type="text" name="cruis_peed" value="{}"></td></tr>'.format(self.cruis_speed))
        print('<tr><td>Number of seats:</td><td><input type="text" name="num_of_seats" value="{}"></td></tr>'.format(self.num_of_seats))
   
    def get(self, q):
        super().get(q)
        self.payload = q.getvalue('payload')
        self.cruis_speed = q.getvalue('cruis_speed')
        self.num_of_seats = q.getvalue('num_of_seats')

    def show_list(self):
        print('<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td>'.format(self.model, self.power, self.max_speed, self.crew, self.carrying_cap, self.payload, self.cruis_speed, self.num_of_seats))

        

        
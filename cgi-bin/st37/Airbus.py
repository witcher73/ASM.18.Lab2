from .Cargoplane import Cargoplane

class Airbus(Cargoplane):
    def __init__(self):
        super().__init__()
        self.payload = None
        self.cruis_speed = None
        self.num_of_seats = None
        
    def edit(self):
        super().edit()
        self.payload = input('payload ')
        self.cruis_speed = input('cruising speed ')
        self.num_of_seats = input('number of seats ')
   
    def show(self):
        Cargoplane.show(self)
        print("\n9. Payload: "+self.payload+"\n10. Cruising speed : "+self.cruis_speed+"\n11. Number of seats: "+self.num_of_seats)


        
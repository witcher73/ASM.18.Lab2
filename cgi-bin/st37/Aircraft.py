import pickle
from .Cargoplane import Cargoplane
from .Airbus import Airbus

class Aircraft:
        
    def __init__(self):
        self.aircraft = list()ы
        
    def input_cargoplane(self):
        ap = Cargoplane()
        ap.edit()
        self.aircraft.append(ap)

    def input_airbus(self):
        ap = Airbus()
        ap.edit()
        self.aircraft.append(ap)
        
    def print_aircrafts(self):
        if len(self.aircraft) == 0:
            print("Empty")
            return
        for ap in self.aircraft:
            print(ap.__class__.__name__)
            ap.show()
            print('---------------------')
            
    def save_file(self):
        pickle.dump(self.aircraft, open("data", "wb"))
        print("Saved")

    def load_file(self):
        self.aircraft = pickle.load(open("data", 'rb'))
        print ("Loaded")
        
    def clear_list(self):
        self.aircraft.clear()
        print ("Cleared")

    def edit_aircraft(self):
        if len(self.aircraft) == 0:
            print("Empty")
            return
        n = int(input("Aircraft number:"))
        if n <= (len(self.aircraft)-1) and n >= 0:
            self.aircraft[n].edit()
        else:
            print ("Invalid input")
            return
            
    def del_aircraft(self):
        if len(self.aircraft) == 0:
            print("Empty")
            return
        n = int(input("Aircraft number:"))
        if n <= (len(self.aircraft)-1) and n >= 0:
            self.aircraft.pop(n)
            print("Deleted") 
        else:
            print ("Invalid input")
            return

class Cargoplane:
    def __init__(self):    
        self.model = None
        self.power = None
        self.max_speed = None
        self.crew = None
        self.carrying_cap = None
        self.length = None
        self.height = None
        self.wingspan = None
        
    def edit(self):
        self.model = input('model ')
        self.power = input('power ')
        self.max_speed = input('maximum speed ')
        self.crew = input('crew ')
        self.carrying_cap = input('carrying capacity ')
        self.length = input('length ')
        self.height = input('height ')
        self.wingspan = input('wingspan ')
    
    def show(self):
        print("\n1. Model: "+self.model+"\n2. Power : "+self.power+"\n3. Maximum speed: "+self.max_speed+"\n4. Crew: "+self.crew +"\n5. Carrying capacity"+self.carrying_cap +
      "\n6. Length"+self.length+"\n7. Height"+self.height+"\n8. Wingspan"+self.wingspan)

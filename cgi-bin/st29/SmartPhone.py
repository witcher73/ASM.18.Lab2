from .MobilePhone import MobilePhone

class SmartPhone(MobilePhone):

    def __init__(self):
        self.set_data()
        
    def set_data(self):
        MobilePhone.set_data(self)
        self.os = input("Введите название операционной системы:")
        self.ram = input("Введите количесвто оперативной памяти:")
        
    def display_data(self):
        print(self.brand, self.screen_size, self.os, self.ram)
    
        

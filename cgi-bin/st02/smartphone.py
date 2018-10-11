from .device import Device


class Smartphone(Device):
    
    def __init__(self, vendor, model, os):
        self.vendor = vendor
        self.model = model
        self.os = os

    def set_data(self, vendor, model, os):
        __init__(vendor, model, os)
    
    def get_data(self):
        return 'Смартфон', self.vendor, self.model, self.os
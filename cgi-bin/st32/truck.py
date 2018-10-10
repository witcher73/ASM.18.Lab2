# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:27:26 2018

@author: Владимир


 """       

class Truck:
    def __init__(self):
        self.truck_model=''
        self.serial_number=''
        self.carrying='' 
        self.mileage = ''
    
    def show_data(self):     
        print('Truck model: {0}<br> Serial number: {1}<br> Carrying: {2}<br> Mileage:{3}<br><br>'.format(self.truck_model, self.serial_number, self.carrying, self.mileage))
        
    def input_data(self):     
        print('<tr><td><b>Please, insert data:</b><br></td><tr>')
        print('<tr><td>Truck model:</td><td><input type="text" name="truck_model" value="{0}"></td><tr>'.format(self.truck_model))
        print('<tr><td>Serial number:</td><td><input type="text" name="serial_number" value="{0}"></td></tr>'.format(self.serial_number))
        print('<tr><td>Carrying:</td><td><input type="text" name="carrying" value="{0}"></td></tr>'.format(self.carrying))
        print('<tr><td>Mileage:</td><td><input type="text" name="mileage" value="{0}"></td></tr>'.format(self.mileage))
        
    def get_values(self, q):                                
        self.truck_model= q.getvalue('truck_model')
        self.serial_number = q.getvalue('serial_number')
        self.carrying = q.getvalue('carrying')
        self.mileage = q.getvalue('mileage')

            
   
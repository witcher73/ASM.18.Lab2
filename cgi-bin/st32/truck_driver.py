# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:48:00 2018

@author: Владимир


"""
from .truck import Truck
class Truck_driver(Truck):
    def __init__(self):
        Truck.__init__(self)
        self.firstname=''
        self.lastname=''
        self.age=''
        self.category=''
        self.phone_number=''
        
    def show_data(self):
       print("<br>Model of truck: {0}<br>Serial number: {1}<br>Carrying: {2}<br>Mileage: {3}<br>Driver's info:<br>Firstname: {4}<br>Lastname: {5}<br>Age: {6}<br>Category: {7}<br>Phone number:{8}<br><br>".format(self.truck_model,self.serial_number,self.carrying,self.mileage,self.firstname,self.lastname,self.age,self.category,self.phone_number))

    def input_data(self):
        Truck.input_data(self)
        print('<tr><td>Firstname: </td><td><input type="text" name="firstname" value="{0}"></td><tr>'.format(self.firstname))
        print('<tr><td>Lastname: </td><td><input type="text" name="lastname" value="{0}"></td><tr>'.format(self.lastname))
        print('<tr><td>Age: </td><td><input type="text" name="age" value="{0}"></td><tr>'.format(self.age))
        print('<tr><td>Category: </td><td><input type="text" name="category" value="{0}"></td><tr>'.format(self.category))
        print('<tr><td>Phone number: </td><td><input type="text" name="phone_number" value="{0}"></td><tr>'.format(self.phone_number))


        
    def get_values(self, q):
        Truck.get_values(self, q)
        self.firstname = q.getvalue('firstname')
        self.lastname = q.getvalue('lastname')
        self.age = q.getvalue('age')
        self.category = q.getvalue('category')
        self.phone_number = q.getvalue('phone_number')
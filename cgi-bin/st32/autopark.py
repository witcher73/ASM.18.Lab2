# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:54:35 2018

@author: Владимир

"""
import pickle
from .truck import Truck
from .truck_driver import Truck_driver
class Autopark:
    def __init__(self, q, selfurl):
        self.list_of_autopark =[]
        self.q=q
        self.selfurl=selfurl

    def add_empty_truck(self):
        self.select_from_file()
        self.list_of_autopark.append(Truck())
        self.insert_into_file()
        self.edit_truck()
        

    def add_truck_with_driver(self):
        self.select_from_file()
        self.list_of_autopark.append(Truck_driver())
        self.insert_into_file()
        self.edit_truck()
    
    def clear_all(self):
        self.select_from_file()
        self.list_of_autopark.clear()
        self.insert_into_file()
        self.present_autopark()       

    def present_autopark(self):
        self.select_from_file()
         
        print('<head>')
        print('<hr><br><b>-------------- AUTOPARK-MENU----------------------------------------</b><br><br>')
        print('<table>')
        print('<form action = "{0}" method = "GET"> <input type ="hidden" name = "student" value ="{1}" /> <input type ="hidden" name = "actions" value ="add_empty_truck" /> <input type ="submit" value ="Add empty truck"> </form>'.format(self.selfurl, self.q.getvalue('student')))
        print('<form action = "{0}" method = "GET"> <input type ="hidden" name = "student" value ="{1}" /> <input type ="hidden" name = "actions" value ="add_truck_with_driver" /> <input type ="submit" value ="Add truck with driver"> </form>'.format(self.selfurl, self.q.getvalue('student')))
        print('<form action = "{0}" method = "GET"> <input type ="hidden" name = "student" value ="{1}" /> <input type ="hidden" name = "actions" value ="clear_all" /> <input type ="submit" value ="Clear"> </form>'.format(self.selfurl, self.q.getvalue('student')))
        print('<form action = "{0}"> <input type ="submit" value ="Back to Main Menu"> </form>'.format(self.selfurl))
        print('</table>')
        print('<b>----------------------------------------------------------------------------------</b><br><hr>')
        print('</head>')
        i = 0
        for truck in self.list_of_autopark:
            print('<br>')
            print('<b>Truck number {0}:</b><br><br>'.format(i+1))
            truck.show_data()
            print('<table>')
            print('<form action = "{0}" method = "GET"> <input type ="hidden" name = "student" value ="{1}" /> <input type ="hidden" name = "actions" value ="edit_truck" /> <input type ="hidden" name = "id" value ="{2}" />  <input type ="submit" value ="Edit truck"> </form>'.format(self.selfurl, self.q.getvalue('student'), i))
            print('<form action = "{0}" method = "GET"> <input type ="hidden" name = "student" value ="{1}" /> <input type ="hidden" name = "actions" value ="delete_truck" /> <input type ="hidden" name = "id" value ="{2}" />  <input type ="submit" value ="Delete truck"> </form>'.format(self.selfurl, self.q.getvalue('student'), i))
            print('</table>')
            print('<hr>')
            i+=1
        print('<input type="hidden" name="student" value={0} />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="actions" value="present_autopark" />')
        print('<br>')
        
    
   
    def select_from_file(self):
        with open("cgi-bin/st32/filename.txt", 'rb') as filename:
            self.list_of_autopark = pickle.load(filename)
    
    def insert_into_file(self):
         with open("cgi-bin/st32/filename.txt", 'wb') as filename:
            pickle.dump(self.list_of_autopark, filename)
    
    def delete_truck(self):
        self.select_from_file()
        self.list_of_autopark.pop(int(self.q.getvalue('id')))
        self.insert_into_file()
        self.present_autopark()
        
    def edit_truck(self):
        self.select_from_file()
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="actions" value="get_values" />')
        truck_id = str()
        if 'id' in self.q:
            truck_id = self.q.getvalue('id')
        else:
            truck_id = str(len(self.list_of_autopark)-1)
        print('<input type="hidden" name="id" value="{0}" />'.format(truck_id))
        print('<table>')
        self.list_of_autopark[int(truck_id)].input_data()
        print('</table>')
        print('<input type="submit" value="Save">')
        print('</form>')

    def get_values(self):
        self.select_from_file()
        self.list_of_autopark[int(self.q.getvalue('id'))].get_values(self.q)
        self.insert_into_file()
        self.present_autopark()

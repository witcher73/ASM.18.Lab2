# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:27:06 2018

@author: Владимир

"""
from .autopark import Autopark

def main(q, selfurl):
    autopark = Autopark(q, selfurl)
    MENU = {
        'add_empty_truck': autopark.add_empty_truck,
        'add_truck_with_driver': autopark.add_truck_with_driver,
        'present_autopark': autopark.present_autopark,
        'clear_all': autopark.clear_all,
        'delete_truck': autopark.delete_truck,
        'edit_truck': autopark.edit_truck,
        'get_values': autopark.get_values
        
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'actions' in q:
        MENU[q['actions'].value]()
    else:
        MENU['present_autopark']()

'''
auto_park = Autopark()
def end_function():
    return
menu_list = [
                ["Add an empty truck", auto_park.add_empty_truck ],
                ["Add truck with driver", auto_park.add_truck_with_driver],
                ["Present autopark", auto_park.present_autopark ],
                ["Clear all autopark", auto_park.clear_all ],
                ["Delete one item", auto_park.delete_truck ],
                ["Edit item", auto_park.edit_truck ],
                ["Insert data into file", auto_park.insert_into_file ],
                ["Select data from file", auto_park.select_from_file ],
                ["Exit"  ],
            ]


def trucks_menu():
    print("-------------AUTOPARK--------------")
    for i, item in enumerate(menu_list):
        print("{0:2} - {1}".format(i+1, item[0]))
    print("----created by st32 <V.Sazonov>----\n")
    return int(input())-1

def main():
        try:
                while True:
                        menu_list[trucks_menu()][1]()
        except:
                

                print("Exit...")

'''

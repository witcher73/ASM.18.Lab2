import pickle

from .master import Master
from .engineer import Engineer


class Station:

    FILE_NAME = 'cgi-bin/st23/data'

    def __init__(self):
        self.__staff = []


    def add_master(self, lastname, category):
        self.__staff.append(Master(lastname, category))


    def add_engineer(self, lastname, category, numEducations, rank):
        self.__staff.append(Engineer(lastname, category, numEducations, rank))


    def get_staff(self):
        return self.__staff


    def clear_staff(self):
        self.__staff = []


    def delete_item(self, i):
        del self.__staff[i]


    def edit_master(self, i, lastname, category):
        self.__staff[i] = Master(lastname, category)

    
    def edit_engineer(self, i, lastname, category, numEducations, rank):
        self.__staff[i] = Engineer(lastname, category, numEducations, rank)


    def save_to_file(self):
        with open(self.FILE_NAME, 'wb') as f:
            pickle.dump(self.__staff, f, -1)


    def load_from_file(self):
        try:
            with open(self.FILE_NAME, 'rb') as f:
                self.__staff = pickle.load(f)
        except FileNotFoundError:
            print('<script>alert("Нет файла")</script>')

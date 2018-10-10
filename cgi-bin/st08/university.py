import pickle

from .bachelor import Bachelor
from .master import Master


class University:
    def __init__(self):
        self.__people = []
        self.__filename = 'cgi-bin/st08/dump'


    def add_bachelor(self, lastname: str, university: str):
        self.__people.append(Bachelor(lastname, university))


    def edit_bachelor(self, i: int, lastname: str, university: str):
        self.__people[i] = Bachelor(lastname, university)


    def add_master(self, lastname: str, university: str, scientific_adviser: str):
        self.__people.append(Master(lastname, university, scientific_adviser))


    def edit_master(self, i: int, lastname: str, university: str, scientific_adviser: str):
        self.__people[i] = Master(lastname, university, scientific_adviser)


    def get_people(self):
        return self.__people


    def delete_one_item(self, i: int) -> list:
        del self.__people[i]


    def clear_storage(self):
        self.__people = []

    
    def save_to_file(self):
        with open(self.__filename, 'wb') as f:
            pickle.dump(self.__people, f, -1)


    def load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f:
                self.__people = pickle.load(f)
        except FileNotFoundError:
            print('<script>alert("Нет файла")</script>')
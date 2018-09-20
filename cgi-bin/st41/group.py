from .person import Person
from .student import Student
import pickle 

class Group:
    
    FILE_NAME = "cgi-bin/st41/backup"
    
    def __init__(self):
        self.__peoples = []
    
    def addPerson(self, name, age):
        self.__peoples.append(Person(name, age))
        
    def addStudent(self, name, age, course, faculty):
        self.__peoples.append(Student(name, age, course, faculty))
           
    def getMembers(self): 
        return self.__peoples;
    
    def __checkRange(self, i):
        if i < 0 or i >= len(self.__peoples):
            raise IndexError("Out of range")
    
    def edit(self, i):
        self.__checkRange(i)
        self.__peoples[i].read() 
        
    def remove(self, i):
        self.__checkRange(i)
        del self.__peoples[i]
            
    def clear(self):
        self.__peoples.clear()
        
    def saveToFile(self):
        with open(self.FILE_NAME, "wb") as f:
            pickle.dump(self.__peoples, f)
            
    def loadFromFile(self):
        with open(self.FILE_NAME, "rb") as f:
            self.__peoples = pickle.load(f)
        
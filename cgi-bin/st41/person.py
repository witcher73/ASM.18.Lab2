class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = int(age)
           
    def get(self):
        return { "Type": "Person", "Name": self.__name, "Age": self.__age }
    
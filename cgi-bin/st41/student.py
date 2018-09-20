from .person import Person

class Student(Person):
    
    def __init__(self, name, age, course, faculty):
        Person.__init__(self, name, age)
        self.__course = int(course)
        self.__faculty = faculty
                  
    def get(self):
        return {  "Type": "Student", "Name": Person.get(self)["Name"], "Age": Person.get(self)["Age"], "Faculty": self.__faculty, "Course": self.__course }
    
import pickle
from .base import Student
from .derived import Captain

class Group:
    
    def __init__(self):
        self.group = []
        
    def addStudent(self, q):
        self.addFromFile()
        if (q.getvalue('firstName') != None) and (q.getvalue('lastName') != None) and (q.getvalue('age') != None):
            self.group.append(Student(q))
            self.saveToFile()
    
    def showAll(self, q):
        self.addFromFile()
        tmp = ""
        if (len(self.group) != 0):
            tmp = """<tr>"""
            for curStudent in self.group:
                tmp += curStudent.showInf(str(self.group.index(curStudent) + 1), type(curStudent).__name__)
                tmp += """<td>
                            <a href=\"?student=""" + q['student'].value + """&action=showModal""" + type(curStudent).__name__ + """&num=""" + str(self.group.index(curStudent) + 1) +"""">Изменить</a> / <a href=\"?student=""" + q['student'].value + """&action=deleteStudent&num=""" + str(self.group.index(curStudent) + 1) +"""">Удалить</a> 
                                  </td>
                              </tr>
                        """
        print("""
        <script>
            $('.table tbody').append(`""" + tmp + """`);
            $('#countStudents strong').append(`""" + str(len(self.group)) + """`);
        </script>""")



    def addCaptain(self, q):
        self.addFromFile()
        if (q.getvalue('firstName') != None) and (q.getvalue('lastName') != None) and (q.getvalue('age') != None) and (q.getvalue('phone') != None) and (q.getvalue('mail') != None):
            self.group.append(Captain(q)) 
            self.saveToFile()
        
    def edit(self, q):
        self.addFromFile()
        index = int(q.getvalue("num")) - 1
        if(len(self.group) > index):
            self.group[index].getInf(q)
        self.saveToFile()    
            
            
    def deleteStudent(self, q):
        self.addFromFile()
        index = int(q.getvalue("num")) - 1
        if(len(self.group) > index):
            self.group.remove(self.group[index])
            self.saveToFile()
        
            
    def deleteAllStudents(self, q):
        self.group = []
        self.saveToFile()
            
    def showModalStudent(self, q):
        self.addFromFile()
        print("""<script>
            
            document.getElementsByName('firstName')[0].value = \"""" + self.group[int(q.getvalue('num'))-1].firstName + """";
            document.getElementsByName('lastName')[0].value = \"""" + self.group[int(q.getvalue('num'))-1].lastName + """";
            document.getElementsByName('age')[0].value = \"""" + self.group[int(q.getvalue('num'))-1].age + """";

            $("#addStudent").modal('show');
        </script>""")

    def showModalCaptain(self, q):
        self.addFromFile()
        print("""<script>
            
            document.getElementsByName('firstName')[1].value = \"""" + self.group[int(q.getvalue('num'))-1].firstName + """";
            document.getElementsByName('lastName')[1].value = \"""" + self.group[int(q.getvalue('num'))-1].lastName + """";
            document.getElementsByName('age')[1].value = \"""" + self.group[int(q.getvalue('num'))-1].age + """";
            document.getElementsByName('phone')[0].value = \"""" + self.group[int(q.getvalue('num'))-1].phone + """";
            document.getElementsByName('mail')[0].value = \"""" + self.group[int(q.getvalue('num'))-1].mail + """";

            $("#addCaptain").modal('show');
        </script>""")
    
    def saveToFile(self):
        with open('cgi-bin/st19/1.txt', 'wb') as f:
            pickle.dump(self.group, f)   

    def addFromFile(self):
        try: 
            with open('cgi-bin/st19/1.txt', 'rb') as f:
                self.group = []
                self.group.extend(pickle.load(f)) 
        except FileNotFoundError:
            print('Файл не найден')    
            

class Student:
    def __init__(self, q):
        self.getInf(q)
        
    def getInf(self, q):
        self.firstName = q.getvalue('firstName')
        self.lastName = q.getvalue('lastName')
        self.age = q.getvalue('age')
        
    def showInf(self, num, nameClass):        
        if nameClass == "Student":
            return """<th>""" + num + """</th>
                      <td>""" + "Студент" + """</td>
                      <td>""" + self.firstName + """</td>
                      <td>""" + self.lastName + """</td>
                      <td>""" + self.age + """</td>
                      <td></td>
                      <td></td>
                      """
        else: 
            return """<th>""" + num + """</th>
                      <td>""" + "Староста" + """</td>
                      <td>""" + self.firstName + """</td>
                      <td>""" + self.lastName + """</td>
                      <td>""" + self.age + """</td>
                      """
        
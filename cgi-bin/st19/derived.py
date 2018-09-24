from .base import Student
class Captain(Student):
    def __init__(self, q):
        self.getInf(q)
        
    def getInf(self, q):
        super().getInf(q)
        self.phone = q.getvalue('phone')
        self.mail = q.getvalue('mail')
        
    def showInf(self, num, nameClass):
        student = super().showInf(num, nameClass)
        return student + """<td>"""+ self.phone + """</td>
                <td>"""+ self.mail + """</td>"""
        
        
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 09:31:45 2018

@author: Александр
"""
from .baseAcademicPlan import BaseAcademicPlan

class ExtendedAcademicPlan(BaseAcademicPlan):
    def __init__(self):
        # вызываем инициализацию родительского класса
        super().__init__()
        
        self._groupId = int
        self._purpose = str
        
    @property
    def groupId(self):
        return self._groupId
    
    @property    
    def purpose(self):
        return self._purpose

    @groupId.setter
    def groupId(self, value):
        self._groupId = value
        
    @purpose.setter
    def purpose(self, value):
        self._purpose = value    
      
    def saveProperties(self, elements, query):
        super().saveProperties(elements, query)
        self.purpose = query.getvalue('purpose') if query.getvalue('purpose') != None else ' '
        self.groupId = int(query.getvalue('groupId')) if query.getvalue('groupId') != None else 0
        
    def formTrContent(self, selfUrl, studentId):
        contentTr = super().formTrBaseContent()
        contentTr +=  """
                           <td>""" + str(self.groupId) + """ </td>
                           <td>""" + self.purpose + """ </td>
                           <td> <a href = """ + selfUrl + """?student=""" + str(studentId) + """&action=showExtendedPlanForPut&id="""+ str(self.id) + """> Ред. </a></td>
                           <td> <a href = """ + selfUrl + """?student=""" + str(studentId) + """&action=deletePlan&id="""+ str(self.id) + """> Удалить </a></td>
                       </tr>"""
        
        return contentTr          
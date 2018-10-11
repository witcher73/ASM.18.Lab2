# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:14:55 2018

@author: Александр
"""
global str

class BaseAcademicPlan:
    
    def __init__(self):
        self._id = int
        self._name = str
        self._yearBegin = int
        self._federalStudyStandardNumber = int
       
    @property
    def id(self):
        return self._id
    
    @property    
    def name(self):
        return self._name
    
    @property    
    def yearBegin(self):
        return self._yearBegin
    
    @property    
    def federalStudyStandardNumber(self):
        return self._federalStudyStandardNumber
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @name.setter
    def name(self, name):
        self._name = name
        
    @yearBegin.setter
    def yearBegin(self, value):
        self._yearBegin = int(value)
        
    @federalStudyStandardNumber.setter
    def federalStudyStandardNumber(self, value):
        self._federalStudyStandardNumber = int(value)      
    
    def saveProperties(self, elements, query):
        self.id = int(query.getvalue('id'))
        self.yearBegin = int(query.getvalue('year')) if query.getvalue('year') != None else 0
        self.name = query.getvalue('name') if (query.getvalue('name')) != None else ' '
        self.federalStudyStandardNumber = int(query.getvalue('federalStudyStandard')) if query.getvalue('federalStudyStandard') != None else 0
                
    def formTrBaseContent(self):
        contentTr =  """<tr>
                           <th scope="row"> """ + str(self.id) + """</th>
                           <td> """ + str(self.federalStudyStandardNumber) + """ </td>
                           <td> """ + self.name + """</td>
                           <td> """ + str(self.yearBegin) + """ </td>
                     """
                       
        return contentTr 

    def formTrContent(self, selfUrl, studentId):
        contentTr = self.formTrBaseContent()
        contentTr +=  """
                           <td> </td>
                           <td> </td>
                           <td> <a href = """ + selfUrl + """?student=""" + str(studentId) + """&action=showBasePlanForPut&id="""+ str(self.id) + """> Ред. </a></td>
                           <td> <a href = """ + selfUrl + """?student=""" + str(studentId) + """&action=deletePlan&id="""+ str(self.id) + """> Удалить </a></td>
                        </tr>"""
        
        return contentTr               
                       
            
            
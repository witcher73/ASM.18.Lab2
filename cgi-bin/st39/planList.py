# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:17:47 2018

@author: Александр
"""
from .extendedAcademicPlan import ExtendedAcademicPlan
from .baseAcademicPlan import BaseAcademicPlan
import pickle
import inspect

class PlanList:
    def __init__(self, query, selfUrl):
        self._elements = []
        self._query = query
        self._selfUrl = selfUrl
        self.downloadElementsFromFile()
        self.printTable()
    
    def printTable(self):
        print("""
                <script>
                    $('.table tbody').empty();
                </script>""")
        for plan in self.elements:
            contentTr = plan.formTrContent(self.selfUrl, self.query.getvalue('student'))
            print("""
                <script>
                    $('.table tbody').append(`""" + contentTr + """`);
                </script>""")
    
    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, plan):
        self._elements = self._elements.append(plan)
        
    @property
    def query(self):
        return self._query
    
    @query.setter
    def query(self, value):
        self._query = value
        
    @property
    def selfUrl(self):
        return self._selfUrl
    
    @selfUrl.setter
    def selfUrl(self, value):
        self._selfUrl = value    
    
    def findById(self, id):
        searchElement = None
        for element in self.elements:
            if element.id == int(id):
                searchElement = element
        
        return searchElement 

    def showPlan(self, query, dialogName, actionName):
        print ("""
               <div class="modal" id = "myModal">
                   <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title">""" + dialogName + """</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        <form id ="saveBasePlan">
                          <fieldset>
                            <div class="form-group">
                              <input type="hidden" class="form-control" name="student" value=""" +query.getvalue('student') +""">
                            </div>
                            <div class="form-group">
                              <input type="hidden" class="form-control" name="action" value=""" + actionName + """>
                            </div>
                          
                            <div class="form-group">
                              <label for="exampleInputEmail1">Название</label>
                              <input type="text" name = "name" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите название плана">
                              <small id="emailHelp" class="form-text text-muted">Введите достоверную информацию</small>
                            </div>
                            <div class="form-group">
                              <label for="exampleInputEmail1">Год</label>
                              <input type="number" name="year" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите год учебного плана">
                            </div>
                            <div class="form-group">
                              <label for="exampleInputEmail1">ГОС</label>
                              <input type="number" name="federalStudyStandard" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите номер федерального стандарта">
                            </div>
                            <div class="form-group">
                              <input type="hidden" name = "id" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                            </div> 
                    """)
        plan = None
        if (query.getvalue("id") != None):    
            plan = self.findById(query.getvalue("id"))
            
        if (plan != None):
            print ("""
               <script>
                  document.getElementsByName('id')[0].value = \"""" + query.getvalue("id") + """";
                  document.getElementsByName('name')[0].value = \"""" + plan.name + """";
                  document.getElementsByName('year')[0].value = \"""" + str(plan.yearBegin) + """";
                  document.getElementsByName('federalStudyStandard')[0].value = \"""" + str(plan.federalStudyStandardNumber) + """";
               </script>""")
        return plan    
            
        
    def closePlan(self):
        print ("""
                           </fieldset>
                          </fieldset>
                        </form>
                      </div>
                      <div class="modal-footer">
                        <input type="submit" form="saveBasePlan" class="btn btn-primary">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Отмена</button>
                      </div>
                    </div>
                  </div>
                </div>
                
        """)
        
        print ("""
               <script>
               $('#myModal').modal({show:true})
               </script>""")

    def showBasePlan(self, query, dialogName, actionName):
        self.showPlan(query, dialogName, actionName)
        self.closePlan()
    
    def openBasePlanForInsert(self, query):
         self.showBasePlan(query, "Добавление базового плана", "addBasePlan")                    
         id = self.getIdNewElement()
         print("""<script>           
                    document.getElementsByName('id')[0].value = \"""" + str(id) + """";
                </script>""")
         
    
    def openBasePlanForPut(self, query):
        self.showBasePlan(query, "Редактирование базового плана", "editBasePlan")
            
    def showExtendedPlan(self, query, dialogName, actionName):
        plan = self.showPlan(query, dialogName, actionName)
        print("""
              <div class="form-group">
                              <label for="exampleInputEmail1">Группа</label>
                              <input type="number" name="groupId" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите номер группы">
                            </div>
                            <div class="form-group">
                              <label for="exampleInputEmail1">Цель</label>
                              <input type="text" name = "purpose" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите цель">
                            </div> 
        """)
        if (plan != None):
            print ("""
               <script>
                  document.getElementsByName('groupId')[0].value = \"""" + str(plan.groupId) + """";
                  document.getElementsByName('purpose')[0].value = \"""" + plan.purpose + """";
               </script>""") 
            
        self.closePlan() 
        
    def openExtendedPlanForInsert(self, query):
        self.showExtendedPlan(query, "Добавление расширенного плана", "addExtendedPlan")
        id = self.getIdNewElement()
        print("""<script>           
                    document.getElementsByName('id')[0].value = \"""" + str(id) + """";
                </script>""")
         
    def openExtendedPlanForPut(self, query):
        self.showExtendedPlan(query, "Редактирование расширенного плана", "editExtendedPlan")
        
    def addBasePlan(self, query):
        baseAcademicPlan = BaseAcademicPlan()
        self.addPlan(query, baseAcademicPlan)
        
    def addExtendedPlan(self, query):
        extendedAcademicPlan = ExtendedAcademicPlan()
        self.addPlan(query, extendedAcademicPlan)
        
    def addPlan(self, query, academicPlan):
        academicPlan.saveProperties(self.elements, query)
        self._elements.append(academicPlan)
        self.printToFile()
        self.printTable()
            
    def eraseElements(self, query):
         self.elements.clear()
         self.printToFile()
         self.printTable()
         
    def printToFile(self):
        try:
            with open('cgi-bin/st39/plans.data', 'wb') as filehandle:
                pickle.dump(self.elements, filehandle)
        except Exception as e:
            print("Ошибка при выгрузке в файл")
            print (e)
            # вызвать выход
            
    def downloadElementsFromFile(self):
        try:
            with open('cgi-bin/st39/plans.data', 'rb') as filehandle:
                self._elements = pickle.load(filehandle)
        except Exception as e:
            print("Ошибка при загрузки из файла")
            print (e)
            # вызвать выход

    def editPlan(self, query):
        plan = self.findById(query.getvalue("id"))
        plan.name = query.getvalue("name")
        plan.federalStudyStandardNumber = int(query.getvalue("federalStudyStandard"))
        plan.yearBegin = int(query.getvalue("year"))
        return plan
    
    def editBasePlan(self, query):
        self.editPlan(query)
        self.printToFile()
        self.printTable()

    def editExtendedPlan(self, query):
        plan = self.editPlan(query)
        plan.groupId = int(query.getvalue("groupId"))
        plan.purpose = query.getvalue("purpose")
        self.printToFile()
        self.printTable()  
    
    def deletePlan(self, query):
        plan = self.findById(query.getvalue("id"))
        self.elements.remove(plan)
        self.printToFile()
        self.printTable()
        
    def getIdNewElement(self):
         id = 0
         for element in self.elements:
             if element.id > id:
                 id = element.id
         id += 1
         
         return id
                 

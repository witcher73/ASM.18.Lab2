# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:01:54 2018

@author: Александр
"""
from .planList import PlanList

def main (query, selfUrl):
    studentId = query['student'].value
    print("Content-type: text/html")
    print("""
        <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <meta charset="UTF-8">
                <title>Lab 2</title>
                <link rel="stylesheet" href="https://bootswatch.com/4/flatly/bootstrap.min.css">
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
            </head>
            <body>
            <div class="jumbotron">
              <h1 class="display-5">Hello, my friend!</h1>
              <p class="lead">Это лабораторная работа №2 ( Шилов А.И. АСМ-18-04 )</p>
            </div>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
              <div class="collapse navbar-collapse" id="navbarColor02">
                <ul class="navbar-nav mr-auto">
                  <li class="nav-item active">
                    <a class="nav-link" href=" """ + selfUrl + """?student=""" +studentId+ """&action=showBasePlanForInsert">Добавить основной уч. план <span class="sr-only">(current)</span></a>
                  </li>
                  <li class="nav-item active">
                    <a class="nav-link" href=" """ + selfUrl + """?student=""" +studentId+ """&action=showExtendedPlanForInsert">Добавить расширенный уч. план <span class="sr-only">(current)</span></a>
                  </li>
                  <li class="nav-item active">
                    <a class="nav-link" href=" """ + selfUrl + """?student=""" +studentId+ """&action=clear">Очистить список</a>
                  </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                  <a class="nav-link" href=" """ + selfUrl + """">Выйти</a>
                </form>
              </div>
            </nav>
            
            <table class="table table-hover">
              <thead>
                <tr class="table-primary">
                  <th scope="row">ИН</th>
                  <td>ГОС</td>
                  <td>Название</td>
                  <td>Год</td>
                  <td>ИН факультета</td>
                  <td>Цель</td>
                  <td> </td>
                  <td> </td>
                </tr>
              </thead>
              <tbody>
              </tbody>
            </table> 
                                                    """)
    planList = PlanList(query, selfUrl)
    
    menuList = {
        "clear": planList.eraseElements,
        "showBasePlanForInsert": planList.openBasePlanForInsert,
        "showExtendedPlanForInsert": planList.openExtendedPlanForInsert,
        "showBasePlanForPut": planList.openBasePlanForPut,
        "showExtendedPlanForPut": planList.openExtendedPlanForPut,
        "addBasePlan": planList.addBasePlan,
        "addExtendedPlan": planList.addExtendedPlan,
        "editBasePlan": planList.editBasePlan,
        "editExtendedPlan": planList.editExtendedPlan,
        "deletePlan": planList.deletePlan
    }

    menuList[query.getvalue('action')](query)
#!/usr/bin/env python3
from .container import Group

group = Group()

def addContainer(q, selfurl):
    print("Content-type: text/html")
    print("""
        <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <meta charset="UTF-8">
                <title>Lab 2</title>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
            </head>
            <body>

                <div class="modal fade" id="addStudent" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Студент</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        <form action=\"""" + selfurl + """" id="formStudent" method="get">
                          <input type="text" name="student" value=\"""" + q['student'].value + """" hidden>
                                                    """)
    if q.getvalue('action') == 'showModalStudent':
        print("""<input type="text" name="action" value="edit" hidden>""")
        print("""<input type="text" name="num" value=\"""" + q.getvalue('num') + """" hidden>""")
    else:
        print("""<input type="text" name="action" value="addStudent" hidden>""")
    print(""" 
                          <div class="form-group">
                            <label for="recipient-name" class="col-form-label">Имя:</label>
                            <input type="text" class="form-control" name="firstName">
                          </div>
                          <div class="form-group">
                            <label for="message-text" class="col-form-label">Фамилия:</label>
                            <input type="text" class="form-control" name="lastName">
                          </div>
                          <div class="form-group">
                            <label for="message-text" class="col-form-label">Возраст:</label>
                            <input type="text" class="form-control" name="age">
                          </div>
                        </form>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Закрыть</button>
                        <input type="submit" form="formStudent" class="btn btn-primary">
                      </div>
                    </div>
                  </div>
                </div>

                <div class="modal fade" id="addCaptain" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Студент</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        <form action=\"""" + selfurl + """" id="formCaptain" method="get">
                          <input type="text" name="student" value=\"""" + q['student'].value + """" hidden>
                          """)
    if q.getvalue('action') == 'showModalCaptain':
        print("""<input type="text" name="action" value="edit" hidden>""")
        print("""<input type="text" name="num" value=\"""" + q.getvalue('num') + """" hidden>""")
    else:
        print("""<input type="text" name="action" value="addCaptain" hidden>""")
    print(""" 
                          <div class="form-group">
                            <label for="recipient-name" class="col-form-label">Имя:</label>
                            <input type="text" class="form-control" name="firstName">
                          </div>
                          <div class="form-group">
                            <label for="message-text" class="col-form-label">Фамилия:</label>
                            <input type="text" class="form-control" name="lastName">
                          </div>
                          <div class="form-group">
                            <label for="message-text" class="col-form-label">Возраст:</label>
                            <input type="text" class="form-control" name="age">
                          </div>
                          <div class="form-group">
                            <label for="message-text" class="col-form-label">Телефон:</label>
                            <input type="text" class="form-control" name="phone">
                          </div>
                          <div class="form-group">
                            <label for="message-text" class="col-form-label">Почта:</label>
                            <input type="text" class="form-control" name="mail">
                          </div>
                        </form>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Закрыть</button>
                        <input type="submit" form="formCaptain" class="btn btn-primary">
                      </div>
                    </div>
                  </div>
                </div>

                <div class="d-flex flex-column text-center">
                    <h2 style="margin-top:35px;">Лаба 2 CGI Левочко</h2>
                    <br>
                    <div class="menu d-flex flex-wrap justify-content-center">
                        <div class="dropdown show" style="margin:5px">
                          <a class="btn btn-secondary btn-success dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Добавить
                          </a>

                          <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                            <a class="dropdown-item" data-toggle="modal" data-target="#addStudent" href="">Студента</a>
                            <a class="dropdown-item" data-toggle="modal" data-target="#addCaptain" href="">Старосту</a>
                          </div>
                        </div>
                        <a class="btn btn-danger" href="?student=""" + q['student'].value + """&action=deleteAllStudents" role="button" style="margin:5px">Очистить</a>
                        <a class="btn btn-light" href="
    """)                    
    print(selfurl)                   
    print("""
                        " role="button" style="margin:5px">Назад</a>
                    </div>
                    <br><br>
                    <p id="countStudents">Всего студентов в группе: <strong></strong></p>
                    <div class="container">
                        <h3>Список группы:</h3><br>
                        <table class="table table-hover">
                          <thead class="thead-light">
                            <tr>
                              <th scope="col">#</th>
                              <th scope="col">Статус</th>
                              <th scope="col">Имя</th>
                              <th scope="col">Фамилия</th>
                              <th scope="col">Возраст</th>
                              <th scope="col">Телефон</th>
                              <th scope="col">Почта</th>
                              <th scope="col">Действие</th>
                            </tr>
                          </thead>
                          <tbody>
                          </tbody>
                        </table>

                    </div>
                </div> 
                
              """)

menu = {
    "showAll": group.showAll,
    "addStudent": group.addStudent,
    "addCaptain": group.addCaptain,
    "showModalStudent": group.showModalStudent,
    "edit": group.edit,
    "showModalCaptain": group.showModalCaptain,
    "deleteAllStudents": group.deleteAllStudents, 
    "deleteStudent": group.deleteStudent, 
}

def main(q, selfurl):
    addContainer(q, selfurl)
    if "action" in q:
        menu[q.getvalue('action')](q)
    menu["showAll"](q)
#    
#    print("""
#    </body>
#        </html> """)


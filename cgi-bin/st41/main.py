from .group import Group

g = Group()

def editMember():
    i = int(input("Index: "))
    g.edit(i - 1)
       
def deleteMember(q):
    if "id" in q:
        i = int(q["id"].value)
        g.remove(i)
        g.saveToFile()

def addPerson(q):  
    if q["type"].value == "person":
        g.addPerson(q["name"].value, q["age"].value)
    elif q["type"].value == "student":
        g.addStudent(q["name"].value, q["age"].value, q["course"].value, q["faculty"].value)
    g.saveToFile()
        
    
methods = [g.addPerson, g.addStudent, editMember, deleteMember, g.saveToFile, g.loadFromFile]
actions = { "delete": deleteMember, "add": addPerson }

def printHead():
    print ("""Content-type: text/html; charset=utf-8\n\n
    <style>
        .brd {
                border: 1px solid black; 
                overflow:hidden; 
                background-color: #EEE; 
                width: 300px; 
                padding: 5px; 
                margin-top: 5px;
            }
        .btn {
                float: right;
            }
        input {
                margin: 2px; 
                width: 70px;
            }
        select {
                margin: 2px; 
                width: 70px;
            }
        form {
            width: 300px
            }
    </style>""")   

def printContent(q, selfurl):        
    print("<form action='{0}' method='get'>".format(selfurl))
    print("<input type='hidden' name='student' value={0}></a>".format(q['student'].value))
    print("<input type='hidden' name='action' value='add'></a>".format(q['student'].value))
    
    print("""
          <select id='type' name='type' onchange='onChange()'>
              <option value='person'>Person</option>
              <option value='student'>Student</option>
          </select>""")
    print("<br>")
    
    print("""
          <input placeholder='Name' name='name'>
          <input placeholder='Age' name='age'>
          <input type='submit' value='Add'>
          <br>
          <input placeholder='Course' class='forst' name='course' style='visibility: hidden'>
          <input placeholder='Faculty' class='forst' name='faculty' style='visibility: hidden'>
          <br>
          </form>""")

    print("""<script type='text/javascript'>
    function onChange() {
        var type = document.getElementById('type').value;
        if (type == 'person') {
        	document.getElementsByClassName('forst')[0].style.visibility = 'hidden';
        	document.getElementsByClassName('forst')[1].style.visibility = 'hidden';
        } else {
        	document.getElementsByClassName('forst')[0].style.visibility = 'visible';
        	document.getElementsByClassName('forst')[1].style.visibility = 'visible';
        }
    }
    </script>""")
            
    members = g.getMembers()
    for i, m in enumerate(members):
        print("<div class='brd'>")
        print("<a href='{0}?student={1}&action=delete&id={2}'><input class='btn' type='button' value='Delete'></a>".format(selfurl, q['student'].value, i))
        for key, value in m.get().items():
            print("{0} : {1}<br>".format(key, value))        
        print("</div>")
        
    print ('<br><a href="{0}">Назад</a> | <a href="{0}?student={1}">Главная</a>'.format(selfurl, q["student"].value))
        
    
        
    

def main(q, selfurl):     
    printHead();
    g.loadFromFile()
    try:
        if ("action" in q) and (q["action"].value in actions):
            actions[q["action"].value](q)
    except ValueError:
            print("<script>alert('{0}')</script>".format('Incorrect input'))
    except IndexError as e:
            print("<script>alert('{0}')</script>".format(e))
    except Exception as e:
            print("<script>alert('{1}')</script>".format(e))
    printContent(q, selfurl)
    
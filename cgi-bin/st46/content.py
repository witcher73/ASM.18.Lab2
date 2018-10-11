from .Visite import Visite
from .Employe import Employe
import pickle


class Content:
    
    def __init__(self,q,selfurl):
        self.q = q
        self.list=[]
        self.selfurl=selfurl
        self.readfile()

    def ajoutvis(self):
        self.readfile()
        self.list.append(Visite())
        self.change()
        self.writefile()
        
    def ajoutemp(self):
        self.readfile()
        self.list.append(Employe())
        self.change()
        self.writefile()

    def getdata(self):
        self.readfile()
        self.list[int(self.q.getvalue('id'))].GetData(self.q)
        self.writefile()
        self.print()


    def change(self):
    
        print(f""" <form role="form" method="get" >
                     <input type="hidden" name=student value="{self.q.getvalue('student')}">
                     <input type="hidden" name=act value="recevoir_info" > 
                      """)

        _id = int(self.q.getvalue('id') if 'id' in self.q else len(self.list)-1)
        print(f'<input type="hidden" name="id" value="{_id}">')
        
        self.list[_id].input()
        
        print('<button type="submit" class="btn btn-success" style="margin:10px 600px;"><span class="glyphicon glyphicon-off"></span> Valider</button>')
        print('</form>')

        
    def print(self):
        self.readfile()
        print(f"""
                <div class="container">
                <div class="row" style="padding:30px 400px;">
                <div class="col-xs-12">
                
                <div class="btn-group">
                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                     Add<span class="caret"></span></button>
                    <ul class="dropdown-menu" role="menu">
                      <li><a href="{self.selfurl}?student={self.q.getvalue('student')}&act=ajout_visite">Visite</a></li>
                      <li><a href="{self.selfurl}?student={self.q.getvalue('student')}&act=ajout_employe">Employe</a></li>
                    </ul>
                </div>
        <a href="{self.selfurl}" role="button" class="btn btn-primary">Back</a>
        <a href="{self.selfurl}?student={self.q.getvalue('student')}&act=delete_all" role="button" class="btn btn-danger">Clear</a>
        <h3> Лаб 2 -- Оди Вилфриэд </h3>
          </div>
            </div>
            </div>""")
        
        print("""
        <div class="container">
            <div class="row" style="padding:10px;">
            <div class="col-xs-12">
        <table class="table table-hover" style="padding:30px;">
        <thead>
        <tr>
        <th scope="col">Name</th> <th scope="col">Surname</th><th scope="col">Telephone</th><th scope="col">Service</th><th scope="col">CodeP</th> <th>Option</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        """)
        for i, l in enumerate(self.list):
            print(l.__str__())
            print("""
                    <td>
                    <a href={0}?student={1}&act=modifier&id={2} role="button" class="btn btn-link">Change</a>
                    <a href={0}?student={1}&act=delete&id={2} role="button" class="btn btn-link">Delete</a>
                    </td></tr><tr>""".format(self.selfurl, self.q.getvalue('student'),i))
            

        print("""
            </tr>
            </tbody>
            </table>
            </div>
            </div>
            </div>""")  
            
    def delete(self):
        self.readfile()
        self.list.pop(int(self.q.getvalue('id')))
        self.writefile()
        self.print()
    
    def writefile(self):
        with open('cgi-bin/st46/file','wb') as fich:
            pickle.dump(self.list,fich)
        
    def readfile(self):
        with open('cgi-bin/st46/file','rb') as fich:
            self.list=pickle.load(fich)
      

    def deleteall(self):
        self.readfile()
        self.list.clear()
        self.writefile()
        self.print()




        
        


from .Visite import Visite

class Employe:

    def __init__(self):
        self.service = ''
        self.codep = ''
        Visite.__init__(self)


    def input(self):
        Visite.input(self)
        
        print(f""" <div class="modal-body" style="padding:0px 500px; padding-top:-10px; " id="myModal">
                <div class="form-group">
		    <label for="service"><span class="glyphicon glyphicon-office"></span>service</label>
		    <input type="text" class="form-control" name=service placeholder="Enter your service" value="{self.service}" id="service">
                </div>
        
		<div class="form-group">
		    <label for="codep"><span class="glyphicon glyphicon-phone"></span>codep</label>
		    <input type="text" class="form-control" name=codep placeholder="Enter your code" value="{self.codep}" id="codep">
		</div>
		</div>
		""")

    def __str__(self):
    
    	return """
    		<td>{}</td>
  		<td>{}</td>
  		<td>{}</td>
  		<td>{}</td>
  		<td>{}</td>
		""".format(self.name,self.surname,self.tel,self.service,self.codep)

    def GetData(self,q):
        Visite.GetData(self,q)
        self.service = q.getvalue('service')
        self.codep = q.getvalue('codep')
        

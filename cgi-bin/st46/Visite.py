
class Visite:

    def __init__(self):

        self.name = ''
        self.surname = ''
        self.tel = ''
         

    def input(self):

        print(f""" <div class="modal-body" style="padding:20px 500px;">
                    <div class="form-group">
                        <label for="name"><span class="glyphicon glyphicon-user"></span>Name</label>
                        <input type="text" name=name value="{self.name}" class="form-control" id="name" placeholder="Enter your name">
                    </div>
        
                    <div class="form-group">
                        <label for="surname"><span class="glyphicon glyphicon-user"></span>Surname</label>
                        <input type="text" name= surname value="{self.surname}" id="surname" class="form-control" placeholder="Enter your surname">
                    </div>
    
                    <div class="form-group">
                        <label for="tel"><span class="glyphicon glyphicon-phone"></span>Tel</label>
                        <input type="text" name=tel class="form-control" id="tel" placeholder="Enter your telephone" value="{self.tel}" >
                    </div>
                </div>
	             """)
		
        
    def __str__(self):
    	return f"""
    		<td>{self.name}</td>
  		<td>{self.surname}</td>
  		<td>{self.tel}</td>
                <td>    </td>
                <td>    </td>
                """

    def GetData(self,q):
        self.name = q.getvalue('name')
        self.surname = q.getvalue('surname')
        self.tel = q.getvalue('tel')
        

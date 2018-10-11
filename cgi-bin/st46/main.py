from .content import Content


def main(q,selfurl):

        print("""Content-type: text/html

        <!DOCTYPE html>
        <html>
		<head>
                <meta charset="utf-8">
		<title> </title>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
 	 	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  		</style>
		</head>
		<body> """)
		
		    
        G=Content(q,selfurl)
        menu = {
        "ajout_visite":G.ajoutvis,
        "ajout_employe":G.ajoutemp,
        "recevoir_info":G.getdata,
        "afficher":G.print,
        "modifier":G.change,
        "delete":G.delete,
        "delete_all":G.deleteall
        }
	
        if 'act' in q:
                menu[q.getvalue('act')]()
        else:
                menu['afficher']()
	
        print("""
	</body>
        </html>
	""") 




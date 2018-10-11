from .computers import Computers
import cgi

def main(q, selfurl):
	
	Comp=Computers(q, selfurl)
	print ("Content-type: text/html; charset=utf-8\n\n")
	if 'action' in q:
		if (q['action'].value=="1"): 
			Comp.read()
		if (q['action'].value=="2"):
			Comp.write()
		if (q['action'].value=="3"):
			Comp.delete()
	else: 
		Comp.write()
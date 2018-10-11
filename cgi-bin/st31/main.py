from .container import *

def main(q, selfurl):
        print ("Content-type: text/html; charset=utf-8\n\n")
        book=Container(q,selfurl)
        book.tbl()
        if ("action" in q):
                if (q["action"].value == "2") or (q["action"].value == "3")  or (q["action"].value == "5") or (q["action"].value == "6") and (q["index"].value == "-1")  or (q["action"].value == "7") and (q["index"].value == "-1"):
                    book.add()
                    
                if (q["action"].value == "8"):
                    book.clear_container()
                    
                if (q["action"].value == "4") or ((q["action"].value == "6") and (q["index"].value != "-1"))  or ((q["action"].value == "7") and (q["index"].value != "-1")):
                    book.edit()
                    





if __name__ == '__main__':
	main()

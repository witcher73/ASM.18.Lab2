from .bank import cont
def main(q, selfurl):
    c=cont(q, selfurl)
    
    MENU = {
            "addv": c.addv,
            "addm": c.addm,
            "edit": c.edit,
            "delete": c.delete_item,
            "print_all": c.print_all,
            "clear": c.clear,
            "save": c.save_to_file,
            "load": c.load_from_file,
            "get": c.get,
	}

    print("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q.getvalue('act')]()
    else:
        MENU['print_all']()
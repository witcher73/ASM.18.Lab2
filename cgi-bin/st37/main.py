from .Aircraft import Aircraft

def main(q, selfurl):
    a = Aircraft(q, selfurl)
    a.load_file()
    menu = {
        "add_cargoplane": a.input_cargoplane,
        "add_airbus": a.input_airbus,
        "show": a.show,
        "get": a.get_aircraft,
        "clear": a.clear_list,
        "edit": a.edit_aircraft,
        "delete": a.del_aircraft
        }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        menu[q.getvalue('act')]()
    else:
        menu['show']()

    a.save_file()



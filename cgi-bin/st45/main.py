#from container import Container
from .container import Container

def main(q, selfurl):
	camera = Container(q, selfurl)
	menu = {
		"add_dslr": camera.add_dslr,
		"add_slr": camera.add_slr,
		"edit": camera.edit_item,
		"delete": camera.delete_list,
		"show": camera.show,
		"clear": camera.clear,
		"save": camera.save,
		"open": camera.open,
		"get": camera.get,
	}

	print("Content-type: text/html; charset=utf-8\n\n")
	if 'act' in q:
		menu[q.getvalue('act')]()
	else:
		menu['show']()
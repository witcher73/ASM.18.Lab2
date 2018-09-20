from .container import Container

def main(q, selfurl):
	container = Container(q, selfurl)
	menu = {
		"add_base": container.add_base,
		"add_derived": container.add_derived,
		"edit": container.edit_item,
		"delete": container.delete_item,
		"print_all": container.print_all,
		"clear": container.clear,
		"save": container.save_to_file,
		"load": container.load_from_file,
		'get': container.get,
	}

	print("Content-type: text/html; charset=utf-8\n\n")
	if 'act' in q:
		menu[q.getvalue('act')]()
	else:
		menu['print_all']()

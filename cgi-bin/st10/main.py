from Container import Container

def main(q,selfurl):
container = Container()

    MENU = [
        ["Добавить сотрудника", container.addworker],
        ["Добавиь главу отдела", container.addhead],
        ["Редактировать элемент", container.edittarget],
        ["Вывести весь список", container.show],
        ["Удалить элемент",container.delete_target],
        ["Удалить список", container.clearcontainer],
        ["Считать список из файла", container.fromfile],
        ["Записать список в файл", container.infile],
        ["Принять значение", container.get]
    ]
    print("Content-type: text/html; charset=utf-8\n\n")
	if 'act' in q:
		menu[q.getvalue('act')]()
	else:
		menu['Вывести весь список']()
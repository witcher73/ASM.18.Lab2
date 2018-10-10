from Container import Container

container=Container()


MENU=[
    ["Добавить сотрудника", container.addworker],
    ["Добавиь главу отдела", container.addhead],
    ["Редактировать элемент", container.edittarget],
    ["Вывести весь список", container.show],
    ["Удалить список", container.clearcontainer],
    ["Считать список из файла", container.fromfile],
    ["Записать список в файл", container.infile],
    ["Выход"]
]

def main():
    while True:
        for i,item in enumerate(MENU):
            print("{0:2}.{1}".format(i,item[0]))
        print("Выберите действие")
        flag=int(input())
        if flag > 7:
            print("Некорректный ввод")
        elif flag == 7:
            break
        else:
            MENU[flag][1]()


if __name__ == "__main__":
    main()
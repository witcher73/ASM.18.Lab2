from .Aircraft import Aircraft

a = Aircraft()

menu = [
        ["Добавить грузовой самолёт", a.input_cargoplane],
        ["Добавить пассажирский самолёт", a.input_airbus],
        ["Вывести список", a.print_aircrafts],
        ["Записать в файл", a.save_file],
        ["Загрузить список из файла", a.load_file],
        ["Очистить список", a.clear_list],
        ["Изменить данные по самолёту", a.edit_aircraft],
        ["Удалить самолет", a.del_aircraft],
        ["Выход"]
    ]

def main():
    print("------AirCrafts------")
    i = 0
    for item in menu:
        print("{0:2}. {1}".format(i, item[0]))
        i += 1
    num = int(input("Введите номер: "))
    if num != 8:
        menu[num][1]()
        main()

if __name__ == '__main__':
	main()

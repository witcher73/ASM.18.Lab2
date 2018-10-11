# -*- coding: utf-8 -*-


from pickle import dump, load
from .MobilePhone import MobilePhone
from .SmartPhone import SmartPhone

class Shop:

    def __init__(self, q, selfurl):
        self.db = []
        self.q = q
        self.selfurl = selfurl

    def insert_MobilePhone(self):

        self.read_file()
        phone = MobilePhone(self.q)
        self.db.append(phone)
        phone.add()
        phone.save_form(self.q)
        if phone.brand != ' ':
            self.write_file()

    def insert_SmartPhone(self):

        self.read_file()
        sphone = SmartPhone(self.q)
        self.db.append(sphone)
        sphone.add()
        sphone.save_form(self.q)
        if sphone.brand != ' ':
            self.write_list()

    def save_form(self):
        
        self.read_file()
        self.db[int(self.q.getvalue('id'))].save_form(self.q)
        self.write_form()
        self.get_shop()

    def edit_shop(self):
        
        self.read_file()
        self.db[int(self.q.getvalue('id'))].edit(self.q)

    def get_list(self):

        self.read_file()
        print(f'<br><a href="{self.selfurl}">Меню</a> | <a href="{self.selfurl}?student={self.q.getvalue("student")}">Обновить</a><br>')
        if len(self.db) == 0:
            print('<br>Список пуст<br>')
        else:
            print("""
            <table border>
             <Caption><H3>Список</H3></Caption>
              <tr><th rowspan="2" width="15%">Тип</th><th colspan="3">Информация</th><th colspan="2">Доп. информация</th><th rowspan="2">Действия</th></tr>
              <tr><th width="25%">ФИО</th><th>Возраст</th><th width="20%">Телефон</th>
              <th>Кафедра</th></tr>""")
            i = 0
            for item in self.db:
                    item.show_form()
                    print(f"""
                      <td>
                       <a href="{self.selfurl}?student={self.q.getvalue('student')}&action=delete_list&id={i}">Удалить</a> /
                       <a href="{self.selfurl}?student={self.q.getvalue('student')}&action=edit_list&id={i}">Изменить</a>
                      </td>
                     </tr>
                     """)
                    i += 1
        print(f"""
            </table>
             <br><a href="{self.selfurl}?student={self.q.getvalue('student')}&action=insert_MobilePhone">Добавить телефон</a>
             <br><a href="{self.selfurl}?student={self.q.getvalue('student')}&action=insert_MobilePhone">Добавить смартфон</a>
             <br><a href="{self.selfurl}?student={self.q.getvalue('student')}&action=clear_shop">Очистить список</a>
        """)

    def delete_list(self):
        self.read_list()
        self.db.pop(int(self.q.getvalue('id')))
        self.write_list()
        self.get_list()

    def read_file(self):

        with open('cgi-bin/st29/db.dat', 'rb') as f:
            self.db = load(f)

    def write_file(self):

        with open('cgi-bin/st26/db.dat', 'wb') as f:
            dump(self.db, f)

    def clear_file(self):

        self.read_list()
        self.db.clear()
        self.write_list()
        self.get_list()






# -*- coding: utf-8 -*-




class Shop:
    
    shop = []
    
    def __init__(self, q, selfurl):
        self.db = []
        self.q = q
        self.selfurl = selfurl
        
    def insert_MobilePhone(self):
        mobile_phone = MobilePhone()
        self.shop.append(mobile_phone)
        print("Мобильный телефон добавлен!")

    def insert_SmartPhone(self):
        smart_phone = SmartPhone()
        self.shop.append(smart_phone)
        print("Смартфон добавлен!")

    def edit_phone(self):
        if self.shop:
            self.display_shop()
            k = int(input("Введите номер телефона для редактирования:"))
            if k > len(self.shop):
                print("Число больше допустимого!")
            else:
                self.shop[k-1].set_data()
        else:
            print("Телефона нет в магазине!") 

    def delete_phone(self):
        if self.shop:
            self.display_shop()
            k = int(input("Введите номер телефона:"))
            if k > len(self.shop):
                print("Число больше допустимого!")
            else:   
                self.shop.pop(k-1)
                print("Телефон номер ", k, " удален!")
        else:
            print("Телефона нет в магазине!")
        
    def display_shop(self):
        if not self.shop:
            print("Телефона нет в магазине!")
        else:    
            for i in range (0, len(self.shop)):
                print("Телефон номер ", i+1)
                self.shop[i].display_data()

    def read_from_file(self):
        try:
            file = open('mobile_phone_shop.dat', 'rb')
            self.shop = pickle.load(file)    
            print("Выполнено!")
            file.close()
        except FileNotFoundError:
            print('\nФайл не существует')

    def write_to_file(self):
        file = open('mobile_phone_shop.dat', 'wb')
        pickle.dump(self.shop, file)        
        print("Выполнено!")
        file.close()    
            
    def clear_shop(self):
        self.shop.clear()
        print("Магазин пустой!")
        

import pickle
if __name__ == '__main__':
    from customer import Customer
    from vip_customer import Customer
else:
    from .customer import Customer
    from .vip_customer import VipCustomer


class Database:

    def __init__(self, q, selfurl):
        self.base = []
        self.q = q
        self.selfurl = selfurl

    def add_customer(self):
        self.load_from_file()
        customer = Customer(self.q)
        customer.input_data(self.q)
        # customer.save_form(self.q)
        self.base.append(customer)
        if customer.name != '':
            self.save_to_file()

    def add_vipcustomer(self):
        self.load_from_file()
        vipcustomer = VipCustomer(self.q)
        vipcustomer.input_data(self.q)
        # vipcustomer.save_form(self.q)
        self.base.append(vipcustomer)
        if vipcustomer.name != '':
            self.save_to_file()

    def display_customers(self):
        self.load_from_file()
        if len(self.base) == 0:
            print('<p>База клиентов пуста</p>')
        else:
            print('<table border="1"><tr align="center"><td>Имя</td><td>Возраст</td><td>Номер карты</td><td>Размер скидки</td></tr>')
            for i, customer in enumerate(self.base, start=1):
                print(customer)
            print('</table>')

        # print('<table><tr align="center"><td>Field1</td><td>Field2</td><td>Field3</td><td>Actions</td></tr>')
        # for i, item in enumerate(self.__items):
        #     item.show()
        #     print(
        #         '<td><a href={0}?student={1}&act=edit&id={2}>Edit</a><br><a href={0}?student={1}&act=delete&id={2}>Delete</a></td></tr></tr>'.format(
        #             self.selfurl, self.q.getvalue('student'), i))
        # print('</table><br>')
        # print('<a href={}?student={}&act=add_base>Add Base</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        # print('<a href={}?student={}&act=add_derived>Add Derived</a><br>'.format(self.selfurl,
        #                                                                          self.q.getvalue('student')))
        # print(
        #     '<a href={}?student={}&act=clear>Очистить список</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        # print(f'<a href={self.selfurl}>Назад</a>')

    def load_from_file(self):
        try:
            with open('cgi-bin/st25/base.pickle', 'rb') as f:
                self.base = pickle.load(f)
        except FileNotFoundError:
            print('\nФайл с БД ещё не создан')

    def save_to_file(self):
        try:
            filename = 'cgi-bin/st25/base.pickle'
            data = self.base
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
        except Exception:
            print('\nОшибка при записи в файл')

    # def delete_customer(self):
    #     self.display_customers()
    #     while True:
    #         try:
    #             index = int(input('Введите номер клиента, которого хотите удалить: '))
    #             break
    #         except ValueError:
    #             print('Индекс должен быть целым неотрицательным числом! Попробуйте еще раз.')
    #         except IndexError:
    #             print(f'Номер должен быть в диапазоне от 0 до {len(self.base)} включительно.')
    #     del self.base[index]

    def clean_base(self):
        self.load_from_file()
        self.base.clear()
        self.save_to_file()

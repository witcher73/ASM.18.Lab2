from .customer import Customer


class VipCustomer(Customer):
    def __init__(self, q):
        self.name = ''
        self.age = 0
        self.q = q
        self.card_number = ''
        self.amount_of_discount = 0

    def input_data(self, q):
        if 'name' in self.q:
            self.name = q.getvalue('name')
            self.age = q.getvalue('age')
            self.card_number = q.getvalue('card_number')
            self.amount_of_discount = q.getvalue('amount_of_discount')
        else:
            print(f"""
                     <h3>Добавление клиента</h3>
                     <form>
                      <input type=hidden name=student value="{self.q.getvalue('student')}">
                      <input type=hidden name=action value="add_vipcust">
                       Имя:<input type=text name=name value="{self.name}"><br>
                       Возраст:<input type=text name=age value="{self.age}"><br>
                       Номер карты:<input type=text name=card_number value="{self.card_number}"><br>
                       Размер скидки:<input type=text name=amount_of_discount value="{self.amount_of_discount}"><br>
                       <input type=submit value="Сохранить">
                      </form>
                    """)

    def save_form(self, q):
        if 'name' in self.q:
            self.name = q.getvalue('name')
            self.age = q.getvalue('age')
            self.card_number = q.getvalue('card_number')
            self.amount_of_discount = q.getvalue('amount_of_discount')
        else:
            self.name = ''

    def __str__(self):
        return f"<tr align='center'><td>{self.name}</td><td>{self.age}</td><td>{self.card_number}</td><td>{self.amount_of_discount}</td></tr>"
        # return super().__str__() + f"Номер карты: {self.card_number}\nРазмер скидки: {self.amount_of_discount}\n"


if __name__ == '__main__':
    cus = VipCustomer()
    cus.read_data_from_concole()
    print(cus)
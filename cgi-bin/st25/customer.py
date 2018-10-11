class Customer:
    def __init__(self, q):
        self.q = q
        self.name = ''
        self.age = 0


    def input_data(self, q):
        if 'name' in self.q:
            self.name = q.getvalue('name')
            self.age = q.getvalue('age')
        else:
            print(f"""
                     <h3>Добавление клиента</h3>
                     <form>
                      <input type=hidden name=student value="{self.q.getvalue('student')}">
                      <input type=hidden name=action value="add_cust">
                       Имя:<input type=text name=name value="{self.name}"><br>
                       Возраст:<input type=text name=age value="{self.age}"><br>
                       <input type=submit value="Сохранить">
                      </form>
                    """)

    def save_form(self, q):
        if 'name' in self.q:
            self.name = q.getvalue('name')
            self.age = q.getvalue('age')
        else:
            self.name = ' '

    # строковое представление объекта
    def __str__(self):
        return f"<tr align='center'><td>{self.name}</td><td>{self.age}</td><td>-</td><td>-</td></tr>"
        # return f"Имя клиента: {self.name}\nВозраст клиента: {self.age}\n"


if __name__ == '__main__':
    print('привет')
    cus = Customer()
    cus.read_data_from_concole()
    print(cus)
from Specialist import Specialist


class Head(Specialist):
    def __init__(self):
        super().__init__()
        self.phone = ''
        self.code = ''

    def fprint(self):
        print('<td>{0}<td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td><td>{8}</td></td>'.format(self.fname,
                                                                                                                                    self.lname,
                                                                                                                                    self.position,
                                                                                                                                    self.age,
                                                                                                                                    self.ident,
                                                                                                                                    self.phone,
                                                                                                                                    self.code,
                                                                                                                                    '-', '-'))

    def output(self):
        super.output()
        print('<tr><td>Телефон:</td><td><input type="text" name="phone" value="{0}"></td><tr>'.format(self.phone))
        print('<tr><td>СпецID:</td><td><input type="text" name="code" value="{0}"></td><tr>'.format(self.code))

    def get(self, q):
        super.get(q)
        self.phone = getvalue ('phone')
        self.code = getvalue ('code')
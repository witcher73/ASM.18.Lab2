class Worker:
    def __init__(self, q):
        self.get_inf(q)

    
    def get_inf(self, q):
        self.lastname = q.getvalue('lastname')
        self.department = q.getvalue('department')


    def show_inf(self, num):
        print(
            """
            <tr>
            <td>""" + num + """</td>
            <td>Работник</td>
            <td>""" + self.lastname + """</td>
            <td>""" + self.department + """</td>
            <td>-</td>
            """
        )
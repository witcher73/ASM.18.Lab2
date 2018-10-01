from .worker import Worker


class Manager(Worker):
    def __init__(self, q):
        self.get_inf(q)


    def get_inf(self, q):
        super().get_inf(q)
        self.project = q.getvalue('project')

    
    def show_inf(self, num):
        print(
            """
            <tr>
            <td>""" + num + """</td>
            <td>Управляющий</td>
            <td>""" + self.lastname + """</td>
            <td>""" + self.department + """</td>
            <td>""" + self.project + """</td>
            """
        )
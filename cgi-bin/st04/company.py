import pickle

from .worker import Worker
from .manager import Manager


class Company:
    def __init__(self, q, selfurl):
        self.__storage = []
        self.__filename = 'cgi-bin/st04/dump'

        self.q = q
        self.url = selfurl


    def add_worker(self):
        self.load_from_file()
        self.__storage.append(Worker(self.q))
        self.save_to_file()
        self.show_all()


    def add_manager(self):
        self.load_from_file()
        self.__storage.append(Manager(self.q))
        self.save_to_file()
        self.show_all()


    def show_all(self):
        self.load_from_file()
        
        print(
            """
            <h2 class="header-legend">Lab #2 Василевский</h2>
            <table class="table">
                <tr>
                <th>№</th>
                <th>Тип</th>
                <th>Фамилия</th>
                <th>Департамент</th>
                <th>Проект</th>
                <th>Действие</th>
            """
        )
        if len(self.__storage) != 0:
            for i, value in enumerate(self.__storage):
                value.show_inf(str(i))

                print(
                    """
                    <td><a href={0}?student={1}&action=edit_person&num={2}&class_name={3}>Изменить</a> / <a href={0}?student={1}&action=delete_person&num={2}>Удалить</a></td>
                    </tr>
                    """.format(self.url, self.q.getvalue('student'), i, value.__class__.__name__)
                )
        
        print('</table>')
        print(
            """
            <div class="div-button-group">
                <a href={0}?student={1}&action=show_input_worker class="button button-black" role="button">Добавить работника</a>
                <a href={0}?student={1}&action=show_input_manager class="button button-black" role="button">Добавить управляющего</a>
                <a href={0}?student={1}&action=clear class="button button-black" role="button">Очистить</a>
                <a href={0} class="button button-gray" role="button">Назад</a>
            </div>
            """.format(self.url, self.q.getvalue('student')))


    def show_input_worker(self):
        self.show_all()

        if self.q.getvalue('action') == 'edit_person':
            method = 'rewrite_person_information'
        else:
            method = 'add_worker'

        print(
            """
            <div class="div-input">
                <form action={0} method="get">
                    <input type="hidden" name="student" value={1}>
                    <input type="hidden" name="action" value={2}>

                    <label for="fname">Фамилия</label>
                    <input type="text" id="fname" name="lastname">

                    <label for="dep">Департамент</label>
                    <input type="text" id="dep" name="department">

                    <input type="hidden" name="num" value={3}>

                    <input type="submit" value="Submit">
                </form>
            </div>
            """.format(self.url, self.q.getvalue('student'), method, self.q.getvalue('num')))


    def show_input_manager(self):
        self.show_all()

        if self.q.getvalue('action') == 'edit_person':
            method = 'rewrite_person_information'
        else:
            method = 'add_manager'

        print(
            """
            <div class="div-input">
                <form action={0} method="get">
                    <input type="hidden" name="student" value={1}>
                    <input type="hidden" name="action" value={2}>

                    <label for="fname">Фамилия</label>
                    <input type="text" id="fname" name="lastname">

                    <label for="dep">Департамент</label>
                    <input type="text" id="dep" name="department">

                    <label for="proj">Проект</label>
                    <input type="text" id="proj" name="project">

                    <input type="hidden" name="num" value={3}>

                    <input type="submit" value="Submit">
                </form>
            </div>
            """.format(self.url, self.q.getvalue('student'), method, self.q.getvalue('num')))


    def edit_person(self):
        if self.q.getvalue('class_name') == 'Worker':
            self.show_input_worker()
        else:
            self.show_input_manager()
        

    def rewrite_person_information(self):
        self.load_from_file()
        self.__storage[int(self.q.getvalue('num'))].get_inf(self.q)
        self.save_to_file()
        self.show_all()


    def clear_storage(self):
        self.__storage.clear()
        self.save_to_file()
        self.show_all()


    def delete_person(self):
        self.load_from_file()
        del self.__storage[int(self.q.getvalue('num'))]
        self.save_to_file()
        self.show_all()


    def save_to_file(self):
        with open(self.__filename, 'wb') as f:
            pickle.dump(self.__storage, f, -1)


    def load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f:
                self.__storage = pickle.load(f)
        except FileNotFoundError:
            print('Файл не существует')
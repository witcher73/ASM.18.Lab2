from .Menu import Menu


class Form:
    def __init__(self, url, q):
        self.url = url
        self.q = q

    def render(self, model):
        placeholders = model.placeholder
        params = model.params
        student_id = self.q.getvalue('student')
        id = self.q.getvalue('id', -1)
        act_id = self.q.getvalue('act')
        print('Форма редактирования {0}'.format(model.type))
        print('</br>')
        print('<form>')
        print('<input type=hidden value={0} name="student">'.format(student_id))
        print('<input type=hidden value={0} name="act">'.format(act_id))
        if id != -1:
            print('<input type=hidden value={0} name="id">'.format(id))

        for i, param in enumerate(params):
            print('<input type="text" name="{0}" placeholder={1} value={2}>'.format(param, placeholders[i],
                                                                                    getattr(model, param)))
            print('</br>')
        print('<input type=submit value="Сохранить">')
        print('</form>')
        Menu.back_button(self.url, student_id)

    def is_saving(self):
        return True if 'first_name' in self.q else False

import cgi

from .Organization import *


def main(q: cgi.FieldStorage, self_url):
    ORG = Organization(self_url, q)
    student_id = int(q.getvalue('student', 0))
    Menu.response_ok()
    menu = Menu(ORG, self_url, student_id)

    if 'act' not in q:
        menu.show_menu(self_url, student_id)
    else:
        act_id = int(q.getvalue('act', Menu.EXIT_CODE))
        if act_id == -1:  # remove
            ORG.remove_man(q.getvalue('id'))
            return
        menu.start(act_id)

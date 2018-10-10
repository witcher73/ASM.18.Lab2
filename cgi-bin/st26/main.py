# -*- coding: utf-8 -*-

from .container import Container


def main(q, selfurl):
    container = Container(q, selfurl)
    main_menu_list = {
        'add_student': container.add_list_student,
        'add_teacher': container.add_list_teacher,
        'show_list': container.get_list,
        'edit_list': container.edit_list,
        'clear_list': container.clear_list,
        'delete_list': container.delete_list,
        'save_form': container.save_form,
    }
    print("""Content-type: text/html charset=utf-8\n\n
    <!DOCTYPE HTML>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Артём Печенкин Лаба 2</title>
      </head>
     <body>
    """)
    if 'action' in q:
        main_menu_list[q.getvalue('action')]()
    else:
        main_menu_list['show_list']()
    print(' </body>')
    print('</html>')

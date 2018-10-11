if __name__ == '__main__':
    from database import Database
else:
    from .database import Database


def main(q, selfurl):
    print("""Content-type: text/html charset=utf-8\n\n
        <!DOCTYPE HTML>
         <html>
          <head>
           <meta charset="utf-8">
           <title>Лаба 2</title>
          </head>
         <body>
        """)
    db = Database(q, selfurl)
    print(f'<h2>~~~~~База данных клиентов~~~~~</h2>')
    if 'action' in q:
        if q.getvalue('action') == 'add_cust':
            db.add_customer()
        elif q.getvalue('action') == 'add_vipcust':
            db.add_vipcustomer()
        elif q.getvalue('action') == 'display_cust':
            # db.display_customers()
            pass
        elif q.getvalue('action') == 'save_to_file':
            db.save_to_file()
        elif q.getvalue('action') == 'load_from_file':
            db.load_from_file()
        elif q.getvalue('action') == 'clean_base':
            db.clean_base()

    db.display_customers()

    print(f'<h3>~~~~~Действия с базой~~~~~</h3>')
    print(f"<a href={selfurl}?student={q.getvalue('student')}&action=add_cust>Добавить клиента</a><br>")
    print(f"<a href={selfurl}?student={q.getvalue('student')}&action=add_vipcust>Добавить VIP-клиента</a><br>")
    print(f"<a href={selfurl}?student={q.getvalue('student')}&action=display_cust>Вывод базы на экран</a><br>")
    print(f"<a href={selfurl}?student={q.getvalue('student')}&action=clean_base>Отчистить базу</a><br>")
    # print(f"<a href={selfurl}?student={q.getvalue('student')}&action=save_to_file>Сохранить базу в файл</a><br>")
    print(f"<a href={selfurl}?student={q.getvalue('student')}&action=load_from_file>Загрузить базу из файла</a><br>")
    print(f'<p><a href={selfurl}>Назад</a></p>')

    print(' </body>')
    print('</html>')


if __name__ == '__main__':
	main()


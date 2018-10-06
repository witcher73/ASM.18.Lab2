from .university import University


u = University()


def main(q: dict, selfurl: str):
    print("Content-type: text/html; charset=utf-8\n\n")

    actions = {
        'add_bachelor': show_input_form,
        'add_master': show_input_form,
        'edit_form': show_input_form,
        'edit': edit_item,
        'add': add_to_storage,
        'delete': delete_item_from_storage,
        'clear': clear_storage
    }

    try:
        if 'action' in q:
            actions[q['action'].value](q, selfurl)
        else:
            show_content(q, selfurl)
    except Exception as e:
        print('<script>{}</script>'.format(e))


def add_to_storage(q: dict, selfurl: str):
    u.load_from_file()

    if q['class_name'].value == 'Бакалавр':
        u.add_bachelor(q['lastname'].value, q['university'].value)
    elif q['class_name'].value == 'Магистр':
        u.add_master(q['lastname'].value, q['university'].value, q['scientific_adviser'].value)
    
    u.save_to_file()
    show_content(q, selfurl)


def edit_item(q: dict, selfurl: str):
    u.load_from_file()

    if q['class_name'].value == 'Бакалавр':
        u.edit_bachelor(int(q['num'].value), q['lastname'].value, q['university'].value)
    elif q['class_name'].value == 'Магистр':
        u.edit_master(int(q['num'].value), q['lastname'].value, q['university'].value, q['scientific_adviser'].value)

    u.save_to_file()
    show_content(q, selfurl)


def delete_item_from_storage(q: dict, selfurl: str):
    u.load_from_file()
    u.delete_one_item(int(q['num'].value))
    u.save_to_file()
    show_content(q, selfurl)


def clear_storage(q: dict, selfurl: str):
    u.clear_storage()
    u.save_to_file()
    show_content(q, selfurl)


def show_content(q: dict, selfurl: str):
    u.load_from_file()
    attach_style()

    if len(u.get_people()) == 0:
        print('<h2 class="legend-empty-storage">Никого нет в хранилище</h2>')
    else:
        print(
            """
            <table class="table">
                <tr>
                <th>#</th>
                <th>Степень</th>
                <th>Фамилия</th>
                <th>Университет</th>
                <th>Научный руководитель</th>
                <th>Действие</th>
                </tr>
            """)

    for i, value in enumerate(u.get_people()):
        row = tuple(value.get_information())

        if row[0] == 'Бакалавр':
            print('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>-</td>'.format(
                i, row[0], row[1], row[2]
            ))
        elif row[0] == 'Магистр':
            print('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td>'.format(
                i, row[0], row[1], row[2], row[3]
            ))
        
        print('<td><a href={0}?student={1}&action=edit_form&num={2}&class_name={3}>Изменить</a> | <a href={0}?student={1}&action=delete&num={2}>Удалить</a></td></tr>'.format(
            selfurl, q['student'].value, i, row[0]))
    print('</table>')

    print(
        """
        <div>
            <a href={0}?student={1}&action=add_bachelor class="button" role="button">Добавить бакалавра</a>
            <a href={0}?student={1}&action=add_master class="button" role="button">Добавить магистра</a>
            <a href={0}?student={1}&action=clear class="button" role="button">Очистить</a>
            <a href={0} class="button" role="button">Назад</a>
        </div>
        """.format(selfurl, q['student'].value))


def show_input_form(q: dict, selfurl: str):
    attach_style()

    if q['action'].value == 'edit_form':
        act = 'edit'
        num_item = q['num'].value

        if q['class_name'].value == 'Бакалавр':
            class_name = 'Бакалавр'
            additional_input = ''
        elif q['class_name'].value == 'Магистр':
            class_name = 'Магистр'
            additional_input = '<input type="text" name="scientific_adviser" placeholder="Научный руководитель">'

    elif q['action'].value == 'add_bachelor' or q['action'].value == 'add_master':
        act = 'add'
        num_item = None

        if q['action'].value == 'add_bachelor':
            class_name = 'Бакалавр'
            additional_input = ''
        elif q['action'].value == 'add_master':
            class_name = 'Магистр'
            additional_input = '<input type="text" name="scientific_adviser" placeholder="Научный руководитель">'
    
    print(
        """
            <div class="div-input">
                <h3>{3}</h2>
                <form action={0} method="get">
                    <input type="hidden" name="student" value={1}>
                    <input type="hidden" name="action" value={4}>


                    <input type="text" name="lastname" placeholder="Фамилия">
                    <input type="text" name="university" placeholder="Университет">
                    {2}
                    <input type="hidden" name="class_name" value={3}>
                    <input type="hidden" name="num" value={5}>

                    <div>
                        <input type="submit" value="Отправить">
                        <a href={0}?student={1} class="button" role="button">Назад</a>
                    </div>
                </form>
            </div>
        """.format(selfurl, q['student'].value, additional_input, class_name, act, num_item))


def attach_style():
    print(
        """
        <html>
        <head>
        <title>Винокуров</title>

        <style>
            .table {
                border-collapse: collapse;               
            }

            table, th, td {
                border: 1px solid black;
                font-size: 16px;
                padding: 5px;
            }

            .button {
                background-color: black;
                border-radius: 4px;
                color: white;
                text-decoration: none;
                padding: 10px 20px;
                display: inline-block;
                font-size: 15px;
                margin: 4px 2px;
                cursor: pointer;
                transition-duration: 0.4s;
            }

            .button:hover {
                background-color: #39353D;
            }

            .div-input {
                width: 250px;
                border-radius: 5px;               
            }

            input[type=text], select {
                padding: 12px ;
                margin: 8px 0;
                display: inline-block;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
            }

            input[type=submit] {
                background-color: black;
                color: white;
                padding: 11px ;
                margin: 8px 0;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            input[type=submit]:hover {
                background-color: black;
            }

            .button-input-group {
                    width: 50%;
                    margin-left: 25%;
                }

            .legend-empty-storage { 
                margin-top: 40px;
            }
        </style>
        </head>
        """)
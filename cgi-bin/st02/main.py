from .group import Office

u = Office()

def main(q: dict, selfurl: str):

    print("Content-type: text/html; charset=utf-8\n\n")

    actions = {
        'add': add_item,
        'delete': delete_item,
        'clear': clear_all
    }

    u.load_from_file()

    try:
        if 'action' in q:
            actions[q['action'].value](q, selfurl)
        else:
            update_view(q, selfurl)

    except Exception as e:
        print('<script>{}</script>'.format(e))


def add_item(q: dict, selfurl: str):

    try:
        if q['type'].value == 'device':
            u.add_device(q['vendor'].value, q['model'].value)
        else:
            u.add_smartphone(q['vendor'].value, q['model'].value, q['os'].value)

    except Exception as ex:
            print(ex)
            print('Ошибка!')

    
    u.save_to_file()
    update_view(q, selfurl)


def delete_item(q: dict, selfurl: str):
    u.delete_from_list(int(q['num'].value))
    u.save_to_file()
    update_view(q, selfurl)


def clear_all(q: dict, selfurl: str):
    u.clear()
    u.save_to_file()
    update_view(q, selfurl)

def print_head():
    print(
        """
        <head>
            <title>Аметова</title>

            <style>
                body {
                    font-family: Arial;
                }

                .table {
                    border-collapse: collapse;               
                }

                a {
                    text-decoration: none;
                }

                table, th, td {
                    border: 1px solid #ccc;
                    font-size: 14px;
                    padding: 5px 15px;
                    text-align: center;
                }

                table th {
                    color: #E8760C;
                }

                table a {
                    color: #FF0000;
                }

                select, input, .btn {
                    margin: 4px 2px;
                    padding: 0 20px;
                    line-height: 36px;
                    font-size: 15px;
                    border-radius: 5px;
                }

                select, input {
                    border: 1px solid #ccc;
                }
                
                select {
                    padding: 12px 20px;
                }

                .btn {
                    display: inline-block;
                    background-color: #E8760C;
                    color: white;
                    border: none;
                    cursor: pointer;
                    text-decoration: none;
                }

                .div-input {
                    width: 250px;
                    border-radius: 5px;               
                }
                
                h2 {

                }
            </style>
        </head>
        """)

def print_body(q: dict, selfurl: str):

    print("<a href={0} class='btn'>Назад</a>".format(selfurl))

    print("<form action='{0}' method='get'>".format(selfurl))
    print("<input type='hidden' name='student' value={0}></a>".format(q['student'].value))
    print("<input type='hidden' name='action' value='add'></a>".format(q['student'].value))
    
    print("""
            <select id='type' name='type' onchange='onChange()'>
                <option value='device'>Устройство</option>
                <option value='smartphone'>Смартфон</option>
            </select>
          """)

    print("<br>")
    
    print(  """
                    <input placeholder='Производитель' name='vendor'>
                    <input placeholder='Модель' name='model'>
                    <input placeholder='ОС' id='os-input' name='os' style='visibility: hidden'>
                    <br>
                    <button class="btn" type='submit'>Добавить</button>
                    <br>
                </form>
            """)

    if len(u.get_devices()) == 0:
        print('<h2>Список устройств пуст</h2>')
    else:
        print(  """
                    <table class="table">
                        <tr>
                            <th>#</th>
                            <th>Тип</th>
                            <th>Производитель</th>
                            <th>Модель</th>
                            <th>Операционная система</th>
                            <th></th>
                        </tr>
                """)

        for i, value in enumerate(u.devices):
                row = tuple(value.get_data())

                if row[0] == 'Устройство':
                    print('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>-</td>'.format(i, row[0], row[1], row[2]))
                elif row[0] == 'Смартфон':
                    print('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td>'.format(i, row[0], row[1], row[2], row[3]))
                
                print( ('<td>' +
                            '<a href={0}?student={1}&action=delete&num={2}>Удалить</a>' +
                        '</td></tr>')
                            .format(selfurl, q['student'].value, i, row[0]))

        print('</table>')

    print(  """
                <div>
                    <a href={0}?student={1}&action=clear class="btn">Удалить все</a>
                </div>
            """
        .format(selfurl, q['student'].value))

def print_scripts():
    print(  """
                <script type='text/javascript'>
                    function onChange() {
                        var type = document.getElementById('type').value;
                        document.getElementById('os-input').style.visibility = type === 'smartphone' ? 'visible' : 'hidden';
                    }
                </script>
            """)

def update_view(q: dict, selfurl: str):
    print_head()
    print_body(q, selfurl)
    print_scripts()
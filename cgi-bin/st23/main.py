from .station import Station


s = Station()


def main(q, selfurl):

    actions = {
        'add': add_staff,
        'delete': delete_item,
        'edit_form': show_edit_form,
        'edit': edit_item,
        'clear': clear_staff
    }

    print("Content-type: text/html; charset=utf-8\n\n")

    try:
        if 'action' in q:
            actions[q['action'].value](q, selfurl)
        else:
            show_content(q, selfurl)
    except Exception as e:
        print('<script>alert({0})</script>'.format(e))


def add_staff(q, selfurl):
    s.load_from_file()

    if q['class'].value == 'master':
        s.add_master(q['lastname'].value, q['category'].value)
    elif q['class'].value == 'engineer':
        s.add_engineer(q['lastname'].value, q['category'].value, q['num_educations'].value, q['rank'].value)
    
    s.save_to_file()
    show_content(q, selfurl)


def delete_item(q, selfurl):
    s.load_from_file()
    s.delete_item(int(q['num'].value))
    s.save_to_file()
    show_content(q, selfurl)


def edit_item(q, selfurl):
    s.load_from_file()

    if q['class'].value == 'master':
        s.edit_master(
            int(q['num'].value), 
            q['lastname'].value, 
            q['category'].value)
    
    elif q['class'].value == 'engineer':
        s.edit_engineer(
            int(q['num'].value), 
            q['lastname'].value, 
            q['category'].value, 
            q['num_educations'].value, 
            q['rank'].value)

    s.save_to_file()
    show_content(q, selfurl)


def show_edit_form(q, selfurl):
    s.load_from_file()
    st =  s.get_staff()[int(q['num'].value)].get_inf()

    lastname = st[1]
    category = st[2]

    if st[0] == 'Master':
        num_educations = None
        rank = None
    else:
        num_educations = st[3]
        rank = st[4]

    style()

    print(
        """
       <div class="input-group">
            <form action={0} method="get">
                <input type="hidden" name="student" value={1}>
                <input type="hidden" name="action" value=edit>

                <select id="cls" name="class" onchange="onChange()" class="select">
                    <option value="master">Мастер</option>
                    <option value="engineer">Инженер</option>
                </select><br><br>

                <input type="text" name="lastname" placeholder="Фамилия" value={2} onfocus="this.value=''" size="15">
                <input type="text" name="category" placeholder="Категория" value={3} onfocus="this.value=''" size="15"><br>

                <input type="text" name="num_educations" class="engi" placeholder="Число высших образований" value="1" onfocus="this.value=''" style="visibility: hidden" size="25">
                <input type="text" name="rank" class="engi" placeholder="Разряд" value="5" onfocus="this.value=''" style="visibility: hidden" size="15"><br><br>
                
                <input type="hidden" name="num" value={6}>

                <div class="button-group">
                    <input type="submit" value="Отправить">
                    <a href={0}?student={1} class="back-button" role="button">Назад</a>
                </div>
            </form>
        </div>
        """.format(
            selfurl, 
            q['student'].value, 
            lastname, 
            category, 
            num_educations, 
            rank, 
            q['num'].value))
    
    print(
        """
        <script>
            function onChange() {
                var cls = document.getElementById('cls').value
                if (cls == 'master') {
                    document.getElementsByClassName('engi')[0].style.visibility = 'hidden';
                    document.getElementsByClassName('engi')[1].style.visibility = 'hidden';
                }
                else {
                    document.getElementsByClassName('engi')[0].style.visibility = 'visible';
                    document.getElementsByClassName('engi')[1].style.visibility = 'visible';
                }
            }
        </script>
        """)


def clear_staff(q, selfurl):
    s.load_from_file()
    s.clear_staff()
    s.save_to_file()
    show_content(q, selfurl)


def show_content(q, selfurl):
    s.load_from_file()
    staff = s.get_staff()
    
    style()
    
    print(
        """
        <h2 class="legend">Машуров (Лаба №2)</h2>
        <table class="table">
            <tr>
            <th>#</th>
            <th>Должность</th>
            <th>Фамилия</th>
            <th>Категория</th>
            <th>Число высших образований</th>
            <th>Разряд</th>
            <th>Действие</th>
            </tr>
        """
    )

    for i, value in enumerate(staff):
        row = value.get_inf()
        
        if row[0] == 'Master':
            print('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>-</td><td>-</td>'.format(
                i, row[0], row[1], row[2]))
        elif row[0] == 'Engineer':
            print('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td>'.format(
                i, row[0], row[1], row[2], row[3], row[4]))

        print('<td><a href={0}?student={1}&action=edit_form&num={2}&class_name={3}>Изменить</a> / <a href={0}?student={1}&action=delete&num={2}>Удалить</a></td></tr>'.format(
           selfurl, q['student'].value, i, row[0]))

    print(
        """
        <div class="input-group">
            <form action={0} method="get">
                <input type="hidden" name="student" value={1}>
                <input type="hidden" name="action" value=add>

                <select id="cls" name="class" onchange="onChange()" class="select">
                    <option value="master">Мастер</option>
                    <option value="engineer">Инженер</option>
                </select><br><br>

                <input type="text" name="lastname" placeholder="Фамилия" value="Иванов" onfocus="this.value=''" size="15">
                <input type="text" name="category" placeholder="Категория" value="5" onfocus="this.value=''" size="15"><br>

                <input type="text" name="num_educations" class="engi" placeholder="Число высших образований" value="1" onfocus="this.value=''" style="visibility: hidden" size="25">
                <input type="text" name="rank" class="engi" placeholder="Разряд" value="7" style="visibility: hidden" onfocus="this.value=''" size="15"><br><br>


                <div class="button-group">
                    <input type="submit" value="Отправить">
                    <a href={0}?student={1}&action=clear class="clear-button" role="button">Очистить</a>
                    <a href={0} class="back-button" role="button">Назад</a>
                </div>
                
            </form>
        </div>""".format(selfurl, q['student'].value))
    
    print(
        """
        <script>
            function onChange() {
                var cls = document.getElementById('cls').value
                if (cls == 'master') {
                    document.getElementsByClassName('engi')[0].style.visibility = 'hidden';
                    document.getElementsByClassName('engi')[1].style.visibility = 'hidden';
                }
                else {
                    document.getElementsByClassName('engi')[0].style.visibility = 'visible';
                    document.getElementsByClassName('engi')[1].style.visibility = 'visible';
                }
            }
        </script>
        """)



def style():
    print(
        """
        <head>
        <title>Машуров</title>

        <style>
            .table {
                margin: 20px 20%;
                border-collapse: collapse;
                width: 60%;
                align-self: center;
				font-size: 15px;
				text-align: left;
				border-collapse: collapse;
				border-radius: 20px;
				box-shadow: 0 0 0 10px #79da7f;
				
            }

            table, th, td { 
				padding: 10px 8px;
				background: white;
				border-top: 5px solid #79da7f;

            }

            .legend {
                margin-top: 35px;
                text-align: center;
            }

            .button-group {
                width: 50%;
                margin-left: 25%;
				
            }

            .back-button {
                text-decoration: none;
				outline: none;
				display: inline-block;
				width: 140px;
				height: 45px;
				line-height: 45px;
				border-radius: 45px;
				border: 2px solid rgba(255,255,255,.4);
				margin: 5px 10px;
				font-family: 'Montserrat', sans-serif;
				font-size: 11px;
				text-transform: uppercase;
				text-align: center;
				letter-spacing: 3px;
				font-weight: 600;
				color: #524f4e;
				background: white;
				box-shadow: 0 8px 15px rgba(0,0,0,.1);
				transition: .3s;
            }

            .back-button:hover {
                background-color: #2ee59d;
				box-shadow: 0 15px 20px rgba(46,229,157,.4);
				color: white;
				transform: translateY(-7px);
				
            }

            .clear-button {
				text-decoration: none;
				outline: none;
				display: inline-block;
				width: 140px;
				height: 45px;
				line-height: 45px;
				border-radius: 45px;
				border: 2px solid rgba(255,255,255,.4);
				margin: 5px 10px;
				font-family: 'Montserrat', sans-serif;
				font-size: 11px;
				text-transform: uppercase;
				text-align: center;
				letter-spacing: 3px;
				font-weight: 600;
				color: #524f4e;
				background: white;
				box-shadow: 0 8px 15px rgba(0,0,0,.1);
				transition: .3s;
            }

            .clear-button:hover {
                background-color: #2ee59d;
				box-shadow: 0 15px 20px rgba(46,229,157,.4);
				color: white;
				transform: translateY(-7px);
            }

            input[type=submit] {
				text-decoration: none;
				outline: none;
				display: inline-block;
				width: 140px;
				height: 45px;
				line-height: 45px;
				border-radius: 45px;
				border: 2px solid rgba(255,255,255,.4);
				margin: 5px 10px;
				font-family: 'Montserrat', sans-serif;
				font-size: 11px;
				text-transform: uppercase;
				text-align: center;
				letter-spacing: 3px;
				font-weight: 600;
				color: #524f4e;
				background: white;
				box-shadow: 0 8px 15px rgba(0,0,0,.1);
				transition: .3s;

            }

            input[type=submit]:hover {
				background-color: #2ee59d;
				box-shadow: 0 15px 20px rgba(46,229,157,.4);
				color: white;
				transform: translateY(-7px);
            }

            .input-group {
                width: 50%;
                margin-left: 25%;
                text-align: center;
            }

            .select {
				text-decoration: none;
				outline: none;
				display: inline-block;
				width: 200px;
				height: 50px;
				margin: 10px 20px;
				line-height: 45px;
				border-radius: 45px;
				border: 2px solid rgba(255,255,255,.4);
				font-family: 'Montserrat', sans-serif;
				font-size: 11px;
				text-transform: uppercase;
				text-align: center;
				letter-spacing: 3px;
				font-weight: 600;
				color: #524f4e;
				background: #6ec1c5;
				box-shadow: 0 8px 15px rgba(0,0,0,.1);
            }

            input[type=text] {
                text-decoration: none;
				outline: none;
				display: inline-block;
				width: 250px;
				height: 50px;
				margin: 10px 20px;
				line-height: 45px;
				border-radius: 45px;
				border: 2px solid rgba(255,255,255,.4);
				font-family: 'Montserrat', sans-serif;
				font-size: 11px;
				text-transform: uppercase;
				text-align: center;
				letter-spacing: 3px;
				font-weight: 600;
				color: #524f4e;
				background: #6ec1c5;
				box-shadow: 0 8px 15px rgba(0,0,0,.1);
            }

        </style>
        </head>
        """)
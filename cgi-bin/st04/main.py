from .company import Company


def main(q, selfurl):

    cpn = Company(q, selfurl)

    MENU = {
        'add_worker': cpn.add_worker,
        'add_manager': cpn.add_manager,
        'show_input_worker': cpn.show_input_worker,
        'show_input_manager': cpn.show_input_manager,
        'show_all': cpn.show_all,
        'clear': cpn.clear_storage,
        'delete_person': cpn.delete_person,
        'edit_person': cpn.edit_person,
        'rewrite_person_information': cpn.rewrite_person_information
    }

    head()

    if 'action' in q:
        MENU[q.getvalue('action')]()
    else:
        MENU['show_all']()

    print(
        """
        </html>
        """
    )


def head():
    print("Content-type: text/html; charset=utf-8\n\n")

    print(
    """
    <html>
    <head>
    <title>Vasilevsky</title>
    
    <style>
        .table {
            margin: 20px 20%;
            border-collapse: collapse;
            width: 60%;
            align-self: center;
        }

        table, th, td {
            border: 1px solid #ccc;
            border-radius: 4px;
            text-align: center;
            font-size: 18px;
            padding: 10px;
        }

        tr:hover {
            background-color: #ecebf0;
        }

        .div-input {
            width: 250px;
            border-radius: 5px;
            background-color: #073fb615;
            padding: 20px;
            margin-left: 40%;
        }

        input[type=text], select {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type=submit] {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        input[type=submit]:hover {
            background-color: #45a049;
        }

        .div-button-group {
            width: 50%;
            margin-left: 30%;
        }

        .button {            
            border: 2px solid #213451;
            color: white;
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            -webkit-transition-duration: 0.4s; /* Safari */
            transition-duration: 0.4s;
            cursor: pointer;
        }

        .button-black {
            background-color: #213451;
            color: #ecebf0;
        }

        .button-black:hover {
            background-color: #ecebf0;
            color:  #213451;
            border: 2px solid #213451;
        }

        .button-gray {
            background-color: #978683;
            color: #ecebf0;
        }

        .button-gray:hover {
            background-color: #ecebf0;
            color:  #213451;
            border: 2px solid #978683;
        }

        .header-legend {
            margin-top: 25px;
            text-align: center;
        }
    </style>
    </head>
    """
    )
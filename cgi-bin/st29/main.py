# -*- coding: utf-8 -*-

from .shop import Shop


def main(q, selfurl):
    shop = Shop(q, selfurl)
    actions ={
        'insert_MobilePhone': shop.insert_MobilePhone,
        'insert_SmartPhone': shop.insert_SmartPhone,
        'show_shop': shop.get_shop,
        'edit_shop': shop.edit_shop,
        'clear_shop': shop.clear_shop,
        'delete_shop': shop.delete_shop,
        'save_form': shop.save_form,
    }
    print("""Content-type: text/html charset=utf-8\n\n
    <!DOCTYPE HTML>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Редька Дмитрий Lab 2</title>
      </head>
     <body>
    """)
    if 'action' in q:
        actions[q.getvalue('action')]()
    else:
        actions['show_shop']()
    print(' </body>')
    print('</html>')
            
        

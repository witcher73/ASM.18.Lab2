# -*- coding: utf-8 -*-

from .container import Container

def main(q, selfurl):
   a = Container(q, selfurl)
   MENU = {
          'AddAnimal': a.AddAnimal,
          'AddSpecies': a.AddSpecies,
          'EditAnimal': a.EditAnimal,
          'DeleteAnimal': a.DeleteAnimal,
          'ClearContainer': a.ClearContainer,
          'ShowContainer': a.ShowContainer,
          'WriteFile': a.WriteFile,
          'ReadFile': a.ReadFile,
    }

   print("""Content-type: text/html charset=utf-8\n\n
    <!DOCTYPE HTML>
     <html>
      <head>
       <meta charset="utf-8">
       <title>Шкуренков Виктор ЛР 2</title>
      </head>
     <body>
    """)
   
   if 'action' in q:
       MENU[('action')]()
   else:
       MENU['ShowContainer']()
   print(' </body>')
   print('</html>')

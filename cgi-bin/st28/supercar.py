from .car import *

class Supercar(Car):
    def __init__(self):
        super().__init__()
        self.nitro = ""
        self.masloradiatory = ""

    def tbl (self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Цвет: ')
        print('<input type = "text" name = "color" value="{0}">'.format(self.color))
        print('Скорость: ')
        print('<input type = "text" name = "speed" value="{0}">'.format(self.speed))
        print('Модель: ')
        print('<input type = "text" name = "model" value="{0}">'.format(self.model))
        print('Объем азота: ')     
        print('<input type = "text" name = "nitro" value="{0}">'.format(self.nitro))
        print('<br><br>Модель маслорадиатора: ' )    
        print('<input type = "text" name = "masloradiatory" value="{0}">'.format(self.masloradiatory))
        print('<br><br><input type = "submit" value = "Добавить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')

    def read(self, q ,selfurl):
        super().read(q ,selfurl)
        if ('nitro' in self.q):
            self.nitro = self.q['nitro'].value
        else: self.nitro = ""
        if ('masloradiatory' in self.q):
            self.masloradiatory = self.q['masloradiatory'].value
        else: self.masloradiatory = ""

    def write(self):
        print(
    '''<br>
Цвет: {0}
скорость: {1}
модель: {2}
Объем азота: {3}
Модель маслорадиатора: {4}
'''.format(self.color,
           self.speed,
           self.model,
           self.nitro,
           self.masloradiatory))
        

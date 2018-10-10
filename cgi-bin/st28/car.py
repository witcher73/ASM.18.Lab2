class Car():
    def __init__(self):
        self.color = ""
        self.speed = ""
        self.model = ""

    
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
        print('<br><br><input type = "submit" value = "Добавить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')


    def read(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('color' in self.q):
            self.color = self.q['color'].value
        else: self.color = ""
        if ('speed' in self.q):
            self.speed = self.q['speed'].value
        else: self.speed = ""
        if ('model' in self.q):
            self.model = self.q['model'].value
        else: self.model = ""

    def write(self):
        print("<br> Цвет: {0} | Скорость: {1} | Модель: {2} ".format(self.color,self.speed,self.model))





# Использовать q  для получения значений параметров формы,  selfurl - для получения url скрипта
# Обратите внимание: полученный из q идентификатор студентов необходимо передавать во все формы
# и ссылки в своем коде - см. образец

class group:
	def __init__(self, q, selfurl):
		self.q = q
		self.selfurl = selfurl

	def f(self):
		print("st00.group.f()<br>")
		for p in self.q.list:
			print("{0}: {1}<br>".format(p.name, p.value))
		print ('<br><a href="{0}">Назад</a> | <a href="{0}?student={1}">Повторить</a>'.format(self.selfurl, self.q['student'].value));

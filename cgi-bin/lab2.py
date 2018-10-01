import cgi, cgitb, os, sys, codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

import st00.main
import st06.main
import st41.main
import st34.main
import st19.main
import st04.main


#	добавить импорт своего модуля по шаблону
#	import st<номер по журналу>.main


MENU = [
	["[00] Образец", st00.main.main],
	["[06] Василюк", st06.main.main],
    ["[34] Сурков", st34.main.main],
	["[41] Шнякин", st41.main.main],
	["[19] Левочко", st19.main.main],
	["[04] Василевский", st04.main.main],
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]


def menu(selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
	print ('<pre>------------------------------');
	for i, item in enumerate(MENU):
		print('<a href="{0}?student={1}">{2}</a>'.format(selfurl, i+1, item[0]))
	print ("------------------------------</pre>");


def main():
	q = cgi.FieldStorage()
	selfurl = os.environ['SCRIPT_NAME']
	st = int(q.getvalue('student', 0))
	if st > 0 and st <= len(MENU):
		MENU[st-1][1](q, selfurl)
	else:
		menu(selfurl)

main()
import cgi, cgitb, os, sys, codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

import st00.main
import st03.main
import st04.main
import st06.main
import st10.main
import st12.main
import st13.main
import st19.main
import st26.main
import st28.main
import st29.main
import st34.main
import st41.main
#import st43.main
import st23.main
import st08.main
import st46.main
import st32.main
import st15.main
import st39.main
import st40.main
import st45.main

#	добавить импорт своего модуля по шаблону
#  ПО АЛФАВИТУ, ПОЖАЛУЙСТА
#	import st<номер по журналу>.main


MENU = [
	["[00] Образец", st00.main.main],
	["[03] Васенков", st03.main.main],
    ["[04] Василевский", st04.main.main],
	["[06] Василюк", st06.main.main],
    ["[08] Винокуров", st08.main.main],
    ["[10] Гордиенко", st10.main.main],
    ["[12] Деордице В", st12.main.main],
    ["[13] Деордице Д", st13.main.main],
	["[15] Казак", st15.main.main],
    ["[19] Левочко", st19.main.main],
	["[23] Машуров", st23.main.main],
    ["[26] Печенкин", st26.main.main],
    ["[28] Рамазанов", st28.main.main],
    ["[28] Редька", st29.main.main],	
    ["[32] Сазонов", st32.main.main],	
    ["[34] Сурков", st34.main.main],
    ["[39] Шилов", st39.main.main],
    ["[40] Шкуренков", st40.main.main],
    ["[41] Шнякин", st41.main.main],
    #["[43] Шушпанникова", st43.main.main],
    ["[45] Жаманкин", st45.main.main],    
    ["[46] Соанху", st46.main.main]
    

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

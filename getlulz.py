#!/usr/bin/env python
#-*-coding: utf-8 -*-
#       РАЗРАЗИ МЕНЯ КРОТЫ!!!11111
#       html.image.parser 0.1
#       by artemy_m, edigaryev
#		каждая функция должна отдавать сипсок со ссылками
import urllib2, re, sys, optparse

if __name__=="__main__":
	parser = optparse.OptionParser("usage: %prog [-u http://foo.com/bar.html] [-1] [-2] [-w out.html]")
	parser.add_option("-u", "--url", dest="url", type="string",help="Url of page to parse")
	parser.add_option("-1", "--jru", dest="jru",action="store_true",help="Link is jabber.ru HTML log")
	parser.add_option("-2", "--dvach", dest="dvach",action="store_true",help="Link is 2-ch.ru thread")
	parser.add_option("-f", "--file", dest="file", type="string",help="Use this, if you want HTML output.")
	# тынц
	(options, args) = parser.parse_args()
	# url для getdata(), file для to_file()
	global url,file
	url,file=options.url,options.file
	# проверяем, что юзер собрался парсить
	if (options.jru and options.dvach):
		parser.error("You can specify only one argument: [-1] or [-1]. See help.")
	elif options.jru:
		type=1
	elif options.dvach:
		type=2
# регекспы
jru_regexp = re.compile('a href="(.*(?:jpg|jpeg|png|gif|pdf))"')
dvach_r = re.compile('''["']/c/src/[^+]*?['"]''') # регексп для двача

def uniq(seq):
# функция uniq() находит совпадающие элементы в массиве, и выдает новый массив, без совпадающих элементов
    checked = []
    for i in seq:
        if i not in checked:
            checked.append(i)
    return checked
	
def mystrip(arr):
# функция mystrip. Принимает в качестве аргумента массив, содержащий выдранные ссылки на изображение. Возвращает массив с элементами без символа ковычек (")
# например, есть массив arr['"http://foo/bar.jpg"','"http://example.com/foo/bar.png"']
# обработав данный массив, функция возвратит следующий массив: result['http://foo/bar.jpg','http://example.com/foo/bar.png']
	ret=[]
	for i in arr:
		i = i.strip('"').strip("'")
		ret.append(i)
	return ret

def getdata(url):
# получает страницу по адресу url, и помещает ее в глобальную переменную raw
	global raw
	usock = urllib2.urlopen(url)
	raw = usock.read()
	usock.close()
#
# вот тут начинаются функции, которые парсят HTML. Все функции возвращают массив со ссылками.
# аргументы функциям никакие не нужны, они сами допрашивают переменную raw, которая в свою очередь должна быть заправлена функцией getdata()
#
def dvach():
# трепанирует raw и извлекает ссылки на картинки.
# по идее должна работать со всеми wakaba-based имейджбордами
	result=[]
	data_re = dvach_r.findall(raw)
	data_uniq = uniq(data_re)
	data_strip = mystrip(data_uniq)
	# так надо. попробуйте убрать -- получите говно, а не ссылки
	for i in data_strip:
		result.append("http://2-ch.ru"+i)
	return result

def jru():
# трепанирует raw и извлекает ссылки на картинки.
# http://chatlogs.jabber.ru/
	result=[]
	data_re = jru_regexp.findall(raw)
	data_uniq = uniq(data_re)
	data_strip = mystrip(data_uniq)
	result=data_strip
	return result
#
# здесь две функции: обе принимают в качестве аргумента массив со ссылками (об этом заботятся функции такие как jru(), dvach()) но выдают разное содержимое
# to_stdout каждый элемент массива (ссылку) печатает с новой строки в stdout
# to_file делает HTML с картинками. А еще эта функция должна уметь определять по filename html это или нет, и если html писать в виде HTML, а если нет -- писать то же что и в stdout, но только в указанный файл
#
def to_stdout(data_arr):
	for i in data_arr:
		print i
		
def to_file(data_arr,filename):
	html=""
	for i in data_arr:
		html += '\n\n\n <input type="text" value=' + i + '><br><img src="' + i + '"><br><br>\n'
	f = open('./'+filename, 'w')
	f.write(html)
	f.close

# наполняем переменную raw говном и, возможно, лулзами
# кстати, между возможно и лулзами нужна запятая?
getdata(url)
# коммандный центр слушает вас!
# а еще..

if type==1:
	if file:
		to_file(jru(),file)
	else:
		to_stdout(jru())
elif type==2:
	if file:
		to_file(dvach(),file)
	else:
		to_stdout(dvach())

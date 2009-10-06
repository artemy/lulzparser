#!/usr/bin/python
#-*-coding: utf-8 -*-
#       РАЗРАЗИ МЕНЯ КРОТЫ!!!11111
#       html.image.parser 0.1
#       by artemy_m, edigaryev
#		
#		Эта версия использует функции и optparse
#		НУЖНО БОЛЬШЕ ЯДЕРНЫХ КОММЕНТОВ!!!
import urllib2,re,sys
#регулярное выражение для поиска ссылки и картинок
regexp = re.compile('''["']http://[^+]*?['"]''')
regexp2 = ['pdf','jpg','jpeg','png','gif']
#эта функция получает получает код страницы url
def getdata(url):
	#открываем соединение с WEB сервером
	usock = urllib2.urlopen(url)
	#GET
	data = usock.read()
	#закрываем соединение
	usock.close()
	return data
def makestandart(url):
	data=getdata(url)
	parsed = regexp.findall(data)
	for i in parsed:
		i = i.strip('"').strip("'")
		if i[-3:] in regexp2: #это пиздец, я этого не делал. artemy, сделай НОРМАЛЬНЫЙ регексп
			print i # выводим каждый линк
def makehtml(url):
	data=getdata(url)
	htmloutput=""
	parsed = regexp.findall(data)
	for i in parsed:
		i = i.strip('"').strip("'")
		if i[-3:] in regexp2: #это пиздец, я этого не делал. artemy, сделай НОРМАЛЬНЫЙ регексп
			htmloutput += '\n\n\n <input type="text" value=' + i + '><br><img src="' + i + '"><br><br>\n' # засовываем каждый линк в будуший HTML
	f = open('./html.html', 'w')
	f.write(htmloutput)
	f.close
from optparse import OptionParser
#инициализируем optparser, добавляем нужные аргументы
usage = "usage: %prog [-u] url [-p]"
parser = OptionParser(usage=usage)
parser.add_option("-u", "--url", dest="url", help="specify a url to fetch",default=0)
parser.add_option("-s", "--standart", dest="standart", help="use standart non HTML formatted output to stdout",default=1)
parser.add_option("-p", "--html", dest="html",action="store_true", help="use HTML formatted output to file lulzparser.html",default=0)
(options, args) = parser.parse_args()
#если options.url=0, значит URL не задан
if options.url==0:
	print "Please specify a URL."
else:
	if options.html!=0: #если options.html!=0 значит пользователь выбрал опцию --html
		makehtml(options.url)
	elif options.standart==1: #если options.standart==1, значит пользователь ничего не выбрал, т.е. автоматически будет выбран --standart
		makestandart(options.url)

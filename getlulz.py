#!/usr/bin/python
#-*-coding: utf-8 -*-
#       РАЗРАЗИ МЕНЯ КРОТЫ!!!11111
#       html.image.parser 0.1
#       by artemy_m, edigaryev
#		каждая функция должна отдавать сипсок со ссылками
import urllib2,re,sys

href = re.compile('''["']http://[^+]*?['"]''') # регексп для логов jabber.ru
filetypes = re.compile('.*(png|jpg|jpeg|gif|pdf)$') # регексп нужных расширений файлов
dvach_r = re.compile('''["']/c/src/[^+]*?['"]''') # регексп для двача

def uniq(seq):
    checked = []
    for i in seq:
        if i not in checked:
            checked.append(i)
    return checked
	
def mystrip(arr):
# функция mystrip. Принимает в качестве аргумента массив, содержащий куски ссылки на изображение. Возвращает массив с элементами, лишенными символа "
# например, есть массив arr['"http://foo/bar.jpg"','"http://example.com/foo/bar.png"']
# обработав данный массив, программа возвратит следующий массив: result['http://foo/bar.jpg','http://example.com/foo/bar.png']
	ret=[]
	for i in arr:
		i = i.strip('"').strip("'")
		ret.append(i)
	return ret

def getdata():
# функция getdata. Использует модуль urllib2. Получает содержимое веб-страницы, находящейся по адресу url а затем возвращает его.
	url=sys.argv[1]
	usock = urllib2.urlopen(url)
	data = usock.read()
	usock.close()
	return data

def dvach():
# Функция dvach, да. Возвращает (как и все другие парсящие функции) массив с url'ами картинок.
	data=getdata()
	data_re = dvach_r.findall(data)
	data_uniq = uniq(data_re)
	data_strip = mystrip(data_uniq)
	result=[]
	for i in data_strip:
		result.append("http://2-ch.ru"+i)
	return result

def jru():
	result=[]
	data=getdata()
	data_re = href.findall(data)
	data_uniq = uniq(data_re)
	data_strip = mystrip(data_uniq)
	for i in data_strip:
		if filetypes.match(i):
			result.append(i)
	return result


myswitch=jru() #dvach(), jru()

def getlulz():
	for i in myswitch:
		print i
		
def htmllulz(filename):
	html=""
	for i in myswitch:
		html += '\n\n\n <input type="text" value=' + i + '><br><img src="' + i + '"><br><br>\n'
	f = open('./'+filename, 'w')
	f.write(html)
	f.close
	
#weblulz("result.html") # отдаем HTML в файл
getlulz() #отдаем все ссылки в stdout

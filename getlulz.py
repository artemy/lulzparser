#!/usr/bin/python
#-*-coding: utf-8 -*-
#       РАЗРАЗИ МЕНЯ КРОТЫ!!!11111
#       html.image.parser 0.1
#       by artemy_m, edigaryev

import urllib2,re,sys
#урл
url = sys.argv[1]
#регулярное выражение для поиска ссылки
regexp = re.compile('''["']http://[^+]*?['"]''')
regexp2 = ['pdf','jpg','jpeg','png','gif']
#открываем соединение с WEB сервером
usock = urllib2.urlopen(url)
#GET
data = usock.read()
#закрываем соединение
usock.close()

#парсим HTML на предмет URL'ов

parsed = regexp.findall(data)
data = ""
for i in parsed:
    i = i.strip('"').strip("'")
    if i[-3:] in regexp2:
        data = data + '\n\n\n <input type="text" value=' + i + '><br><img src="' + i + '"><br><br>\n'



f = open('./html.html', 'w')
f.write(data)
f.close

#!/usr/bin/python
#-*-coding: utf-8 -*-
#       РАЗРАЗИ МЕНЯ КРОТЫ!!!11111
#       html.image.parser 0.1
#       by artemy_m, edigaryev

import urllib2,re,sys, optparse

#урл


def geturl(urlname):
    #открываем соединение с WEB сервером
    usock = urllib2.urlopen(urlname)
    #GET
    data = usock.read()
    #закрываем соединение
    usock.close()
    return data

def getfile(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data
    


#парсим HTML на предмет URL'ов
#parsed = regexp.findall(data)
#привет, я список lulz!
lulz=[]
#убираем уебанские символы
#for i in parsed:
#    lulz.append(i.strip('"').strip("'"))
#for i in lulz:
#	print i

if __name__=="__main__":
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", type="string")
    parser.add_option("-u", "--url", dest="urlname", type="string")
    (options, args) = parser.parse_args(sys.argv[:1])
    if len(args) == 2:
        parser.error("Please specify only one type of getting file")
    if len(str(options.filename)) == 0:
        data = getfile(options.filename)
    elif len(str(options.urlname)) == 0:
        data = geturl(options.urlname)
    else: print "get the fuck out!"
        
        
#    portnum = options.portnum
 #   #регулярное выражение для поиска ссылки
  #  regexp = re.compile('''["']http://[^+]*?['"]''')
   # regexp2 = re.compile('.(pdf|jpg|jpeg|png|gif)$')


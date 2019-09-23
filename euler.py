import urllib.request
from htmldom import htmldom

for i in range(1, 671):
    url = 'https://projecteuler.net/problem=%d' % i
    data = urllib.request.urlopen(url).read().decode('utf-8')
    dom = htmldom.HtmlDom().createDom(data)
    element = dom.find('#content')
    data = element.find('p').html()
    data = data.replace('<p>', '').replace('</p>', '')
    print(r'\begin{zadanie}')
    print(data)
    print(r'\href{%s}{Zadanie %i}' % (url, i))
    print(r'\end{zadanie}')

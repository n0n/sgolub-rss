import json
from urllib import urlopen

'''
Можно уменьшить количество обращений API если хранить локально последний результат локально и все эксперименты по форматированию проводить с локальной копией
'''
print "Connecting to API ..."
res = json.load(urlopen("http://www.kimonolabs.com/api/9y18ts42?apikey=b81d276e162cf00311048bba646c782a"))
print "Data recieved. Start generate HTML."

html=u'''<html><meta charset="utf-8"><head>Golubev</head><body><ul>'''

'''
Прочитать про переменную %s тогда код цикла можно уменьшить
'''

for i in res["results"]["collection1"]:
    html += '''<li>'''
    html += '''<a href="'''
    html += i["title-link"]["href"]
    html += '''">'''
    html += i["title-link"]["text"]
    html += '''</a><p>'''
    html += i["pre-text"]
    html += '''</p></li>'''

html += '''</ul></body></html>'''

print html


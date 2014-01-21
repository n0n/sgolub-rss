import json
from urllib import urlopen

print "Connecting to API ..."
res = json.load(urlopen("http://www.kimonolabs.com/api/9y18ts42?apikey=b81d276e162cf00311048bba646c782a"))
print "Data recieved. Start generate HTML."

html=u'''<html><meta charset="utf-8"><head>Golubev</head><body><ul>'''

for i in res["results"]["collection1"]:
    html += '<li><a href="%s">%s</a><p>%s</p></li>' % (i["title-link"]["href"], i["title-link"]["text"], i["pre-text"])


html += '''</ul></body></html>'''

print html


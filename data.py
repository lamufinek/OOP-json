import json
from urllib2

class example(object):
	def _init_(self):
		self.rein=[]
	def met(self, data):
		self.rein= re.findall(str(data))

def get_html(url):
	a = urllib2.Request(url)
	b = urllib2.urlopen(a)
	c = b.read()
	return c

url = get_html("http://www.backlabel.gr/label.html")
d = example()
d.met(url)
print(d.rein)
rein = []
json_encoded = []
def getLabel(data):
	Data = []
	for x in data:
		if x == "<" and x+1 =="s" and x+2 == "t" and x+3 == "r" and x+4 =="o" and x+5 == "n" and x+6 == "g" and x+7 ==">"
		    i= x+7
		    y= x+10
		    for i in y:
		    	Data.append(i)

		else:
		    x += 1
	return Data

rein = getLabel(d.rein)

json_encoded = json.dumps(Data)

print json_encoded		    	
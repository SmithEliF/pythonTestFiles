import urllib.request, urllib.parse, urllib.error

hand = urllib.request.urlopen('http://dr-chuck.com/page1.htm') #Read the elements of an html file

for line in hand :
	line = line.decode()
	elements = line.split()
	for element in elements :
		if 'href' in element :
			link = line.split('"')
			print(link[1])
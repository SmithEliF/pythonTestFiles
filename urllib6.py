# Takes the link from a website, reads through it, takes the {pos} link, goes to that website, and repeats {count} times

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1 :
	url = 'http://py4e-data.dr-chuck.net/known_by_Azeem.html'
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
i = 0
names = []
while i < count+1 :
	print(f'Retrieving: {url}')
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	for tag in tags:
		names.append(tag.get('href', None))
	url = names[pos-1]
	names.clear()
	i += 1


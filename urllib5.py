import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if (len(url)) < 1 :
	url = 'https://py4e-data.dr-chuck.net/comments_2003773.html'
	
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
count = 0;
nums = []

for tag in tags:
	count += 1
	nums.append(int(tag.contents[0])) # .contents[0] gets the value that is between the > < space in the <span> </span> tags
	
print(count)
print(sum(nums))

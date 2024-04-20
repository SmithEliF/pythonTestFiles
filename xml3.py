import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if (len(url)) < 1 :
	url = 'https://py4e-data.dr-chuck.net/comments_42.xml'
	
file = urllib.request.urlopen(url, context = ctx).read()
tree = ET.fromstring(file)
lst = tree.findall('comments/comment')
nums = []

for item in lst :
	nums.append(int(item.find("count").text))
	
print(sum(nums))


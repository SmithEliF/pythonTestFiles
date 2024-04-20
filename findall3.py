import re

x = 'From: smith.eli.frank@gmail.com Jan 5 2023 08:30:27.26432'

y = re.findall('\S+@\S+',x)

print(y)
import re

x = 'We just recieved $10 for cookies'

y = re.findall('\$[0-9.]+',x) # '\' makes special characters behave normally (most of the time)

print(f'Money recieved: {y}')
import json

data = \
'''
[
	{
	"id" : "001",
	"x" : "7",
	"name" : "Jack"
	} ,
	{
	"id" : "007",
	"x" : "2",
	"name" : "Thidney"
	}
]
'''

info = json.loads(data)
print(f'User Count: {len(info)}')
# Goes through the two dictionaries in the list
for item in info:
	print(f'Name: {item["name"]}')
	print(f'Id: {item["id"]}')
	print(f'Attr: {item["x"]}')
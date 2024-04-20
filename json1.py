import json

# The backslash character means the statement is continued on the next line
data = \
'''
{
	"name" : "Eli",
	"phone" : {
		"type" : "intl",
		"number" : "+1 705 388 0830"
	},
	"email" : {
		"hide" : "Yes"
	}
}
'''

info = json.loads(data)
print(f'Name: {info["name"]}')
print(f'Hide: {info["email"]["hide"]}')
import xml.etree.ElementTree as ET
input = '''
<stuff>
	<users>
		<user x = "2">
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x = "7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>
'''

tree = ET.fromstring(input)
lst = tree.findall('users/user')
print(f'User Count: {len(lst)}')
for item in lst :
	print(f'Name: {item.find("name").text}')
	print(f'ID: {item.find("id").text}')
	print(f'Attr: {item.get("x")}')

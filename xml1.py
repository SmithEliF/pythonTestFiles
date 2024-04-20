import xml.etree.ElementTree as ET
data = '''<person>
	<name>Chuck</name>
	<phone type="intl">
		+1 734 303 4456
	</phone>
	<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print(f'Name: {tree.find("name").text}') # Gets the text from an node, this returns Chuck
print(f'Attr: {tree.find("email").get("hide")}') # Gets the attribute called inside the node, this would return the value "yes"
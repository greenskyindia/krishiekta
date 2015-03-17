import xml.etree.ElementTree as ET

tree = ET.parse('data001/blgen002.xml')
root = tree.getroot()

for child in root:
	print(child.tag, child.attrib, child.text)
	for sub_child in child:
#		print("\t",sub_child.tag, sub_child.attrib, sub_child.text)
		if sub_child.tag == 'item':
			if sub_child[1].text == 'Sports':			
				for sub_child2 in sub_child:
			#	if sub_child2.text == 'International':
					print("\t\t",sub_child2.tag, sub_child2.attrib, sub_child2.text)
					for sub_child3 in sub_child2:
						print("\t\t\t",sub_child3.tag, sub_child3.attrib, sub_child3.text)
